import datetime

def parse_tasks(message):
    """
        Assumes message startswith 'remind me on'.
        Splits message into lists.
        Checks for any underlying errors in date and time format.
        Returns date, task description and time set.
    """

    # a = "remind me on 4 dec for packing up early at 16"
    b = message.split('remind me on ',1)[1]
    dat = b.split(' for ',1)[0]
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
            return ("Incorrect format for date.\n\nPlease try something like *remind me on 4 dec for packing up early at 16*\n\n OR \n\n*remind me on 4 dec for packing up early at 16:01*",)

    c = b.split(' for ', 1)[1]
    desc = c.split(" at ", 1)[0]
    time = c.split(" at ", 1)[1]
    try:
        verify_time = datetime.datetime.strptime(time, '%H')
        time = verify_time.strftime('%H:%M')
        # We will further save it into our db to keep the formats static.
    except ValueError: 
        try:
            verify_time = datetime.datetime.strptime(time, '%H:%M')
            time = verify_time.strftime('%H:%M')
            # We will further save it into our db to keep the formats static.
        except ValueError:
            return ("Incorrect format for time.\n\nPlease try something like *remind me on 4 dec for packing up early at 16*\n\n OR \n\n*remind me on 4 dec for packing up early at 16:01*",)

    return (dat, desc, time)

# print(tasks('remind me on 4 dec for going to school for sdfasresults at 16:01'))