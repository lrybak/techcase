#!/usr/bin/env python3

import argparse
from datetime import datetime

import nmap
import sys
import os

from scanner.models import Scan, Host, Port, PortScan

MAX_SCANS = 2


def scan_network(hosts):
    """
    Scans network

    Params:
        hosts (str): IP address or ip address range

    Returns:
        nmap.PortScanner: Scanner object with scan results
    """
    try:
        scanner = nmap.PortScanner()
        scanner.scan(hosts=hosts, arguments='-T4 -F')
    except nmap.PortScannerError as error:
        print(f"Error during scanning: {error}")
        return None

    return scanner


def is_running_in_kubernetes():
    """Checks if application is running in Kubernetes environment"""
    return 'KUBERNETES_SERVICE_HOST' in os.environ and 'KUBERNETES_SERVICE_PORT' in os.environ


def get_cache_path():
    """Returns path to cache file"""
    pickle_file_name = '.scanner-cache.json'
    if is_running_in_kubernetes():
        return os.path.join('/mnt/scanner', pickle_file_name)
    else:
        return os.path.join(os.path.expanduser('~'), pickle_file_name)


def load_cache():
    """
    Function that deserialize scan object
    If no file found, new object is returned
    """
    try:
        with open(get_cache_path(), 'r') as f:
            scan_json = f.read()
            if scan_json:
                return Scan.parse_raw(scan_json)
            else:
              return Scan()
    except FileNotFoundError:
        return Scan()


def save_scan(obj):
    """Function that serialize scan object """
    with open(get_cache_path(), 'w') as f:
        f.write(obj.json())


def main():
    """
    Main function that parses command line arguments, initiates a network scan, and prints scan results.
    """

    # Parse command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("ipaddress", help="IP address or network range")
    parser.add_argument("-v", action="count", default=0, help="Increase verbosity level")
    args = parser.parse_args()

    # Deserialize scan object
    scan = load_cache()

    # Scan network
    current_scan = scan_network(hosts=args.ipaddress)

    # Handle errors in the scan
    if 'error' in current_scan.scaninfo():
        for erritem in current_scan.scaninfo()['error']:
            print(erritem, file=sys.stderr)

    # Loop through hosts in nmap scan results
    for host in current_scan.all_hosts():
        h = scan.get_host(ip_address=host)

        # Loop through protocols in nmap scan results
        for protocol in current_scan[host].all_protocols():
            ports = current_scan[host][protocol].keys()

            # Loop through port in nmap scan results
            # Feed the data into data models
            for port in ports:
                p = Port(
                    port_number=port,
                    protocol=protocol,
                    service_name=current_scan[host][protocol][port]['name'],
                    max_scans=88
                )
                p.add_scan(
                    PortScan(
                        timestamp=datetime.now(),
                        state=current_scan[host][protocol][port]['state']
                    )
                )
                h.add_port(p)
                scan.add_host(h)

        # Print the results
        print(h)

    # Print additional scan information
    if args.v > 0:
        scan_stats = current_scan.scanstats()
        total_hosts = scan_stats.get('totalhosts', 'N/A')
        up_hosts = scan_stats.get('uphosts', 'N/A')
        down_hosts = scan_stats.get('downhosts', 'N/A')
        elapsed_time = scan_stats.get('elapsed', 'N/A')

        print(
            f"{total_hosts} IP address in range ({up_hosts} hosts up, {down_hosts} hosts down) scanned in {elapsed_time} seconds")

    # Print scan object
    if args.v > 1:
        print(scan.json(indent=2))

    # Serialize scan object
    save_scan(scan)


if __name__ == '__main__':
    main()
