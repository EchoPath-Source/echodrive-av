# EchoDrive AV

EchoDrive AV is the autonomy-focused EchoPath XR repository for AV-specific pathing, motion quality, and pilot packaging.

## Purpose
- AV-facing EchoPath integration work
- Flask/Render server setup for protected endpoints
- Q-RRG path refinement experiments for autonomy stacks
- pilot packaging for OEM and mobility evaluations
- motion-quality benchmarks such as jerk, curvature, replan stability, and multi-agent scaling

## Positioning
EchoDrive AV is a planner-neutral enhancement layer. It is designed to sit on top of existing occupancy, cost, or planner outputs and refine them into smoother, lower-jerk, lower-curvature trajectories with more stable replans.

## Initial layout
- `server/` Flask app for protected API endpoints
- `sdk/` future client wrappers and integration surfaces
- `docs/` architecture, metrics, pilots, and positioning docs
- `sim/` simulation notes, benchmarks, and experiment stubs

## Immediate next steps
- stand up the Flask app on Render
- expose a health endpoint and pilot-facing endpoints
- add example request and response schemas for path refinement
- move current benchmark packets and explainers into `docs/`
- prepare AV pilot one-pagers and evaluation criteria
