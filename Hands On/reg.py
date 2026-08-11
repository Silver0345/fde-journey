'''Week 2 Day 3 hands-on: parse log lines with re.

Extracts the timestamp from each log entry using a regex with capture
groups for the date and time portions. The pattern also matches (but
does not yet capture) the log level and a variable-length IPv4 address,
verified against entries with differing octet digit counts.
'''

import re

times_stamp = [
   "2026-08-10 14:23:01 ERROR Failed login for user admin from 192.168.1.15",
    "2026-08-10 14:23:05 INFO User admin logged in from 192.168.1.15",
    "2026-08-10 14:24:10 INFO User root logged in from 10.0.0.1",
    "2026-08-10 14:25:30 ERROR Failed login for user root from 192.168.1.100"

]

for t in times_stamp:
    #print(t.strip())
    if matches := re.search(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) [?:a-z ]*\d*\.\d*\.\d*\.\d*$", t, re.IGNORECASE):
        print(f"Time: ", matches.group(2))
        