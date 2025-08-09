def test_quiz():
    import app.questions as q
    import random
    
    # test that the file runs
    assert True
    
    # test that every list has 32 items (one for each NFL team)
    assert len(q.list_name) == 32
    assert len(q.list_alias) == 32
    assert len(q.list_market) == 32
    assert len(q.list_owner) == 32
    assert len(q.list_general_manager) == 32
    assert len(q.list_president) == 32
    assert len(q.list_mascot) == 32
    assert len(q.list_venue_name) == 32
    
    # test alias question
    def test_alias_choices():
        team = 0
        answer = q.list_alias[team]
        wrong = [a for a in q.list_alias if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1

    # test market question
    def test_market_choices():
        team = 0
        answer = q.list_market[team]
        wrong = [a for a in q.list_market if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1

    # test owner question
    def test_owner_choices():
        team = 0
        answer = q.list_owner[team]
        wrong = [a for a in q.list_owner if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1

    # test general manager question
    def test_gm_choices():
        team = 0
        answer = q.list_general_manager[team]
        wrong = [a for a in q.list_general_manager if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1

    # test president question
    def test_president_choices():
        team = 0
        answer = q.list_president[team]
        wrong = [a for a in q.list_president if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1

    # test mascot question
    def test_mascot_choices():
        team = 0
        answer = q.list_mascot[team]
        wrong = [a for a in q.list_mascot if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1

    # test venue question
    def test_venue_choices():
        team = 0
        answer = q.list_venue_name[team]
        wrong = [a for a in q.list_venue_name if a != answer]
        choices = random.sample(wrong, 3) + [answer]
        random.shuffle(choices)

        # test that there are 4 unique choices and one of them is the answer
        assert len(choices) == 4
        assert len(set(choices)) == 4
        assert choices.count(answer) == 1
