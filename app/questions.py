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

correct_count = 0
random_teams = random.sample(range(0, 32), 5)

if __name__ == "__main__":
    for team in random_teams: 
        random_variables = random.randint(0, 6)
        if random_variables == 0:
            print(f"What is the alias of the {list_name[team]}?")
            answer_alias = list_alias[team]
            filtered_alias = [alias for alias in list_alias if alias != answer_alias]
            wrong_alias = random.sample(filtered_alias, 3)
            choices_alias = wrong_alias + [answer_alias]
            random.shuffle(choices_alias)
            for index, choice in enumerate(choices_alias, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_alias):
                    selected_choice = choices_alias[selected_index]
                    if selected_choice == answer_alias:
                        print("Correct answer!")
                        correct_count = correct_count +1
                        print()
                    else:
                        print(f"Incorrect. The right answer is {answer_alias}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
        #next variable
        elif random_variables == 1: 
            print(f"Where do the {list_name[team]} play?")
            answer_market = list_market[team]
            filtered_market = [market for market in list_market if market != answer_market]
            wrong_market = random.sample(filtered_market, 3)
            choices_market = wrong_market + [answer_market]
            random.shuffle(choices_market)
            for index, choice in enumerate(choices_market, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_market):
                    selected_choice = choices_market[selected_index]
                    if selected_choice == answer_market:
                        print("Correct answer!")
                        print()
                        correct_count = correct_count +1
                    else:
                        print(f"Incorrect. The right answer is {answer_market}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
        #next variable
        elif random_variables == 2: 
            print(f"Who is the owner of the {list_name[team]}?")
            answer_owner = list_owner[team]
            filtered_owner = [owner for owner in list_owner if owner != answer_owner]
            wrong_owner = random.sample(filtered_owner, 3)
            choices_owner = wrong_owner + [answer_owner]
            random.shuffle(choices_owner)
            for index, choice in enumerate(choices_owner, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_owner):
                    selected_choice = choices_owner[selected_index]
                    if selected_choice == answer_owner:
                        print("Correct answer!")
                        print()
                        correct_count = correct_count +1
                    else:
                        print(f"Incorrect. The right answer is {answer_owner}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
        #next variable
        elif random_variables == 3: 
            print(f"Who is the general manager of the {list_name[team]}?")
            answer_general_manager = list_general_manager[team]
            filtered_general_manager = [general_manager for general_manager in list_general_manager if general_manager != answer_general_manager]
            wrong_general_manager = random.sample(filtered_general_manager, 3)
            choices_general_manager = wrong_general_manager + [answer_general_manager]
            random.shuffle(choices_general_manager)
            for index, choice in enumerate(choices_general_manager, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_general_manager):
                    selected_choice = choices_general_manager[selected_index]
                    if selected_choice == answer_general_manager:
                        print("Correct answer!")
                        print()
                        correct_count = correct_count +1
                    else:
                        print(f"Incorrect. The right answer is {answer_general_manager}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
        #next variable
        elif random_variables == 4: 
            print(f"Who is the president of the {list_name[team]}?")
            answer_president = list_president[team]
            filtered_president = [president for president in list_president if president != answer_president]
            wrong_president = random.sample(filtered_president, 3)
            choices_president = wrong_president + [answer_president]
            random.shuffle(choices_president)
            for index, choice in enumerate(choices_president, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_president):
                    selected_choice = choices_president[selected_index]
                    if selected_choice == answer_president:
                        print("Correct answer!")
                        print()
                        correct_count = correct_count +1
                    else:
                        print(f"Incorrect. The right answer is {answer_president}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
        #next variable
        elif random_variables == 5: 
            print(f"What is the mascot of the {list_name[team]}?")
            answer_mascot = list_mascot[team]
            filtered_mascot = [mascot for mascot in list_mascot if mascot != answer_mascot]
            wrong_mascot = random.sample(filtered_mascot, 3)
            choices_mascot = wrong_mascot + [answer_mascot]
            random.shuffle(choices_mascot)
            for index, choice in enumerate(choices_mascot, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_mascot):
                    selected_choice = choices_mascot[selected_index]
                    if selected_choice == answer_mascot:
                        print("Correct answer!")
                        print()
                        correct_count = correct_count +1
                    else:
                        print(f"Incorrect. The right answer is {answer_mascot}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
        #next variable
        elif random_variables == 6: 
            print(f"What stadium do the {list_name[team]} play in?")
            answer_venue = list_venue_name[team]
            filtered_venue = [venue for venue in list_venue_name if venue != answer_venue]
            wrong_venue = random.sample(filtered_venue, 3)
            choices_venue = wrong_venue + [answer_venue]
            random.shuffle(choices_venue)
            for index, choice in enumerate(choices_venue, start=1):
                print(f"{index}. {choice}")
            user_input = input("Choose the correct option (1-4): ")
            try:
                selected_index = int(user_input) - 1  # Convert to 0-based index

                if 0 <= selected_index < len(choices_venue):
                    selected_choice = choices_venue[selected_index]
                    if selected_choice == answer_venue:
                        print("Correct answer!")
                        print()
                        correct_count = correct_count +1
                    else:
                        print(f"Incorrect. The right answer is {answer_venue}.")
                        print()
                else:
                    print("Invalid choice. Please pick a number between 1 and 4.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a number.")
                print()
    
    print(f"You got {correct_count} questions correct!")








