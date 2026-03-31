# Proposed ML Folder Structure for CMS DQM in HEPTAPOD

## Goal
Add a structured ML layer for CMS Data Quality Monitoring workflows covering:
- data access
- preprocessing
- training
- offline evaluation
- real-time inference
- alert generation

## Design Principles
- modular and extensible
- reproducible via run-card/config driven execution
- compatible with HEPTAPOD tool-based orchestration
- clear separation between offline training and online inference
- human-in-the-loop review for anomaly alerts

## Proposed Directory Layout
heptapod/
├── tools/
│   ├── cms_dqm/
│   │   ├── data/
│   │   │   ├── loaders.py
│   │   │   ├── schemas.py
│   │   │   └── adapters.py
│   │   ├── preprocessing/
│   │   │   ├── transforms.py
│   │   │   ├── feature_engineering.py
│   │   │   └── validation.py
│   │   ├── training/
│   │   │   ├── train.py
│   │   │   ├── evaluate.py
│   │   │   ├── datasets.py
│   │   │   └── metrics.py
│   │   ├── models/
│   │   │   ├── baseline_model.py
│   │   │   ├── anomaly_model.py
│   │   │   └── registry.py
│   │   ├── inference/
│   │   │   ├── predict.py
│   │   │   ├── postprocess.py
│   │   │   └── thresholds.py
│   │   ├── deployment/
│   │   │   ├── realtime_worker.py
│   │   │   ├── batch_worker.py
│   │   │   └── alerting.py
│   │   ├── configs/
│   │   │   ├── data_config.yaml
│   │   │   ├── train_config.yaml
│   │   │   └── deploy_config.yaml
│   │   ├── runcards/
│   │   │   ├── train_baseline.yaml
│   │   │   └── realtime_inference.yaml
│   │   ├── README.md
│   │   └── __init__.py
├── examples/
│   ├── cms_dqm_demo.py
│   └── todos/
│       └── cms_dqm_workflow.md
└── docs/
    └── cms_dqm_proposed_architecture.md

## Workflow
1. Access CMS DQM data
2. Validate and preprocess data
3. Train baseline/anomaly model offline
4. Save model artifact and metadata
5. Run batch or streaming inference
6. Produce structured anomaly reports for shifters

## Rationale
Explain why each folder exists.

## Future Extensions
- model registry
- active learning
- feedback loop from shifters
- MCP/LLM-assisted DQM interpretation