"""Tests minimaux de generer_liens.py. Lancer : python3 -m unittest test_generer_liens -v"""

import csv
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generer_liens as g  # noqa: E402

CANAUX_REGISTRE = [
    "gbp_reserver", "gbp_post", "instagram_bio", "site_bouton",
    "email_reactivation", "sms_reactivation", "gads", "meta_ads",
]


class TestPlan(unittest.TestCase):
    def setUp(self):
        self.plan = g.generer_plan("vivants-bordeaux", "https://exemple.fr/reserver", "202612")

    def test_tous_les_canaux_du_registre(self):
        self.assertEqual([l["canal"] for l in self.plan], CANAUX_REGISTRE)

    def test_convention_utm(self):
        for l in self.plan:
            q = parse_qs(urlsplit(l["lien"]).query)
            self.assertEqual(q["utm_source"], [l["canal"]])
            self.assertEqual(len(q["utm_medium"]), 1)
            self.assertEqual(q["utm_campaign"], ["pilote_vivants-bordeaux_202612"])

    def test_codes_uniques_et_prefixes(self):
        codes = [l["code"] for l in self.plan]
        self.assertEqual(len(codes), len(set(codes)))
        self.assertIn("VIV-GBP", codes)
        self.assertTrue(all(c.startswith("VIV-") for c in codes))

    def test_url_avec_parametres_existants(self):
        plan = g.generer_plan(
            "vivants-bordeaux",
            "https://exemple.fr/r?lang=fr&utm_source=ancien&x=1#form",
            "202612",
        )
        parts = urlsplit(plan[0]["lien"])
        q = parse_qs(parts.query)
        self.assertEqual(q["lang"], ["fr"])
        self.assertEqual(q["x"], ["1"])
        self.assertEqual(q["utm_source"], ["gbp_reserver"])  # ancien UTM remplacé, pas doublé
        self.assertEqual(parts.fragment, "form")
        self.assertEqual(parts.query.count("?"), 0)

    def test_entrees_invalides(self):
        for args in [
            ("Vivants Bordeaux", "https://exemple.fr", "202612"),
            ("vivants-bordeaux", "exemple.fr/reserver", "202612"),
            ("vivants-bordeaux", "https://exemple.fr", "202613"),
            ("vivants-bordeaux", "https://exemple.fr", "2026-12"),
        ]:
            with self.assertRaises(ValueError):
                g.generer_plan(*args)

    def test_csv_ecrit(self):
        with tempfile.TemporaryDirectory() as d:
            rc = g.main(["vivants-bordeaux", "https://exemple.fr/reserver", "202612", "--sortie", d])
            self.assertEqual(rc, 0)
            chemin = Path(d) / "plan-tracage_vivants-bordeaux_202612.csv"
            with open(chemin, encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f, delimiter=";"))
            self.assertEqual(len(rows), 8)
            self.assertEqual(list(rows[0].keys()), g.COLONNES)


if __name__ == "__main__":
    unittest.main()
