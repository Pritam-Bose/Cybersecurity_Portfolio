# Task 6 – Comprehensive Penetration Testing Report & Capstone

## RabTech Academy Internship

**Prepared by:** Pritam Bose  
**Internship:** Cybersecurity & Ethical Hacking  

## Overview

This folder contains the final consolidated VAPT report prepared from the cybersecurity assessment work completed during Tasks 2–5 of the RabTech Academy internship.

The assessment covered:

- Legal scope and security lab authorization
- Asset inventory and STRIDE threat modeling
- Network reconnaissance and port scanning
- Wireshark network traffic analysis
- OWASP Juice Shop web application assessment
- SQL Injection
- DOM-based Cross-Site Scripting (XSS)
- Broken Object-Level Authorization (BOLA/IDOR)
- Cryptography and secure authentication controls

## Assessment Tools

- Kali Linux
- Nmap
- Wireshark
- Burp Suite
- Firefox
- Node.js
- bcrypt

## Key Findings

### SQL Injection
The web application authentication mechanism was demonstrated to be susceptible to SQL Injection.

**Recommended remediation:** Use parameterized queries/prepared statements and apply server-side input validation.

### DOM-Based XSS
A DOM-based XSS proof of concept was demonstrated in the OWASP Juice Shop environment.

**Recommended remediation:** Use safe DOM APIs, contextual output encoding and avoid unsafe HTML sinks.

### BOLA / IDOR
Object-level authorization testing demonstrated access to another object's data after modifying the object identifier.

**Recommended remediation:** Enforce server-side authorization checks for every protected object and verify ownership or authorization.

## Cryptography & Secure Authentication

Task 5 included practical implementations of:

- AES-256-GCM authenticated encryption and decryption
- RSA-2048 key generation and digital signature verification
- bcrypt password hashing and verification

## Risk Assessment

The final report includes:

- CVSS 3.1 assessment
- Risk matrix
- Finding prioritization
- OWASP mapping
- Remediation recommendations
- Suggested remediation timelines

## Evidence

The consolidated report contains evidence collected during the previous tasks, including:

- Nmap reconnaissance screenshots
- Wireshark packet-analysis screenshots
- Burp Suite request/response evidence
- OWASP Juice Shop vulnerability evidence
- Cryptography implementation and execution screenshots

References
OWASP Top 10
OWASP Juice Shop
OWASP Web Security Testing Guide
PortSwigger Burp Suite Documentation
Nmap Documentation
Kali Linux Documentation
RabTech Academy Internship Task Instructions and Rules of Engagement