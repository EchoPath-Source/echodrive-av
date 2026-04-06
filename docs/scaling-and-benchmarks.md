# Scaling and Benchmarks

## Current measured anchors

### Unified stack anchor
- 8-agent dual-layer reference: nav success 96%, tube stability 0.93, resonance sync 0.88, decoherence drop 28% vs baseline.

### Noise / occlusion stress tests
- 30 agents, occlusion density 0.4, 15% dynamic noise: nav success 83.5%, tube stability 0.85, resonance sync 0.75.
- 30 agents, tau-shift ±2-3, 10% noise: nav success 87.2%, tube stability 0.88, resonance sync 0.81.
- 40 agents, same tau-shift setup: nav success 84%, tube stability 0.85, resonance sync 0.78.

## Practical reading of the curve

- resonance sync degrades before tube stability as load and noise increase
- tau-shift helps mitigate noise impact
- the stack degrades gracefully rather than collapsing abruptly

## SLAM-style motion-quality proxy

In the current noisy-grid proxy:

- success rate: 100%
- path length: approximately 1.4% shorter vs baseline
- mean curvature: approximately 32% lower
- mean jerk: approximately 32% lower

## Benchmarking guidance

Public-facing claims should prefer:

- internal baseline vs hybrid comparisons
- comfort-threshold references from published literature
- motion-quality deltas under controlled scenarios

Avoid unsupported direct claims against proprietary OEM stacks unless the comparison is scenario-matched and source-verifiable.

## Metrics to preserve

- mean jerk
- mean curvature
- max curvature
- replan stability
- tube persistence
- ID continuity
- split / merge rate
- churn under anomaly windows
