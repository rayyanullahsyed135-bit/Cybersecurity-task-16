# Cybersecurity-task-16

Project Overview

This project simulates a real-world security incident involving repeated failed SSH login attempts on a Linux (Ubuntu) system. The objective was to detect, analyze, contain, and remediate the incident using system logs.

Objective

Simulate a brute-force login attempt

Analyze authentication logs

Classify the incident

Contain and remediate the threat

Document timeline and actions taken

Recommend preventive measures

2.Tools Used

Ubuntu 25.04 (Target System)

Kali Linux (Attacker Simulation)

Linux Authentication Logs (/var/log/auth.log)

Python (Log parsing automation)

🔍 Incident Simulation Steps (Based on Mini Guide)
1️⃣ Incident Simulation

Simulated repeated failed SSH login attempts from Kali Linux: ssh fakeuser@192.168.195.130
Multiple incorrect passwords were entered to generate log entries.

Log Analysis
Monitored authentication logs: sudo tail -f /var/log/auth.log

Sample Log Evidence: Failed password for invalid user fakeuser from 192.168.195.129 port 59452 ssh2
Failed password for invalid user fakeuser from 192.168.195.129 port 59453 ssh2
Connection closed by invalid user fakeuser 192.168.195.129 port 59453 [preauth]

Indicators Identified:
Repeated failed login attempts
Same source IP address
Invalid username attempts

Incident Classification

Attack Type: Brute Force (Credential Guessing)
Severity: Medium to High
Reason:
Authentication abuse
Potential credential compromise risk

Containment Actions
Blocked attacking IP using firewall: sudo ufw deny from 192.168.195.129

Disabled password authentication in SSH configuration
Restarted SSH service

Threat Removal & Root Cause Fix

Root Cause:

Password-based SSH authentication enabled

Fix:

Implemented SSH key authentication

Disabled password authentication

6️⃣ System Restoration

Verified SSH service functionality

Confirmed no further failed login attempts

Validated firewall rules

7️⃣ Incident Timeline Document
Incident Timeline
Time	Event
10:05	First failed login attempt detected
10:07	Multiple repeated failed attempts
10:10	Log analysis confirmed brute force pattern
10:15	IP address blocked via firewall
10:18	Password authentication disabled
10:25	System verified secure
