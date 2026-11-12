# Python TCP Port Scanner

A Python-based TCP port scanner that identifies open ports on a target IPv4 address using socket programming.

This project is part of my journey in learning Python, computer networking, and cybersecurity. My long-term goal is to develop it into a web-based network scanning application.

## Features

- **IPv4 Validation** — Uses regular expressions (regex) to validate IPv4 addresses.
- **Top 10 Port Scan** — Scans the 10 most common TCP ports.
- **Top 100 Port Scan** — Scans the 100 most common TCP ports.
- **Custom Port Scan** — Allows users to specify ports separated by commas.
- **Input Validation** — Checks custom port numbers and removes duplicates.
- **Timeout Handling** — Handles connection timeouts and refused connections.
- **Interactive CLI** — Provides a menu for selecting scan modes and running additional scans.

## Technologies Used

- Python
- `socket` — TCP networking
- `re` — IPv4 address validation
- `sys` — Program termination

## Getting Started

### Requirements

- Python 3
- An internet or local network connection when scanning remote targets

No additional Python packages are required.

### Running the Program

1. Clone the GitHub repository or download the source code.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

4. Enter a valid IPv4 address.
5. Select a scan mode.
6. View the results in the terminal.

### Example

```text
Enter the IP address: 127.0.0.1

1) Top 10 most common port
2) Top 100 most common port
3) Custom ports

Enter your choice: 3

Enter custom ports: 80,443,8080

Port 80 is closed
Port 443 is open
Port 8080 is closed

There is 1 ports open
```

*Example output is illustrative. Actual results depend on the target.*

## Future Development

Planned features include:

- [ ] Domain name validation and DNS resolution
- [ ] Service identification and banner grabbing
- [ ] Concurrent scanning for improved performance
- [ ] UDP scanning
- [ ] Flask backend integration
- [ ] HTML, CSS and JavaScript frontend
- [ ] Web-based results dashboard

## Disclaimer

This project is intended for educational purposes and authorised network security testing only.

Only scan systems that you own or have explicit permission to test.

## Project Status

**In development** — The basic command-line TCP scanner is implemented, with additional features planned.
