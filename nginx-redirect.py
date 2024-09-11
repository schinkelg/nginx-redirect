#!/usr/bin/python3

import re
import sys
from collections import defaultdict

root_directory = "/var/www/html"
vhosts = defaultdict(set)

pattern = re.compile(r"^([a-zA-Z0-9.-]+)\s+-->\s+(http[a-zA-Z0-9-./:]+)$")

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("#"):
        continue

    match = pattern.match(line)
    if not match:
        print(f"# Parse error: {line}.", file=sys.stderr)
        continue

    vhosts[match.group(2)].add(match.group(1))

print("# Auto-generated file. Please don't make changes to this file, they will be overwritten.")
for key, server_names in vhosts.items():
    server_names_str = " ".join(server_names)
    print(
        f"server {{ "
        f"listen 80; listen [::]:80; "
        f"server_name {server_names_str}; "
        f"root {root_directory}; "
        f"location /.well-known/ {{try_files $uri =404;}} "
        f"location / {{return 302 {key};}}}}"
    )
