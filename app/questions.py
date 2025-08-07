import random
from app.team_data import get_teams

teams = get_teams()

question_fields = {
    "mascot": "What is the mascot of the {team_name}?",
    "owner": "Who owns the {team_name}?",
    "founded": "In what year was the {team_name} founded?",
    "president": "Who is the president of the {team_name}?",
    "general_manager": "Who is the GM of the {team_name}?",
    "championships_won": "How many championships have the {team_name} won?",
    "playoff_appearances": "How many playoff appearances have the {team_name} had?",
    "venue_name": "What stadium do the {team_name} play in?"
}

def get_random_question():
    field = random.choice(list(question_fields.keys()))
    template = question_fields[field]

    correct_team = random.choice(teams)
    correct_answer = correct_team[field]
    team_name = f"{correct_team['market']} {correct_team['name']}"

    # Getting wrong answers / used GPT to find set() function to avoid duplicates
    wrong_answers = set()
    while len(wrong_answers) < 3:
        team = random.choice(teams)
        if team != correct_team:
            wrong_answers.add(str(team[field]))
    options = list(wrong_answers) + [str(correct_answer)]
    random.shuffle(options)

    return {
        "question": template.format(team_name=team_name),
        "options": options,
        "answer": str(correct_answer)
    }