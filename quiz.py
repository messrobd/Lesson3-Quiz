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

def makeQuestionLists(question):
    """given a properly formatted question (see below), outputs a list
    of all words in the question string + a list placing question numbers
    in their proper position in the question string. the question must be
    formatted as follows:
    ["the question string including a ?question word", ["question"]]"""
    q_list = question[0].split()#magic number
    q_words = question[1]#magic number
    q_tag, q_tag_index = "?", 0
    q_number = 0
    q_words_located = []

    for word in q_list:
        element = ""
        w_number = q_list.index(word)
        for question in q_words:
            if question in word and word[q_tag_index] == q_tag:
                element = q_number
                q_list[w_number] = word[1:]
                q_words = q_words[1:]
                q_number += 1
                break
        q_words_located.append(element)

    return q_list, q_words_located

def getAnsweredQuestionPart(question,q_number):
    """given a properly formatted question (see below) and a question number,
    outputs the list of words preceding the question, and the position of the
    question in the list of question words. the question must be formatted as
    follows:
    ["the question string including a ?question word", ["question"]]"""
    try:
        q_list, q_words_located = makeQuestionLists(question)
        q_index = q_words_located.index(q_number)
        a_list = q_list[:q_index]
    except:
        return "No matching question words found in question"

    return q_index, a_list

def composeQuestionString(question,q_number):
    """given a properly formatted question (see below) and a question number,
    ouputs a question string with blanks in place of the questions yet to
    be answered. the question must be formatted as follows:
    ["the question string including a ?question word", ["question"]]"""
    try:
        q_index, a_list = getAnsweredQuestionPart(question,q_number)
        q_list = makeQuestionLists(question)[0][q_index:]#magic number
        q_words = question[1][q_number:]#magic number
    except:
        return "No matching question words found in question"

    for word in q_list:
        for question in q_words:
            if question in word:
                blank = "_" * len(question)
                word = word.replace(question, blank)
                q_list = q_list[1:]
                q_words = q_words[1:]
                q_number += 1
                break
            q_index += 1
        a_list.append(word)
    q_string = " ".join(a_list)

    return q_string

def answerQuestion(question, q_number):
    """given a properly formatted question (see below) and a question number,
    shows the question string and outputs the result of checking the user's
    answer. the user has 5 attempts to answer correctly, after which the correct
    answer is shown. the question must be formatted as follows:
    ["the question string including a ?question word", ["question"]]"""
    q_string = composeQuestionString(question,q_number)
    q_word = question[1][q_number]#magic number

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
    q_words = level_question[1]#magic number

    score = 0
    for question in q_words:
        q_number = q_words.index(question)
        answer = answerQuestion(level_question, q_number)
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
    #findAllQuestionWords
    assert makeQuestionLists(questions[0])[1] == ["", "", "", 0]
    assert makeQuestionLists(questions[1])[1] == ["", 0, "", ""]
    assert makeQuestionLists(questions[2])[1] == ["", "", "", 0, 1, 2, "", 3]
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
    assert getAnsweredQuestionPart(questions[2],1) == (4, ["this", "is", "a", "test1,"])
    assert getAnsweredQuestionPart(questions[3],1) == (3, ["a", "test,", "another"])
    assert getAnsweredQuestionPart(questions[6],0) == "No matching question words found in question"
    assert getAnsweredQuestionPart(questions[7],0) == "No matching question words found in question"

    #composeQuestionString
    assert composeQuestionString(questions[0],0) == "this is a ____"
    assert composeQuestionString(questions[1],0) == "a ____, this is"
    assert composeQuestionString(questions[2],0) == "this is a _____, _____, _____ and _____"
    assert composeQuestionString(questions[3],0) == "a ____, another ____"
    assert composeQuestionString(questions[4],0) == "this is not a test, but this is a ____"
    assert composeQuestionString(questions[5],0) == "this is a ____, but this is not a test"
    assert composeQuestionString(questions[2],1) == "this is a test1, _____, _____ and _____"
    assert composeQuestionString(questions[3],1) == "a test, another ____"
    assert composeQuestionString(questions[6],0) == "No matching question words found in question"
    assert composeQuestionString(questions[7],0) == "No matching question words found in question"

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
