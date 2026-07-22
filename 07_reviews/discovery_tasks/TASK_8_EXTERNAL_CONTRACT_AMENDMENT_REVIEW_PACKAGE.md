# Task 8 External Release-Contract Amendment Review Package

## Review range

- Purpose: owner-approved narrow amendment that replaces only the two blocked Task 8 external release interpretations
- Base SHA: `352588c0059122de7385498c6d17f8fcdbd495f3`
- Initial amendment SHA: `2927eae1b01e634bb18e007f6914a998e167e8d9`
- Amendment repair SHA and reviewed head: `d0d873abe08256184bd5028fde8cf1f2f020b576`
- Exact complete diff package: `.superpowers/sdd/review-352588c..d0d873a.diff`
- Exact complete diff SHA256: `9e621bab349900b5847220e02acc87452eddc19aef68dec8496ad5f9838e03df`
- Amendment plan: `docs/superpowers/plans/2026-07-22-broad-discovery-external-release-contract-amendment.md`
- Amendment plan SHA256: `62e379c09e513afb83ffbb467b74c45381f75e1645786c5b259aabb2e7242609`
- Decision log SHA256: `5b62d932eb351a4e3f0c21169739bd911a653a223d7a2d9925cc6899bca3da28`
- Implementer report: `.superpowers/sdd/external-contract-amendment-report.md`
- Implementer report SHA256: `1664577926255a3a1fa79c711ef168eaa2cdb69b12bc754dff9834ee2841f772`

## Contract boundary

The amendment preserves the original broad-discovery plan, frozen external baseline, existing validator, and every scientific, review, merge, remote-equality, and push gate. It replaces only the Task 8 release interpretations that the existing external validator itself must exit `0` and that the live pointer-filtered status must equal the phase-start receipt. The legacy validator remains mandatory and nonpassing; release instead requires the exact independently reviewed dual-receipt gate for the sole owner-owned GBD status delta.

## Review history

The first independent review returned `NEEDS FIXES — 0 Critical, 1 Important, 1 Minor`. The Important finding was an impossible pre-commit scope check that could not see the untracked contract JSON. The Minor finding was an unbound JSON/gate dual source.

Repair `d0d873abe08256184bd5028fde8cf1f2f020b576` changed only the amendment plan. It requires exact pre-stage status, exact staged paths and statuses, cached JSON SHA/content/whitespace review, and an exact JSON SHA at creation, full gate, and cached-blob checkpoints.

The same reviewer re-reviewed the complete fixed range and returned `PASS — 0 Critical, 0 Important, 0 Minor`. This authorizes the original Task 8 implementer to perform the bounded three-file repair; it does not complete Task 8 or authorize whole-branch review, merge, or push.
