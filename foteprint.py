import nmap
def os_fingerprint(ip_range):
    nm = nmap.PortScanner()
    arguments = '-O -Pn'  # Enable OS detection and disable ping scan

    for ip in ip_range:
        result = nm.scan(ip, arguments=arguments)

        if 'osmatch' in result['scan'][ip]:
            print(f"IP: {ip}")
            for os in result['scan'][ip]['osmatch']:
                print(f"Operating System: {os['name']}")
                print(f"Accuracy: {os['accuracy']}\n")
        else:
            print(f"No OS fingerprinting results for IP: {ip}\n")

# Prompt the user to enter an IP address or a range of IP addresses
ip_input = input("Enter an IP address or a range of IP addresses (e.g., '192.168.0.1' or '192.168.0.1-10'): ")

# Split the input by '-' to check if it's a range of IP addresses
ip_range = ip_input.split('-')

# Check if it's a single IP address or a range
if len(ip_range) == 1:
    os_fingerprint(ip_range)
else:
    start_ip = ip_range[0].strip()
    end_ip = ip_range[1].strip()

    # Generate a range of IP addresses
    ip_list = []
    ip_parts = start_ip.split('.')
    start = int(ip_parts[3])
    end = int(end_ip.split('.')[3])

    for i in range(start, end + 1):
        ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{i}"
        ip_list.append(ip)

    os_fingerprint(ip_list)
