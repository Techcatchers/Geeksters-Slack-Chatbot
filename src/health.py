import json
import random


def health_tips():
    """
        Fetches random health tip from our health dataset.
        Returns category, title, descripition from the fetched health tip.

        Here's a Sample of the returned health tip.:
            category = 'Diet'
            title = "Learn proper portion size."
            description = "To avoid eating too much of even the healthiest foods, keep track of how much you're eating. For most people, meat servings should be about the size of a deck of cards and other servings vary by the type of food."
    """

    # Opens our dataset and loads the json
    with open('health_dataset.json') as f:
        data = json.load(f)

    # Generates random int for fetching health tips randomly where a and b are inclusive ints passed.
    random_tip = random.randint(0,202)

    # Extracts required content from the JSON
    category = data["content"][random_tip]["category"]
    title = data["content"][random_tip]["title"]
    description = data["content"][random_tip]["description"]

    return (category, title, description)

# print(health_tips())