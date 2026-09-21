# Labelbox DevOps / IaC AI-training challenge evaluator

This runnable POC models the reviewer side of a realistic infrastructure challenge. It evaluates Terraform, Kubernetes, and CI submissions against an explicit, weighted scoring contract rather than relying on subjective checklist review.

## What it evaluates

- reusable Terraform modules, remote state locking, and environment-safe design;
- private workloads, narrow security groups, least-privilege IAM, and externalized secrets;
- non-root Kubernetes workloads with explicit resource bounds;
- CI plan/policy checks before deployment;
- clear written rationale alongside the technical implementation.

Each failed control returns a stable finding code, its scoring weight, and a remediation hint. Input shape and types are validated so a malformed candidate/model result is never silently scored.

## Run

python3 -m unittest discover -s tests -v

python3 -m src.app < examples/submissions.jsonl

## Challenge design notes

Effective AI-training scenarios contain an intentionally unsafe baseline, a deployable target state, acceptance tests, explicit non-goals, and a scoring rubric. Require the model to justify trade-offs: why a policy prevents a risk, how state is protected, what would be observed in failure, and which changes need human approval. Keep cloud-provider adapters separate from invariant security/reliability checks so the same scenario can be evaluated on AWS, GCP, or Azure.

### Suggested challenge packet

1. A deliberately insecure Terraform/EKS starter repository.
2. A target architecture and non-functional requirements (tenants, recovery target, cost ceiling).
3. Hidden validation tests plus public contract tests.
4. A machine-readable score and a short human-review rubric for the model's reasoning.
5. An evidence bundle: plan JSON, policy output, Kubernetes manifests, CI logs, and explanation.

## Production extension

Connect the evaluator to Terraform validation and plan JSON, OPA/Conftest or Checkov, Kubernetes admission-policy output, and GitHub Actions artifacts. Persist results and explanation as evaluation traces, then score both the infrastructure result and reasoning quality rather than configuration text alone.
