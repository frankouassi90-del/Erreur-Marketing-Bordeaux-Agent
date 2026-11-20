#!/usr/bin/env python3
"""Génère le plan de traçage d'un pilote : un lien UTM et un code court par canal.

Convention (fiche agent Développeur) :
    utm_source=<canal>&utm_medium=<type>&utm_campaign=pilote_<client>_<AAAAMM>

Sortie : plan-tracage_<client>_<AAAAMM>.csv (séparateur « ; », comme le registre).
Bibliothèque standard uniquement. Aucun appel réseau : le script ne teste pas les liens,
il les fabrique. Le test de chaque lien avant J1 reste à faire à la main.
"""

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

# Canaux de l'en-tête de outils/registre-reservations-pilote.csv (hors mot_cle_telephone,
# qui n'est pas un lien). Ordre = ordre de sortie du CSV.
# canal: (utm_medium, suffixe du code, où placer le lien, preuve attendue)
CANAUX = {
    "gbp_reserver": (
        "reservation",
        "GBP",
        "Fiche Google, champ « Lien de réservation » (gestionnaire de la fiche)",
        "Ligne d'export ou demande de formulaire avec canal=gbp_reserver, clics Google en appoint seulement",
    ),
    "gbp_post": (
        "publication",
        "POST",
        "Bouton « Réserver » de chaque publication Google de la période",
        "Ligne d'export ou demande de formulaire avec canal=gbp_post",
    ),
    "instagram_bio": (
        "bio",
        "INSTA",
        "Lien unique de la bio Instagram du commerce",
        "Ligne d'export ou demande de formulaire avec canal=instagram_bio",
    ),
    "site_bouton": (
        "bouton",
        "SITE",
        "Bouton « Réserver » du site du commerce (accès au site requis)",
        "Ligne d'export ou demande de formulaire avec canal=site_bouton",
    ),
    "email_reactivation": (
        "email",
        "MAIL",
        "Bouton de l'e-mail de réactivation (clients existants, lien de désinscription obligatoire)",
        "Stats d'envoi agrégées + ligne d'export avec canal=email_reactivation ou code cité",
    ),
    "sms_reactivation": (
        "sms",
        "SMS",
        "Lien court du SMS de réactivation (clients existants, mention STOP obligatoire)",
        "Stats d'envoi agrégées + ligne d'export avec canal=sms_reactivation ou code cité",
    ),
    "gads": (
        "cpc",
        "GADS",
        "URL finale des annonces Google Ads (si la dépense est validée)",
        "Rapport de campagne + ligne d'export avec canal=gads",
    ),
    "meta_ads": (
        "paid_social",
        "META",
        "URL de destination des publicités Meta (si la dépense est validée)",
        "Rapport de campagne ou ID de formulaire pub + ligne d'export avec canal=meta_ads",
    ),
}

COLONNES = ["canal", "lien", "code", "ou_placer", "preuve_attendue", "test_avant_j1"]
UTM_CLES = ("utm_source", "utm_medium", "utm_campaign")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def valider_slug(slug):
    if not SLUG_RE.match(slug):
        raise ValueError(
            f"slug invalide : {slug!r} (minuscules, chiffres et tirets, ex. vivants-bordeaux)"
        )
    return slug


def valider_mois(mois):
    if not re.fullmatch(r"\d{6}", mois):
        raise ValueError(f"mois invalide : {mois!r} (format AAAAMM, ex. 202612)")
    annee, m = int(mois[:4]), int(mois[4:])
    if not 1 <= m <= 12 or annee < 2000:
        raise ValueError(f"mois invalide : {mois!r} (format AAAAMM, ex. 202612)")
    return mois


def valider_url(url):
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise ValueError(f"URL invalide : {url!r} (doit commencer par https://)")
    return url


def prefixe_par_defaut(slug):
    """3 premières lettres du premier mot du slug, en majuscules (vivants-bordeaux -> VIV)."""
    return slug.split("-")[0][:3].upper()


def ajouter_utm(url, source, medium, campaign):
    """Ajoute les UTM à l'URL en gardant ses paramètres existants et son ancre.

    Les utm_source / utm_medium / utm_campaign déjà présents sont remplacés,
    pour qu'une URL de base mal recopiée ne crée pas deux sources.
    """
    parts = urlsplit(url)
    params = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k not in UTM_CLES]
    params += [("utm_source", source), ("utm_medium", medium), ("utm_campaign", campaign)]
    return urlunsplit((parts.scheme, parts.netloc, parts.path or "/", urlencode(params), parts.fragment))


def generer_plan(slug, url_base, mois, prefixe=None):
    valider_slug(slug)
    valider_url(url_base)
    valider_mois(mois)
    prefixe = (prefixe or prefixe_par_defaut(slug)).upper()
    if not re.fullmatch(r"[A-Z0-9]{2,6}", prefixe):
        raise ValueError(f"préfixe invalide : {prefixe!r} (2 à 6 lettres ou chiffres)")
    campagne = f"pilote_{slug}_{mois}"
    lignes = []
    for canal, (medium, suffixe, ou, preuve) in CANAUX.items():
        lignes.append(
            {
                "canal": canal,
                "lien": ajouter_utm(url_base, canal, medium, campagne),
                "code": f"{prefixe}-{suffixe}",
                "ou_placer": ou,
                "preuve_attendue": preuve,
                "test_avant_j1": "[À COMPLÉTER] date du test + capture",
            }
        )
    return lignes


def ecrire_csv(lignes, chemin):
    with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=";")
        w.writeheader()
        w.writerows(lignes)


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="generer_liens.py",
        description=(
            "Génère le plan de traçage d'un pilote : pour chaque canal du registre, "
            "un lien avec UTM (utm_campaign=pilote_<client>_<AAAAMM>) et un code court. "
            "Écrit plan-tracage_<client>_<AAAAMM>.csv. Aucun appel réseau."
        ),
        epilog=(
            "Exemple : python3 generer_liens.py vivants-bordeaux "
            "\"https://exemple.fr/reservation?lang=fr\" 202612 --sortie /tmp"
        ),
    )
    p.add_argument("client", help="slug du client, comme le dossier clients/<client> (ex. vivants-bordeaux)")
    p.add_argument("url_base", help="URL de réservation de base (paramètres existants conservés)")
    p.add_argument("mois", help="mois du pilote au format AAAAMM (ex. 202612)")
    p.add_argument("--prefixe", help="préfixe des codes (défaut : 3 lettres du slug, ex. VIV)")
    p.add_argument("--sortie", default=".", help="dossier de sortie (défaut : dossier courant)")
    args = p.parse_args(argv)

    try:
        lignes = generer_plan(args.client, args.url_base, args.mois, args.prefixe)
    except ValueError as e:
        p.error(str(e))

    dossier = Path(args.sortie)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / f"plan-tracage_{args.client}_{args.mois}.csv"
    ecrire_csv(lignes, chemin)
    print(f"{len(lignes)} canaux écrits dans {chemin} ({date.today().isoformat()})")
    for l in lignes:
        print(f"  {l['code']:<12} {l['lien']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
