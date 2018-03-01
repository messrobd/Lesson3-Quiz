def blankQuestionWords(word, question_words):
    #only supporting unique question words
    for q in question_words:
        if q in word:
            return "_____"
    return

def poseQuestion(question):
    question_string = question[0].split()
    return question_string



def tests():
    #blankQuestionWords
    question_words = ["test", "another_test"]
    test_words = ["test", "test,", "negative"]

    assert blankQuestionWords(test_words[0],question_words) == "_____"
    assert blankQuestionWords(test_words[1],question_words) == "_____"
    assert blankQuestionWords(test_words[2],question_words) == None

    question = ["this is a test", ["test"]]

    assert poseQuestion(question) == ["this", "is", "a", "test"]

    print "ran all tests"

tests()
