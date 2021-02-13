#!/usr/bin/env python3

""" Flowchart Challenge! """


def flowchart(r, q):
    if q == 0:
        print('Do you have a problem?')
        q += 1
        return q
    elif (q == 1) and (r.lower() == 'yes'):
        print('Can you do something about it?')
        q += 1
        return q
    elif (q == 2) or ((q == 1) and (r.lower() == 'no')):
        print("Then don't worry.")
        q = 0
        return q
    else:
        print('Invalid entry, yes or no responses only please')
        q = 0
        return q
        


def main():

    response = ''
    question = 0

    while response != 'q':
        question = flowchart(response, question)
        response = input('>')


main()
