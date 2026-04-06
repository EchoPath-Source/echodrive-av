# API Spec Draft

## Overview

EchoDrive AV currently exposes stub endpoints for two initial workflows:

1. path refinement
2. motion-quality evaluation

The proprietary logic should remain server-side. Client integrations should send only the minimum required request payloads and receive refined outputs plus metrics.

## POST `/api/v1/refine-path`

### Purpose
Refine an incoming route or candidate corridor into a smoother path with lower curvature, lower jerk risk, and better replan stability.

### Candidate request body

```json
{
  "path_points": [[0.0, 0.0], [1.0, 1.2], [2.0, 2.5]],
  "occupancy_map": "optional reference or encoded payload",
  "cost_map": "optional reference or encoded payload",
  "dynamic_obstacles": [],
  "constraints": {
    "max_curvature": 0.12,
    "max_jerk": 0.5,
    "speed_profile": "urban"
  },
  "scenario_metadata": {
    "scenario_id": "demo-001",
    "planner": "astar",
    "environment": "urban"
  }
}
```

### Candidate response body

```json
{
  "status": "ok",
  "refined_path": [[0.0, 0.0], [0.8, 1.0], [1.8, 2.3]],
  "metrics": {
    "mean_curvature": 0.025,
    "mean_jerk_proxy": 0.116,
    "stability_score": 0.88
  },
  "notes": ["stub schema - replace with protected implementation"]
}
```

## POST `/api/v1/evaluate-motion`

### Purpose
Evaluate a baseline or refined trajectory using motion-quality metrics.

### Candidate request body

```json
{
  "trajectory": [[0.0, 0.0], [1.0, 1.1], [2.1, 2.4]],
  "time_series": [0.0, 0.1, 0.2],
  "baseline_trajectory": [[0.0, 0.0], [1.2, 1.4], [2.3, 2.8]],
  "scenario_metadata": {
    "noise": 0.1,
    "occlusion_density": 0.4,
    "agents": 30
  }
}
```

### Candidate response body

```json
{
  "status": "ok",
  "metrics": {
    "mean_jerk": 0.116,
    "mean_curvature": 0.025,
    "max_curvature": 0.109,
    "replan_stability": 0.88,
    "tube_persistence": 0.84,
    "id_continuity": 0.82,
    "split_merge_rate": 0.06
  },
  "comparison": {
    "baseline_mean_jerk": 0.170,
    "baseline_mean_curvature": 0.037
  }
}
```

## Notes

- keep route refinement logic protected behind the API
- publish schemas and outputs before publishing mechanism details
- treat public values above as examples, not formal claims
