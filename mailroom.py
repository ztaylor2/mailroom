"""."""

import sys


USER_DONATION_HISTORY = {"zach": [1, 2, 3], "mike": [5000, 1, 3], "someone":
                         [5, 2, 3]}


def get_user_input(prompt, validator=None):
    """."""
    reply = None
    while reply is None:
        reply = input(prompt)
        if reply == 'Q' or reply == 'quit':
            main()
        if validator:
            print('validator true')
            if validator(reply) is None:
                reply = None
    return reply


def validate_user_input_thank_report(reply):
    """."""
    if reply == 'thank you' or reply == 'report':
        return reply


def send_a_thank_you():
    """."""

    print('thank you was put in')


def create_a_report():
    """."""
    donors_donation_list = []
    for key in USER_DONATION_HISTORY:
        new_donor = []
        new_donor.append(sum(USER_DONATION_HISTORY[key]))
        new_donor.append(key)
        donors_donation_list.append(new_donor)
    print(sorted(donors_donation_list, reverse=True))
    print(create_donor_table(USER_DONATION_HISTORY, colList=None))
    main()


def create_donor_table(USER_DONATION_HISTORY, colList=None):
    """Function puts our donor data in a table and prints it out."""
    # if not column_list:  # This line throws an error that I cant figure.
    column_list = list(USER_DONATION_HISTORY[0].keys()
                       if USER_DONATION_HISTORY
                       else []
                       )
    my_list = [column_list]  # 1st row = header
    for donor in USER_DONATION_HISTORY:
        my_list.append([str(donor[col] or '') for col in column_list])
    column_size = [max(map(len, col)) for col in zip(*my_list)]
    table_row = ' | '.join(["{{:<{}}}".format(i) for i in column_size])
    my_list.insert(1, ['-' * i for i in column_size])  # Seperating line
    for donor in my_list:
        print(table_row.format(*donor))


def main():
    """."""
    print('ctrl + c to quit')
    initial_user_input = get_user_input('input: \'thank you\' or \'report\'',
                                        validate_user_input_thank_report)
    if initial_user_input.lower() == 'thank you':
        send_a_thank_you()
    if initial_user_input.lower() == 'report':
        create_a_report()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye")
        sys.exit()
