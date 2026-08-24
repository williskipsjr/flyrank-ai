import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from scraper import parse_price_gbp


def test_parse_price_gbp():
    assert parse_price_gbp("\u00a351.77") == 51.77
