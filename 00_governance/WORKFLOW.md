# Workflow

## Stage 1 — Broad discovery

- **Inputs:** reproducible searches, citation chasing, journal scans, and the frozen seed scan.
- **Required record:** a dated search log and paper-registry discovery record.
- **Exit gate:** the record has a resolvable title, year, source URL, discovery route, and preliminary method label.
- **Forbidden shortcut:** excluding a lead because it is not AMR, not LMIC-specific, not global, not immediately public, or not executable by one researcher.

## Stage 2 — Method lineage

- **Inputs:** promising applied seeds and method-led papers from Stage 1.
- **Required record:** linked original or authoritative method sources, later corrections, accepted diagnostics, and duplicate-name resolution.
- **Exit gate:** the method's lineage and current defensible use can be described from primary sources.
- **Forbidden shortcut:** treating a high-impact application or review article as the authoritative method source without checking lineage.

## Stage 3 — Card construction

- **Inputs:** verified method lineage and relevant infectious-disease applications.
- **Required record:** a method card linked to paper IDs.
- **Exit gate:** estimand, required data signature, identification assumptions, mandatory diagnostics, falsification tests, common misuses, and stop rules are explicit; unresolved assumptions are recorded as defects.
- **Forbidden shortcut:** completing a card that only summarizes papers or lists software.

## Stage 4 — Translation generation

- **Inputs:** a mature method card.
- **Required record:** linked translation cards for one direct AMR application, one AMR mechanism/policy/surveillance/transmission application, and one non-AMR infectious-disease application when scientifically coherent.
- **Exit gate:** each candidate states a question, estimand, setting, identification route, falsification strategy, and stop rules.
- **Forbidden shortcut:** choosing a familiar dataset first and retrofitting a method without a defensible question or estimand.

## Stage 5 — Feasibility and data audit

- **Inputs:** translation candidates and official dataset sources.
- **Required record:** dataset cards covering access, licence, time/geographic grain, unit, numerator, denominator, observation process, missingness, revisions, linkage, compute, LMIC relevance, and solo workload.
- **Exit gate:** access and licence are verified or explicitly unresolved, and the data structure can or cannot identify the candidate estimand for stated reasons.
- **Forbidden shortcut:** calling data public because a paper used them or because a landing page exists.

## Stage 6 — Portfolio ranking

- **Inputs:** mature cards, feasibility audits, novelty checks, and design preflights.
- **Required record:** an auditable category decision and rationale.
- **Exit gate:** candidate is classified as `flagship`, `lower_risk_public_data`, `infrastructure_prospective`, `collaboration_dependent`, or `no_go`; categories are not collapsed into one score.
- **Forbidden shortcut:** relaxing thresholds, hiding failed preflights, or promoting solely on journal fit.

## Stage 7 — Project graduation

- **Inputs:** owner-reviewed portfolio candidate.
- **Required record:** mature method card, data audit, novelty check, estimand, falsification strategy, preflight plan, decision-log entry, and owner approval.
- **Exit gate:** a separate paper repository and protocol are authorized; the Library retains immutable links and the graduation decision.
- **Forbidden shortcut:** running the definitive analysis or treating an agent recommendation as owner approval.
