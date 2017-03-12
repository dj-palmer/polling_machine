#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from poller import Poller
from collections import OrderedDict

def do_poll():
    """ Create a poll of candidates, and a menu screen to allow a user to view
        the poll or add a vote
    """

    # Some intial setup to get a MVP, will do this dynamically later
    candidates = ["Candidate 1",
                  "Candidate 2",
                  "Candidate 3",
                  "Candidate 4",
                  "Candidate 5"
    ]
    
    poll = Poller()

    # Generate our list of candidates
    for candidate in candidates:
        poll.add_candidate(candidate)

    menu = OrderedDict([])
    menu['P/p'] = "Print current poll status" 
    menu['V/v'] = "Vote"
    menu['Q/q'] = "Quit"
    while True: 
        print "\nMain Menu"
        print "-----------------------------"
        options = menu.keys()
        for entry in options: 
          print entry, menu[entry]

        selection=raw_input("Selection:").lower()
        if selection == 'p': 
            print(poll)
        elif selection == 'v': 
            manual_vote(poll)
        elif selection == 'q': 
          quit()
        else: 
          print "\nUnknown Option Selected - please try again" 

def manual_vote(poll):
    voter = raw_input("Please enter your name:")
    print "Who would you like to vote for?:"
    selection={}
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
                vote=int(vote)
                if vote in selection.keys():
                    print "adding vote"
                    success = poll.add_vote(selection[vote], voter) 
                    if not success:
                        print "Sorry, you have already voted %s times, please try as a different user" % (poll.VOTE_LIMIT)
                    break
                else: 
                    print "\nUnknown Option Selected - please try again or enter 'q' to go back to main menu "
        except ValueError: 
                print "\nUnknown Option Selected - please try again or enter 'q' to go back to main menu "

def parse_args():
    parser = argparse.ArgumentParser(
                description =
                "A script that sets up a poll for 5 candidates"
                "and allows users to cast votes."
                "A running total can be printed at any time by hitting 'p'"
                ""
             )
    # Placeholder for creating a dynamic list of candidates
    # parser.add_argument('-n', '--number_of_candidates', default=5,
    #                    help="Creates a poll for n number of candidates")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    do_poll()
