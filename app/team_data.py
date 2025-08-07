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

# TESTING API
if __name__ == "__main__":
    teams = get_teams()
    print(f"Total teams: {len(teams)}")
    print("First team example:")
    print(teams[0:31])
    print(f"Team Name: {teams[0]['market']} {teams[0]['name']}")
    print(f"Founded: {teams[0]['founded']}")
    print(f"Owner: {teams[0]['owner']}")
    print(f"General Manager: {teams[0]['general_manager']}")
    print(f"President: {teams[0]['president']}")
    print(f"Mascot: {teams[0].get('mascot', 'N          /A')}")
    print(f"Championships Won: {teams[0].get('championships_won', 'N/A')}")
    print(f"Championship Seasons: {teams[0].get('championship_seasons', 'N/A')}")
    print(f"Playoff Appearances: {teams[0]['playoff_appearances']}")
    print(f"Venue Name: {teams[0]['venue_name']}")
