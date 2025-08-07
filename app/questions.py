from app.team_data import get_teams
from app.team_data import variables

#import all lists 
from app.team_data import list_alias
from app.team_data import list_market
from app.team_data import list_name
from app.team_data import list_founded
from app.team_data import list_owner
from app.team_data import list_general_manager
from app.team_data import list_president
from app.team_data import list_mascot
from app.team_data import list_championships_won
from app.team_data import list_playoff_appearances
from app.team_data import list_venue_name


import random 

questions = 0

while questions < 6: 
    selected_variable = random.choice(variables)
    selected_team = random.choice(list_name)

    print(f"What is the ",selected_variable,"for ",selected_team,"?")
    quetions = questions + 1






