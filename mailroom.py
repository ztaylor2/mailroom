"""."""

import sys
from tabulate import tabulate


USER_DONATION_HISTORY = {"zach": [1, 2, 3],
                         "mike": [5000, 1, 3], "someone": [5, 2, 3]}


def get_user_input(prompt, validator=None):  # pragma: no cover
    """Handle asking for user input and validation."""
    reply = None
    while reply is None:
        reply = input(prompt)
        if reply == 'Q' or reply == 'quit':
            main()
        if validator:
            if validator(reply) is None:
                reply = None
    return reply


def validate_user_input_thank_report(reply):
    """Validate user input."""
    if reply == 'thank you' or reply == 'report':
        return reply


def validate_donation(reply):
    """Validate donation input."""
    try:
        val = int(reply)
        return reply
    except ValueError:
        return None


def send_a_thank_you():  # pragma: no cover
    """Gather our user input hence the pragma: no cover."""
    USER_DONATION_HISTORY
    full_name_input = get_user_input('input full name:')
    if full_name_input == 'list':
        create_a_report()
        send_a_thank_you()
    elif full_name_input not in USER_DONATION_HISTORY:
        USER_DONATION_HISTORY[full_name_input] = []
        request_donation_output = 'input {}\'s donation amount:'.format(full_name_input)
    elif full_name_input in USER_DONATION_HISTORY:
        request_donation_output = 'input {}\'s donation amount:'.format(full_name_input)
    donation_amount = int(get_user_input(request_donation_output, validate_donation))
    print(name_selected(full_name_input, donation_amount))
    main()


def name_selected(full_name_input, donation_amount):
    """Request donation amount from the name selected."""
    USER_DONATION_HISTORY
    USER_DONATION_HISTORY[full_name_input].append(donation_amount)
    return 'Thank you {} for your donation of {}!'.format(full_name_input, donation_amount)


def handle_report():
    """Call create report and main function."""
    create_a_report()
    main()


def create_a_report():
    """Organize data into list of lists."""
    donors_donation_list = []
    for key in USER_DONATION_HISTORY:
        new_donor = []
        new_donor.append(sum(USER_DONATION_HISTORY[key]))
        new_donor.append(key)
        new_donor.append(len(USER_DONATION_HISTORY[key]))
        new_donor.append(sum(USER_DONATION_HISTORY[key]) / len(USER_DONATION_HISTORY[key]))
        donors_donation_list.append(new_donor)
    sorted_donor_list = sorted(donors_donation_list, reverse=True)
    print_report_table(sorted_donor_list)


def print_report_table(sorted_donor_list):
    """Print out data as a table."""
    print(tabulate(sorted_donor_list, headers=['Donation Total', 'Name', 'Num of Donations', 'Avg Donation Amount']))


def main():  # pragma: no cover
    """Grab initial user input and calls functions based on that.  Requires user input so pragma: no cover."""
    print('ctrl + c to quit')
    initial_user_input = get_user_input('input: \'thank you\' or \'report\'',
                                        validate_user_input_thank_report)
    if initial_user_input.lower() == 'thank you':
        send_a_thank_you()
    if initial_user_input.lower() == 'report':
        handle_report()


if __name__ == "__main__":  # pragma: no cover
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye")
        sys.exit()
