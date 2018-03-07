def define3LevelGame(easy_q, medium_q, hard_q):
    easy_level = ["Easy", easy_q]
    medium_level = ["Medium", medium_q]
    hard_level = ["Hard", hard_q]

    game = [easy_level, medium_level, hard_level]

    return game

def pickLevel(game):
    print "Pick a level:"
    for g in game:
        print "{0} - {1}".format(game.index(g), g[0])
    valid_pick = False
    while valid_pick == False:
        pick = raw_input()
        try:
            pick = game[int(pick)]
            valid_pick = True
        except:
            print "Please pick a number 0 - {0}".format(len(game)-1)
    return pick

def makeQuestionLists(question):
    q_list = question[0].split()
    q_words = question[1]
    q_number = 0
    q_words_located = []
    for w in q_list:
        e = ""
        w_number = q_list.index(w)
        for q in q_words:
            if q in w and w[0] == "?":
                e = q_number
                q_list[w_number] = w[1:]
                q_words = q_words[1:]
                q_number += 1
                break
        q_words_located.append(e)

    return q_list, q_words_located

def getAnsweredQuestionPart(question,q_number):
    try:
        q_list, q_words_located = makeQuestionLists(question)
        q_index = q_words_located.index(q_number)
        a_list = q_list[:q_index]
    except:
        return "No matching question words found in question"

    return q_index, a_list

def composeQuestionString(question,q_number):
    try:
        q_index, a_list = getAnsweredQuestionPart(question,q_number)
        q_list = makeQuestionLists(question)[0][q_index:]
        q_words = question[1][q_number:]
    except:
        return "No matching question words found in question"

    for w in q_list:
        for q in q_words:
            if q in w:
                b = "_" * len(q)
                w = w.replace(q, b)
                q_list = q_list[q_index+1:]
                q_words = q_words[q_number+1:]
                q_number += 1
                break
            q_index += 1
        a_list.append(w)
    q_string = " ".join(a_list)

    return q_string


def answerQuestion(question, q_number):
    q_string = composeQuestionString(question,q_number)
    q = question[1][q_number]

    print "Question {0}:".format(q_number+1)
    print q_string
    answered = False
    lives = 5
    while answered == False and lives >= 1:
        answer = raw_input("Answer: ")
        if answer.lower() == q.lower():
            print "Correct!"
            answered = True
            return
        elif lives > 1:
            lives -= 1
            print "Sorry, that's not correct. Try again ({0} attempts left): ".format(lives)
        else:
            print "Unlucky. The answer is {0}".format(q.upper())
            return

def play(game):
    level = pickLevel(game)
    question = level[1]
    q_words = question[1]

    for q in q_words:
        q_number = q_words.index(q)
        answerQuestion(question, q_number)

    return


question = ["this is a stupid question, luckily it's only a test",["stupid", "test"]]

#answerQuestion(question, 1)
# play(question)

def tests():
    questions = [
    ["this is a ?test", ["test"]],
    ["a ?test, this is", ["test"]],
    ["this is a ?test1, and ?test2", ["test1", "test2"]],
    ["a ?test, another ?test", ["test", "test"]],
    ["this is not a test, but this is a ?test",["test"]],
    ["this is a ?test, but this is not a test",["test"]],
    ["this is a neg1", ["test"]],
    ["this is a test", ["neg2"]]
    ]
    #findAllQuestionWords
    assert makeQuestionLists(questions[0])[1] == ["", "", "", 0]
    assert makeQuestionLists(questions[1])[1] == ["", 0, "", ""]
    assert makeQuestionLists(questions[2])[1] == ["", "", "", 0, "", 1]
    assert makeQuestionLists(questions[3])[1] == ["", 0, "", 1]
    assert makeQuestionLists(questions[4])[1] == ["", "", "", "", "", "", "", "", "", 0]
    assert makeQuestionLists(questions[5])[1] == ["", "", "", 0, "", "", "", "", "", ""]
    assert makeQuestionLists(questions[6])[1] == ["", "", "", ""]
    assert makeQuestionLists(questions[7])[1] == ["", "", "", ""]

    #getAnsweredQuestionString
    assert getAnsweredQuestionPart(questions[0],0) == (3, ["this", "is", "a"])
    assert getAnsweredQuestionPart(questions[1],0) == (1, ["a"])
    assert getAnsweredQuestionPart(questions[2],0) == (3, ["this", "is", "a"])
    assert getAnsweredQuestionPart(questions[3],0) == (1, ["a"])
    assert getAnsweredQuestionPart(questions[4],0) == (9, ["this", "is", "not", "a", "test,", "but", "this", "is", "a"])
    assert getAnsweredQuestionPart(questions[5],0) == (3, ["this", "is", "a"])
    assert getAnsweredQuestionPart(questions[2],1) == (5, ["this", "is", "a", "test1,", "and"])
    assert getAnsweredQuestionPart(questions[3],1) == (3, ["a", "test,", "another"])
    assert getAnsweredQuestionPart(questions[6],0) == "No matching question words found in question"
    assert getAnsweredQuestionPart(questions[7],0) == "No matching question words found in question"

    #composeQuestionString
    assert composeQuestionString(questions[0],0) == "this is a ____"
    assert composeQuestionString(questions[1],0) == "a ____, this is"
    assert composeQuestionString(questions[2],0) == "this is a _____, and _____"
    assert composeQuestionString(questions[3],0) == "a ____, another ____"
    assert composeQuestionString(questions[4],0) == "this is not a test, but this is a ____"
    assert composeQuestionString(questions[5],0) == "this is a ____, but this is not a test"
    assert composeQuestionString(questions[2],1) == "this is a test1, and _____"
    assert composeQuestionString(questions[3],1) == "a test, another ____"
    assert composeQuestionString(questions[6],0) == "No matching question words found in question"
    assert composeQuestionString(questions[7],0) == "No matching question words found in question"

    #define3LevelGame
    game = define3LevelGame(questions[0], questions[1], questions[2])
    assert game[0][0] == "Easy"
    assert game[1][0] == "Medium"
    assert game[2][0] == "Hard"
    assert game[0][1] == ["this is a ?test", ["test"]]
    assert game[1][1] == ["a ?test, this is", ["test"]]
    assert game[2][1] == ["this is a ?test1, and ?test2", ["test1", "test2"]]

    #play(game)

    #ran all tests
    print "ran all tests"

tests()
