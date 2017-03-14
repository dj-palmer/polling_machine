#!/usr/bin/python
import unittest
import pdb
from poller import Poller, Candidate
from copy import deepcopy

class TestPoller(unittest.TestCase):

    def setUp(self):
        self.test_poll = Poller()
        self.test_poll._candidates = [Candidate("candidate1"),
                                      Candidate("candidate2")]
        self.test_poll._miscast = deepcopy(self.test_poll._candidates)

    def test_add_to_poll(self):
        """ Ensure when we add a candidate to a poll that they exist, and
            that we've only added them once. Furthermore check
        """
        new_candidate="numero3"
        preLen = len(self.test_poll._candidates)
        self.test_poll.add_candidate(new_candidate)
        postLen = len(self.test_poll._candidates)
        self.assertEqual(preLen + 1, postLen, "Check - we've added more than just %s" % (new_candidate))
        self.assertTrue(Candidate(new_candidate) in self.test_poll._candidates, "Candidate %s cannot be added" % (new_candidate))
        self.assertTrue(Candidate(new_candidate) in self.test_poll._miscast, "Candidate %s was not added to our log of miscast votes" % (new_candidate))

    def test_unique_candidates(self):
        duplicate="duplicate candidate"
        self.test_poll.add_candidate(duplicate)
        with self.assertRaises(Exception):
            self.test_poll.add_candidate(duplicate)

    def test_add_vote(self):
        current_votes = len(self.test_poll._candidates[0]._votes)
        self.test_poll.add_vote("candidate1", "user1")
        new_votes = len(self.test_poll._candidates[0]._votes)
        self.assertEqual(new_votes, current_votes + 1, "Vote not saved correctly")

        # Check if we exceed the voting limit it becomes a miscast vote
        for i in range(0, self.test_poll.VOTE_LIMIT):
            self.test_poll.add_vote("candidate1", "user1")
        self.assertEquals(len(self.test_poll._miscast[0]._votes), 1, "Vote limit was exceeded and not captured as a miscast vote")

    def tearDown(self):
        self.test_poll = None

if __name__ == '__main__':
    unittest.main()