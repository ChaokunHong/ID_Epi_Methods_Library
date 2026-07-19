# Agent Entry Point

Before acting, read these files in order:

1. `HANDOFF.md`
2. `00_governance/PROJECT_CHARTER.md`
3. `00_governance/DECISION_LOG.md`
4. `00_governance/WORKFLOW.md`
5. the active approved plan named in `HANDOFF.md`

Operating rules:

- Verify the live worktree and referenced SHA values instead of trusting prior narration.
- Keep discovery claims separate from verified claims.
- Use primary sources for substantive method, software, and dataset claims.
- Do not use AMR, LMIC status, global scope, or public-data availability as discovery-stage exclusion gates.
- Preserve failed and null designs; never relax a gate merely to promote a candidate.
- Do not modify `../Surveillance_AMR` except through an explicit, separately reviewed task.
- Update `HANDOFF.md` at every stopping point and record the exact Git commit.
- Run `python3 00_governance/scripts/validate_library.py --root .` before reporting completion.

The design `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md` was approved by the owner on 2026-07-20; bootstrap is governed by `docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md`.
