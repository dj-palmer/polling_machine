# -*- coding: utf-8 -*-


class Poller(object):

    """ Holds candidates for a poll and counts up the votes
        cast to each candidate
    """

    def __init__(self, candidates=[]):
        self._candidates = candidates

    def add_candidate(self, name):
        new_candidate = Candidate(name)
        if new_candidate not in self._candidates:
            self._candidates.append(new_candidate)
        else:
            raise Exception("Candidate already exists")

    def __iter__(self):
        return iter(self._candidates)

    def __repr__(self):
        """ A nice representation of our poll for displaying to the host"""
        
        results = "\nThe results are in!:" \
            + "\n:--------------------------------:" \
            + "\n|Candidate     | Votes           |" \
            + "\n:--------------------------------:"
        
        for candidate in self._candidates:
            results += "\n|%s   |%s                |" % (candidate._name, len(candidate._votes))

        results += "\n:--------------------------------:"

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