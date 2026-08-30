# REST API Security Assessment – crAPI

A controlled API security assessment performed against OWASP crAPI (Completely Ridiculous API) in a local laboratory environment.

## Objective

The objective of this project was to understand how REST APIs handle authentication, object identifiers, and object-level authorization, and to test whether an authenticated user could access an object belonging to another user.

## Environment

- Kali Linux
- OWASP crAPI
- Docker / Docker Compose
- Burp Suite
- Firefox
- Two controlled test accounts

## Methodology

The assessment followed a simple API testing workflow:

Application Setup  
→ User Authentication  
→ Video Upload  
→ API Request Capture  
→ Endpoint Analysis  
→ Burp Repeater  
→ Object ID Manipulation  
→ Response Comparison

## Key Finding

### Broken Object Level Authorization (BOLA)

The API exposed video objects through endpoints containing object identifiers.

Requests such as:

`GET /identity/api/v2/user/videos/<object_id>`

were captured using Burp Suite and replayed through Repeater.

The object identifier was modified during testing to determine whether authorization was enforced based on the authenticated user's ownership of the requested object.

The test demonstrated successful HTTP `200 OK` responses when accessing the tested object identifier, providing evidence for investigating object-level authorization.

## Tools Used

- Burp Suite
- Kali Linux
- Docker
- Firefox

## Documentation

The complete methodology, API request/response evidence, analysis, and conclusion are documented in:

`report.pdf`

## Repository Structure

```text
rest-api-security-assessment/
│
├── README.md
├── report.pdf
├── screenshots/
├── requests/
└── notes/