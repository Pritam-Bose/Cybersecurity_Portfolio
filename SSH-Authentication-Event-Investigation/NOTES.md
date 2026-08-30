# Command Notes

## 1. Nmap Service Discovery

Command:

sudo nmap 192.168.202.130

Purpose:

Used to identify open network ports and services exposed by the Metasploitable 2 target.

Important result:

22/tcp open ssh

This confirmed that SSH was available on the target.

---

## 2. SSH Connection Test

Command:

ssh msfadmin@192.168.202.130

Purpose:

Used to initiate an SSH connection to the Metasploitable 2 system.

In the laboratory, an incorrect password was used to generate a failed authentication event.

---

## 3. SSH Connection Using Legacy RSA Host-Key Algorithm

Command:

ssh -oHostKeyAlgorithms=+ssh-rsa msfadmin@192.168.202.130

Purpose:

The Metasploitable 2 SSH implementation is very old. The option allows the modern SSH client to accept the legacy RSA host-key algorithm used by the laboratory target.

This command was used to establish the successful SSH session.

---

## 4. Verify Current User

Command:

whoami

Purpose:

Displays the username associated with the current shell session.

Expected result:

msfadmin

This verified that the SSH session was operating under the expected laboratory account.

---

## 5. Verify Hostname

Command:

hostname

Purpose:

Displays the hostname of the system currently being accessed.

Expected result:

metasploitable

This confirmed that the SSH session was connected to the intended target.

---

## 6. Search for Successful SSH Authentication

Command:

grep "Accepted password" /var/log/auth.log

Purpose:

Searches the authentication log for successful password-based authentication events.

This was used to verify that the successful SSH login was recorded by the target system.

---

## 7. Search for Failed and Successful Authentication Events

Command:

grep -E "Failed password|Accepted password" /var/log/auth.log

Purpose:

Searches the authentication log for both failed and successful password authentication events.

This allows the events to be viewed together and compared according to their timestamps, username and source address.

---

## Important Note

These commands were executed only against the intentionally vulnerable Metasploitable 2 laboratory machine.

The purpose was service identification, controlled authentication testing and log analysis rather than unauthorized access.