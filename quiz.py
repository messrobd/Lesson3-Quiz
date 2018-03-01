def poseQuestion(question):
    question_string = question[0].split()
    return question_string



def tests():
    question = ["this is a test", ["test"]]

    assert poseQuestion(question) == ["this", "is", "a", "test"]

    print "ran all tests"

tests()
