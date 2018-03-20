#functions
def define3LevelGame(easy_question, medium_question, hard_question):
    """
    1. Behaviour: packs the questions corresponding to 3 named
    levels (easy, medium, hard) into a single object
    2. Inputs: 3 questions
    3. Outputs: a tuple containing 3 values:
        i. a list of level objects, each which has a name and a question
        ii. the locations of the name and question values within
        each level object
    """
    easy_level = ["Easy", easy_question]
    medium_level = ["Medium", medium_question]
    hard_level = ["Hard", hard_question]

    game = [easy_level, medium_level, hard_level]
    level_label_index = 0
    level_question_index = 1

    return game, level_label_index, level_question_index

def pickLevel(gamelevels, level_label_index):
    """
    1. Behaviour: shows the user the available levels, and
    prompts them user to pick one
    2. Inputs: a list of game levels, and the location of the level
    label value
    3. Outputs: the chosen level object
    """
    print "Pick a level:"
    for level in gamelevels:
        print "{0} - {1}".format(gamelevels.index(level), level[level_label_index])
    valid_pick = False
    while valid_pick == False:
        pick = raw_input()
        try:
            pick = gamelevels[int(pick)]
            valid_pick = True
        except:
            print "Please pick a number 0 - {0}".format(len(gamelevels)-1)

    return pick

def prepareQuestion(question):
    """
    1. Behaviour: performs a rudimentary check that the question object
    is formed per expectations (below), and returns the 2 expected parts
    2. Inputs: a question formatted as follows:
    ["the question string including a ?question word", ["question"]]
    3. Outputs: the question parts:
        i. a list containing all the words in the question string
        ii. a list containing those words that are to be blanked
    """
    required_question_fields = 2
    try:
        assert len(question) == required_question_fields
    except:
        "Invalid question format: missing field"

    question_string_index = 0
    question_words_index = 1
    try:
        question_list = question[question_string_index].split()
        question_words = question[question_words_index]
    except:
        "Invalid question format"

    return question_list, question_words

def locateQuestionWords(question_list, question_words):
    """
    1. Behaviour: wherever there is a tagged word in the question, do 2 things:
        i. remove the tag
        ii. store it as a numbered question
    2. Inputs: 2 lists, 1 containing all words, the other conatining those
    that are to be blanked
    3. Outputs: the processed results:
        i. a list containing all the words in the question string, with tags
        removed
        ii. a list with numbers wherever there is a question, in the string, and
        empty strings everywhere else
    """
    question_tag, question_tag_index = "?", 0
    question_number = 0
    question_word_locations = []
    question_list_detagged = []

    for word in question_list:
        element = ""
        word_number = question_list.index(word)
        for question in question_words:
            if question in word and word[question_tag_index] == question_tag:
                element = question_number
                word = word[1:]
                question_words = question_words[1:]
                question_number += 1
                break
        question_word_locations.append(element)
        question_list_detagged.append(word)

    return question_word_locations, question_list_detagged

def getAnsweredPart(question_list, question_words, question_number):
    """
    1. Behaviour: finds the part of the question string that precedes
    the current question
    2. Inputs: the list of all words in the question, the list of words
    to be blanked, and the current question number
    3. Outputs: a list of words preceding the current question
    """
    question_word_locations, question_list_detagged = locateQuestionWords(question_list, question_words)
    try:
        question_index = question_word_locations.index(question_number)
    except:
        return "No matching question words found in question"

    answered_list = question_list_detagged[:question_index]

    return answered_list

def makeUnansweredPart(question_list, question_words, question_number):
    """
    1. Behaviour: finds the part of the question string from the current
    question onwards, and inserts blanks wherever there is a question
    remaining to be answered
    2. Inputs: the list of all words in the question, the list of words
    to be blanked, and the current question number
    3. Outputs: a list of words from the current question onwards, with blanks
    in place of the remaining question words
    """
    question_word_locations, question_list_detagged = locateQuestionWords(question_list, question_words)
    try:
        question_index = question_word_locations.index(question_number)
    except:
        return "No matching question words found in question"

    question_list_detagged = question_list_detagged[question_index:]

    unanswered_list = []
    for word in question_list_detagged:
        for question in question_words:
            if question in word:
                blank = "_" * len(question)
                word = word.replace(question, blank)
                question_list_detagged = question_list_detagged[1:]
                question_words = question_words[1:]
                question_number += 1
                break
        unanswered_list.append(word)

    return unanswered_list

def makeCurrentAnswerElement(question_list, question_words, question_number):
    """
    1. Behaviour: finds the element from the question string corresponding to
    the current question, and returns it in upper case
    2. Inputs: the list of all words in the question, the list of words
    to be blanked, and the current question number
    3. Outputs: a string in upper case from the question list, corresponding to the current
    question
    """
    question_word_locations, question_list_detagged = locateQuestionWords(question_list, question_words)
    try:
        question_index = question_word_locations.index(question_number)
    except:
        return "No matching question words found in question"

    unanswered_word = question_list_detagged[question_index].upper()

    return unanswered_word


def composeQuestionString(question_list, question_words):
    """
    1. Behaviour: splices together the question lists either side of the
    first question
    2. Inputs: the list of all words in the question, and the list of words
    to be blanked
    3. Outputs: the question list, as a string, with blanks in place of all
    question words
    """
    question_number = 0
    answered_list = getAnsweredPart(question_list, question_words, question_number)
    unanswered_list = makeUnansweredPart(question_list, question_words, question_number)

    question_string = " ".join(answered_list + unanswered_list)

    return question_string

def composeResponseString(question_list, question_words, question_number):
    """
    1. Behaviour: splices together the question lists either side of the
    current question, with the answer to the current question in upper case
    2. Inputs: the list of all words in the question, the list of words
    to be blanked, and the current question number
    3. Outputs: the question list, as a string, with the current question in
    upper case and the remaining questions blanked
    """
    answered_list = getAnsweredPart(question_list, question_words, question_number)
    unanswered_list  = makeUnansweredPart(question_list, question_words, question_number)
    unanswered_word = makeCurrentAnswerElement(question_list, question_words, question_number)

    answered_list.append(unanswered_word)

    response_string = " ".join(answered_list + unanswered_list[1:])

    return response_string

def askQuestion(question_list, question_words):
    """
    1. Behaviour: composes a string to show at the beginning of the game
    2. Inputs: the list of all words in the question, and the list of words
    to be blanked
    3. Outputs: a string comprising a prompt followed by the question list
    """
    question_string = composeQuestionString(question_list, question_words)
    return ("\nQuestion: \n" + question_string)

def checkAnswer(question_words, question_number):
    """
    1. Behaviour: prompts the user to answer the current question. Gives them a
    number of attempts to do so before returning
    2. Inputs: the list of question words, and the current question number
    3. Outputs: True if the question was answered correctly, None if it isn't
    """
    question_word = question_words[question_number]

    answered = False
    lives = 5
    while answered == False and lives >= 1:
        answer = raw_input("Answer to blank number {0}: ".format(question_number+1))
        if answer.lower() == question_word.lower():
            answered = True
            return answered
        elif lives > 1:
            lives -= 1
            print "Sorry, that's not correct. Try again ({0} attempts left): ".format(lives)
        else:
            return

def giveResponse(question_list, question_words, question_number, answer):
    """
    1. Behaviour: composes a string to show in response to the user's attempt
    to answer the question
    2. Inputs: the list of all words in the question, the list of words
    to be blanked, the current question number, and the result of the user's
    attempt to answer
    3. Outputs: a string comprising a response message, followed by the
    response string for the current question
    """
    response_string = composeResponseString(question_list, question_words, question_number)
    question_word = question_words[question_number]

    if answer:
        return ("\nCorrect! \n" + response_string)
    else:
        return ("\nUnlucky. The answer is {0} \n".format(question_word.upper()) + response_string)


def play(game):
    """
    1. Behaviour: initiates a game, and steps through the question words in the
    chosen level until they have all been attempted
    2. Inputs: a game
    3. Outputs: the game result, in the form of a score
    """
    gamelevels, level_label_index, level_question_index = game
    level = pickLevel(gamelevels, level_label_index)
    level_question = level[level_question_index]
    question_list, question_words = prepareQuestion(level_question)

    print (askQuestion(question_list, question_words) + "\n")

    score = 0
    for question in question_words:
        question_number = question_words.index(question)
        answer = checkAnswer(question_words, question_number)
        print (giveResponse(question_list, question_words, question_number, answer) + "\n")
        if answer:
            score += 1

    print "You're done! You scored {0} out of {1}".format(score, len(question_words))

    return

#gameplay
easy_question = ["""
It is often necessary to repeat a block of code, for example when it needs to be executed
for each of a set of entities. A ?loop is a statement that allows this. Python provides 2
loop concepts. A ?for loop iterates over every element in a list. A ?while loop continues until
a defined condition is met; the condition must be calculated in the loop to prevent ?infinite
repetitions.
""", ["loop", "for", "while", "infinite"]]
medium_question = ["""
It is important to structure python code around functions, also known as ?procedures. Without them,
?control logic can be complicated and highly nested. Functions also allow you to ?reuse code, and
helps you ?test your code by creating independently addressable units.
""", ["procedures", "control", "reuse", "test"]]
hard_question = ["""
A ?list is a structured data type in python. Lists have many operations in common with the ?string
type, such as index operations. This is because strings are also lists (of characters).
However, lists differ in an important way: they are ?mutable. This means many variables can refer
to the same list; this is known as ?aliasing. Because of this property, a change to a list via one
variable can propagate to other variables.
""", ["list", "string", "mutable", "aliasing"]]

game = define3LevelGame(easy_question, medium_question, hard_question)
play(game)

#testing
def tests():
    questions = [
    ["this is a ?test", ["test"]],
    ["a ?test, this is", ["test"]],
    ["this is a ?test1, ?test2, ?test3 and ?test4", ["test1", "test2", "test3", "test4"]],
    ["a ?test, another ?test", ["test", "test"]],
    ["this is not a test, but this is a ?test",["test"]],
    ["this is a ?test, but this is not a test",["test"]],
    ["this is a neg1", ["test"]],
    ["this is a test", ["neg2"]]
    ]
    #prepareQuestion
    assert prepareQuestion(questions[0]) == (["this", "is", "a", "?test"], ["test"])
    assert prepareQuestion(questions[1]) == (["a", "?test,", "this", "is"], ["test"])
    assert prepareQuestion(questions[2]) == (["this", "is", "a", "?test1,", "?test2,", "?test3", "and", "?test4"], ['test1', 'test2', 'test3', 'test4'])
    assert prepareQuestion(questions[3]) == (["a", "?test,", "another", "?test"], ["test", "test"])
    assert prepareQuestion(questions[4]) == (["this", "is", "not", "a", "test,", "but", "this", "is", "a", "?test"],["test"])
    assert prepareQuestion(questions[5]) == (["this", "is", "a", "?test,", "but", "this", "is", "not", "a", "test"],["test"])
    assert prepareQuestion(questions[6]) == (["this", "is", "a", "neg1"], ["test"])
    assert prepareQuestion(questions[7]) == (["this", "is", "a", "test"], ["neg2"])

    #locateQuestionWords
    question_list_0, question_words_0 = prepareQuestion(questions[0])
    question_list_1, question_words_1 = prepareQuestion(questions[1])
    question_list_2, question_words_2 = prepareQuestion(questions[2])
    question_list_3, question_words_3 = prepareQuestion(questions[3])
    question_list_4, question_words_4 = prepareQuestion(questions[4])
    question_list_5, question_words_5 = prepareQuestion(questions[5])
    question_list_6, question_words_6 = prepareQuestion(questions[6])
    question_list_7, question_words_7 = prepareQuestion(questions[7])

    assert locateQuestionWords(question_list_0, question_words_0)[0] == ["", "", "", 0]
    assert locateQuestionWords(question_list_1, question_words_1)[0] == ["", 0, "", ""]
    assert locateQuestionWords(question_list_2, question_words_2)[0] == ["", "", "", 0, 1, 2, "", 3]
    assert locateQuestionWords(question_list_3, question_words_3)[0] == ["", 0, "", 1]
    assert locateQuestionWords(question_list_4, question_words_4)[0] == ["", "", "", "", "", "", "", "", "", 0]
    assert locateQuestionWords(question_list_5, question_words_5)[0] == ["", "", "", 0, "", "", "", "", "", ""]
    assert locateQuestionWords(question_list_6, question_words_6)[0] == ["", "", "", ""]
    assert locateQuestionWords(question_list_7, question_words_7)[0] == ["", "", "", ""]

    #getAnsweredPart
    question_list_0, question_words_0 = prepareQuestion(questions[0])
    question_list_1, question_words_1 = prepareQuestion(questions[1])
    question_list_2, question_words_2 = prepareQuestion(questions[2])
    question_list_3, question_words_3 = prepareQuestion(questions[3])
    question_list_4, question_words_4 = prepareQuestion(questions[4])
    question_list_5, question_words_5 = prepareQuestion(questions[5])
    question_list_6, question_words_6 = prepareQuestion(questions[6])
    question_list_7, question_words_7 = prepareQuestion(questions[7])

    assert getAnsweredPart(question_list_0, question_words_0,0) == ["this", "is", "a"]
    assert getAnsweredPart(question_list_1, question_words_1,0) == ["a"]
    assert getAnsweredPart(question_list_2, question_words_2,0) == ["this", "is", "a"]
    assert getAnsweredPart(question_list_3, question_words_3,0) == ["a"]
    assert getAnsweredPart(question_list_4, question_words_4,0) == ["this", "is", "not", "a", "test,", "but", "this", "is", "a"]
    assert getAnsweredPart(question_list_5, question_words_5,0) == ["this", "is", "a"]
    assert getAnsweredPart(question_list_2, question_words_2,1) == ["this", "is", "a", "test1,"]
    assert getAnsweredPart(question_list_3, question_words_3,1) == ["a", "test,", "another"]
    assert getAnsweredPart(question_list_6, question_words_6,0) == "No matching question words found in question"
    assert getAnsweredPart(question_list_7, question_words_7,0) == "No matching question words found in question"

    #makeUnansweredPart
    question_list_0, question_words_0 = prepareQuestion(questions[0])
    question_list_1, question_words_1 = prepareQuestion(questions[1])
    question_list_2, question_words_2 = prepareQuestion(questions[2])
    question_list_3, question_words_3 = prepareQuestion(questions[3])
    question_list_4, question_words_4 = prepareQuestion(questions[4])
    question_list_5, question_words_5 = prepareQuestion(questions[5])
    question_list_6, question_words_6 = prepareQuestion(questions[6])
    question_list_7, question_words_7 = prepareQuestion(questions[7])

    assert makeUnansweredPart(question_list_0, question_words_0,0) == ["____"]
    assert makeUnansweredPart(question_list_1, question_words_1,0) == ["____,", "this", "is"]
    assert makeUnansweredPart(question_list_2, question_words_2,0) == ["_____,", "_____,", "_____", "and", "_____"]
    assert makeUnansweredPart(question_list_3, question_words_3,0) == ["____,", "another", "____"]
    assert makeUnansweredPart(question_list_4, question_words_4,0) == ["____"]
    assert makeUnansweredPart(question_list_5, question_words_5,0) == ["____,", "but", "this", "is", "not", "a", "test"]
    assert makeUnansweredPart(question_list_2, question_words_2,1) == ["_____,", "_____", "and", "_____"]
    assert makeUnansweredPart(question_list_3, question_words_3,1) == ["____"]
    assert makeUnansweredPart(question_list_6, question_words_6,0) == "No matching question words found in question"
    assert makeUnansweredPart(question_list_7, question_words_7,0) == "No matching question words found in question"

    #makeCurrentAnswerElement
    question_list_0, question_words_0 = prepareQuestion(questions[0])
    question_list_1, question_words_1 = prepareQuestion(questions[1])
    question_list_2, question_words_2 = prepareQuestion(questions[2])
    question_list_3, question_words_3 = prepareQuestion(questions[3])
    question_list_4, question_words_4 = prepareQuestion(questions[4])
    question_list_5, question_words_5 = prepareQuestion(questions[5])
    question_list_6, question_words_6 = prepareQuestion(questions[6])
    question_list_7, question_words_7 = prepareQuestion(questions[7])

    assert makeCurrentAnswerElement(question_list_0, question_words_0,0) == "TEST"
    assert makeCurrentAnswerElement(question_list_1, question_words_1,0) == "TEST,"
    assert makeCurrentAnswerElement(question_list_2, question_words_2,0) == "TEST1,"
    assert makeCurrentAnswerElement(question_list_3, question_words_3,0) == "TEST,"
    assert makeCurrentAnswerElement(question_list_4, question_words_4,0) == "TEST"
    assert makeCurrentAnswerElement(question_list_5, question_words_5,0) == "TEST,"
    assert makeCurrentAnswerElement(question_list_2, question_words_2,1) == "TEST2,"
    assert makeCurrentAnswerElement(question_list_3, question_words_3,1) == "TEST"
    assert makeCurrentAnswerElement(question_list_6, question_words_6,0) == "No matching question words found in question"
    assert makeCurrentAnswerElement(question_list_7, question_words_7,0) == "No matching question words found in question"

    #composeQuestionString
    question_list_0, question_words_0 = prepareQuestion(questions[0])
    question_list_1, question_words_1 = prepareQuestion(questions[1])
    question_list_2, question_words_2 = prepareQuestion(questions[2])
    question_list_3, question_words_3 = prepareQuestion(questions[3])
    question_list_4, question_words_4 = prepareQuestion(questions[4])
    question_list_5, question_words_5 = prepareQuestion(questions[5])
    question_list_6, question_words_6 = prepareQuestion(questions[6])
    question_list_7, question_words_7 = prepareQuestion(questions[7])

    assert composeQuestionString(question_list_0, question_words_0) == "this is a ____"
    assert composeQuestionString(question_list_1, question_words_1) == "a ____, this is"
    assert composeQuestionString(question_list_2, question_words_2) == "this is a _____, _____, _____ and _____"
    assert composeQuestionString(question_list_3, question_words_3) == "a ____, another ____"
    assert composeQuestionString(question_list_4, question_words_4) == "this is not a test, but this is a ____"
    assert composeQuestionString(question_list_5, question_words_5) == "this is a ____, but this is not a test"
    #assert composeQuestionString(question_list_6, question_words_6,0) == "No matching question words found in question"
    #assert composeQuestionString(question_list_7, question_words_7,0) == "No matching question words found in question"

    #composeResponseString
    question_list_0, question_words_0 = prepareQuestion(questions[0])
    question_list_1, question_words_1 = prepareQuestion(questions[1])
    question_list_2, question_words_2 = prepareQuestion(questions[2])
    question_list_3, question_words_3 = prepareQuestion(questions[3])
    question_list_4, question_words_4 = prepareQuestion(questions[4])
    question_list_5, question_words_5 = prepareQuestion(questions[5])
    question_list_6, question_words_6 = prepareQuestion(questions[6])
    question_list_7, question_words_7 = prepareQuestion(questions[7])

    assert composeResponseString(question_list_0, question_words_0,0) == "this is a TEST"
    assert composeResponseString(question_list_1, question_words_1,0) == "a TEST, this is"
    assert composeResponseString(question_list_2, question_words_2,0) == "this is a TEST1, _____, _____ and _____"
    assert composeResponseString(question_list_3, question_words_3,0) == "a TEST, another ____"
    assert composeResponseString(question_list_4, question_words_4,0) == "this is not a test, but this is a TEST"
    assert composeResponseString(question_list_5, question_words_5,0) == "this is a TEST, but this is not a test"
    assert composeResponseString(question_list_2, question_words_2,1) == "this is a test1, TEST2, _____ and _____"
    assert composeResponseString(question_list_3, question_words_3,1) == "a test, another TEST"

    #define3LevelGame
    game = define3LevelGame(questions[0], questions[1], questions[2])
    gamelevels, level_label_index, level_question_index = game
    assert game[0][0][level_label_index] == "Easy"
    assert game[0][1][level_label_index] == "Medium"
    assert game[0][2][level_label_index] == "Hard"
    assert game[0][0][level_question_index] == ["this is a ?test", ["test"]]
    assert game[0][1][level_question_index] == ["a ?test, this is", ["test"]]
    assert game[0][2][level_question_index] == ["this is a ?test1, ?test2, ?test3 and ?test4", ["test1", "test2", "test3", "test4"]]

    #play(game)

    #ran all tests
    print "ran all tests"

#tests()
