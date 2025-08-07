from app.questions import get_random_question
from app.team_data import get_teams

q = get_random_question()

def test_qs():
    assert q is not None
    assert len(q["options"]) == 4
    assert q["answer"] in q["options"]
    assert q["question"] is not None