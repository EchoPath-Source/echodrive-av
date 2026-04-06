# Pilot Outline

## Objective

Evaluate whether EchoDrive AV can improve motion quality and path stability as a modular enhancement layer on top of an existing planning stack.

## Pilot framing

This is a low-friction evaluation, not a rip-and-replace proposal.

## Candidate pilot metrics

- mean jerk
- mean curvature
- max curvature
- replan stability
- path churn during anomaly windows
- multi-agent deconfliction success
- collision-free operating windows

## Suggested pilot structure

### Phase 1: offline benchmark
- compare baseline planner output vs EchoDrive-refined output on fixed scenarios
- use stored occupancy or cost-map inputs
- produce motion-quality deltas and before / after visualizations

### Phase 2: dynamic scenario benchmark
- add obstacle and noise perturbations
- test response stability and continuity under replans

### Phase 3: integration discussion
- if results are compelling, define integration surface, licensing path, and evaluation scope

## Messaging guidance

Use language such as:

- modular enhancement layer
- planner-neutral
- no full stack rebuild required
- measurable motion-quality gains
- pilot-ready evaluation package
