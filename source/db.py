"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""


def fetch_games():
    """
    A function to return all games in the database.
    Soon we probably need a flag to get just active games.
    """
    return {
            "Warcraft": {"descr": "A game like World of Warcraft."},
            "Empires": {"descr": "A game like Age of Empires."},
            "Simmy": {"descr": "A game like Sims."},
           }
