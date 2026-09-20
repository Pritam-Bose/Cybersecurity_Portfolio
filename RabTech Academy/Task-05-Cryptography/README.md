# Task 5 – Cryptography, Key Management & Secure Auth

## RabTech Academy Internship

**Prepared by:** Pritam Bose  

## Objective

This project demonstrates basic secure cryptography and authentication techniques using Node.js.

The implementation covers:

- AES-256-GCM authenticated encryption
- RSA-2048 key generation and digital signatures
- bcrypt password hashing and verification

## Project Structure

```text
task5-cryptography/
├── aes.js
├── rsa.js
├── password.js
├── package.json
├── package-lock.json
├── README.md
└── .gitignore
1. AES-256-GCM

aes.js demonstrates:

256-bit AES key generation
Random GCM IV generation
Encryption of plaintext
Authentication tag generation
Successful decryption

Run:

node aes.js

Expected result:

Encrypted: { ... }
Decrypted: Hello RabTech Academy
2. RSA-2048

rsa.js demonstrates:

RSA-2048 public/private key generation
SHA-256 digital signature creation
Signature verification

Run:

node rsa.js

Expected result:

RSA-2048 key pair generated.
Signature: ...
Signature valid: true
3. bcrypt Password Hashing

password.js demonstrates:

Password hashing
Salt/work factor usage
Password verification
Avoiding plaintext password storage

Run:

node password.js

Expected result:

Password hash:
$2b$12$...
Password verified: true
Security Practices
Never store plaintext passwords.
Protect encryption keys and private RSA keys.
Do not reuse an AES-GCM IV with the same key.
Do not hard-code production secrets.
Keep node_modules excluded through .gitignore.
Technologies
Node.js
JavaScript
Node.js Crypto module
bcrypt
Conclusion

This task demonstrates practical implementation of authenticated encryption,
digital signatures, and secure password hashing using Node.js.

References
RabTech Academy – Task 5: Cryptography, Key Management & Secure Auth
Node.js Crypto Documentation
npm bcrypt Documentation
OWASP Password Storage Cheat Sheet
OWASP Cryptographic Storage Cheat Sheet