#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from poller import Poller

def do_poll():
    """ Create a poll of candidates, and a menu screen to allow a user to view
        the poll or add a vote
    """

    candidates = ["Candidate 1",
                  "Candidate 2",
                  "Candidate 3",
                  "Candidate 4",
                  "Candidate 5"
    ]
    
    poll = Poller()

    for candidate in candidates:
        poll.add_candidate(candidate)

    menu = {}
    menu['P/p']="Print current poll status" 
    menu['V/v']="Vote"
    menu['Q/q']="Quit"
    while True: 
        options=menu.keys()
        options.sort()
        for entry in options: 
          print entry, menu[entry]
    
        selection=raw_input("Please Select:").lower()
        if selection == 'p': 
          print(poll)
        elif selection == 'v': 
          # vote()
          pass
        elif selection == 'q': 
          quit()
        else: 
          print "\nUnknown Option Selected - please try again" 

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
