import time
from slackclient import SlackClient
from lyrics_extractor import Song_Lyrics
from get_music import music
from task import parse_tasks
from reminder import parse_reminders
from football import Football_res
from health import health_tips
from help_info import user_help
from news import get_news
import settings
import requests
import json


# instantiate Slack client
slack_client = SlackClient(settings.SECRET_KEY)

# delay between reading from RTM
RTM_READ_DELAY = 1
COMMANDS = ['help', 'drink water', "quotes", "facts", "news", "live cricket", "live football", "health tips", "no quotes", "no facts", "no water", "no health tips", "no news"]
COMP_SUBS = ['premier league', 'championship', 'serie a', 'primeira liga', 'la liga']
foot_res = Football_res(None, None)

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """

    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            message = event["text"].lower()

            # Splitting user's message for comp_names
            check = set(map(lambda x: x.strip(), message.split(',')))
            # checking if message/s are in comp_names 
            result =  all(elem in COMP_SUBS for elem in check)
            if result:
                foot_res.football_response(message, check, event["channel"])
            else:
                return event["channel"], message.strip()
    return None, None


def handle_command(channel, message):
    """
        Executes bot command if the command is known
    """

    response = None
    # This is where you start to implement more commands!
    if message in COMMANDS or message.startswith("listen ") or message.startswith("lyrics for ") or message.startswith("remind me on "):
        if message == 'drink water':
            response = "Yay... You are going in the right way. Now you will be reminded to drink a glass of water in every 2 hours.\n\nTo deactivate from drink water notifications, type *No water*."

        elif message == 'no water':
            response = "Eh! You are leaving a good habit to stay fit or may be you don't need reminders any more. But please make sure to drink at least 8-10 glasses of water per day.\n\nTo reactivate drink water notifications, type *Drink water*."

        elif message == 'help':
            response = user_help()

        elif message == "quotes":
            quote = requests.get("http://quotes.rest/qod.json?category=inspire")
            data = quote.json()
            quote = data["contents"]["quotes"][0]["quote"]
            author = data["contents"]["quotes"][0]["author"]
            response = "Cool! You are now subscribed for receiving Daily Inspiring Quotes.\n\nTo deactivate from Daily Inspiring Quotes, type *No quotes*.\n\n" 
            response += "*Quote of the day.*\n\n" + quote + "\n - _*" + author + "*_"

        elif message == 'no quotes':
            response = "Eh! You are unsubscribed from receiving Daily Inspiring Quotes. But always try to stay motivated to reach your goals as this tool can make you achieve anything you aspire in your life.\n\nTo reactivate Daily Inspiring Quotes, type *quotes*."

        elif message == 'facts':
            fact = requests.get("http://randomuselessfact.appspot.com/random.json?language=en")
            data = fact.json()
            fact = data["text"]
            response = "Cool! You are now subscribed to Random Facts.\n\nTo deactivate from random facts, type *No facts*.\n\n" + "*Did you know?*\n\n" + fact

        elif message == 'no facts':
            response = 'Eh! You are unsubscribed from Random Facts. But make sure to keep learning and exploring things around you and never let your curiousity die in you.\n\nTo reactivate Random Facts, type *facts*.'

        elif message == "news":
            response = "Cool! You are now subscribed to latest news.\n\nTo deactivate from latest national news, type *No news*.\n\n"
            response += '*Current Affairs*\n\n' + get_news()

        elif message == "no news":
            response = "Eh! You are unsubscribed from latest National news. But make sure to keep yourself updated with the latest current affairs.\n\nTo reactivate latest news, type *news*."

        elif message == "health tips":
            response = "Cool! You are now subscribed to Health Tips.\n\nTo deactivate from health tips, type *No health tips*.\n\n"
            health = health_tips()
            response += "*Today's health tips is about " + health[0] + "*\n\n*_" + health[1] + "_*\n" + health[2]

        elif message == "no health tips":
            response = "Eh! You are unsubscribed from Health Tips. But make sure to stay fit and try to follow all the tips you have received till now.\n\nTo reactivate Health Tips, type *health tips*."

        elif message == "live football":
            response = "We provide live scores for *Premier League*, *Championship*, *Serie A*, *Primeira Liga*, *La Liga*. Which of these would you like to subscribe to receive match updates?\n\nYou can select mutiple competitions by seperating each of them with commas(,)."
            # f_res = threading.Thread(target=football_response, args=(channel, slack_client))
            # f_res.start()
            global foot_res
            foot_res = Football_res(channel, slack_client)

        elif message == "live cricket":
            response = "Subscribed for Cricket live scores."

        elif message.startswith("listen "):
            get_music_name = message[7:]
            store_music = music(get_music_name)
            response = "*" + store_music[0] + "*\n\nAudio Link: " + store_music[1] + "\n\nVideo Link: " + store_music[2]

        elif message.startswith("lyrics for "):
            get_song_name = message[11:]
            lyrics_gen = Song_Lyrics(settings.GCS_API_KEY, settings.GCS_ENGINE_ID)
            song = lyrics_gen.get_lyrics(get_song_name)
            response = '*' + song[0] + '*' + '\n\n' + song[1].replace('<br>','\n')

        # This will execute for tasks which will be scheduled for only once.
        elif message.startswith('remind me on ') and 'at ' in message:
            store_task_vals = parse_tasks(message)
            if len(store_task_vals) == 1:
                # if error, pass the error response to the user.
                response = store_task_vals[0]
            else:
                # Save store_tasks_vals to our db and notifies the user.
                response = 'All set. Your task is scheduled on ' + store_task_vals[0] + ' at ' + store_task_vals[2] + ' hrs.'

        # This will execute for reminders which will be scheduled for every year.
        elif message.startswith('remind me on '):
            store_reminder_vals = parse_reminders(message)
            if len(store_reminder_vals) == 1:
                # if error, pass the error response to the user.
                response = store_reminder_vals[0]
            else:
                # Save store_tasks_vals to our db and notifies the user.
                response = 'Reminder set. Now you will be reminded on ' + store_reminder_vals[0] + ' every year for ' + store_reminder_vals[1] + '\'s ' + store_reminder_vals[2]
    
        # Sends the response back to the channel
        slack_client.api_call(
            "chat.postMessage",
            channel = channel,
            text = response,
        )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")

        # Read bot's user ID by calling Web API method `auth.test`
        # starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            try:
                channel, message = parse_bot_commands(slack_client.rtm_read())
                if message:
                    handle_command(channel, message)
                    # h_cmd = threading.Thread(target=handle_command, args=(channel, message))
                    # h_cmd.start()
                time.sleep(RTM_READ_DELAY)
            except Exception as e:
                print("Reconnecting..." + str(e))
                slack_client.rtm_connect(with_team_state=False)
    else:
        print("Connection failed. Exception traceback printed above.")