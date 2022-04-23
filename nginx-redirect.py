#!/usr/bin/python3

import re
import sys
from collections import defaultdict

root_directory = "/var/www/html"
vhosts = defaultdict(set)

for line in sys.stdin.readlines():
    line = line.strip()
    if not line:  # skip empty lines
        continue

    if line[0] == "#":  # skip comments
        continue

    m = re.search("^([a-zA-Z0-9.-]+)[\\s]+-->[\\s]+(http[a-zA-Z0-9-./:]+)$", line)
    if not m:
        print(f"# Parse error: {line}.", file=sys.stderr)
        continue

    vhosts[m.group(2)].add(m.group(1))


print("# Auto-generated file. Please don't make changes to this file, they will be overwritten.")
for key in vhosts:
    server_names = " ".join(vhosts[key])
    print(
        f"server {{ "
        f"listen 80; listen [::]:80; "
        f"server_name {server_names}; "
        f"root {root_directory}; "
        f"location /.wel {{try_files $uri =404;}} "
        f"location / {{return 302 {key};}}}}"
    )
