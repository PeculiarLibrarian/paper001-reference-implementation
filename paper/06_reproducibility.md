# 6. Reproducibility

All experiments reported in this paper are distributed as executable workflows within the accompanying reference implementation.

**Archived replication package (DOI)**

https://doi.org/10.5281/zenodo.21341462

**Development repository**

https://github.com/PeculiarLibrarian/paper001-reference-implementation

**Archived release**

paper001-v1.0.1

The replication package contains:

- Experiment 01 — RIOT syntax validation
- Experiment 02 — Positive SHACL validation
- Experiment 03 — Adversarial SHACL validation

Each experiment includes:

- executable scripts,
- deterministic inputs,
- documented expected outcomes,
- automated pass/fail assertions.

The adversarial experiment generates a corrupted graph deterministically by removing a mandatory provenance relationship before validation.

Only the documented verification artifacts and experimental workflows are used to support the evaluation reported in this paper; the remaining repository contents provide supporting implementation infrastructure and architectural documentation.

The archived Zenodo release (DOI: https://doi.org/10.5281/zenodo.21341462) constitutes the canonical replication package for this publication. The GitHub repository serves as the active development repository for subsequent revisions.

Running the documented workflows from the archived release in an equivalent software environment is expected to reproduce the experimental results reported in this paper.
