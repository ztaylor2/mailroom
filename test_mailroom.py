"""Testing for mailroom command line app."""

import pytest


THANK_RESULT_TABLE = [("thank you", "thank you"), ("report", "report"),
                      ("anything", None), ("another random string", None)]

# DONATION_VALIDATION_TABLE = [(1, 1), (5, 5), (5.5, 5.5), (20, 20),
#                              ("anything", None),
#                              ("another random string", None)]

# SEND_THANK_YOU_TABLE = [("list", <a dictionary>), (, )]


@pytest.mark.parametrize('n, result', THANK_RESULT_TABLE)
def test_validate_user_input_thank_report(n, result):
    """."""
    from mailroom import validate_user_input_thank_report
    assert validate_user_input_thank_report(n) == result


# @pytest.mark.parametrize('n, result', DONATION_VALIDATION_TABLE)
# def test_donation_input_validation(n, result):
#     """."""
#     from mailroom import donation_input_validation
#     assert donation_input_validation(n) == result


# @pytest.mark.parametrize('n, result', PROCESS_THANK_YOU_TABLE)
# def test_send_a_thank_you(n, result):
#     """."""
#     from mailroom import process_thank_you_input
#     assert process_thank_you_input(n) == result
