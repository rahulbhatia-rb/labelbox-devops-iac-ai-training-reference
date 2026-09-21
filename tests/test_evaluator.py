import unittest
from src.evaluator import Submission,evaluate
class T(unittest.TestCase):
 def test_accepts_complete(self):self.assertTrue(evaluate(Submission(*([True]*10)))["accepted"])
 def test_explains_failures(self):self.assertIn("secrets-in-code",evaluate(Submission(*([False]*10)))["findings"])
