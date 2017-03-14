# -*- coding: utf-8 -*-
import pdb
from copy import deepcopy


class Poller(object):

    """ Holds candidates for a poll and counts up the votes
        cast to each candidate

        Set the VOTE_LIMIT class variable to set the maximum the same user
        can vote. Any votes cast over this limit are stored in the _miscast
        variable, so we can audit all the votes cast if necessary. However,
        our poll object will only report on valid votes cast.

    """
    # A static variable to limit the number of votes a single user can cast
    VOTE_LIMIT = 3

    def __init__(self, candidates=[]):
        self._candidates = candidates
        self._miscast = list(self._candidates)

    def add_candidate(self, name):
        new_candidate = Candidate(name)

        if new_candidate not in self._candidates:
            self._candidates.append(new_candidate)
            self._miscast.append(deepcopy(new_candidate))
        else:
            raise Exception("Candidate already exists")

    def add_vote(self, name, voter):
        votes = 0
        can_vote = True

        for candidate in self:
            votes += candidate._votes.count(voter)
            if votes >= self.VOTE_LIMIT:
                can_vote = False
                break

        if can_vote:
            for candidate in self._candidates:
                if candidate._name == name:
                    candidate._votes.append(voter)
        else:
            for candidate in self._miscast:
                if candidate._name == name:
                    candidate._votes.append(voter)

        return can_vote

    def __iter__(self):
        return iter(self._candidates)

    def __repr__(self):
        """ A nice representation of our poll for displaying to the host.
            Displays up to first 20 chars of candidate names
        """

        results = "\nThe results are in!:" \
            + "\n:---------------------------------------------:" \
            + "\n| {0:<30s} | {1:10s} |".format("Candidate", "Votes") \
            + "\n:---------------------------------------------:"

        for candidate in self._candidates:
            results += "\n| {0:<30s} | {1:10d} |".format(candidate._name[0:20],
                                                         len(candidate._votes))

        results += "\n:---------------------------------------------:" \

        return results


class Candidate(object):

    """ Our basic candidate - holds their name, plus storage of the
        users that vote for them
    """

    def __init__(self, name):
        self._name = name
        self._votes = []

    def add_vote(self, voter):
        self._votes.append(voter)

    def __eq__(self, other):
        """ A candidate must have a unique name, otherwise we
            assume they are the same person.
        """
        if self._name == other._name:
            return True
        else:
            return False
