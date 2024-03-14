status_options = {
    1: "SCHEDULED",
    2: "IN PROGRESS",
    3: "COMPLETED",
    4: "TEST ERROR",
}

vulnerable_ports = {
        "NetBIOS over TCP":["137", "139"],
        "SMB":["445"],
        "SSH":["22"],
        "DNS":["53"],
        "SMTP":["25"],
        "Remote desktop":["3389"],
        "HTTP/HTTPS":["8000","80", "443", "8080", "8443"],
        "FTP":["20", "21"],
        "Telnet":["23"],
        "Database": ["1433", "1434", "3306"]
    }

def generate_status_choices():
    return list(status_options.items())
