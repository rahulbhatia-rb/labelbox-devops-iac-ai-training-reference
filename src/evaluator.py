"""Deterministic, explainable evaluator for a cloud/IaC AI-training challenge."""
from dataclasses import asdict, dataclass
from typing import Any, Dict, List
@dataclass(frozen=True)
class Submission:
    remote_state_locking: bool
    reusable_modules: bool
    vpc_private_workloads: bool
    restrictive_security_groups: bool
    iam_least_privilege: bool
    secrets_out_of_code: bool
    kubernetes_non_root: bool
    resource_requests_limits: bool
    ci_plan_and_policy_check: bool
    reasoning_documented: bool

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "Submission":
        unknown = set(value) - set(cls.__annotations__)
        missing = set(cls.__annotations__) - set(value)
        if unknown or missing:
            raise ValueError("submission fields do not match the challenge contract")
        if not all(isinstance(item, bool) for item in value.values()):
            raise ValueError("each submission control must be boolean")
        return cls(**value)


RUBRIC = {
    "remote_state_locking": ("state-locking-missing", 12, "Use encrypted remote state with locking."),
    "reusable_modules": ("modules-not-reusable", 8, "Separate reusable modules from environment composition."),
    "vpc_private_workloads": ("workloads-not-private", 12, "Place workloads in private subnets; expose only required ingress."),
    "restrictive_security_groups": ("security-groups-too-permissive", 10, "Replace broad ingress/egress with explicit flows."),
    "iam_least_privilege": ("iam-not-least-privilege", 12, "Scope IAM actions and resources to the workload."),
    "secrets_out_of_code": ("secrets-in-code", 10, "Use a secret manager and workload identity."),
    "kubernetes_non_root": ("kubernetes-root-workload", 8, "Set non-root security context and drop capabilities."),
    "resource_requests_limits": ("resource-bounds-missing", 8, "Declare resource requests and limits."),
    "ci_plan_and_policy_check": ("ci-policy-gate-missing", 10, "Run validation, plan, and policy checks in CI."),
    "reasoning_documented": ("reasoning-not-documented", 10, "Explain trade-offs, assumptions, and human approval points."),
}


def evaluate(submission: Submission) -> Dict[str, Any]:
    findings: List[Dict[str, Any]] = []
    score = 0
    for field, (code, weight, remediation) in RUBRIC.items():
        if getattr(submission, field):
            score += weight
        else:
            findings.append({"code": code, "weight": weight, "remediation": remediation})
    return {
        "accepted": not findings,
        "score": score,
        "max_score": sum(rule[1] for rule in RUBRIC.values()),
        "findings": findings,
        "submission": asdict(submission),
    }
