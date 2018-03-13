#functions
def define3LevelGame(easy_q, medium_q, hard_q):
    """outputs a game composed of 3 questions corresponding to the
    easy, medium, and hard levels"""
    easy_level = ["Easy", easy_q]
    medium_level = ["Medium", medium_q]
    hard_level = ["Hard", hard_q]

    game = [easy_level, medium_level, hard_level]
    level_label_index = 0
    level_question_index = 1

    return game, level_label_index, level_question_index

def pickLevel(game, level_label_index):
    """given a game as input, lists the game's levels at the command
    prompt. the output is the user's chosen pick (as int)"""

    print "Pick a level:"
    for level in game:
        print "{0} - {1}".format(game.index(level), level[level_label_index])
    valid_pick = False
    while valid_pick == False:
        pick = raw_input()
        try:
            pick = game[int(pick)]
            valid_pick = True
        except:
            print "Please pick a number 0 - {0}".format(len(game)-1)

    return pick

def prepareQuestion(question):

    q_valid_length = 2
    try:
        assert len(question) == q_valid_length
    except:
        "Invalid question format: missing field"

    q_string_index = 0
    q_words_index = 1
    try:
        q_list = question[q_string_index].split()
        q_words = question[q_words_index]
    except:
        "Invalid question format"

    return q_list, q_words

def locateQuestionWords(q_list, q_words):
    """given a properly formatted question (see below), outputs a list
    of all words in the question string + a list placing question numbers
    in their proper position in the question string. the question must be
    formatted as follows:
    ["the question string including a ?question word", ["question"]]"""
    q_tag, q_tag_index = "?", 0
    q_number = 0
    q_word_locations = []
    q_list_detagged = []

    for word in q_list:
        element = ""
        w_number = q_list.index(word)
        for question in q_words:
            if question in word and word[q_tag_index] == q_tag:
                element = q_number
                word = word[1:]
                q_words = q_words[1:]
                q_number += 1
                break
        q_word_locations.append(element)
        q_list_detagged.append(word)

    return q_word_locations, q_list_detagged

def getAnsweredQuestionPart(q_list, q_words, q_number):
    """given a properly formatted question (see below) and a question number,
    outputs the list of words preceding the question, and the position of the
    question in the list of question words. the question must be formatted as
    follows:
    ["the question string including a ?question word", ["question"]]"""
    q_word_locations, q_list_detagged = locateQuestionWords(q_list, q_words)
    try:
        q_index = q_word_locations.index(q_number)
    except:
        return "No matching question words found in question"

    a_list = q_list_detagged[:q_index]

    return q_index, a_list

def composeQuestionString(q_list, q_words, q_number):
    """given a properly formatted question (see below) and a question number,
    ouputs a question string with blanks in place of the questions yet to
    be answered. the question must be formatted as follows:
    ["the question string including a ?question word", ["question"]]"""
    q_word_locations, q_list_detagged = locateQuestionWords(q_list, q_words)
    try:
        q_index = q_word_locations.index(q_number)
    except:
        return "No matching question words found in question"

    a_list = q_list_detagged[:q_index]
    q_list_detagged = q_list_detagged[q_index:]

    for word in q_list_detagged:
        for question in q_words:
            if question in word:
                blank = "_" * len(question)
                word = word.replace(question, blank)
                q_list_detagged = q_list_detagged[1:]
                q_words = q_words[1:]
                q_number += 1
                break
        a_list.append(word)
    q_string = " ".join(a_list)

    return q_string

def answerQuestion(q_list, q_words, q_number):
    """given a properly formatted question (see below) and a question number,
    shows the question string and outputs the result of checking the user's
    answer. the user has 5 attempts to answer correctly, after which the correct
    answer is shown. the question must be formatted as follows:
    ["the question string including a ?question word", ["question"]]"""
    q_string = composeQuestionString(q_list, q_words, q_number)
    q_word = q_words[q_number]

    print
    print "Question {0}:".format(q_number+1)
    print q_string
    answered = False
    lives = 5
    while answered == False and lives >= 1:
        answer = raw_input("Answer: ")
        if answer.lower() == q_word.lower():
            print "Correct!"
            answered = True
            return answered
        elif lives > 1:
            lives -= 1
            print "Sorry, that's not correct. Try again ({0} attempts left): ".format(lives)
        else:
            print "Unlucky. The answer is {0}".format(q_word.upper())
            return

def play(game, level_label_index, level_question_index):
    """given a game, prompts the user to pick a level and receives their answers to
    each question. presents score at the end."""
    level = pickLevel(game, level_label_index)
    level_question = level[level_question_index]
    q_list, q_words = prepareQuestion(level_question)

    score = 0
    for question in q_words:
        q_number = q_words.index(question)
        answer = answerQuestion(q_list, q_words, q_number)
        if answer:
            score += 1

    print
    print "You're done! You scored {0} out of {1}".format(score, len(q_words))

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

#game, level_label_index, level_question_index = define3LevelGame(easy_question, medium_question, hard_question)
#play(game, level_label_index, level_question_index)

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

    #findAllQuestionWords
    q_list_0, q_words_0 = prepareQuestion(questions[0])
    q_list_1, q_words_1 = prepareQuestion(questions[1])
    q_list_2, q_words_2 = prepareQuestion(questions[2])
    q_list_3, q_words_3 = prepareQuestion(questions[3])
    q_list_4, q_words_4 = prepareQuestion(questions[4])
    q_list_5, q_words_5 = prepareQuestion(questions[5])
    q_list_6, q_words_6 = prepareQuestion(questions[6])
    q_list_7, q_words_7 = prepareQuestion(questions[7])

    assert locateQuestionWords(q_list_0, q_words_0)[0] == ["", "", "", 0]
    assert locateQuestionWords(q_list_1, q_words_1)[0] == ["", 0, "", ""]
    assert locateQuestionWords(q_list_2, q_words_2)[0] == ["", "", "", 0, 1, 2, "", 3]
    assert locateQuestionWords(q_list_3, q_words_3)[0] == ["", 0, "", 1]
    assert locateQuestionWords(q_list_4, q_words_4)[0] == ["", "", "", "", "", "", "", "", "", 0]
    assert locateQuestionWords(q_list_5, q_words_5)[0] == ["", "", "", 0, "", "", "", "", "", ""]
    assert locateQuestionWords(q_list_6, q_words_6)[0] == ["", "", "", ""]
    assert locateQuestionWords(q_list_7, q_words_7)[0] == ["", "", "", ""]

    #getAnsweredQuestionString
    q_list_0, q_words_0 = prepareQuestion(questions[0])
    q_list_1, q_words_1 = prepareQuestion(questions[1])
    q_list_2, q_words_2 = prepareQuestion(questions[2])
    q_list_3, q_words_3 = prepareQuestion(questions[3])
    q_list_4, q_words_4 = prepareQuestion(questions[4])
    q_list_5, q_words_5 = prepareQuestion(questions[5])
    q_list_6, q_words_6 = prepareQuestion(questions[6])
    q_list_7, q_words_7 = prepareQuestion(questions[7])

    assert getAnsweredQuestionPart(q_list_0, q_words_0,0) == (3, ["this", "is", "a"])
    assert getAnsweredQuestionPart(q_list_1, q_words_1,0) == (1, ["a"])
    assert getAnsweredQuestionPart(q_list_2, q_words_2,0) == (3, ["this", "is", "a"])
    assert getAnsweredQuestionPart(q_list_3, q_words_3,0) == (1, ["a"])
    assert getAnsweredQuestionPart(q_list_4, q_words_4,0) == (9, ["this", "is", "not", "a", "test,", "but", "this", "is", "a"])
    assert getAnsweredQuestionPart(q_list_5, q_words_5,0) == (3, ["this", "is", "a"])
    assert getAnsweredQuestionPart(q_list_2, q_words_2,1) == (4, ["this", "is", "a", "test1,"])
    assert getAnsweredQuestionPart(q_list_3, q_words_3,1) == (3, ["a", "test,", "another"])
    assert getAnsweredQuestionPart(q_list_6, q_words_6,0) == "No matching question words found in question"
    assert getAnsweredQuestionPart(q_list_7, q_words_7,0) == "No matching question words found in question"

    #composeQuestionString
    q_list_0, q_words_0 = prepareQuestion(questions[0])
    q_list_1, q_words_1 = prepareQuestion(questions[1])
    q_list_2, q_words_2 = prepareQuestion(questions[2])
    q_list_3, q_words_3 = prepareQuestion(questions[3])
    q_list_4, q_words_4 = prepareQuestion(questions[4])
    q_list_5, q_words_5 = prepareQuestion(questions[5])
    q_list_6, q_words_6 = prepareQuestion(questions[6])
    q_list_7, q_words_7 = prepareQuestion(questions[7])

    assert composeQuestionString(q_list_0, q_words_0,0) == "this is a ____"
    assert composeQuestionString(q_list_1, q_words_1,0) == "a ____, this is"
    assert composeQuestionString(q_list_2, q_words_2,0) == "this is a _____, _____, _____ and _____"
    assert composeQuestionString(q_list_3, q_words_3,0) == "a ____, another ____"
    assert composeQuestionString(q_list_4, q_words_4,0) == "this is not a test, but this is a ____"
    assert composeQuestionString(q_list_5, q_words_5,0) == "this is a ____, but this is not a test"
    assert composeQuestionString(q_list_2, q_words_2,1) == "this is a test1, _____, _____ and _____"
    assert composeQuestionString(q_list_3, q_words_3,1) == "a test, another ____"
    assert composeQuestionString(q_list_6, q_words_6,0) == "No matching question words found in question"
    assert composeQuestionString(q_list_7, q_words_7,0) == "No matching question words found in question"

    #define3LevelGame
    game = define3LevelGame(questions[0], questions[1], questions[2])
    assert game[0][0][0] == "Easy"
    assert game[0][1][0] == "Medium"
    assert game[0][2][0] == "Hard"
    assert game[0][0][1] == ["this is a ?test", ["test"]]
    assert game[0][1][1] == ["a ?test, this is", ["test"]]
    assert game[0][2][1] == ["this is a ?test1, ?test2, ?test3 and ?test4", ["test1", "test2", "test3", "test4"]]

    #play(game)

    #ran all tests
    print "ran all tests"

tests()
