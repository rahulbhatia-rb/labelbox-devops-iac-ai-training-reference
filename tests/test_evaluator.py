import unittest
from src.evaluator import Submission,evaluate
class T(unittest.TestCase):
 def test_accepts_complete(self):self.assertTrue(evaluate(Submission(*([True]*10)))["accepted"])
 def test_explains_failures(self):
  result=evaluate(Submission(*([False]*10)))
  self.assertEqual(result["score"],0)
  self.assertIn("secrets-in-code",[item["code"] for item in result["findings"]])
 def test_rejects_unknown_or_non_boolean_input(self):
  with self.assertRaises(ValueError):Submission.from_dict({"unknown":True})
  with self.assertRaises(ValueError):Submission.from_dict({"remote_state_locking":"true"})
