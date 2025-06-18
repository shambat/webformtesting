# 🛡️ Web3Forms Fake Data Sender (For Testing Purposes Only)

This Python tool uses the [Web3Forms](https://web3forms.com/) API to send **fake form data** automatically. It is designed for **testing purposes only**, such as evaluating how Web3Forms handles high-frequency data or verifying form validation/security controls during development.

> ❗ **Disclaimer:** This tool is intended **only for ethical testing, QA, or red team simulations** with proper authorization. Misuse of this tool for spam or denial-of-service (DoS) attacks is strictly prohibited and may violate Web3Forms' Terms of Service and local cybersecurity laws.

---

## 🔧 Features

- Generates **realistic fake data** using the [Faker](https://faker.readthedocs.io/) library.
- Automates sending multiple POST requests to the Web3Forms endpoint.
- Customizable access key and form parameters.
- Can be used to test:
  - Spam filters
  - Rate limits
  - Backend form processing

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- `requests` library
- `faker` library

You can install dependencies using:

```bash
pip install requests faker
