"""."""


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
    print('report was put in')


def main():
    """."""
    initial_user_input = get_user_input('input: \'thank you\' or \'report\'',
                                        validate_user_input_thank_report)
    if initial_user_input.lower() == 'thank you':
        send_a_thank_you()
    if initial_user_input.lower() == 'report':
        create_a_report()


if __name__ == "__main__":
    main()
