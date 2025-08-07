from app.team_data import get_teams
from app.team_data import variables

#import all lists 
from app.team_data import list_name
from app.team_data import list_alias
from app.team_data import list_market
from app.team_data import list_owner
from app.team_data import list_general_manager
from app.team_data import list_president
from app.team_data import list_mascot
from app.team_data import list_venue_name


import random 


random_teams = random.sample(range(0, 32), 5)

for team in random_teams: 
    random_variables = random.randint(0, 7)
    if random_variables == 1:
        print("What is the alias of the", list_name[team])
    if random_variables == 2: 
        print("What is the market of the", list_name[team])
    if random_variables == 3: 
        print("Who is the owner of the", list_name[team])
    if random_variables == 4: 
        print("Who is the general owner of the", list_name[team])
    if random_variables == 5: 
        print("Who is the president of the", list_name[team])
    if random_variables == 6: 
        print("What is the mascot of the", list_name[team])
    if random_variables == 7: 
        print("What is the venue of the", list_name[team])
   


#questions = 0

#while questions < 6: 
    #selected_variable = random.choice(variables)
    #selected_team = random.choice(list_name)

    #print(f"What is the ",selected_variable,"for ",selected_team,"?")
    #quetions = questions + 1






