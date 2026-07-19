# Methods-first infectious-disease epidemiology library and AMR research portfolio

**Availability verified:** 2026-07-20  
**Scope:** a global, disease-agnostic methods library drawn from primary papers in general medicine, infectious diseases, public health, epidemiology and statistics, followed by a separately scored public-data implementation portfolio. Public availability and LMIC relevance are **later feasibility dimensions**, not search filters. This is a design scan, not a claim that an available association is causally identified. Sources are restricted to official data owners, original methods/applications and author-maintained replication resources.

## Executive conclusion

The most promising move is not to search for another paper whose disease name can simply be replaced by “AMR”. It is to import a mature **epidemiological design structure** into an AMR setting where the observation process is unusually visible. Five candidates merit active development:

| Rank | Candidate | Immediate verdict | Why it clears the bar |
|---:|---|---|---|
| 1 | England voluntary-versus-mandatory surveillance calibration | **GO now** | Monthly public numerator/testing/comparator streams; the observation process is itself the scientific object. |
| 2 | England ICB antibiotic-class exposure → matched resistance with negative controls | **GO to data-geometry preflight** | Monthly subnational prescribing and resistance; matching drug classes creates falsifiable predictions. |
| 3 | US Veterinary Feed Directive update using NARMS source contrasts | **GO as a registered update/replication** | Long pre/post series, explicit 2017 intervention, human/animal/retail-meat contrasts, source spreadsheets. |
| 4 | ECDC percentage-resistant versus resistant-BSI incidence comparison | **GO to extraction pilot** | Entirely public and directly extends the current measurement-construct question without waiting for GRAM. |
| 5 | PCV introduction and resistant invasive pneumococcal disease | **GO to blinded geometry/power audit** | A genuine vaccine-policy event study linking infectious-disease prevention to AMR, with official WHO and ECDC data. |

The following should **not** currently be presented as causal studies: staggered national AMR-action-plan adoption, a 2024 England national-policy ITS, an EU Regulation 2019/6 event study, or pandemic-shock effects on resistance. Their public data are real, but the identifying variation is presently inadequate or entangled with surveillance changes.

There is also a second route that does **not** depend on discovering another ready-made public natural experiment: an AMR-specific simulation or methods paper. A rigorous paper can evaluate failure modes of existing estimators, introduce an observation-process diagnostic, build a public benchmark, or study a mechanistic intervention counterfactual. Real data are not automatically required for every one of these genres; what is required is a consequential AMR-specific data-generating process (DGP), known truth, appropriate operating characteristics, transparent code and a journal whose editorial contract matches the claim.

## Decision rules used in this scan

- **GO now:** the public data exist, the estimand is defined, and a useful paper remains possible under honest non-causal or quasi-experimental language.
- **GO to preflight:** first freeze the actual geography/time/denominator structure and simulate power, leverage and measurement error before registering an outcome model.
- **CONDITIONAL GO:** useful only if a specified data audit or negative-control condition succeeds.
- **NO-GO causal:** the data may support description, but the proposed intervention effect is not credibly identified.

For policy work, a segmented ITS should follow the diagnostics in Bernal, Cummins and Gasparrini's original [public-health ITS tutorial](https://pubmed.ncbi.nlm.nih.gov/27283160/); staggered adoption should use a group-time design such as [Callaway and Sant'Anna](https://doi.org/10.1016/j.jeconom.2020.12.001), not an unexamined two-way fixed-effects model. Negative controls must be justified by a causal argument, not chosen merely because another outcome is available; the foundational epidemiologic formulation is Lipsitch, Tchetgen Tchetgen and Cohen's [negative-control paper](https://dash.harvard.edu/entities/publication/73120379-21f6-6bd4-e053-0100007fdf3b). For spatial work, the infectious-disease analogue is the endemic–epidemic decomposition described by Meyer, Held and Höhle in the original [spatio-temporal surveillance paper](https://www.jstatsoft.org/article/view/v077i11).

## Part I — Methods-first library

### Cluster A — Observation-process models: ascertainment, imperfect measurement and reporting delay

**Representative primary methods.** Hui and Walter's [latent-class model without a gold standard](https://pubmed.ncbi.nlm.nih.gov/7370371/) identifies test sensitivity/specificity using multiple populations and tests; Hook and Regal's [capture–recapture framework and limitations](https://pubmed.ncbi.nlm.nih.gov/8654510/) formalises estimation of unobserved cases from overlapping lists; McGough et al.'s [NobBS](https://pubmed.ncbi.nlm.nih.gov/32251464/) estimates delay-adjusted current incidence from reporting triangles.

- **Core estimand:** latent occurrence/prevalence, test/surveillance-system sensitivity and specificity, list completeness, or the final count at event time (t) before all reports arrive.
- **Identification assumptions:** latent-class conditional independence or explicitly modelled dependence; homogeneous or modelled capture probabilities and identifiable list overlap; stable/estimable delay mechanism; compatible case definitions and populations. Aggregate totals from two systems without record-level overlap do **not** identify capture–recapture completeness.
- **Required data signature:** paired test results across at least two populations; or individual identifiers across at least two lists; or repeated release vintages forming event-time × delay triangles; denominators and coverage metadata.
- **Diagnostics/falsification:** posterior predictive checks; alternative dependence structures; subgroup/period stability; simulation under list dependence; backtesting nowcasts against frozen final vintages; comparison with a genuinely mandatory or high-coverage series.
- **Code/data reproducibility:** NobBS supplies an open R implementation and public dengue/influenza examples; latent-class/capture–recapture implementations exist in standard R packages, but reproducibility depends more on releasing overlap tables and priors than on software choice.
- **AMR translations:** voluntary SGSS versus mandatory HCAI calibration; phenotypic AST versus genomic determinant as imperfect tests; GLASS reporting versus an external burden system; prospective revision nowcasting. The strongest novel estimand is the **observation process itself**, not another policy slope.
- **Non-AMR opportunities:** TB case-detection gaps, dengue reporting-delay correction, measles notification completeness, or comparing syndromic and laboratory respiratory surveillance.
- **Novelty/crowding:** moderate overall, low crowding for AMR observation models; high crowding for generic COVID nowcasting.
- **Workload / flagship potential:** medium; **very high flagship potential** when two or more measurement systems have different, explicitly modelled biases.

### Cluster B — Controlled interrupted time series and counterfactual time-series construction

**Representative primary methods/applications.** Bernal et al.'s [ITS tutorial](https://pubmed.ncbi.nlm.nih.gov/27283160/) defines segmented level/slope effects and time-series diagnostics. Brodersen et al.'s [Bayesian structural time-series causal impact model](https://doi.org/10.1214/14-AOAS788) builds a posterior counterfactual from unaffected controls; the author-maintained [CausalImpact implementation](https://google.github.io/CausalImpact/CausalImpact.html) states the critical unaffected-control assumption. England's Quality Premium [prescribing ITS](https://academic.oup.com/cid/article/69/2/227/5136399) is the directly relevant infectious/AMR application.

- **Core estimand:** immediate level change, post-intervention slope change, or cumulative difference between observed and counterfactual outcome over a prespecified post-period.
- **Identification assumptions:** absent the intervention, pre-trend/seasonal structure and the relation to control series would have persisted; no coincident intervention or anticipatory response; control series are unaffected; measurement definitions remain stable.
- **Required data signature:** a sharp intervention date; preferably ≥24–36 pre and ≥12–24 post time points; stable outcome frequency; prespecified control outcomes/units; intervention exposure or “policy bite”.
- **Diagnostics/falsification:** residual autocorrelation/seasonality, pre-fit and pre-period holdouts, placebo dates, leave-one-control-out analysis, unaffected-outcome controls, alternative interruption/lag dates, simulation-based power and coverage.
- **Code/data reproducibility:** Bernal provides worked R code/data; CausalImpact is open-source. These tools do not confer identification when controls are contaminated.
- **AMR translations:** NARMS Veterinary Feed Directive; a hospital formulary restriction; veterinary-sales regulation; antibiotic-shortage or diagnostic-policy shocks. National AMR plans are usually bundles, not sharp interruptions.
- **Non-AMR opportunities:** vaccine/screening introduction, reporting mandates, outbreak-control measures, diagnostic guideline changes.
- **Novelty/crowding:** high crowding for simple COVID or national-policy ITS; moderate for controlled, target-versus-control AMR outcomes with long follow-up.
- **Workload / flagship potential:** low–medium computationally; **high flagship potential only with a credible control and specific intervention**.

### Cluster C — Staggered adoption, synthetic controls and threshold natural experiments

**Representative primary methods.** Callaway and Sant'Anna's [group-time difference-in-differences](https://doi.org/10.1016/j.jeconom.2020.12.001) handles heterogeneous treatment effects and different adoption times; its [open `did` package](https://bcallaway11.github.io/did/reference/did-package.html) includes replication data. Abadie, Diamond and Hainmueller's [synthetic-control method](https://www.hks.harvard.edu/publications/synthetic-control-methods-comparative-case-studies-estimating-effect-californias-0) constructs a weighted untreated counterfactual. Bor et al.'s epidemiologic RD work is operationalised in the [BMJ healthcare RD guide](https://www.bmj.com/content/352/bmj.i1216) and maintained [`rdrobust` software](https://rdpackages.github.io/rdrobust/).

- **Core estimand:** group-time ATT after adoption; treated-unit effect relative to a synthetic counterfactual; or local average treatment effect at a policy/clinical eligibility cutoff.
- **Identification assumptions:** conditional parallel trends with no anticipation/interference for DiD; stable pre-intervention donor relation and no donor contamination for synthetic control; continuity of potential outcomes and no manipulation at the cutoff for RD.
- **Required data signature:** multiple pre-periods and staggered cohorts/not-yet-treated units; or one/few treated units with a rich donor pool and long pre-period; or a continuously measured running variable with a sharp/fuzzy assignment threshold and dense observations near it.
- **Diagnostics/falsification:** event-study pretrends without treating non-rejection as proof; cohort-specific estimates; donor/placebo reassignments and pre-fit RMSPE; RD density/manipulation test, covariate continuity, bandwidth/donut sensitivity and graphical inspection.
- **Code/data reproducibility:** `did`, `Synth`/synthetic-control replication archives and `rdrobust` offer maintained code and examples.
- **AMR translations:** staggered PCV introduction → resistant invasive pneumococcal disease; threshold-based Quality Premium “policy bite”; a local formulary/diagnostic cutoff; synthetic-control evaluation of a country/state animal-antibiotic ban. TrACSS C/D/E transition is too soft/endogenous to become a treatment merely because `did` can fit it.
- **Non-AMR opportunities:** vaccine schedule changes, age-eligibility rules, vector-control rollouts, screening thresholds, border or notification policies.
- **Novelty/crowding:** methodologically crowded; novelty depends on unusually credible assignment and outcome data, not on using a fashionable estimator.
- **Workload / flagship potential:** medium–high design labour; **high flagship potential** for PCV or a genuinely sharp AMR policy, low if adoption is self-reported.

### Cluster D — Target-trial, self-controlled and test-negative designs

**Representative primary methods.** Hernán and Robins' [target-trial emulation framework](https://academic.oup.com/aje/article-pdf/183/8/758/6652570/kwv254.pdf) forces explicit eligibility, strategies, time zero, follow-up, outcomes and causal contrasts. Farrington's original [self-controlled case-series](https://pubmed.ncbi.nlm.nih.gov/7766778/) conditions on cases to compare risk windows with control time. Sullivan et al.'s [test-negative design rationale](https://www.sciencedirect.com/science/article/pii/S0264410X13002429) addresses vaccine effectiveness among healthcare-seeking tested patients.

- **Core estimand:** intention-to-treat/per-protocol effect of a treatment strategy; within-person relative incidence in a post-exposure risk window; or vaccine effectiveness odds ratio in the tested symptomatic population.
- **Identification assumptions:** no unmeasured confounding, consistency, positivity and aligned time zero for target trials; event-independent exposure and correctly modelled age/time effects for SCCS; comparable care-seeking/testing and no exposure effect on test-negative illnesses for TND.
- **Required data signature:** individual longitudinal exposure, eligibility, confounders and outcomes; exact event/exposure dates for SCCS; individual symptomatic testing, results and vaccination/exposure histories for TND. Country-level public panels cannot emulate these designs.
- **Diagnostics/falsification:** protocol table before analysis, clone/censor/weight diagnostics and weight positivity; pre-exposure SCCS windows; alternative risk windows; TND negative controls, prior-infection and test-misclassification sensitivity.
- **Code/data reproducibility:** methods/code are public, but useful clinical data are usually restricted; this is a collaboration/data-access lane rather than an immediate public-data lane.
- **AMR translations:** target trial of narrow- versus broad-spectrum empiric treatment on later resistant infection; SCCS of antibiotic exposure and resistant infection/colonisation; resistant-versus-susceptible case-case designs among culture-positive patients. These estimate individual effects or exposure enrichment, not national AMR policy effects.
- **Non-AMR opportunities:** vaccine effectiveness/safety, post-exposure vaccination, treatment comparative effectiveness.
- **Novelty/crowding:** high crowding for COVID/vaccine TND; lower for rigorously emulated antimicrobial-treatment strategies with time-varying confounding.
- **Workload / flagship potential:** high and data-access dependent; **potentially flagship with clinical collaboration**, not currently an independent-public-data priority.

### Cluster E — Negative controls and bias-orthogonal triangulation

**Representative primary methods.** Lipsitch, Tchetgen Tchetgen and Cohen's [negative-control framework](https://dash.harvard.edu/entities/publication/73120379-21f6-6bd4-e053-0100007fdf3b) distinguishes exposure and outcome controls; Lawlor, Tilling and Davey Smith's [triangulation framework](https://academic.oup.com/ije/article/45/6/1866/2930550) requires approaches with different, preferably oppositely directed, key biases.

- **Core estimand:** usually the original causal/associational estimand plus a prespecified bias-detection contrast; triangulation yields strengthened/weakened qualitative inference rather than a mechanically pooled estimate.
- **Identification assumptions:** the negative control shares the confounding/selection structure but cannot be caused through the target pathway; triangulated approaches have genuinely different—not merely differently parameterised—biases.
- **Required data signature:** at least one biologically justified control exposure/outcome, or two-plus data/design systems with an explicit expected bias-direction table.
- **Diagnostics/falsification:** DAG for every control; expected sign of bias written before results; positive-control calibration; “leave-one-approach-out” conclusion table; refuse to call correlated antibiotic phenotypes negative controls without addressing co-selection.
- **Code/data reproducibility:** no special software; reproducibility depends on publishing the causal DAG, control definitions and bias-direction ledger.
- **AMR translations:** class-matched prescribing → matched resistance with distant comparator classes; animal-policy target drugs versus unaffected drugs; GLASS/EARS/GRAM comparisons whose ascertainment/model biases point in different directions.
- **Non-AMR opportunities:** vaccine safety/effectiveness, environmental drivers of vector-borne disease, surveillance-policy evaluation.
- **Novelty/crowding:** low as a method label, but still underused correctly in ecological AMR.
- **Workload / flagship potential:** low marginal cost, **high value as an upgrade to every flagship**, rarely sufficient as a standalone paper.

### Cluster F — Distributed-lag and dynamic exposure–response models

**Representative primary method.** Gasparrini, Armstrong and Kenward introduced [distributed lag non-linear models](https://doi.org/10.1002/sim.3940); the open [JSS `dlnm` paper, code and worked data](https://pmc.ncbi.nlm.nih.gov/articles/PMC3191524/) show cross-basis specification and interpretation.

- **Core estimand:** lag-specific and cumulative change in outcome over a frozen lag window and exposure contrast, potentially with a non-linear exposure–response surface.
- **Identification assumptions:** no uncontrolled time-varying confounding correlated across lags; correct temporal alignment; adequate time resolution and support; lag window/basis not chosen from the outcome; no severe exposure measurement error.
- **Required data signature:** regular area-time exposure and outcome series with substantially more time points than lag parameters; seasonality/trend/testing covariates; preferably multiple areas for replication/partial pooling.
- **Diagnostics/falsification:** pre-specified lag basis; penalisation/sensitivity grid; residual autocorrelation; negative-control lags/exposures/outcomes; leave-area-out stability; simulation of lag recovery under the observed geometry.
- **Code/data reproducibility:** `dlnm` is open and the original examples are reproducible.
- **AMR translations:** monthly drug-class prescribing → matched resistance 3–24 months later; weather/flooding → resistant enteric infections; hospital antibiotic use → unit-level resistance where data exist.
- **Non-AMR opportunities:** climate–dengue/malaria, air pollution–respiratory infection, mobility–transmission with delayed effects.
- **Novelty/crowding:** high in climate epidemiology, moderate in AMR; ecological causal interpretation remains the main vulnerability.
- **Workload / flagship potential:** medium; **good lower-risk paper**, flagship only when paired with a strong observation model and negative controls.

### Cluster G — Spatial surveillance, endemic–epidemic decomposition and cluster detection

**Representative primary methods.** Held, Höhle and Hofmann's multivariate surveillance model and Meyer, Held and Höhle's open [`surveillance`/`hhh4` implementation](https://www.jstatsoft.org/article/view/v077i11) decompose endemic, autoregressive and neighbourhood components. Kulldorff's [prospective space–time scan statistic](https://doi.org/10.1111/1467-985X.00186) underlies official [SaTScan](https://surveillance.cancer.gov/satscan/) tools.

- **Core estimand:** relative contribution of endemic, within-area and spatially imported components; power-law/distance decay; or a calibrated alarm for an excess space–time cluster.
- **Identification assumptions:** counts and denominators are comparable; adjacency/mobility weights proxy the transmission-relevant network; observation intensity is modelled; residual dependence is controlled. Scan statistics detect anomalous clusters, not their causes.
- **Required data signature:** regular small-area counts, denominators/offsets, adjacency or connectivity matrix, adequate repeated time; for prospective detection, frozen historical baselines and release schedule.
- **Diagnostics/falsification:** one-step-ahead scoring, residual maps, alternative weight matrices, permutation/simulation false-alarm rates, ascertainment covariates, prospective holdout, cluster stability under reporting exclusions.
- **Code/data reproducibility:** `surveillance` includes paper demos; SaTScan is freely available with documentation.
- **AMR translations:** EARS-Net spatial association; UK ICB resistant-BSI clusters adjusted for testing; emergence alarms for resistance phenotypes. Claim “observed diffusion” unless genomic/epidemiologic linkage supports transmission.
- **Non-AMR opportunities:** measles/TB spread, invasive meningococcal disease, foodborne outbreak detection, vector-borne clusters.
- **Novelty/crowding:** ordinary hotspot maps are crowded; observation-aware endemic–epidemic decomposition or prospective validation remains stronger.
- **Workload / flagship potential:** medium–high; **medium flagship potential** with aggregate data, higher when connected to genomics.

### Cluster H — Genomic phylogeography and transmission-tree reconstruction

**Representative primary methods.** Lemey et al.'s [Bayesian discrete phylogeography](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1000520) jointly infers timed spatial transitions; Didelot et al.'s [TransPhylo](https://xavierdidelot.github.io/TransPhylo/index.html) reconstructs transmission in partially sampled outbreaks and explicitly permits unsampled intermediates.

- **Core estimand:** posterior migration history/rates, introduction count, dated ancestry or transmission tree—not a regression coefficient between country prevalence and distance.
- **Identification assumptions:** adequate molecular-clock signal and phylogenetic model; location sampling process not catastrophically informative or explicitly modelled; correct generation-time/within-host assumptions; recombination controlled for bacterial genomes.
- **Required data signature:** quality-controlled genomes with collection dates, locations and preferably clinical/source metadata; a dated phylogeny; sampling fractions/epidemiology for transmission reconstruction.
- **Diagnostics/falsification:** temporal-signal/date randomisation; downsampling by place/time/source; prior sensitivity; recombination masking; alternative clock/demographic models; posterior predictive checks; compare first observed detection with inferred introduction.
- **Code/data reproducibility:** BEAST-family tools and TransPhylo are open; TransPhylo provides vignettes and code. NCBI/ENA can supply public sequences, but metadata completeness must pass a gate.
- **AMR translations:** importation versus local expansion of carbapenemase-producing *K. pneumoniae*; repeated emergence versus transmission of resistance determinants; One Health source mixing.
- **Non-AMR opportunities:** TB clusters, foodborne outbreaks, zoonotic introductions, influenza/arbovirus spread.
- **Novelty/crowding:** global genome-description papers are crowded; sharp sampling-aware transmission questions can still be flagship.
- **Workload / flagship potential:** high and collaboration-friendly; **very high flagship potential** if metadata and sampling audits succeed.

### Cluster I — Multivariate early warning and probabilistic forecasting

**Representative primary methods.** Kulldorff et al.'s [multivariate scan statistic](https://onlinelibrary.wiley.com/doi/10.1002/sim.2818) and [tree-based scan](https://onlinelibrary.wiley.com/doi/abs/10.1111/1541-0420.00039) search multiple related outcomes while accounting for multiplicity. Reich et al.'s [multi-year influenza forecast comparison](https://pmc.ncbi.nlm.nih.gov/articles/PMC6386665/) supplies public code/data and demonstrates ensemble evaluation; Gneiting and Raftery's [proper scoring-rule framework](https://doi.org/10.1198/016214506000001437) separates calibration and sharpness.

- **Core estimand:** prospective probability of future outcome/threshold, out-of-sample proper score, calibrated alarm rate, or location of an anomalous branch in a prespecified pathogen–drug hierarchy.
- **Identification assumptions:** not causal; requires stable target definition, genuine prospective/rolling-origin evaluation, no leakage, and a reporting-delay policy.
- **Required data signature:** repeated timestamped releases, multiple seasons/years, frozen targets and baselines; for tree scans, counts/denominators mapped to a stable drug/pathogen ontology.
- **Diagnostics/falsification:** rolling-origin holdout, naive seasonal/random-walk benchmark, log/WIS/Brier scores, calibration plots, coverage, false-alert simulations and external-season validation. In-sample RMSE is not sufficient.
- **Code/data reproducibility:** FluSight code/data are archived; scan-statistic software is available; forecast output should use a public schema and immutable vintages.
- **AMR translations:** early warning across pathogen–drug combinations; forecasting local resistance with uncertainty; ensemble comparison of mechanistic, statistical and persistence models. Slow annual GLASS series are weak; UK monthly and isolate/genomic feeds are better.
- **Non-AMR opportunities:** seasonal influenza/RSV, dengue, hospital-acquired infection alerts, foodborne surveillance.
- **Novelty/crowding:** high for generic ML forecasts; lower for prospective AMR benchmark infrastructure with proper scoring and revision handling.
- **Workload / flagship potential:** medium for a benchmark, high calendar-time for prospective evaluation; **medium–high flagship potential** as shared infrastructure, not as a single high-AUC model.

## Simulation, synthetic-data and mechanistic-modelling track

Simulation is not a consolation prize for lacking patient-level data. It answers questions that real data alone cannot answer because bias, coverage, false-alarm probability and the true causal or latent parameter are unknown in observed datasets. The minimum standard should be Morris, White and Crowther's [ADEMP framework](https://pubmed.ncbi.nlm.nih.gov/30652356/): freeze **a**ims, **d**ata-generating mechanisms, **e**stimands, **m**ethods and **p**erformance measures; report Monte Carlo standard errors; preserve failed fits; and release executable code, seeds and scenario manifests. Burton et al.'s earlier [medical-statistics simulation guidance](https://pubmed.ncbi.nlm.nih.gov/16947139/) additionally supports writing the simulation protocol before execution. Calibration to an observed marginal distribution is useful, but it does not validate an unidentifiable DGP.

### Four distinct simulation-paper genres

| Genre | Scientific product and minimum comparison | Is a real-data demonstration necessary for publishability? | AMR-specific DGP or bias that can create genuine novelty | Best-fit outlet family |
|---|---|---|---|---|
| **1. Evaluation of existing estimators** | Map where prespecified estimators fail; include a defensible baseline and report bias, coverage, RMSE, convergence, decision error, leverage and computation, not only power | **No in principle** for a rigorous methodological evaluation; strongly helpful as a geometry anchor. For an AMR journal, include at least one public-data vignette showing that the studied geometry actually occurs | Selective AST, denominator noise, country/laboratory reporting, resistant-isolate deduplication, breakpoint revisions, sparse drug–bug cells, MNAR missingness, small-country leverage, and surveillance-versus-modelled outcome mismatch | *Statistics in Medicine*, *BMC Medical Research Methodology*, *Statistical Methods in Medical Research*; AMR outlet after an applied vignette |
| **2. New estimator or diagnostic development** | Define the estimand and identification region, derive or justify the procedure, compare against relevant competitors, and show calibrated uncertainty plus failure boundaries | **Usually yes as an illustration, not necessarily as proof**, for epidemiology/AMR/npj outlets. A methods journal may accept theory + extensive simulation + open software without a substantive real-data result | A latent ascertainment model; variance correction for noisy resistance proportions; a sign-reversal/construct-discordance diagnostic; partial identification under unknown testing selection; breakpoint-bridging measurement model | *Biometrics*, *Statistics in Medicine*, *BMC Medical Research Methodology*; *npj Antimicrobials and Resistance* when the AMR insight is substantive |
| **3. Benchmark and reproducibility study** | Frozen tasks, public train/test splits or rolling origins, naive baselines, uncertainty scoring, leakage audit, distribution-shift strata and a reusable harness; ideally a hidden or prospective holdout | **Yes for claims about real-world predictive performance.** A synthetic-only challenge is publishable only when the target is estimator recovery or operational characteristics, not clinical utility | Reporting revisions, delayed outcomes, changing panels, class imbalance, new breakpoints, laboratory/country shift, outbreak regimes, phenotype–genotype discordance and missing metadata | *npj Digital Medicine* for a deployable digital-surveillance benchmark; *PLOS Computational Biology*, *Epidemics* or *Eurosurveillance* for infectious-surveillance insight |
| **4. Mechanistic transmission / mathematical / agent-based modelling** | A transparent causal mechanism, parameter and structural uncertainty, competing mechanisms, calibration/validation targets where available, and policy scenarios that expose non-linear or emergent behaviour | **Not intrinsically**, if the contribution is a general theorem/mechanism or a clearly bounded synthetic experiment. **Usually yes** for policy claims and for *Epidemics*, whose scope explicitly requires high-quality novel or published data and biological insight | Antibiotic exposure as both treatment and selection pressure; susceptible/resistant strain competition; fitness costs and compensatory evolution; colonisation versus infection; horizontal gene transfer; patient–hospital–community/animal networks; importation plus changing testing | *Epidemics*, *PLOS Computational Biology*, *Journal of the Royal Society Interface*, *npj Systems Biology and Applications*, *npj Complexity*; stronger AMR journals when calibrated |

These are different manuscripts. “We simulated our planned study and power was low” is design assurance, not automatically a publishable evaluation paper. It becomes a paper when it establishes a general, reproducible failure region, compares realistic alternatives and changes what analysts should do.

### Track S1 — Evaluate ecological AMR estimators under an explicit observation process

**Publishable question.** When do country- or area-level policy–resistance estimates reverse sign, falsely appear equivalent, or become dominated by one unit because AST selection and surveillance coverage differ by exposure and latent resistance?

**DGP.** Generate latent infection/colonisation, prescribing or policy exposure, healthcare access, culture submission, AST completion, resistant status and release/reporting. Cross factors that are characteristic of AMR rather than generic missingness: selection on severity and prior antibiotics; laboratory testing capacity correlated with health-system capacity; pathogen–drug-specific denominators; country entry/exit; breakpoint shifts; aggregation of multiple laboratories; and a second “modelled burden” outcome partially informed by the same surveillance stream. Anchor denominator and coverage ranges to UKHSA, EARS-Net, GLASS or NARMS geometry without inserting their observed association as truth.

**Methods and outputs.** Compare naive weighted/unweighted ecological regression, beta-binomial/hierarchical models, inverse-observation weighting, measurement-error correction and sensitivity/partial-identification analysis. Freeze null, same-sign/different-magnitude, sign-reversal and boundary scenarios. Report component-specific bias, interval width, coverage, false-important/false-equivalent decisions, power, leave-one-unit-out movement, non-convergence and Monte Carlo uncertainty.

**Real-data requirement.** Not necessary for the central operating-characteristic claim, because truth is the reason for simulating. One public-data geometry table and a worked vignette substantially improve credibility and fit for *npj Antimicrobials and Resistance* or a substantive epidemiology journal. This is the most direct simulation flagship for the current programme.

### Track S2 — Develop an observation-process estimator or falsification diagnostic

Three plausible contributions should be treated as alternatives, not packed into one paper:

1. **Latent-SD standardisation for binomial/beta-binomial AMR outcomes:** separate between-area latent variation from finite-denominator sampling variation, propagate uncertainty, and state the boundary at which the correction becomes unstable.
2. **Construct-discordance diagnostic:** quantify whether exposure associations change beyond sampling uncertainty when the outcome is resistance proportion, resistant-infection incidence or modelled burden; include overlap/shared-input sensitivity rather than assuming independent systems.
3. **Partial identification under informative testing:** let culture/AST selection vary within scientifically defensible bounds and return an identification region or robustness value instead of a single corrected effect.

**Minimum evidence.** Mathematical estimand/assumptions, simulation against naive and best available competitors, weak-identification diagnostics, software tests, and one small public example. The example demonstrates usability; it does not prove that the identifying assumptions hold. A purely cosmetic estimator with slightly lower RMSE is unlikely to clear a strong journal. Novelty comes from an AMR observation mechanism that existing generic missing-data tools do not encode.

### Track S3 — Build a leakage-resistant public AMR benchmark

**Candidate tasks.** (i) rolling-origin probabilistic forecasting of pathogen–drug resistance at area-month or country-year level; (ii) early detection of an emerging phenotype/determinant in a prespecified hierarchy; (iii) phenotype prediction from genomes or mass spectra under temporal and geographic shift; or (iv) nowcasting a deliberately archived reporting revision. The benchmark must include persistence/seasonal and parsimonious regression baselines, not just fashionable machine learning.

**Design.** Freeze ontology, eligibility, deduplication, training cutoff, target availability date and evaluation metric; quarantine the final time/geography; distinguish interpolation from external transport; score probabilities with proper rules; report calibration, coverage and subgroup failure; publish containers/environment lock, manifests and a single command that recreates tables. Add synthetic stress tests in which the true delay, missingness or outbreak regime is known. Cluster I's FluSight example shows why multi-year, out-of-sample comparison is a stronger contribution than a single model.

**Real-data requirement.** Yes if the conclusion concerns real surveillance performance. Public UKHSA, EARS-Net, NARMS or NCBI data can provide it without restricted access, but an immutable release archive may have to be created prospectively. *npj Digital Medicine* becomes plausible only when the contribution is a reusable digital-surveillance system with external/temporal validation; generic retrospective AMR prediction is a weak fit.

### Track S4 — Mechanistic AMR transmission and intervention counterfactuals

**Model choices.** Start with the least complex structure able to represent the question: multi-strain compartmental model for population selection/transmission; network or metapopulation model for geographic/hospital importation; or agent-based model only when heterogeneity, contacts, treatment courses and facility movement are causal to the result. Document an ABM using the updated [ODD protocol](https://www.jasss.org/23/2/7.html), and separate calibration targets from validation targets.

**AMR mechanisms worth modelling.** Treatment reduces susceptible disease while selecting resistance; colonisation and infection have different observation probabilities; antibiotics act across bystander species; resistance has variable fitness cost/compensation; horizontal gene transfer and clonal spread coexist; patients move through hospital/community/long-term-care networks; stewardship changes both treatment success and onward transmission.

**Concrete questions.** Compare antibiotic-shortage allocation strategies; identify when PCV reduces resistant invasive disease through disease prevention versus serotype replacement; quantify conditions under which class-specific stewardship merely substitutes resistance; or test whether targeted screening beats universal screening under importation. A 2026 [pneumococcal shortage model](https://www.nature.com/articles/s41467-026-72777-y) shows that calibrated mechanistic AMR counterfactuals can reach a broad journal when they resolve a current policy trade-off.

**Real-data requirement.** A theory/complex-systems paper can be synthetic if it reveals a robust general mechanism. A claim recommending policy needs empirical parameter ranges, uncertainty analysis and calibration/validation against published or public data. Do not call a scenario “predicted impact” when it is an uncalibrated thought experiment.

### Journal-fit ladder for methods and simulation work

The journal should be chosen after the paper genre and evidentiary contract are frozen. Nature Portfolio is broader than only *Nature*/*Nature Medicine*, and a strong specialist venue can be the more credible target.

| Outlet or family | Good fit from this library | Evidence contract / warning |
|---|---|---|
| [npj Antimicrobials and Resistance](https://www.nature.com/npjamar/journal-information) | AMR-specific estimator/diagnostic, calibrated mechanistic model, or observation-process study with a substantive AMR conclusion | Broad basic/applied/clinical AMR scope, but an Article must still be substantial original research. Simulation-only is plausible when AMR insight is central; a generic method relabelled as AMR is not. |
| [npj Systems Biology and Applications](https://www.nature.com/npjsba/aims) | Multi-scale within-host/population resistance dynamics, host–pathogen or horizontal-transfer systems model | Explicitly welcomes computational and mathematical modelling of complex biological systems. Stronger fit for biological mechanism than country-policy regression. |
| [npj Complexity](https://www.nature.com/articles/s44260-024-00004-0) | Network, emergence, non-linearity or cross-scale resistance theory with general complex-systems insight | Can support a synthetic/theoretical contribution, but the result must travel beyond one AMR dataset and be intelligible across disciplines. |
| [npj Digital Medicine](https://www.nature.com/npjdigitalmed/aims) | Deployable/prospective AMR surveillance benchmark, externally validated decision support, digital phenotyping/diagnostics | Not a default home for an ecological simulation. Requires digital-health relevance, robust validation and realistic use context. |
| *Nature Communications* | Mechanistic or methodological work that changes understanding beyond one setting, with decisive validation | Treat as an upside target, not the design criterion. General biological/policy insight and exceptional validation are needed. |
| [Epidemics](https://www.sciencedirect.com/journal/epidemics) | Transmission/phylodynamic models, synthetic challenge plus biological application, calibrated policy scenarios | The journal explicitly requires high-quality novel or published data and a clear biological application; a simulation-only estimator paper without application is mismatched. |
| *PLOS Computational Biology* / *Journal of the Royal Society Interface* | General computational, network, evolutionary or mechanistic contribution with open code and biological insight | Strong specialist options; simulation is normal, but the mechanism or method must be more general than one scenario analysis. |
| *Statistics in Medicine* / *Biometrics* / *BMC Medical Research Methodology* | Existing-estimator evaluation, new estimator, partial-identification or design diagnostic | Best home when operating characteristics/method are the contribution. Real-data illustration is helpful and often expected, but known-truth simulation and methodological advance carry the paper. |
| *Eurosurveillance* / *Emerging Infectious Diseases* / *Clinical Microbiology and Infection* / *JAC—Antimicrobial Resistance* | Real surveillance evaluation, outbreak/implementation result, or validated applied method | Strong applied venues; a real public-health or microbiological result is normally necessary. They should not be treated as fallback journals for an abstract simulation. |

### Ranked simulation-first concepts for an independent researcher

1. **Observation-selection challenge for ecological AMR:** highest fit with the current expertise and directly generalises the Stage-A design diagnostics; feasible with R and public geometry; high methods-journal potential and plausible npj AMR application.
2. **Construct-discordance / partial-identification method:** higher mathematical burden but stronger originality; build only after a narrow estimand and identifiability proof are agreed.
3. **Public AMR forecasting and alarm benchmark:** feasible without restricted data, but requires careful immutable-vintage construction and ideally prospective time; strong shared-resource value.
4. **Mechanistic pneumococcal or hospital-resistance intervention model:** potentially highest impact, but parameterisation, calibration and domain collaboration make it less independent-researcher friendly.
5. **Pure ABM platform:** no-go as a first objective. A platform without a sharp biological question, verification/validation plan and policy-relevant counterfactual is software, not yet an epidemiology paper.

## Methods-derived publication portfolio

### Flagship lanes

1. **Observation-aware AMR epidemiology.** Jointly model mandatory cases, voluntary susceptibility testing and resistance; later triangulate surveillance and modelled burden. This uses Cluster A + E and is immediately instantiated by Candidate 1.
2. **A genuinely designed natural experiment.** Use target/control outcomes and unaffected comparators around a specific policy such as the US VFD or staggered PCV introduction. This uses Clusters B/C/E; a TrACSS category alone does not qualify.
3. **Sampling-aware genomic diffusion.** Separate repeated introductions from local clonal expansion for one prespecified organism–determinant pair. This uses Clusters G/H and requires a strict metadata gate.
4. **Phenotype–genotype measurement without assuming either is a gold standard.** Use paired isolate-level AST/genomic data and a latent-class or discordance model, stratified by source/population. This uses Cluster A/H and could become a high-impact laboratory-surveillance methods paper if a sufficiently complete public or collaborative dataset exists.
5. **Prospective multivariate AMR early-warning benchmark.** Archive immutable releases, publish targets and score probabilistic models/alarms prospectively. This uses Clusters A/I; it is infrastructure-first and slower, but more durable than a one-off forecast.

### Lower-risk, faster papers

- ECDC resistance proportion versus resistant-BSI incidence (Candidate 4): a bounded measurement-construct paper.
- England ICB class-matched prescribing/resistance with testing and negative controls (Candidate 2): a longitudinal ecological paper after simulation.
- NARMS VFD registered replication/update (Candidate 3): lower novelty but high reproducibility.
- PCV event-study geometry/power audit followed by analysis only if cohorts/preperiods pass (Candidate 5).
- A methods note showing why historical GLASS/UKHSA nowcasting is unidentified without release vintages, paired with a prospective archive (Candidate 8).

### LMIC applicability as a later scoring dimension

| Method family | Potential LMIC relevance | Main feasibility bottleneck |
|---|---|---|
| Observation/ascertainment models | Very high | overlap identifiers, denominators and stable case definitions are often unavailable publicly |
| ITS/natural experiments | High where a sharp policy exists | short/irregular surveillance and coincident programmes |
| PCV/vaccine event studies | High | few pre-periods, changing vaccine schedules and sparse invasive isolate counts |
| Spatial/count surveillance | High | changing catchments and denominator quality |
| Genomic epidemiology | High scientific relevance | severe country/time/source sequencing imbalance |
| Forecasting/early warning | High operational relevance | immutable historical vintages and sustained prospective evaluation |
| Target trial/TND/SCCS | High clinical relevance | individual-level linked data and governance, not statistical software |

LMIC applicability should therefore influence later portfolio balance and external validity, but it should not be used to exclude methods or high-income settings at discovery stage.

## Part II — Dataset-verified implementation candidates

### Candidate 1 — Calibrating voluntary AMR surveillance against mandatory bloodstream-infection surveillance in England

**Infectious-disease analogue.** Sentinel influenza or syndromic surveillance is calibrated against a more complete case or hospitalisation series; test volume and reporting coverage are treated as an observation process rather than as ordinary confounders.

**Transferable design.** Linked area-month measurement study. For *E. coli* bloodstream infection, compare the voluntary SGSS AMR module's number tested and percentage tested with mandatory HCAI *E. coli* bacteraemia episodes. Estimate geographic and temporal variation in ascertainment; then quantify how resistance trends/rankings change when the tested sample is calibrated to the mandatory case series. The same architecture can be extended to MRSA and other organisms only where definitions truly align.

**AMR question.** How much of apparent local variation and temporal change in resistance reflects testing/reporting coverage rather than resistant infection occurrence?

**Exact public sources.**

- [UKHSA AMR dashboard](https://ukhsa-dashboard.data.gov.uk/antimicrobial-resistance) — public monthly resistance for seven bloodstream/bacteriuria organism groupings; Open Government Licence, no login.
- [E. coli bacteraemia AMR page](https://ukhsa-dashboard.data.gov.uk/antimicrobial-resistance/antimicrobial-resistance-in-ecoli-bacteraemia) — downloadable monthly resistance, number tested and percentage tested; currently April 2021–April 2026.
- Metric/API names and definitions: [`e-coli_testing_bacteraemiaNumberTestedRollingMonth`](https://ukhsa-dashboard.data.gov.uk/metrics-documentation/antimicrobial-resistance-in-e-coli-bacteraemia-resistance-testing-by-month), `e-coli_testing_bacteraemiaPercentTestedRollingMonth`, and [`e-coli_testing_bacteraemiaPercentResistantRollingMonth`](https://ukhsa-dashboard.data.gov.uk/metrics-documentation/antimicrobial-resistance-in-e-coli-bacteraemia-percent-of-resistance-by-month).
- Mandatory comparator: [`e-coli_cases_countsByOnsetType`](https://ukhsa-dashboard.data.gov.uk/metrics-documentation/e-coli-monthly-cases-by-onset-type), described by UKHSA as mandatory trust-level surveillance covering 135 acute trusts and 106 sub-ICB locations.

**Geographic/time grain and likely coverage.** Monthly; England, UKHSA region, ICB/sub-ICB and/or acute-trust grain depending on metric. The AMR module begins April 2021 and is based on voluntary data from approximately 98% of hospital microbiology laboratories; mandatory HCAI data have broader historical coverage. Expect roughly 61 AMR months and up to about 100 sub-ICB locations, but the exact common geography must be audited because NHS boundaries changed.

**Login/request.** None. Dashboard downloads and API-backed metrics are public under OGL.

**Minimal estimand.** For area (i), month (t), antibiotic (a):

\[
A_{ita}=\frac{\text{SGSS episodes tested}_{ita}}{\text{mandatory E. coli BSI episodes}_{it}},
\]

followed by (i) between-area variance in (A_{ita}), (ii) within-area trend in (A_{ita}), and (iii) the change in area rankings or trend estimates after explicit calibration/standardisation. It is not necessary to claim that the mandatory system is a perfect gold standard.

**Major identification/measurement bias.** Different deduplication, onset and reporting definitions; a susceptibility-tested episode is not guaranteed to be the same episode counted in mandatory surveillance; three-month rolling averages induce serial correlation; laboratory catchments do not perfectly match administrative geography. The ratio may therefore measure system discordance, not literal sensitivity.

**Independent-researcher workload.** **Low–medium.** API/download extraction, organisation-code crosswalk, boundary freeze, beta-binomial or measurement-error modelling. No restricted patient data.

**Novelty risk.** **Low–moderate.** UKHSA previously described the public AMR indicators in a peer-reviewed [Fingertips data paper](https://researchportal.ukhsa.gov.uk/en/publications/improving-feedback-of-surveillance-data-on-antimicrobial-consumpt/), but the new dashboard exposes a particularly useful monthly mandatory/voluntary comparison. A literature search must confirm that this exact calibration has not been published.

**Verdict.** **GO now.** This is the best fit with the current research programme because it turns ascertainment from a nuisance covariate into the estimand.

### Candidate 2 — Matched antibiotic consumption and resistance at ICB-month level, with negative-control classes

**Infectious-disease analogue.** Distributed-lag studies of climate, mobility, vaccination or interventions on infection incidence, strengthened with prespecified outcomes that should not respond to the exposure through the hypothesised pathway.

**Transferable design.** Area-month panel with area and calendar-time effects, flexible seasonality, distributed lags, and drug-class matching. Examples: fluoroquinolone prescribing → ciprofloxacin-resistant *E. coli*; third-generation cephalosporin exposure → 3GC-resistant *E. coli*. Prespecify negative-control outcomes (for example, an antibiotic whose resistance should not respond directly over the selected lag), while acknowledging cross-resistance and co-selection.

**AMR question.** Do local changes in use of a specific antibiotic class precede changes in phenotypically matched resistance, beyond common national trends and changes in testing intensity?

**Exact public sources.**

- [NHSBSA English Prescribing Dataset](https://opendata.nhsbsa.net/dataset/english-prescribing-dataset-epd-with-snomed-code) — comprehensive monthly prescriptions issued by NHS primary-care prescribers and dispensed in the community, linked to GP practice/primary-care organisation; bulk files, no login.
- [UKHSA total antibiotic-use dashboard](https://ukhsa-dashboard.data.gov.uk/antimicrobial-consumption/total-antibiotic-use) — monthly DID and Access proportions, useful for national validation.
- [UKHSA E. coli bacteraemia AMR](https://ukhsa-dashboard.data.gov.uk/antimicrobial-resistance/antimicrobial-resistance-in-ecoli-bacteraemia) and [E. coli bacteriuria AMR](https://ukhsa-dashboard.data.gov.uk/antimicrobial-resistance/antimicrobial-resistance-in-e-coli-bacteriuria) — monthly ICB/region resistance and testing metrics.
- The observation process is documented in the [UKHSA metric methodology](https://ukhsa-dashboard.data.gov.uk/metrics-documentation/antimicrobial-resistance-in-e-coli-bacteraemia-resistance-testing-by-month).

**Geographic/time grain and likely coverage.** Exposure: GP-practice-month nationwide, aggregable to stable ICB/sub-ICB boundaries. Outcome: area-month, April 2021–April 2026 at verification, with seven antibiotic groups for *E. coli* BSI and additional organisms. Roughly 61 months × up to 42 historical ICBs (or approximately 100 sub-ICB locations), subject to boundary and suppression audit.

**Login/request.** None.

**Minimal estimand.** Within-area elasticity or absolute change in resistance proportion associated with a one-SD reduction in matched-class prescriptions over a prespecified lag window, contrasted with the corresponding association for negative-control outcomes/exposures.

**Major identification bias.** Indication and reverse-causation bias (local resistance changes prescribing); unmeasured infection mix and hospital antibiotic use; COVID-era changes in consultation, specimens and patient mix; ecological exposure mismatch; cross-resistance makes many intuitive “negative controls” invalid. Calendar fixed effects remove national shocks but not local time-varying confounding.

**Independent-researcher workload.** **Medium.** NHSBSA files are large but technically manageable; the main labour is code crosswalking, boundary harmonisation and a registered lag/negative-control DAG.

**Novelty risk.** **Moderate.** The 2015 Quality Premium has already been evaluated with non-public linked data in an original [quasi-experimental resistance study](https://pubmed.ncbi.nlm.nih.gov/34363774/). Novelty must come from the new monthly public dashboard, class-matched lags, explicit testing process, and/or post-2021 local heterogeneity—not from claiming to rediscover that stewardship affects prescribing.

**Verdict.** **GO to data-geometry and negative-control preflight.** Strong independent-researcher project if framed as a falsifiable longitudinal ecological study, not as automatic causal proof.

### Candidate 3 — US Veterinary Feed Directive: source-controlled interrupted time series in NARMS

**Infectious-disease analogue.** Vaccine or vector-control ITS with target outcomes, control outcomes and multiple surveillance strata, rather than a single before/after mean.

**Transferable design.** Update the evaluation of the January 2017 implementation of FDA Guidance for Industry #213/Veterinary Feed Directive. Use segmented beta-binomial models across animal, retail-meat and human isolates; compare medically important drug–organism outcomes expected to respond with outcomes less directly targeted; allow source-specific level/slope changes and prespecified biological lags.

**AMR question.** Did resistance decline after veterinary oversight and removal of growth-promotion indications, first in food-animal/retail-meat isolates and subsequently in human foodborne isolates?

**Exact public sources.**

- [FDA NARMS Now Integrated Data](https://www.fda.gov/animal-veterinary/national-antimicrobial-resistance-monitoring-system/narms-now-integrated-data) — source spreadsheets and dashboards for humans, food animals and retail meats; the source data are explicitly non-confidential and require no login.
- [CDC NARMS data and reports](https://www.cdc.gov/narms/data/index.html) — more than two decades of human enteric AMR surveillance and official archive links.
- [FDA policy timeline](https://www.fda.gov/animal-veterinary/antimicrobial-resistance/timeline-fda-action-antimicrobial-resistance) and [FDA VFD fact sheet](https://www.fda.gov/animal-veterinary/development-approval-process/fact-sheet-veterinary-feed-directive-final-rule-and-next-steps) — implementation completed in January 2017.
- Existing original evaluation: [2012–2019 early evaluation](https://pubmed.ncbi.nlm.nih.gov/37448772/) and a published [retail-meat ITS application](https://pmc.ncbi.nlm.nih.gov/articles/PMC10399851/).

**Geographic/time grain and likely coverage.** Source × year × organism × antimicrobial × specimen/animal or meat type; NARMS began in 1996, though consistent strata have shorter series and public state identifiers are incomplete. Effective time-series n is usually roughly 10–20 pre-policy years and 7–9 post-policy years, with hundreds to thousands of isolates per pooled stratum rather than 50 independent states.

**Login/request.** None for aggregate dashboards/source spreadsheets. Human isolate state-level data are limited to states that permit release; pooled totals include all participating states.

**Minimal estimand.** Difference in post-2017 level and slope change for a prespecified target resistance phenotype in food-animal/retail-meat sources versus a prespecified comparison phenotype/source, with a second estimand for a lagged human-source change.

**Major identification bias.** National contemporaneous husbandry, industry and diagnostic changes; changing sampling frames and breakpoint definitions; a single national intervention means no untreated jurisdiction; source populations are not directly linked transmission chains. Target/control selection can be undermined by co-selection.

**Independent-researcher workload.** **Medium.** Data are public and tabular; careful phenotype harmonisation and denominator-based models matter more than computing.

**Novelty risk.** **High for a simple rerun; moderate for a registered update.** The policy has already been evaluated. A publishable contribution requires additional post-2019 data, explicit source contrasts, breakpoint harmonisation, negative controls, power/sensitivity analysis and transparent replication of the earlier findings.

**Verdict.** **GO as a replication/update, not as a first-ever policy evaluation.** This is the cleanest public One Health quasi-experiment in the portfolio.

### Candidate 4 — Do AMR conclusions change when ECDC reports percentage resistant versus resistant-BSI incidence?

**Infectious-disease analogue.** Comparing case positivity, notification rate and modelled incidence in TB, influenza or COVID surveillance: the numerator may be related, but changing the denominator changes the construct and therefore the policy conclusion.

**Transferable design.** Within the same EARS-Net reporting system, compare three constructs where available: percentage of invasive isolates resistant, number tested/resistant, and estimated incidence of resistant bloodstream infections per 100,000. Estimate exposure slopes and country rankings on each scale for the three EU target phenotypes, then quantify concordance/reversal and its association with coverage/testing.

**AMR question.** Are country rankings, trends and associations with antibiotic use/stewardship robust to measuring resistance as a proportion versus resistant-infection incidence?

**Exact public sources.**

- [EARS-Net official data page](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/ears-net-data) — public downloadable Atlas tables, figures and maps; explicitly cautions that population coverage varies.
- [ECDC 2024 AMR report](https://www.ecdc.europa.eu/en/publications-data/antimicrobial-resistance-eueea-ears-net-annual-epidemiological-report-2024) — country-specific resistant-BSI incidence and percent resistant, including the EU target combinations MRSA, 3GC-resistant *E. coli* and carbapenem-resistant *K. pneumoniae*.
- [ESAC-Net consumption dashboard](https://www.ecdc.europa.eu/en/antimicrobial-consumption/surveillance-and-disease-data/database) and [data methodology](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/esac-net-data) — country-year community/hospital DDD per 1,000 inhabitants per day.

**Geographic/time grain and likely coverage.** Approximately 30 EU/EEA countries, annual. Historical percentage data extend back toward 1999 for some pathogens; consistently estimated incidence and target definitions are much shorter. All EU/EEA countries reported 2024 data, but organism–drug completeness varies. A realistic core is 30 countries × 3 target combinations × 2019/2024 or a short 2019–2024 panel, not 90 independent countries.

**Login/request.** None. Atlas/dashboard downloads are public.

**Minimal estimand.** For each prespecified exposure, (\Delta_k=\theta_{incidence,k}-\theta_{proportion,k}) on frozen standardised response scales, plus country-rank concordance and sign classification. A hierarchical mean across three target phenotypes is secondary and must retain country clustering.

**Major identification bias.** The incidence estimate is not an independent measurement system; it is constructed partly from EARS-Net information. Coverage differences, ascertainment and estimated national BSI totals remain. With ~30 countries, policy slopes are leverage-sensitive, and multi-combination records do not create independent national units.

**Independent-researcher workload.** **Low–medium.** Public downloads and a manageable panel; the hard part is estimand/power discipline.

**Novelty risk.** **Moderate.** ECDC already publishes both metrics, but a preregistered quantitative study of inferential reversal across constructs may be novel. It is a narrower, fully public precursor/companion to the GLASS–GRAM project.

**Verdict.** **GO to extraction pilot and Stage-A simulation.** It could yield a methods paper even if it demonstrates that the country-level comparison is underpowered.

### Candidate 5 — Pneumococcal conjugate-vaccine introduction and resistant invasive pneumococcal disease

**Infectious-disease analogue.** Staggered vaccine introduction followed by changes in vaccine-type invasive disease. The direct AMR precedent is Kyaw et al.'s original US active-surveillance study showing declines in antibiotic-resistant invasive pneumococcal disease after PCV introduction ([NEJM, 2006](https://www.nejm.org/doi/full/10.1056/NEJMoa051642)).

**Transferable design.** Link each country's PCV introduction year and subsequent coverage to EARS-Net invasive *S. pneumoniae* penicillin/macrolide non-susceptibility. Use a modern group-time event study, require multiple pre-periods, stratify or censor at vaccine formulation changes, and prespecify a non-pneumococcal comparator outcome as a bias diagnostic rather than a guaranteed negative control.

**AMR question.** Does introducing and scaling PCV reduce resistant invasive pneumococcal disease or the resistant share of invasive isolates, and is the change compatible with reduced vaccine-type carriage/antibiotic exposure rather than a general surveillance trend?

**Exact public sources.**

- WHO Immunization Data Portal public [vaccine-introduction XLSX](https://srhdpeuwpubsa-geecgzbpd5h0fueu.z01.azurefd.net/whdh/WIISE/export/vaccine-introduction-data.xlsx) and [coverage XLSX](https://srhdpeuwpubsa-geecgzbpd5h0fueu.z01.azurefd.net/whdh/WIISE/export/coverage-data.xlsx) — country-year official reporting/WUENIC, no login.
- [ECDC EARS-Net](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/ears-net-data) — invasive blood/CSF *S. pneumoniae* isolate susceptibility by country-year through the Surveillance Atlas, no login.

**Geographic/time grain and likely coverage.** Country-year. The theoretical EU/EEA pool is approximately 20–30 countries, but many introduced PCV before a stable resistance series and therefore contribute no usable pre-period. The effective number of adoption cohorts and countries may fall toward 10–20; this must be counted before any outcome model.

**Login/request.** None.

**Minimal estimand.** Group-time ATT for resistant *S. pneumoniae* proportion or, if a defensible population denominator is available, resistant invasive-disease incidence at event years 0–5 relative to introduction, among countries with adequate pre-data. Coverage should be a secondary continuous dose, not silently substituted for adoption.

**Major identification bias.** PCV adoption and coverage are related to income, health-system capacity and baseline burden; vaccine valency and schedules change; serotype replacement can reverse aggregate trends; EUCAST/CLSI breakpoints, blood-culture intensity and EARS-Net coverage change. Most EU introductions may be too early for credible staggered comparisons, and vaccination can affect comparator pathogens indirectly through antibiotic use.

**Independent-researcher workload.** **Medium.** Public spreadsheets are easy; the work is in vaccine-history harmonisation, breakpoint/coverage audit and simulation of the actual adoption geometry.

**Novelty risk.** **Moderate.** The biological conclusion that PCV can reduce resistant pneumococcal disease is established. Novelty would come from a preregistered cross-country event-study audit of durability, heterogeneity and surveillance bias—not from presenting the mechanism as new.

**Verdict.** **GO to a blinded geometry/power audit.** If there are insufficient pre-periods or adoption cohorts, stop rather than convert it into an uncontrolled before/after study.

### Candidate 6 — Genomic diffusion of a prespecified carbapenemase or other AMR determinant

**Infectious-disease analogue.** Genomic outbreak reconstruction and phylogeographic analysis of introductions, followed by a space–time model of observed lineage/determinant detections.

**Transferable design.** Freeze one organism–gene question before extraction (for example, a carbapenemase determinant in *K. pneumoniae*). Download isolate metadata and AMRFinderPlus calls; distinguish within-cluster expansion from repeated introductions; model time to first observed detection and subsequent cluster spread across locations. Where full phylogenetics is excessive, use NCBI SNP cluster membership and prespecified sensitivity analyses.

**AMR question.** Is the observed geographic expansion of a resistance determinant more consistent with repeated introductions, local clonal expansion, or connectivity-weighted diffusion?

**Exact public sources.**

- [NCBI Pathogen Detection](https://www.ncbi.nlm.nih.gov/pathogens) integrates clinical, food and environmental genomes, clusters related sequences and publicly screens AMR determinants.
- [Isolate Browser/download documentation](https://www.ncbi.nlm.nih.gov/pathogens/pathogens_help/) — metadata downloads for displayed isolates, assemblies for GenBank records, bulk SQL/Google Cloud and FTP routes.
- [AMRFinderPlus](https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/AMRFinder/) — curated AMR genes and resistance-associated mutations; open-source software/databases and public precomputed results.
- [NCBI processing documentation](https://www.ncbi.nlm.nih.gov/pathogens/docs/data_processing/) — clustering and AMR-annotation pipeline.

**Geographic/time grain and likely coverage.** Isolate-level collection date, location and source when submitted. The platform contains hundreds of thousands of isolates overall, but usable n is determined by the chosen organism/gene and metadata completeness; sampling density is highly unequal by country, year and source.

**Login/request.** None. Metadata, many assemblies and precomputed AMR calls are public; bulk compute/storage are required for large selections.

**Minimal estimand.** Hazard/rate ratio for first observed gene/cluster detection as a function of geographic/connectivity exposure, or estimated endemic versus neighbouring-region contribution to monthly/quarterly observed detections. The word **observed** must remain in the estimand.

**Major identification bias.** Submission intensity is not population incidence; first sequence is not first biological introduction; missing dates/locations and outbreak-driven sequencing create informative observation; duplicates and changing pipelines can distort trends. A phylogeny cannot repair an unmodelled sampling process.

**Independent-researcher workload.** **High.** Metadata audit is feasible alone; a rigorous phylogenomic paper requires bioinformatics, compute and preferably a genomic-epidemiology collaborator.

**Novelty risk.** **Moderate–high**, depending on the determinant. Global genome surveys are common; novelty requires a sharp transmission/detection estimand and prespecified observation-process sensitivity, not another world map.

**Verdict.** **CONDITIONAL GO.** Start with a metadata-only feasibility query; stop if date/location completeness or sampling concentration fails a frozen gate.

### Candidate 7 — Spatial diffusion of resistant bloodstream infections across Europe

**Infectious-disease analogue.** Endemic–epidemic models for measles or meningococcal disease decompose local endemic burden, autoregressive persistence and neighbour-imported transmission. The original framework and reproducible software are documented in [Meyer, Held and Höhle](https://www.jstatsoft.org/article/view/v077i11).

**Transferable design.** Fit a multivariate negative-binomial endemic–epidemic model to EARS-Net resistant-BSI incidence/counts. Compare adjacency, distance and mobility/tourism weights; include country-specific reporting/testing terms; evaluate one-step-ahead prediction and simulation-calibrated false diffusion.

**AMR question.** After accounting for country-specific endemic levels and temporal persistence, do nearby or highly connected countries predict subsequent resistant-BSI occurrence?

**Exact public sources.** [EARS-Net/Surveillance Atlas](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/ears-net-data); free [Eurostat REST API](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction); tourism metadata and country-of-residence/destination series from [Eurostat tourism statistics](https://ec.europa.eu/eurostat/web/tourism). Border adjacency can be derived from official Eurostat GISCO boundaries.

**Geographic/time grain and likely coverage.** Approximately 30 countries, annual, potentially 15–25 years for older EARS-Net percentage/count series but shorter for harmonised incidence. Annual intervals are coarse relative to transmission.

**Login/request.** None.

**Minimal estimand.** Relative contribution of the spatially weighted epidemic component to expected resistant-BSI counts, plus out-of-sample predictive improvement over a non-spatial model.

**Major identification bias.** Shared healthcare systems, prescribing and laboratory changes masquerade as diffusion; annual country data cannot identify person-to-person transmission direction; tourism is a poor proxy for healthcare-linked movement; data availability and breakpoints change over time.

**Independent-researcher workload.** **Medium–high.** Technically feasible in R, but extensive harmonisation/simulation is required.

**Novelty risk.** **Moderate.** Spatial AMR maps are common; an observation-aware endemic–epidemic model is more distinctive.

**Verdict.** **CONDITIONAL GO as a predictive/spatial-association paper; NO-GO for claiming transmission routes.**

### Candidate 8 — Prospective nowcasting of AMR surveillance revisions

**Infectious-disease analogue.** Reporting-triangle nowcasting of dengue, influenza or COVID. The original NobBS paper models both reporting-delay probabilities and temporal smoothing and validates on dengue/ILI [McGough et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32251464/). CDC explains that nowcasting requires repeated database snapshots containing event and reporting dates or release vintages in its [official nowcasting guide](https://www.cdc.gov/cfa-behind-the-model/php/data-research/nowcasting.html).

**Transferable design.** Archive every UKHSA/WHO/ECDC public release on a fixed schedule. Build revision triangles for area-month resistance/testing values; estimate the final value from early releases; compare naive latest-value, delay-only and temporally smoothed nowcasts.

**AMR question.** Can routinely published AMR signals be corrected in real time for delayed/revised reporting, and how much do unrevised values misclassify local trends?

**Exact public sources.** [UKHSA AMR dashboard](https://ukhsa-dashboard.data.gov.uk/antimicrobial-resistance), [WHO AMR profile](https://data.who.int/dashboards/amr/antimicrobial-resistance-profile), and [ECDC EARS-Net](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/ears-net-data).

**Geographic/time grain and likely coverage.** UKHSA monthly is the best candidate. Historical public pages do not expose a complete vintage-by-event reporting triangle; the dashboard text currently says no reporting-delay period is tracked for these charts.

**Login/request.** No login for prospective snapshots. Archived historical vintages may require agency cooperation.

**Minimal estimand.** Mean absolute error and 95% interval coverage for predicting a value frozen (K) months later from the value available at first/second release.

**Major identification bias.** Without genuine vintages, one cannot reconstruct reporting delays from a final CSV. Pipeline or definition changes are not ordinary late reports. A prospective archive risks endpoint changes and requires at least 12–24 months before serious validation.

**Independent-researcher workload.** **Low ongoing, long calendar time.** Automated downloads, hashes and snapshots are straightforward.

**Novelty risk.** **Low–moderate** if real revisions are large; high risk of a null operational finding if values rarely revise.

**Verdict.** **NO-GO as an immediate retrospective paper; GO as prospective research infrastructure.** Begin snapshotting now only if the maintenance burden is acceptable.

### Candidate 9 — CDC state stewardship adoption and resistance

**Infectious-disease analogue.** Staggered programme-adoption event study with pretrend diagnostics and negative-control outcomes.

**Transferable design.** Use state-year percentage of hospitals meeting all seven Core Elements as a continuous programme-intensity exposure; relate within-state change to NHSN resistance phenotypes and HAI outcomes. A policy discontinuity could be analysed only if state-specific legal implementation dates are independently documented.

**AMR question.** Does increasing hospital stewardship implementation precede lower healthcare-associated resistance within states?

**Exact public sources.** [CDC AR & Patient Safety Portal](https://www.cdc.gov/healthcare-associated-infections/php/data/ar-patient-safety-portal.html); [ARPSP About the Data/downloads](https://arpsp.cdc.gov/about?tab=hospital-stewardship) reports hospital stewardship for 2014–2024 and supplies data/methodology/dictionary downloads; [AR Data Explorer](https://arpsp.cdc.gov/explorer) provides state/year number tested, number resistant and percent resistant for NHSN HAI phenotypes.

**Geographic/time grain and likely coverage.** Up to 50 states plus DC × 11 years, but resistance cells are suppressed/selected and NHSN participation changes. Antibiotic-use SAAR and stewardship reporting are not population-complete.

**Login/request.** None for aggregate downloads.

**Minimal estimand.** Within-state change in target-phenotype resistance associated with a 10-percentage-point increase in hospitals meeting all Core Elements, with event-time/pretrend diagnostics if a credible adoption threshold is used.

**Major identification bias.** Stewardship reporting/adoption is endogenous to AMR burden and hospital capacity; facility composition changes; outcome is limited to selected NHSN HAIs; national accreditation/CMS changes affect all states. Continuous exposure invalidates a naive treated/untreated event study.

**Independent-researcher workload.** **Medium.** Public tabular data but many suppression/definition issues.

**Novelty risk.** **Moderate.** The portal is underused academically, but the causal claim is difficult.

**Verdict.** **CONDITIONAL GO for a surveillance/implementation association; NO-GO causal without a defensible state policy discontinuity.**

### Candidate 10 — Staggered national AMR action-plan adoption using TrACSS

**Infectious-disease analogue.** Cross-country vaccine/policy adoption event study.

**Transferable design.** Define first transition to TrACSS C/D/E as adoption/implementation and estimate group-time effects with modern staggered-DiD methods, explicitly testing anticipation and pretrends. Use ESAC-Net consumption as a nearer behavioural outcome before EARS-Net resistance.

**AMR question.** Does formal implementation/funding of a national AMR action plan precede lower antibiotic use or resistance?

**Exact public sources.** WHO's [TrACSS 2016–2017](https://www.who.int/publications/m/item/tripartite-amr-country-self-assessment-survey-2016-2017) through the [2024 governance dashboard](https://data.who.int/dashboards/amr/governance-awareness-education), with machine-readable annual country responses; [EARS-Net](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/ears-net-data); [ESAC-Net](https://www.ecdc.europa.eu/en/antimicrobial-consumption/surveillance-and-disease-data/database).

**Geographic/time grain and likely coverage.** Global TrACSS country-year from 2016/17; the viable outcome intersection is about 30 EU/EEA countries and 8–9 annual observations. Adoption transitions may reverse because the measure is annual self-assessment, not a statutory implementation date.

**Login/request.** None.

**Minimal estimand.** Group-time average change in consumption after first sustained C-or-higher transition among adopters versus not-yet-adopters, with resistance only as a delayed secondary outcome.

**Major identification bias.** Adoption is strongly endogenous to capacity, prior AMR and donor support; self-reporting and questionnaire changes; few untreated countries; interference/spillover; parallel trends unlikely. “NAP exists” is not a sharp treatment.

**Independent-researcher workload.** **Low–medium.** Data are easy; credible identification is not.

**Novelty risk.** **Moderate**, but apparent novelty should not override invalid causal language.

**Verdict.** **NO-GO causal.** Acceptable only as a descriptive implementation trajectory or a pretrend/falsification study. Do not make this the next flagship paper.

### Candidate 11 — EU animal-antimicrobial regulation / JIACRA update

**Infectious-disease analogue.** Controlled policy ITS comparing targeted and untargeted drug/pathogen outcomes across surveillance sectors.

**Transferable design.** Evaluate the 2022 application of EU veterinary medicinal-product rules using human versus animal consumption/resistance, targeted drug classes and negative controls. Alternatively reproduce JIACRA's integrated model with a frozen causal estimand.

**AMR question.** Did the regulation reduce veterinary antimicrobial use and animal resistance, with later change in human resistance?

**Exact public sources.** [EMA ESVAC 2009–2023 archive](https://www.ema.europa.eu/en/veterinary-regulatory-overview/antimicrobial-resistance-veterinary-medicine/european-surveillance-veterinary-antimicrobial-consumption-esvac-2009-2023); [ESUAvet transition information](https://www.ema.europa.eu/en/news/first-report-eu-wide-sales-use-antimicrobials-animals); [EFSA zoonoses/AMR dashboards](https://www.efsa.europa.eu/en/resources/data-collection-zoonoses/interactive-tools?topic%5B364%5D=364); [JIACRA IV](https://www.ema.europa.eu/en/veterinary-regulatory-overview/antimicrobial-resistance-veterinary-medicine/analysis-antimicrobial-consumption-resistance-jiacra-reports), which already integrates five EU-wide networks and reports 2014–2021 trends.

**Geographic/time grain and likely coverage.** About 29–31 EU/EEA countries, annual. ESVAC offers 2010–2022 trends; ESUAvet begins with 2023 under mandatory reporting. EFSA dashboards cover country/pathogen/animal-food strata since 2016.

**Login/request.** Reports/dashboards are public. EMA states that underlying ESVAC Power BI extraction requires an AskEMA request; therefore a fully reproducible raw-data panel may need official assistance even though report tables are public.

**Minimal estimand.** Post-2022 change in targeted veterinary sales/resistance relative to comparison classes and human-sector outcomes.

**Major identification bias.** Only 2–3 post-policy years; surveillance changed from voluntary ESVAC to mandatory ESUAvet at the intervention; COVID and secular stewardship coincide; regulation applied broadly, leaving no clean untreated EU control. JIACRA has already analysed the central associations.

**Independent-researcher workload.** **Medium–high.** Multiple dashboards, alternating animal species by surveillance year, and a measurement-regime break.

**Novelty risk.** **High** for simple consumption–resistance correlations because JIACRA IV already did them.

**Verdict.** **NO-GO causal now.** Revisit after additional ESUAvet post-policy years and an explicit bridge study across the surveillance transition.

### Candidate 12 — England 2024–2029 AMR action plan as a national ITS

**Infectious-disease analogue.** A national infection-control intervention evaluated using segmented monthly regression.

**Transferable design.** April/May 2024 interruption in national antibiotic consumption and resistant BSI metrics, with matched non-target outcomes and synthetic/comparative series if compatible UK nations can be found.

**Public sources.** [UKHSA AMR monthly dashboard](https://ukhsa-dashboard.data.gov.uk/antimicrobial-resistance), [UKHSA monthly consumption](https://ukhsa-dashboard.data.gov.uk/antimicrobial-consumption/total-antibiotic-use), and NHSBSA prescribing files.

**Grain/access/coverage.** England/region/ICB month, no login. At verification there are only about 37 pre-plan and 24 post-plan months in the AMR series, all embedded in post-COVID recovery.

**Minimal estimand.** Immediate level and post-plan slope change in a prespecified target outcome versus a prespecified comparator.

**Major identification bias.** The plan is a bundle, not a sharp intervention; no untreated England; insufficient post-period; COVID recovery, diagnostic change and prior policies violate stable counterfactual trends.

**Workload/novelty.** Low workload, low inferential value; high risk of a misleading “policy effect”. The original England Quality Premium literature—including the [prescribing ITS](https://academic.oup.com/cid/article/69/2/227/5136399)—shows what a more specific intervention and long series look like.

**Verdict.** **NO-GO now.** Reassess near 2029, preferably with a controlled design.

### Candidate 13 — Pandemic antibiotic-use shock and subsequent AMR

**Infectious-disease analogue.** Mobility/NPI shocks used as natural experiments for respiratory infection transmission.

**Transferable design.** Estimate country- or area-specific 2020 prescribing/consumption shocks, then model lagged resistance changes with target/control drug classes and testing adjustment.

**Public sources.** ECDC [ESAC-Net](https://www.ecdc.europa.eu/en/antimicrobial-consumption/surveillance-and-disease-data/database) + [EARS-Net](https://www.ecdc.europa.eu/en/about-us/networks/disease-networks-and-laboratory-networks/ears-net-data), or NHSBSA + UKHSA England data. ECDC offers downloadable annual tables, including a [2020 data release](https://www.ecdc.europa.eu/en/publications-data/surveillance-antimicrobial-consumption-europe-2020).

**Grain/access/coverage.** About 29–30 EU/EEA countries annually from 2011; England practice-month exposure but public AMR outcomes begin only in 2021. No login.

**Minimal estimand.** Association between the size of the 2020 class-specific consumption deviation and 2021–2024 matched resistance deviation.

**Major identification bias.** The pandemic directly altered infections, healthcare, hospital antibiotic use, laboratory submission and population mixing. The “instrument” affects resistance through many pathways other than outpatient antibiotic use; exclusion restriction is untenable.

**Workload/novelty.** Low–medium workload; crowded literature and high causal-overclaim risk.

**Verdict.** **NO-GO causal.** At most a descriptive natural-history analysis with explicit multi-pathway interpretation.

### Recommended portfolio sequence

1. **Open a simulation-methods lane now.** Write an ADEMP protocol for Track S1 using only geometry and margins, with estimator-level bias decomposition and immutable thresholds. This does not depend on GRAM access and turns the failed design preflight into general methodological knowledge rather than post-hoc threshold adjustment.
2. **Run a metadata-only UKHSA/NHSBSA extraction pilot.** Freeze exact geographies, dates, suppression, rolling-window definitions and organisation crosswalks without testing policy associations.
3. **Develop Candidate 1 first.** It is closest to an infectious-disease surveillance methods paper and does not depend on country-level GRAM access.
4. **Use Candidate 1's observation model in Candidate 2.** The two papers are related but have distinct estimands: measurement/ascertainment versus lagged exposure–resistance association.
5. **Use Candidate 3 as the One Health replication project.** Begin with a protocol that explicitly reproduces the earlier NARMS estimates before adding new post-years and source contrasts.
6. **Pilot Candidate 4 in parallel with the global GLASS–GRAM project.** It can tell us whether the measurement-construct problem appears even inside the better-covered EU/EEA system.
7. **Audit Candidate 5 without looking at post-introduction effects.** Count usable countries, adoption cohorts, pre-periods, vaccine transitions and isolate denominators; proceed only if the event-study geometry survives.
8. **Pursue Candidate 6 or Track S4 only after a bounded metadata/parameter audit.** They offer the largest expansion into transmission epidemiology but also the highest solo workload and greatest need for domain collaboration.

### What not to do

- Do not count pathogen–drug combinations as independent countries to manufacture sample size.
- Do not call a national-plan category a treatment date without demonstrating a stable intervention definition.
- Do not use resistance to another antibiotic as a negative control without addressing co-selection and cross-resistance.
- Do not infer transmission from adjacent-country correlations or first sequence submissions.
- Do not fit nowcasting models to a final historical file lacking release vintages.
- Do not treat dashboards as immutable. Download raw exports, hash them, retain metric documentation and freeze administrative boundaries.

### Bottom line

An independent researcher can do credible infectious-disease epidemiology in AMR without proprietary patient data. The strongest immediate niche is **observation-aware surveillance epidemiology and simulation methods**: separate biological occurrence from testing, reporting, denominators and measurement constructs; use known-truth DGPs to find estimator failure regions; then carry the defensible observation model into a small number of falsifiable longitudinal or quasi-experimental analyses. England's monthly AMR/HCAI infrastructure provides the clearest immediate empirical opportunity; NARMS supplies the clearest One Health policy replication; ECDC supplies the clearest fully public measurement-system comparison. Mechanistic and genomic transmission work remain legitimate higher-upside directions, but they demand stricter parameter/metadata gates and are less solo-friendly.
