# ATM & Bank Account Simulator

## Overview of the project
A modular, CLI-based ATM simulator built in Python. It allows users to log in, manage their balance, and track transactions with persistent local storage.

## Features
- User authentication
- Deposits, withdrawals, and balance inquiries
- Mini-statement generation
- Persistent JSON database

## Technologies/tools used
- Python 3.x
- Built-in `json` and `datetime` libraries

## Steps to install & run the project
1. Clone the repository: `git clone [repository_url]`
2. Navigate to the project directory: `cd atm_simulator_project`
3. Ensure the `data` directory exists with a valid `accounts.json` file.
4. Run the application: `python src/main.py`

## Instructions for testing
Log in using the test account credentials provided in the `accounts.json` file. Attempt to withdraw more money than the current balance to test the error handling validation.
