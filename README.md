# Virtual Host Redirect Generator

## Description
This script reads domain-to-URL mappings from standard input, parses them, and generates Nginx server block configurations to redirect multiple virtual hosts to their corresponding destination URLs. The generated configuration is output to standard output.

## Usage
### 1. Provide input to the script:
The script expects input in the following format:
```plaintext
example.com  --> http://destination.com/whatever
sub.example.com  --> http://destination.com
another.com  --> http://another-destination.com/example
```
Each line consists of a source domain, followed by `-->`, and the destination URL.

### 2. Run the script:
```sh
cat input.txt | python3 script.py > output.conf
```
Alternatively, you can provide input interactively:
```sh
echo "example.com  --> http://destination.com" | python3 script.py
```

## Output
The script generates an Nginx configuration file containing server blocks for each destination URL. Example output:
```nginx
# Auto-generated file. Please don't make changes to this file, they will be overwritten.
server {
    listen 80; listen [::]:80;
    server_name example.com sub.example.com;
    root /var/www/html;
    location /.well-known/ { try_files $uri =404; }
    location / { return 302 http://destination.com; }
}

server {
    listen 80; listen [::]:80;
    server_name another.com;
    root /var/www/html;
    location /.well-known/ { try_files $uri =404; }
    location / { return 302 http://another-destination.com; }
}
```

## Configuration
- The script assumes the root directory is `/var/www/html`. Change this in the script if needed.
- It processes only valid input lines and ignores comments (`#` prefix) and malformed entries.
- Each server block redirects traffic from the specified domains to the corresponding destination URL using a `302` temporary redirect.

## Error Handling
- Lines that do not match the expected format are reported to stderr as parse errors.
- The script does not modify existing configuration files; it only generates output based on input mappings.

## Notes
- The output should be saved as an Nginx configuration file (e.g., `output.conf`) and included in the main Nginx configuration using the `include` directive.
- Restart Nginx after updating the configuration: 
  ```sh
  sudo systemctl restart nginx
  ```
- Ensure the destination URLs are accessible and correctly configured.

## License
This script is provided as-is, with no warranty. Modify and use it at your discretion.

