import datetime

def parse_reminders(message):
    """
        Assumes message startswith 'remind me on'.
        Splits message into lists.
        Checks for any underlying errors in date format.
        Capitalizes the name and occasion.
        If name does not contain 's then returns an error.
        Returns date, person's name and occasion.
    """

    # a = "remind me on 4 dec for sara's birthday"
    b = message.split('remind me on ')[1]
    dat = b.split(' for ', 1)[0]
    try:
        verify_date = datetime.datetime.strptime(dat, '%d %b')
        dat = verify_date.strftime('%d %B')
        # We will further save it into our db to keep the formats static.
    except ValueError: 
        try:
            verify_date = datetime.datetime.strptime(dat, '%d %B')
            dat = verify_date.strftime('%d %B')
            # We will further save it into our db to keep the formats static.
        except ValueError:
            return ("Incorrect format for date.\n\nPlease try something like *remind me on 4 dec for sara's birthday*",)

    c = b.split(' for ', 1)[1]
    try:
        name = (c.split("'s ", 1)[0]).capitalize()
        occa = (c.split("'s ", 1)[1]).capitalize()
    except IndexError:
        return ("Incorrect format for setting up a reminder.\n\nDid you forget to put an *'s* after the name?\n\nPlease try something like *remind me on 4 dec for sara's birthday*",)

    return (dat, name, occa)

# print(tasks('remind me on 4 dec for going to school for sdfasresults at 16:01'))