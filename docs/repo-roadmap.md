# Repo Roadmap

## Phase 0 - scaffold

Current status:
- basic Flask service exists
- route stubs exist for health, refine, and metrics
- service layer scaffolds exist for motion metrics and path refinement
- AV-facing docs exist for architecture, pilots, scaling, and API shape

## Phase 1 - deployment-ready backend

Goals:
- unify runtime entrypoint around `server/wsgi.py`
- point Render start command to `gunicorn --chdir server wsgi:app`
- retire legacy runtime scaffolds once the modular path is confirmed
- add environment-aware config and structured logging

## Phase 2 - protected logic integration

Goals:
- connect refine service to protected path-refinement implementation
- connect motion metrics service to real jerk / curvature / continuity calculations
- add request validation models and error handling
- define API authentication approach for partner and demo use

## Phase 3 - pilot packaging

Goals:
- add scenario packs and benchmark assets
- add reproducible before / after examples
- package offline pilot evaluation flow
- support partner-facing evaluation reports and trial endpoints

## Phase 4 - integration surfaces

Goals:
- Python client wrapper
- JavaScript helper for demos
- Unity / C# bridge notes or wrapper
- OEM evaluation contract templates

## Immediate cleanup items

1. update `render.yaml` to use `wsgi:app`
2. wire v2 routes into the route registry
3. consolidate or retire older stub-only files once runtime path is confirmed
4. add validated request / response schemas
