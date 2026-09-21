import json,sys
from src.evaluator import Submission,evaluate
for l in sys.stdin:
 if l.strip():print(json.dumps(evaluate(Submission.from_dict(json.loads(l)))))
