def findQuestionWords(word, question_words):
    #only supporting unique question words
    for q in question_words:
        if q in word:
            return q
    return

def composeQuestionString(question):
    question_string = question[0].split()
    question_words = question[1]
    blanked_q = []
    for w in question_string:
        q = findQuestionWords(w, question_words)
        if q != None:
            w = w.replace(q, "_____")
        blanked_q.append(w)
    blanked_q_string = " ".join(blanked_q)
    return blanked_q_string

def play(question):
    blanked_q_string = composeQuestionString(question)
    print blanked_q_string

    n = 1
    for q in question[1]:
        answer = raw_input("Fill in blank {0}: ".format(n))
        if answer.lower() == q.lower():
            print "Correct!"
        else:
            print "Sorry, the correct answer is {0}".format(q.upper())
        n += 1

    return

question = ["this is a test question",["test"]]

play(question)

def tests():
    #findQuestionWords
    question_words = ["test", "another_test"]
    test_words = ["test", "test,", "negative"]

    assert findQuestionWords(test_words[0],question_words) == "test"
    assert findQuestionWords(test_words[1],question_words) == "test"
    assert findQuestionWords(test_words[2],question_words) == None

    #composeQuestionString
    questions = [
    ["this is a test", ["test"]],
    ["this is a test1, and test2", ["test1", "test2"]],
    ["this is a neg1", ["test"]],
    ["this is a test", ["neg2"]]
    ]

    assert composeQuestionString(questions[0]) == "this is a _____"
    assert composeQuestionString(questions[1]) == "this is a _____, and _____"
    assert composeQuestionString(questions[2]) == "this is a neg1"
    assert composeQuestionString(questions[3]) == "this is a test"

    #ran all tests
    print "ran all tests"

tests()
