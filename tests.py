#!/usr/bin/python
import unittest
import pdb
from poller import Poller, Candidate

class TestPoller(unittest.TestCase):

    def setUp(self):
        self.test_poll = Poller()
        self.test_poll._candidates = [Candidate("candidate1"), 
                                      Candidate("candidate2")]

    def test_add_to_poll(self):
        new_candidate="numero3"
        preLen = len(self.test_poll._candidates)
        self.test_poll.add_candidate(new_candidate)
        postLen = len(self.test_poll._candidates)
        self.assertEqual(preLen + 1, postLen, "Check - we've added more than just %s" % (new_candidate))
        #pdb.set_trace()
        self.assertTrue(Candidate(new_candidate) in self.test_poll, "Candidate %s cannot be added" % (new_candidate))

    def test_unique_candidates(self):
        duplicate="duplicate candidate"
        self.test_poll.add_candidate(duplicate)
        with self.assertRaises(Exception):
            self.test_poll.add_candidate(duplicate)

    def tearDown(self):
        self.test_poll = None

if __name__ == '__main__':
    unittest.main()