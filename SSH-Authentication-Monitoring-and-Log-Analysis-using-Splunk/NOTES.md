# `NOTES.md`

````markdown
# Report 6 — Setup & Commands

## Setup

### 1. Start the Lab Machines

Start:

- Kali Linux
- Metasploitable 2
- Splunk Enterprise

Make sure Kali and Metasploitable are connected to the same isolated VMware network.

### 2. Check Target IP

Metasploitable:

```bash
ifconfig
````

Target IP used in this lab:

```text
192.168.202.130
```

Kali IP:

```text
192.168.202.131
```

### 3. Check Connectivity

From Kali:

```bash
ping -c 4 192.168.202.130
```

### 4. Start Splunk

Open:

```text
http://localhost:8000
```

Log in to Splunk Enterprise.

---

# Commands

## Nmap Reconnaissance

Full scan:

```bash
sudo nmap 192.168.202.130
```

SSH-specific scan:

```bash
sudo nmap -p 22 192.168.202.130
```

Expected:

```text
22/tcp open ssh
```

---

## SSH Login

Connect to Metasploitable:

```bash
ssh msfadmin@192.168.202.130
```

After successful login:

```bash
whoami
```

```bash
hostname
```

Exit:

```bash
exit
```

---

## Generate Failed Authentication

From Kali:

```bash
ssh msfadmin@192.168.202.130
```

Enter an incorrect password several times.

---

## Generate Successful Authentication

From Kali:

```bash
ssh msfadmin@192.168.202.130
```

Enter the correct laboratory password.

After login:

```bash
whoami
```

```bash
hostname
```

Then:

```bash
exit
```

---

# Authentication Log

On Metasploitable:

```bash
grep -E "Failed password|Accepted password" /var/log/auth.log
```

Failed authentication only:

```bash
grep "Failed password" /var/log/auth.log
```

Successful authentication only:

```bash
grep "Accepted password" /var/log/auth.log
```

Search for the user:

```bash
grep "msfadmin" /var/log/auth.log
```

Search for the Kali IP:

```bash
grep "192.168.202.131" /var/log/auth.log
```

View recent entries:

```bash
tail -n 30 /var/log/auth.log
```

---

# Transfer auth.log to Kali

From Kali:

```bash
scp msfadmin@192.168.202.130:/var/log/auth.log ~/auth.log
```

Check the file:

```bash
ls -lh ~/auth.log
```

Optional verification:

```bash
grep -E "Failed password|Accepted password" ~/auth.log
```

---

# Splunk Setup

Open:

```text
http://localhost:8000
```

Go to:

```text
Settings
→ Add Data
→ Upload
```

Upload:

```text
~/auth.log
```

Set source as:

```text
auth.log
```

Set source type as:

```text
linux_secure
```

Then complete the upload.

---

# SPL Searches

## Check All Events

```spl
source="auth.log"
```

## Failed Authentication

```spl
source="auth.log" "Failed password"
```

## Accepted Authentication

```spl
source="auth.log" "Accepted password"
```

## Combined Search

```spl
source="auth.log" "Failed password" OR "Accepted password"
```

---

# Screenshot Order

## Screenshot 1

Nmap result showing:

```text
22/tcp open ssh
```

## Screenshot 2

Metasploitable authentication log showing:

```text
Failed password
```

and

```text
Accepted password
```

## Screenshot 3

Splunk search:

```spl
source="auth.log" "Failed password"
```

## Screenshot 4

Splunk search:

```spl
source="auth.log" "Accepted password"
```

## Screenshot 5

Splunk combined search:

```spl
source="auth.log" "Failed password" OR "Accepted password"
```

```
```
