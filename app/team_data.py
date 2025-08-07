import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SPORTRADAR_API_KEY")
API_URL = f"https://api.sportradar.com/nfl/official/trial/v7/en/league/hierarchy.json?api_key={API_KEY}"

def get_teams():
    response = requests.get(API_URL)
    data = response.json()

    teams = []
    for conference in data["conferences"]:
        for division in conference["divisions"]:
            for team in division["teams"]:
                teams.append({
                    "alias": team["alias"],
                    "market": team["market"],
                    "name": team["name"],
                    "founded": team["founded"],
                    "owner": team["owner"],
                    "general_manager": team["general_manager"],
                    "president": team["president"],
                    "mascot": team.get("mascot"),
                    "championships_won": team.get("championships_won"),
                    "championship_seasons": team.get("championship_seasons"),
                    "playoff_appearances": team["playoff_appearances"],
                    "venue_name": team["venue"]["name"]
                })
    return teams