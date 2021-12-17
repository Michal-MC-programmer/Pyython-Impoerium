import sys
from collections import defaultdict

file_name = sys.argv[1]

user_total_time = defaultdict(int)

user_last_login = {}

with open(file_name) as f:
    for line in f:
        user, action, t = line.strip().split(";")
        t = int(t)

        if action == "LOGIN":
            user_last_login[user] = t
        elif action == "LOGOUT":
            user_total_time[user] += t - user_last_login[user]

for user, t in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(f" - {user:10}: {t} s")