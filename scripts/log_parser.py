# Extract failed login attempts from auth.log

with open('auth.log_sample.txt', 'r') as file:
    for line in file:
        if "Failed password" in line:
            print(line.strip())
