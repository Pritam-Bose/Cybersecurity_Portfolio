# Task 02 — Legal Scope, Asset Inventory & Threat Model

## Overview

This repository contains the deliverables for Task 02 of the RabTech cybersecurity training program.

The task establishes the authorized security-testing scope, asset inventory, Rules of Engagement, data-flow boundaries, and STRIDE-based threat model for the isolated training environment.

## Scope

The authorized assets are:

| Asset ID | Asset | Environment | IP / URL |
|---|---|---|---|
| LAB-01 | Local training web app | Isolated localhost | 127.0.0.1:8080 |
| LAB-02 | Deliberately vulnerable VM | Private host-only network | 192.168.56.20 |

Testing is restricted to the assets explicitly listed in the approved inventory.

## Contents

`Task-02-Legal-Scope-Threat-Model.pdf` contains the complete security lab dossier, including:

- Written authorization and scope
- Authorized asset inventory
- Rules of Engagement
- Testing restrictions and stop conditions
- Evidence-handling requirements
- Data-flow diagram
- STRIDE threat model
- Abuse cases
- Risk prioritization
- Supporting evidence

The `screenshots/` directory contains supporting laboratory evidence.

## Evidence

The evidence is classified as:

**Confidential training evidence**

Only the minimum evidence necessary for the assessment is retained, with sensitive information redacted where applicable.

## Authorization Notice

All security-testing activities described in the report are intended for the authorized isolated training environment only. Systems outside the approved asset inventory are out of scope.

## Disclaimer

This repository is for authorized cybersecurity training and educational purposes only.