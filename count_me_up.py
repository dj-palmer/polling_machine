#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import sys
from poller import Poller
from collections import OrderedDict
from random import randint
from timeit import default_timer as timer


def do_poll():
    """ Create a poll of candidates, and a menu screen to allow a user to view
        the poll or add a vote
    """

    # Some intial setup to get a MVP, will do this dynamically later
    candidates = ["Candidate 1",
                  "Candidate 2",
                  "Candidate 3",
                  "Candidate 4",
                  "Candidate 5"]

    poll = Poller()

    # Generate our list of candidates
    for candidate in candidates:
        poll.add_candidate(candidate)

    menu = OrderedDict([])
    menu['P/p'] = "Print current poll status"
    menu['V/v'] = "Vote"
    menu['A/a'] = "Auto vote with x votes"
    menu['Q/q'] = "Quit"
    while True:
        print "\nMain Menu"
        print "-----------------------------"
        options = menu.keys()
        for entry in options:
            print entry, menu[entry]

        selection = raw_input("Selection:").lower()
        if selection == 'p':
            start = timer()
            print(poll)
            stop = timer()
            print "\nPoll displayed in %.2f seconds" % (stop - start)
        elif selection == 'v':
            manual_vote(poll)
        elif selection == 'a':
            auto_vote(poll)
        elif selection == 'q':
            quit()
        else:
            print "\nUnknown Option Selected - please try again"


def manual_vote(poll):
    """ Allows a user to enter a username and cast a vote for a candidate
        in the poll. A user is limited to a max number of votes as defined
        in the VOTE_LIMIT Poller class variable
    """
    voter = raw_input("Please enter your name:")
    print "Who would you like to vote for?:"
    selection = {}
    for id, candidate in enumerate(poll._candidates):
        selection[id + 1] = candidate._name

    options = selection.keys()
    options.sort()
    for entry in options:
        print entry, selection[entry]

    while True:
        try:
            vote = raw_input("Please enter a number from this selection:")
            if vote.lower() == 'q':
                break
            else:
                vote = int(vote)
                if vote in selection.keys():
                    print "adding vote"
                    success = poll.add_vote(selection[vote], voter)
                    if not success:
                        print ("Sorry, you have already voted %s times, " +
                               " please try as a different user" % (poll.VOTE_LIMIT))
                    break
                else:
                    print ("\nUnknown Option Selected - please try again or " +
                           "enter 'q' to go back to main menu ")
        except ValueError:
            print ("\nUnknown Option Selected - please try again or " +
                   "enter 'q' to go back to main menu ")


def auto_vote(poll):
    """ For testing the polling machine, allows you to specify a number of
        votes you would like automatically cast. The username is set to a
        random number up to these votes -- which are still limited to the
        VOTE_LIMIT of Poller.

        So you may find total number of votes in the poll are lower,
        as some will be refused over the VOTE_LIMIT.
    """
    selection = {}
    for id, candidate in enumerate(poll._candidates):
        selection[id + 1] = candidate._name

    while True:
        try:
            vote_num = raw_input("How many votes would you like to " +
                                 "automatically cast? Or q to quit:")
            if vote_num.lower() == 'q':
                break
            else:
                start = timer()
                vote_num = int(vote_num)
                sys.stdout.write("Auto voting, vote 1 of %s\r" % (vote_num))
                for i in range(0, vote_num):
                    voter = randint(1, vote_num)
                    vote = randint(1, len(poll._candidates))
                    poll.add_vote(selection[vote], voter)
                    sys.stdout.write("Auto voting, vote %s of %s\r" % (i+1, vote_num))
                stop = timer()
                print "\nCast %d votes in %.2f seconds" % (vote_num, stop - start)
                break
        except ValueError:
            print ("\nUnknown Option Selected - please try again or enter " +
                   "'q' to go back to main menu")

if __name__ == "__main__":
    do_poll()
