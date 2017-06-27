#!/usr/bin/python
'''
Port of BASIC game to Python. Attempts to guess the animal you are thinking of.
'''
import sys
import io

Q_POS = 0
Y_POS = 1
N_POS = 2

last_answer = ''  # Was the last answer Y or N
last_question = '' # index of the last question asked

next_index = 1  # 1 + number of entries in our array

another = True

questions = [["Does it live in the water", "Dolphin", "Koala"]]


def ask(curr_question):
    '''
    Ask a question
    '''
    global last_answer
    global last_question

    asking = questions[curr_question]
    print asking[Q_POS]
    last_answer = io.getch()
    last_question = curr_question
    if last_answer[0] == 'Y':
        if type(asking[Y_POS]) == int:  # we are pointing to another Q
            ask(asking[Y_POS])
        else:
            guess(Y_POS, asking)
    else:
        if type(asking[N_POS]) == int:  # we are pointing to another Q
            ask(asking[N_POS])
        else:
            guess(N_POS, asking)


def give_up(my_guess):
    '''
    Give up and get the info on the new animal
    '''
    global last_answer
    global last_question
    global next_index
    global questions

    print "I give up. Well done!! What is the answer?"
    answer = sys.stdin.readline()
    answer = answer.strip
    print "What is a question to decide between a", my_guess, "and a", answer
    new_question = sys.stdin.readline()
    new_question = new_question.strip()
    print "Is the answer for", answer, "'Y' or 'N'?"
    new_answer = io.getch()
    
    # now to save info
    if last_answer[0] == 'Y':
        questions[last_question][Y_POS] = next_index
    else:
        questions[last_question][N_POS] = next_index
    if new_answer[0] == 'Y':
        questions.append([new_question.strip(), answer, my_guess])
    else:
        questions.append([new_question.strip(), my_guess, answer])
    next_index = next_index + 1


def guess(pos, animal):
    '''
    We think we know the answer
    '''
    print "Are you thinking of a", animal[pos]
    an_answer = io.getch()
    if an_answer[0] == 'Y':
        print "Fantastic!! I'm getting pretty good at this!"
    else:
        give_up(animal[pos])


if __name__ == "__main__":
    while another:
        ask(0)
        print "Would you like another game?"
        more = io.getch()
        if more[0] == 'N':
            another = False
