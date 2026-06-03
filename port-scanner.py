import socket
import time

# Common ports to check
COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    143,  # IMAP
    443,  # HTTPS
    3306, # MySQL
    3389  # RDP
]

def scan_port(host, port):
    """
    Attempts to connect to a TCP port.
    Returns True if the port is open.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        sock.close()

        return result == 0

    except socket.gaierror:
        print(f"[ERROR] Unable to resolve hostname: {host}")
        return False

    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")
        return False


def main():
    print("=" * 50)
    print("Port Scanner")
    print("=" * 50)

    host = input(
        "\nEnter IP address or hostname "
        "(example: localhost or 127.0.0.1): "
    ).strip()

    print(f"\nScanning {host}...")
    start_time = time.time()

    open_ports = []

    for port in COMMON_PORTS:
        if scan_port(host, port):
            open_ports.append(port)
            print(f"[OPEN ] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

    end_time = time.time()

    print("\n" + "=" * 50)
    print("Scan Summary")
    print("=" * 50)

    if open_ports:
        print("\nOpen Ports Found:")
        for port in open_ports:
            print(f" - {port}")
    else:
        print("\nNo open ports detected from the scanned list.")

    print(
        f"\nScan completed in "
        f"{round(end_time - start_time, 2)} seconds"
    )


if __name__ == "__main__":
    main()
