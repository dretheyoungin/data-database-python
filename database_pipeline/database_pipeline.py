import json
import time

print("Bot: Initializing Autonomous Database Ledger Pipeline...")

# Simulated secure corporate transaction database logs
raw_database_records = [
    '{"user_id": 101, "action": "login", "status": "success"}',
    '{"user_id": 102, "action": "withdrawal", "status": "failed"}',
    '{"user_id": 103, "action": "password_change", "status": "success"}'
]

print("\nBot: Sweeping database tables for operational failures...")

# Open a permanent audit log text file to record system anomalies automatically
with open("security_audit_log.txt", "w") as audit_file:
    for record in raw_database_records:
        # Parse the JSON database text string into live data features
        parsed_data = json.loads(record)

        # Security Trigger: If any transaction status failed, flag it immediately
        if parsed_data["status"] == "failed":
            log_msg = f"[CRITICAL SECURITY ALERT] - User {parsed_data['user_id']} execution FAILED during {parsed_data['action']} action.\n"
            print(f"-> Found Anomaly! Writing to security log...")
            audit_file.write(log_msg)

print("\nBot: Success! Database sweep complete. Audit logs compiled cleanly.")