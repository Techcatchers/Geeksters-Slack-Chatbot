import http.client
import json
import time
import settings


def live_football(comp_set):
    """
        Takes arg as set containing competition names.
        Converts names into id using dict.
        Fetches live football scores of all the live matches for arg provided.
        It only fetches live matches for Premier League, Championship, Serie A, Primeira Liga, La Liga.
        Extracts required information and stores in a tuple.
        Stores each tuple as separate matches in a list.
        Returns list of tuples if API contains any ongoing matches, containing the desired info of filtered matches.
        Else returns None.
    """

    comp_id = {'premier league': '2021', 
                'championship': '2016', 
                'serie a': '2019', 
                'primeira liga': '2017', 
                'la liga': '2140'}

    id = ''
    for name in comp_set:
        id += comp_id[name] + ','

    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': settings.FTLIVE_AUTH_TOKEN }
    connection.request('GET', '/v2/matches?status=LIVE&competitions=' + id[:-1], None, headers )
    response = json.loads(connection.getresponse().read().decode())

    count = response["count"]
    if count > 0:
        capture_football_live = []
        for c in range(count):
            competition = response["matches"][c]["competition"]["name"]
            home_team = response["matches"][c]["homeTeam"]["name"]
            away_team = response["matches"][c]["awayTeam"]["name"]

            fulltime_score_hometeam = str(response["matches"][c]["score"]["fullTime"]["homeTeam"] or 'NA')
            fulltime_score_awayteam = str(response["matches"][c]["score"]["fullTime"]["awayTeam"] or 'NA')

            halftime_score_hometeam = str(response["matches"][c]["score"]["halfTime"]["homeTeam"] or 'NA')
            halftime_score_awayteam = str(response["matches"][c]["score"]["halfTime"]["awayTeam"] or 'NA')
            
            extratime_score_hometeam = str(response["matches"][c]["score"]["extraTime"]["homeTeam"] or 'NA')
            extratime_score_awayteam = str(response["matches"][c]["score"]["extraTime"]["awayTeam"] or 'NA')

            penalties_hometeam = str(response["matches"][c]["score"]["penalties"]["homeTeam"] or 'NA')
            penalties_awayteam = str(response["matches"][c]["score"]["penalties"]["awayTeam"] or 'NA')

            winning_team = response["matches"][c]["score"]["winner"] or 'NA'
            if winning_team == 'HOME_TEAM':
                winning_team = home_team
            elif winning_team == 'AWAY_TEAM':
                winning_team = away_team

            capture_football_live.append((competition, home_team, away_team, halftime_score_hometeam, halftime_score_awayteam, fulltime_score_hometeam, fulltime_score_awayteam, extratime_score_hometeam, extratime_score_awayteam, penalties_hometeam, penalties_awayteam, winning_team))

        return capture_football_live
    return None


class Football_res():
    """
        Stores sub_channel and slack_client passed in from live football cmd.
        
        When the user types in further response selecting his competition then the function in it gets executed taking in set and channel as its args.
        
        It then fetches live scores calling another function passing in set of competition names required to be fetched for live football matches.
        
        Sends the message back to the user confirming about his subscription, if the channel the message came from is same as channel who subscribed for live football scores.
        
        Returns None.
    """

    def __init__(self, sub_channel, slack_client):
        self.sub_channel = sub_channel
        self.slack_client = slack_client

    def football_response(self, message, comp_set, channel):
        # we will save in our db list of comp of message as a list
        football_live = live_football(comp_set)
        # comp_subs = ['premier league', 'championship', 'serie a', 'primeira liga', 'la liga']

        if self.sub_channel == channel:
            if football_live != None:
                response = "You are now subscribed to live scores for football and you will now get notified when any football matches goes live for " + message.title() + ".\n\n*Live Football Scores*"
                for match in football_live:
                    response += "\n\n______________________________\n\n*" + match[0] + "*\n\n_*"\
                                + match[1] + ' V/s ' + match[2] + '*_\n\n*Half Time:* '\
                                + match[3] + ' | ' + match[4] + '\n\n*Full Time:* '\
                                + match[5] + ' | ' + match[6] + '\n\n*Extra Time:* '\
                                + match[7] + ' | ' + match[8] + '\n\n*Penalties:* '\
                                + match[9] + ' | ' + match[10] + '\n\n*Winner:* '\
                                + match[11]

                self.slack_client.api_call(
                "chat.postMessage",
                channel = channel,
                text = response,
                )

            else:
                response = 'No matches are live right now for ' + message.title() + '. But you will now get notified when any football matches goes live for ' + message.title() + '.'
                self.slack_client.api_call(
                "chat.postMessage",
                channel = channel,
                text = response,
                )

            self.sub_channel = None
        return None
        