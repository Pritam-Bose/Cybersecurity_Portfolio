# Task 4 – OWASP Top 10 Vulnerability Assessment

**Organization:** RabTech Academy  
**Internship:** Cybersecurity & Ethical Hacking  
**Target:** OWASP Juice Shop (Localhost)  
**Tester:** Pritam Bose  

## Objective

To identify and demonstrate common web application vulnerabilities in the authorized OWASP Juice Shop sandbox and document suitable security mitigations.

## Tools Used

- Kali Linux
- OWASP Juice Shop
- Burp Suite
- Nmap
- Firefox

## Vulnerabilities Tested

### 1. SQL Injection

SQL Injection was demonstrated through the Juice Shop login functionality using Burp Suite.

**Observation:**  
A manipulated login request resulted in a successful authentication response.

**Impact:** Authentication bypass and potential database compromise.

**Remediation:** Use parameterized queries/prepared statements.

```js
const query = "SELECT * FROM users WHERE email = ?";
db.query(query, [email]);
````

---

### 2. Cross-Site Scripting (XSS)

XSS testing was performed against the Juice Shop search functionality and related XSS challenges.

**Observation:**
A proof-of-concept XSS payload successfully triggered the relevant Juice Shop challenge.

**Impact:** Malicious JavaScript execution and possible user/session attacks.

**Remediation:**

```js
element.textContent = userInput;
```

Avoid unsafe DOM operations such as `innerHTML` with untrusted input.

---

### 3. Broken Access Control / IDOR

API requests were inspected using Burp Suite, including basket-related endpoints.

Example:

```http
GET /rest/basket/7
```

The server returned a successful response containing basket information.

**Security Concern:** Object-level authorization must be verified on the server for every requested resource.

**Remediation:**

```js
if (basket.UserId !== req.user.id) {
    return res.status(403).json({ error: "Access denied" });
}
```

---

## Network / API Testing

Burp Suite HTTP History was used to identify application endpoints, requests, authentication headers and responses.

Nmap was used to identify the local Juice Shop service:

```bash
nmap -sV 127.0.0.1 -p 3000
```

Port `3000/tcp` was identified as open.

## Evidence

* **SS1:** SQL Injection – Burp Suite request/response
* **SS2:** XSS – Juice Shop PoC
* **SS3:** Basket/API request – Burp Repeater
* **SS4:** Burp Suite HTTP History
* **SS5:** Nmap service scan

## Conclusion

The assessment demonstrated the security risks associated with improper input handling, XSS and insufficient object-level authorization. The main recommended defenses are parameterized database queries, proper output encoding, safe DOM handling and server-side authorization checks.

All testing was performed against the authorized local OWASP Juice Shop sandbox as part of the **RabTech Academy Cybersecurity & Ethical Hacking Internship**.

## References

1. OWASP Top 10 – [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
2. OWASP Juice Shop – [https://owasp.org/www-project-juice-shop/](https://owasp.org/www-project-juice-shop/)
3. OWASP SQL Injection Prevention Cheat Sheet
4. OWASP Cross-Site Scripting Prevention Cheat Sheet
5. PortSwigger Web Security Academy
6. Nmap Documentation

