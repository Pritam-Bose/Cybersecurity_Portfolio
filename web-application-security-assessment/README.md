# Web Application Security Assessment

A controlled security assessment of a deliberately vulnerable Flask web application developed for security testing and remediation practice.

## Objective

The objective of this project was to identify common web application vulnerabilities, demonstrate their impact, implement appropriate security controls, and verify the effectiveness of the remediation through retesting.

## Environment

- Kali Linux
- Python
- Flask
- SQLite
- Burp Suite
- Firefox
- Localhost environment

## Vulnerabilities Assessed

- SQL Injection
- Cross-Site Scripting (XSS)
- Broken Access Control

## Methodology

The assessment followed an attack-and-remediation workflow:

Application Analysis
→ Vulnerability Identification
→ Manual Testing
→ Evidence Collection
→ Root Cause Analysis
→ Remediation
→ Retesting

## Key Work

### SQL Injection

The authentication mechanism was tested using crafted input to determine whether user-controlled data could alter the underlying database query.

Remediation involved replacing unsafe query construction with parameterized SQL queries.

### Cross-Site Scripting

The search functionality was tested using controlled JavaScript input to determine whether user-supplied content could be interpreted as executable browser content.

The rendering behavior was then corrected so that untrusted input was treated as data.

### Broken Access Control

The profile functionality was tested by modifying the user-controlled profile identifier.

The application was subsequently modified to enforce authorization on the server side and prevent access to another user's profile.

## Retesting

After remediation, each vulnerability was tested again to verify that the original behavior could no longer be reproduced while legitimate application functionality remained available.

## Documentation

The complete assessment, screenshots, findings, remediation process, and retesting results are available in:

`report.pdf`

## Repository Structure

```text
web-application-security-assessment/
│
├── README.md
├── report.pdf
├── screenshots/
├── notes/
├── vulnerable-version/
└── remediated-version/