def findQuestionWords(word, question_words):
    #only supporting unique question words
    for q in question_words:
        if q in word:
            return q
    return

def findAllQuestionWords(question):
    q_word_list = question[0].split()
    w_number = 0
    q_words = question[1]
    q_number = 0
    q_words_located = []
    for q in q_words:
        for w in q_word_list:
            if q in w:
                q_words_located.append(q_number)
                q_word_list = q_word_list[w_number+1:]
                q_number += 1
                break
            else:
                q_words_located.append(False)
            w_number += 1
    return q_words_located

def composeQuestionString(question,q_number):
    """inputs:
    1. a question of the following form:
    question = ["python is answer", ["answer"]]
    2. question number (0-based)
    output is a string with the remaining question words replaced with blanks.
    question words must be unique"""

    question_string = question[0].split()
    question_words = question[1][q_number:]
    blanked_q = []
    for w in question_string:
        q = findQuestionWords(w, question_words)
        if q != None:
            w = w.replace(q, "_____")
        blanked_q.append(w)
    blanked_q_string = " ".join(blanked_q)
    return blanked_q_string

def answerQuestion(question):
    """loops over the question words in the question"""
    q_number = 0
    for q in question[1]:
        answered = False
        blanked_q_string = composeQuestionString(question,q_number)
        print "Question {0}:".format(q_number+1)
        print blanked_q_string
        while answered == False:
            answer = raw_input("Answer: ")
            if answer.lower() == q.lower():
                print "Correct!"
                answered = True
            else:
                print "Sorry, that's not correct. Try again: "
        q_number += 1

    return

question = ["this is a stupid question, luckily it's only a test",["stupid", "test"]]

#answerQuestion(question)

def tests():
    #findQuestionWords
    question_words = ["test", "another_test"]
    test_words = ["test", "test,", "negative"]

    assert findQuestionWords(test_words[0],question_words) == "test"
    assert findQuestionWords(test_words[1],question_words) == "test"
    assert findQuestionWords(test_words[2],question_words) == None

    #findAllQuestionWords, composeQuestionString
    questions = [
    ["this is a test", ["test"]],
    ["this is a test1, and test2", ["test1", "test2"]],
    ["a test, another test", ["test", "test"]],
    ["this is a neg1", ["test"]],
    ["this is a test", ["neg2"]]
    ]

    assert composeQuestionString(questions[0],0) == "this is a _____"
    assert composeQuestionString(questions[1],0) == "this is a _____, and _____"
    assert composeQuestionString(questions[2],0) == "a _____, another _____"
    assert composeQuestionString(questions[3],0) == "this is a neg1"
    assert composeQuestionString(questions[4],0) == "this is a test"
    assert composeQuestionString(questions[1],1) == "this is a test1, and _____"
    #assert composeQuestionString(questions[2],1) == "a test, another _____"

    assert findAllQuestionWords(questions[0]) == [False, False, False, 0]
    assert findAllQuestionWords(questions[1]) == [False, False, False, 0, False, 1]
    assert findAllQuestionWords(questions[2]) == [False, 0, False, 1]
    assert findAllQuestionWords(questions[3]) == [False, False, False, False]
    assert findAllQuestionWords(questions[4]) == [False, False, False, False]

    #ran all tests
    print "ran all tests"

tests()
