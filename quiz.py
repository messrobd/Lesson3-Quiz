def findAllQuestionWords(question):
    q_list = question[0].split()
    w_number = 0
    q_words = question[1]
    q_number = 0
    q_words_located = []
    for q in q_words:
        for w in q_list:
            if q in w:
                q_words_located.append(q_number)
                q_list = q_list[w_number+1:]
                q_number += 1
                break
            else:
                q_words_located.append("")
            w_number += 1
    return q_words_located

def getAnsweredQuestionString(question,q_number):
    q_list = question[0].split()
    q_words_located = findAllQuestionWords(question)
    q_index = q_words_located.index(q_number)
    a_list = q_list[:q_index]
    return q_index, a_list

def composeQuestionString(question,q_number):
    q_index, a_list = getAnsweredQuestionString(question,q_number)
    q_list = question[0].split()[q_index:]
    q_words = question[1][q_number:]

    for w in q_list:
        for q in q_words:
            if q in w:
                b = "_" * len(q)
                w = w.replace(q, b)
                a_list.append(w)
                q_list = q_list[q_index+1:]
                q_words = q_words[q_number+1:]
                q_number += 1
                break
            else:
                a_list.append(w)
            q_index += 1

    q_string = " ".join(a_list)
    return q_string


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
    #findAllQuestionWords, composeQuestionString
    questions = [
    ["this is a test", ["test"]],
    ["this is a test1, and test2", ["test1", "test2"]],
    ["a test, another test", ["test", "test"]],
    ["this is a neg1", ["test"]],
    ["this is a test", ["neg2"]]
    ]

    assert composeQuestionString(questions[0],0) == "this is a ____"
    assert composeQuestionString(questions[1],0) == "this is a _____, and _____"
    assert composeQuestionString(questions[2],0) == "a ____, another ____"
    #assert composeQuestionString(questions[3],0) == "this is a neg1" negative tests fail
    #assert composeQuestionString(questions[4],0) == "this is a test" negative tests fail
    assert composeQuestionString(questions[1],1) == "this is a test1, and _____"
    assert composeQuestionString(questions[2],1) == "a test, another ____"
    """
    print composeQuestionString(questions[0],0)
    print composeQuestionString(questions[1],0)
    print composeQuestionString(questions[2],0)
    #print composeQuestionString(questions[3],0) negative tests fail
    #print composeQuestionString(questions[4],0) negative tests fail
    print composeQuestionString(questions[1],1)
    print composeQuestionString(questions[2],1)
    """
    assert findAllQuestionWords(questions[0]) == ["", "", "", 0]
    assert findAllQuestionWords(questions[1]) == ["", "", "", 0, "", 1]
    assert findAllQuestionWords(questions[2]) == ["", 0, "", 1]
    assert findAllQuestionWords(questions[3]) == ["", "", "", ""]
    assert findAllQuestionWords(questions[4]) == ["", "", "", ""]

    #ran all tests
    print "ran all tests"

tests()
