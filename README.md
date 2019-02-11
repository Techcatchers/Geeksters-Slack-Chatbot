# Geeksters: Slack Chatbot in Python

Meet Geeksters! A Slack Chatbot Prototype built with Python. This Slackbot has some interesting features to be worked on which aims to increase the user's productivity at work.

If you are interested to know how the project got initiated then [here's a PDF](https://drive.google.com/file/d/1b3v5K1x4ILq1xHJIY-bEu4ZQHXeVC7PP/view?usp=sharing) for you.

**NOTE: This project was submitted for TCS Inframind Contest 2018. Unfortunately, we couldn't make it to the finals.**

Here's a [demo video](https://youtu.be/McJr1AOhyj8) for you which explains the entire project and its working.

I have put this project together to call out all the developers who would like to reuse it and contribute to this project.

It really works. Test it now!

## Features

1. You can get live scores for football on the chatbot for current live matches.
2. You can get lyrics for songs on your Slack chatbot.
3. You can get audio and video version of your desired songs from the slack chatbot.
4. You can set tasks, to-do lists, and birthday & anniversary reminders. You will get reminded on the set date and time by the chatbot.

    **NOTE: You need a database to store the user information for the same.**
5. You can get the latest breaking news on the chatbot.
6. You can get health tips right on your chatbot.

    **NOTE: You need a health tips dataset for the same and I have provided a demo dataset for storing more health tips by scraping any websites or downloading available datasets.**
7. Your users will get an entire set of premade help commands on the chatbot whenever they would like to know about any of the available commands.

AND many more features coming soon...

## Requirements

* You need to get a [Slack API key](https://api.slack.com/apps?new_app=1).
* You need to get a Bitly username and Bitly API key from [here](https://bitly.com/a/sign_in?rd=/a/oauth_apps)

    **NOTE: You will surely need [this article](https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/) later.**
* You need to get a [Youtube Data API](https://console.developers.google.com/apis/credentials?project=_) key.
* You need to get a [Live football score](https://www.football-data.org/client/register) API key.
* You need to create a [Custom Search Engine ID](https://cse.google.com/cse/create/new) by adding any or all of the following websites as per your choice:
  * https://genius.com/
  * http://www.lyricsted.com/
  * http://www.lyricsbell.com/
  * https://www.glamsham.com/
  * http://www.lyricsoff.com/
  * http://www.lyricsmint.com/

  **NOTE: For more information, you may look at the [Lyrics Extractor](https://github.com/Techcatchers/PyLyrics-Extractor) Python Library.**
* You need to get a [Google Custom Search JSON](https://developers.google.com/custom-search/v1/overview) API key.
* You need to get a [News API](https://newsapi.org/) key.

## How to Use

1. Clone this repository and set up environment variables in a `.env` file stored in `/src` directory with all the required credentials.

2. Install all the package requirements from the `requirements.txt` file.

    ```python
    pip install -r requirements.txt
    ```

3. Run the program.

    **NOTE: If something doesn't work as expected even after following all the above mentioned steps then please raise an issue and we will try to fix the issue as soon as possible.**

## How to Contribute

1. Fork this repository.
2. Clone it onto your local machine and test if everything works correctly before making any changes.
3. Make the appropriate changes.
4. Test it.
5. Test it again.
6. If everything's fine, commit new changes to your forked repository and open a pull request.

We will be more than happy to review your Pull Requests. So go for it and contribute to this awesome open source community.

If your Pull Request is accepted, you will surely get credits here.

## Contributors

* [Rishabh Agrawal](https://github.com/Techcatchers)

## Copyright Information

You are free to modify & use this project for commercial purposes as this project is licensed under MIT.

___

### If you liked this Repository, then please leave a star on this repository so that I can know you liked this project. It motivates me to contribute more in such Open Source projects in the future.