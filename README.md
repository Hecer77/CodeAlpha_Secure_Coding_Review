
# CodeAlpha - Secure Coding Review

This repository contains **TASK 3: Secure Coding Review** developed as part of the **CodeAlpha Cyber Security Internship (Module 1)**. 

The objective of this project is to perform a static analysis of a Python (Flask) web application, identify critical security vulnerabilities (SQL Injection and Cross-Site Scripting), explain their risks, and implement secure code remediation.

---

## 🔍 Vulnerability Assessment Report

### 🚨 Finding 1: SQL Injection (SQLi)
* **Vulnerability Type:** CWE-89: Improper Neutralization of Special Elements used in an SQL Command
* **Location:** `vulnerable_code.py` -> `/login` endpoint
* **Severity:** Critical

#### Description:
The application uses raw string formatting (`f"SELECT ... '{username}'"`) to construct database queries using direct user inputs. An attacker can manipulate the input structure by injecting malicious SQL payloads. For example, entering `' OR '1'='1` in the username field bypasses the authentication completely without a valid password.

#### Remediation (How it was fixed):
We replaced string concatenation with **Parameterized Queries (Prepared Statements)** in `secure_code.py`. By using placeholder variables (`?`), the database treats user input strictly as data, not executable SQL commands.

---

### 🚨 Finding 2: Reflected Cross-Site Scripting (XSS)
* **Vulnerability Type:** CWE-79: Improper Neutralization of Input During Web Page Generation
* **Location:** `vulnerable_code.py` -> `/search` endpoint
* **Severity:** High

#### Description:
The web application accepts input from the `q` URL parameter and renders it directly into the HTML response via `render_template_string` without encoding or sanitization. If an attacker tricks a user into clicking a link containing a malicious JavaScript payload (e.g., `<script>alert(document.cookie)</script>`), the browser will execute the script within the context of the user's session.

#### Remediation (How it was fixed):
We migrated from dangerous inline string formatting to Flask’s structured **Jinja2 rendering engine** (`render_template`). Jinja2 automatically applies **HTML Entity Escaping**, converting dangerous symbols like `<` and `>` into safe HTML entities (`&lt;` and `&gt;`), rendering payloads harmless.

---

## 📁 Repository Structure
* `vulnerable_code.py`: Source code containing the security vulnerabilities.
* `secure_code.py`: Patched and secured source code.
* `README.md`: Code review documentation and security report.
