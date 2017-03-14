# Count Me Up - a polling machine

## Synopsis

A basic implementation of a polling machine in Python, using the command line
to allow users to vote, and for the poll results to be displayed.

Currently the polling machine will also generate automatic votes for 
testing/profiling purposes. The time it takes to display the poll is timed,
and the poller reports the time. 

## Running the polling machine

run count_me_up.py using Python (2.7 onwards), or make the file 
executable and run directly.

~ python ./count_me_up.py ~

or make executable and run
~ chmod +x ./count_me_up.py ~
~ ./count_me_up.py ~

This will bring up a menu screen where you can select from the following
options

['P/p'] : Prints the current standing of the poll.
['V/v'] : Allows a user to enter a username, and vote for one of the candidates
		  in the poll.
['A/a'] : Allows a user to specify a number of votes, that are made under
		  anonymous users.
['Q/q'] : Quits the poll machines.

To build a poll with X number of votes, choose option 'a', then enter the
number of votes. A progress will be displayed whilst the votes are building.

You are then returned to the main menu where the poll can be displayed on-demand.

# File Summary

## poller.py
Class definitions of the poll machine and a candidate within the poll
## count_me_up.py
The executable that brings up the polling machine menu
## tests.py
An executable of some unit tests for ensuring votes are cast correctly.