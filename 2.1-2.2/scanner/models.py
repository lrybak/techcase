from enum import Enum

import humanize
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class State(str, Enum):
    """Enum representing the state of a port scan."""
    OPEN = "open"
    CLOSED = "closed"


class Protocol(str, Enum):
    """Enum representing the protocol used for scanning (TCP/UDP)."""
    TCP = "tcp"
    UDP = "udp"


MAX_SCANS = 4  # default number of kept scans


class PortScan(BaseModel):
    """
    A model representing a single port scan.

    Attributes:
        timestamp: A datetime indicating when the scan was performed.
        state: A State enum indicating the state of the port (OPEN/CLOSED).
    """
    timestamp: datetime
    state: State


class Port(BaseModel):
    """
    A model representing a network port.

    Attributes:
        protocol: A Protocol enum (TCP/UDP).
        port_number: An integer indicating the port number.
        scans: An optional list of PortScan objects representing previous scans.
        service_name: A string representing the name of the service running on the port.
    """
    protocol: Protocol
    port_number: int
    scans: Optional[List[PortScan]] = None
    service_name: str

    def add_scan(self, scan: PortScan):
        if self.scans is None:
            self.scans = []
        self.scans.append(scan)
        self.scans = sorted(self.scans, key=lambda x: x.timestamp, reverse=True)[:MAX_SCANS]


class Host(BaseModel):
    """
    A model representing a host with scanned ports.

    Attributes:
        ip_address: A string representing the host's IP address.
        scanned_ports: An optional list of Port objects representing scanned ports.
    """
    ip_address: str
    scanned_ports: Optional[List[Port]] = None

    def add_port(self, port: Port):
        if self.scanned_ports is None:
            self.scanned_ports = []
        existing_port = next(
            (p for p in self.scanned_ports if p.protocol == port.protocol and p.port_number == port.port_number), None)
        if existing_port:
            for scan in port.scans:
                existing_port.add_scan(scan)
        else:
            self.scanned_ports.append(port)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Host object.
        """
        result = f"{self.ip_address}\n"
        for p in self.scanned_ports or []:
            result += f"* {p.port_number}/{p.protocol} {p.service_name}: "
            for index, s in enumerate(p.scans or []):
                result += f"{s.state} ({humanize.naturaltime(s.timestamp)})"

                # Check if it's the last loop iteration
                if index < len(p.scans) - 1:
                    result += ", "
            result += "\n"
        return result


class Scan(BaseModel):
    """
    A model representing a collection of hosts.

    Attributes:
        hosts: An optional list of Host objects.
    """
    hosts: Optional[List[Host]] = None

    def find_host(self, ip_address) -> Optional[Host]:
        """Find host item"""
        if self.hosts:
            for host in self.hosts:
                if host.ip_address == ip_address:
                    return host
        return None

    def get_host(self, ip_address: str) -> Optional[Host]:
        """Get host item, create new host instance if not exists"""
        if not self.find_host(ip_address):
            self.add_host(Host(ip_address=ip_address))

        return self.find_host(ip_address)

    def add_host(self, host: Host):
        """Adds Host item"""
        if self.hosts is None:
            self.hosts = []
        if not any(existing_host.ip_address == host.ip_address for existing_host in self.hosts):
            self.hosts.append(host)
