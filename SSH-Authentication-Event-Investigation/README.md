# SSH Authentication Event Investigation

## Overview

This project is a controlled cybersecurity laboratory exercise focused on investigating SSH authentication activity on a Metasploitable 2 system.

The assessment was performed using Kali Linux as the assessment machine and Metasploitable 2 as the target. Nmap was used to identify the exposed SSH service, followed by controlled failed and successful SSH authentication attempts. The corresponding authentication events were then examined from the target's `/var/log/auth.log` file.

The main purpose of the project was to understand how network-level activity and server-side authentication logs can be correlated during a basic security investigation.

## Objectives

- Identify the SSH service exposed by the target.
- Perform controlled SSH authentication testing.
- Verify failed authentication activity through server-side logs.
- Verify successful authentication and the resulting session.
- Correlate failed and successful authentication events.
- Understand how authentication logs can support security investigations.

## Lab Environment

**Assessment Machine:** Kali Linux  
**Target:** Metasploitable 2  
**Target IP:** `192.168.202.130`  
**Service Investigated:** SSH  
**Port:** TCP 22

## Tools Used

- Nmap
- OpenSSH client
- Linux terminal
- Metasploitable authentication logs

## Methodology

The assessment first identified open services on the target using Nmap. TCP port 22 was found to be open and identified as SSH.

A controlled failed SSH authentication attempt was then generated and verified from the target's authentication log. A valid SSH login was subsequently performed and the active account and hostname were verified.

The authentication log was examined again to locate the corresponding successful authentication event. Finally, failed and successful authentication entries were correlated to establish a basic authentication timeline.

## Key Findings

The assessment confirmed that:

- SSH was exposed on TCP port 22.
- Failed SSH authentication was recorded by the target.
- A successful SSH authentication was subsequently recorded.
- The source IP address and authentication events could be correlated through the server logs.
- The observed evidence demonstrates authentication activity but does not, by itself, prove a brute-force attack.

## Evidence

The report contains screenshots demonstrating:

1. Nmap identification of the SSH service.
2. Failed SSH authentication recorded in the target log.
3. Successful SSH login with account and hostname verification.
4. Accepted SSH authentication recorded in the target log.
5. Correlation of failed and successful authentication events.

## Security Relevance

SSH is commonly used for remote administration, making its authentication activity important to monitor. In a production environment, repeated failed authentication attempts, unusual source addresses, unexpected successful logins, or abnormal login times could require further investigation.

This laboratory demonstrates the basic process of identifying an exposed service, generating controlled authentication events, examining server-side logs, and correlating events during security analysis.

## Disclaimer

This project was performed entirely within an isolated and controlled virtual laboratory environment using Metasploitable 2 for educational cybersecurity testing.