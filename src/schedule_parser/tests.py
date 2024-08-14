from datetime import date

from utils import _get_week_code


def test_get_week_code():
    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 12)) == "2"
    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 15)) == "2"
    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 18)) == "2"

    assert _get_week_code(date(2024, 8, 9), date(2024, 8, 15)) == "2"
    assert _get_week_code(date(2024, 8, 11), date(2024, 8, 15)) == "2"


    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 19)) == "1"
    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 25)) == "1"
    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 22)) == "1"

    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 5)) == "1"
    assert _get_week_code(date(2024, 8, 5), date(2024, 8, 11)) == "1"

    assert _get_week_code(date(2023, 12, 25), date(2024, 1, 1)) == "2"
    assert _get_week_code(date(2023, 12, 31), date(2024, 1, 7)) == "2"
    assert _get_week_code(date(2023, 12, 25), date(2024, 1, 8)) == "1"


if __name__ == "__main__":
    test_get_week_code()