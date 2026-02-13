# Simple incident classification logic

def classify_failed_attempts(count):
    if count >= 10:
        return "High Severity - Brute Force Suspected"
    elif count >= 5:
        return "Medium Severity - Suspicious Activity"
    else:
        return "Low Severity"

print(classify_failed_attempts(8))
