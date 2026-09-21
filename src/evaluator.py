"""Deterministic evaluator for a cloud/IaC AI-training challenge."""
from dataclasses import dataclass,asdict
from typing import Any
@dataclass(frozen=True)
class Submission:
 remote_state_locking:bool; reusable_modules:bool; vpc_private_workloads:bool; restrictive_security_groups:bool; iam_least_privilege:bool; secrets_out_of_code:bool; kubernetes_non_root:bool; resource_requests_limits:bool; ci_plan_and_policy_check:bool; reasoning_documented:bool
 @classmethod
 def from_dict(cls,v:dict[str,Any])->"Submission":return cls(**v)
def evaluate(s:Submission)->dict[str,Any]:
 c={"state-locking-missing":s.remote_state_locking,"modules-not-reusable":s.reusable_modules,"workloads-not-private":s.vpc_private_workloads,"security-groups-too-permissive":s.restrictive_security_groups,"iam-not-least-privilege":s.iam_least_privilege,"secrets-in-code":s.secrets_out_of_code,"kubernetes-root-workload":s.kubernetes_non_root,"resource-bounds-missing":s.resource_requests_limits,"ci-policy-gate-missing":s.ci_plan_and_policy_check,"reasoning-not-documented":s.reasoning_documented}
 f=[k for k,v in c.items() if not v];return {"accepted":not f,"findings":f,"submission":asdict(s)}
