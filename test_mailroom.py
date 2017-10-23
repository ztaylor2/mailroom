"""Testing for mailroom command line app."""

import pytest


THANK_RESULT_TABLE = [("thank you", "thank you"), ("report", "report"),
                      ("anything", None), ("another random string", None)]

DONATION_VALIDATION_TABLE = [(1, 1), (5, 5), (5.5, 5.5), (20, 20),
                             ("anything", None),
                             ("another random string", None)]


NAME_TABLE = [(['zach', 5], 'Thank you zach for your donation of 5!')]


@pytest.mark.parametrize('n, result', THANK_RESULT_TABLE)
def test_validate_user_input_thank_report(n, result):
    """."""
    from mailroom import validate_user_input_thank_report
    assert validate_user_input_thank_report(n) == result


@pytest.mark.parametrize('n, result', DONATION_VALIDATION_TABLE)
def test_validate_donation(n, result):
    """."""
    from mailroom import validate_donation
    assert validate_donation(n) == result


@pytest.mark.parametrize('n, result', NAME_TABLE)
def test_name_selected(n, result):
    """."""
    from mailroom import name_selected
    assert name_selected(n[0], n[1]) == result
