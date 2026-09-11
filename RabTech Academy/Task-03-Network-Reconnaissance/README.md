# Task 03 — Network Reconnaissance & Port Scanning Audit

## Overview

This task focuses on performing authorized network reconnaissance and port scanning against a deliberately vulnerable virtual machine in an isolated training environment.

The assessment used **Nmap** for host discovery, TCP/UDP port scanning, service/version enumeration, and OS detection. **Wireshark** was used to capture and analyze the resulting network traffic.

---

## Authorized Target

| Asset | Details |
|---|---|
| Asset ID | LAB-02 |
| Asset Name | Deliberately Vulnerable VM |
| Owner | RabTech Lab |
| Environment | Private Host-Only Network |
| Target IP | `192.168.56.20` |
| Authorization | Authorized training environment |

Testing was restricted to the authorized LAB-02 system.

---

## Objectives

- Perform structured TCP reconnaissance.
- Identify open TCP and UDP ports.
- Detect running services and their versions.
- Perform OS detection.
- Capture reconnaissance traffic using Wireshark.
- Analyze TCP SYN and UDP reconnaissance packets.
- Document the discovered attack surface.
- Produce a formal Network Reconnaissance Findings Report.

---

## Tools Used

- **Nmap 7.99**
- **Wireshark**
- **Kali Linux**
- **Metasploitable 2**

---

## Scans Performed

### 1. TCP SYN and OS Detection

```bash
sudo nmap -sS -O 192.168.56.20
````

This scan was used to identify reachable TCP services and perform OS detection.

### 2. Service and Version Detection

```bash
sudo nmap -sV 192.168.56.20
```

This identified running services and their detected versions.

### 3. UDP Top-Port Scan

```bash
sudo nmap -sU --top-ports 100 192.168.56.20
```

This checked the most common UDP ports and identified services such as DNS, rpcbind, NetBIOS-NS, and NFS.

### 4. Consolidated Nmap Scan

```bash
sudo nmap -sS -sV -O 192.168.56.20 -oN task3-nmap.txt
```

The output was saved to `task3-nmap.txt` for evidence and reporting.

---

## Key Findings

The TCP service enumeration identified numerous exposed services, including:

* FTP
* SSH
* Telnet
* SMTP
* DNS
* HTTP
* SMB/NetBIOS
* RPC/NFS
* MySQL
* PostgreSQL
* VNC
* IRC
* Apache JServ
* Apache Tomcat

The UDP scan identified open services including:

* `53/UDP` — DNS
* `111/UDP` — rpcbind
* `137/UDP` — NetBIOS-NS
* `2049/UDP` — NFS

Several legacy service versions were also detected, demonstrating the intentionally vulnerable nature of the training system.

---

## Wireshark Analysis

Wireshark was used to validate the network activity generated during reconnaissance.

### TCP Traffic

TCP SYN packets from the scanning system to `192.168.56.20` were observed across multiple destination ports.

Example filter:

```text
ip.addr == 192.168.56.20 && tcp.flags.syn == 1
```

### UDP Traffic

UDP reconnaissance traffic targeting multiple ports was observed.

Example filter:

```text
ip.addr == 192.168.56.20 && udp
```

ICMP **Destination Unreachable — Port Unreachable** responses were also observed, indicating that some probed UDP ports were closed.

---

## Evidence

The report contains screenshots documenting:

* TCP port discovery
* Service/version enumeration
* UDP scanning
* Consolidated Nmap results
* TCP SYN reconnaissance traffic in Wireshark
* UDP reconnaissance traffic and ICMP responses in Wireshark

### Figures

* **SS03** — Service and Version Enumeration Results for LAB-02
* **SS04** — OS Detection and Open Port Enumeration Results for LAB-02
* **SS05** — UDP Top-Port Scan Results for LAB-02
* **SS06** — Consolidated TCP Port and Service Enumeration Results for LAB-02
* **SS07** — Wireshark Capture of TCP SYN Reconnaissance Traffic
* **SS08** — Wireshark Capture of UDP Reconnaissance Traffic and ICMP Port-Unreachable Response

---

## Security Observations

The assessment revealed a broad exposed service surface on the deliberately vulnerable VM. Multiple network services and legacy versions were accessible, increasing the potential attack surface.

These results represent **reconnaissance observations and service exposure**, not confirmation that every discovered service is exploitable.

Recommended defensive actions include:

* Disable unnecessary services.
* Restrict exposed services using firewall rules.
* Upgrade unsupported or legacy software.
* Restrict administrative services to trusted networks.
* Monitor network traffic for reconnaissance and scanning activity.
* Regularly perform authorized vulnerability assessments.

---

## Rules of Engagement

The assessment followed the authorized laboratory rules:

* Testing was limited to the approved LAB-02 asset.
* No denial-of-service activity was performed.
* No destructive payloads were used.
* No persistence mechanisms were deployed.
* No third-party systems were targeted.
* Evidence was limited to the minimum required for reporting.
* Testing was performed within the isolated training environment.

---

## Conclusion

This task demonstrated the practical workflow of network reconnaissance: identifying a target, discovering exposed ports, enumerating services and versions, examining UDP services, and validating reconnaissance activity through packet capture.

The combination of **Nmap and Wireshark** provided both endpoint-level and network-level evidence of the assessment activity.

---

## References

* [Nmap Official Documentation](https://nmap.org/book/man.html)
* [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
* [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)

---

## Author

**Pritam Bose**

Cybersecurity Training Portfolio
Task 03 — Network Reconnaissance & Port Scanning Audit

````

**GitHub folder structure** rakhna simple:

```text
network-reconnaissance/
│
├── README.md
├── Task_03_Network_Reconnaissance_Audit_Report.pdf
│
└── screenshots/
    ├── SS03.png
    ├── SS04.png
    ├── SS05.png
    ├── SS06.png
    ├── SS07.png
    └── SS08.png
