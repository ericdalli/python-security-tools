"""
ioc_checker.py

Very simple example IOC checker.

Reads a list of indicators (IPs, domains, URLs) from a file
and prints a mock "reputation" based on basic rules.

Usage:
    python ioc_checker.py iocs.txt
"""

import sys
from typing import List, Dict


def load_iocs(path: str) -> List[str]:
    iocs: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            value = line.strip()
            if not value or value.startswith("#"):
                continue
            iocs.append(value)
    return iocs


def classify_ioc(ioc: str) -> Dict[str, str]:
    """
    Mock IOC classification logic.

    In a real implementation this is where you would call:
      - VirusTotal
      - Hybrid Analysis
      - Internal TI platform
    """
    score = "unknown"
    reason = "no heuristic matched"

    if "malware" in ioc or "bad" in ioc:
        score = "malicious"
        reason = "matched local keyword heuristic"
    elif "test" in ioc or "example" in ioc:
        score = "benign"
        reason = "matched known test pattern"
    elif ioc.startswith("192.0.2.") or ioc.startswith("198.51.100.") or ioc.startswith("203.0.113."):
        score = "benign"
        reason = "RFC 5737 documentation address range"

    return {"ioc": ioc, "score": score, "reason": reason}


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ioc_checker.py iocs.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    iocs = load_iocs(input_file)

    if not iocs:
        print("No IOCs found in input file.")
        sys.exit(0)

    for ioc in iocs:
        result = classify_ioc(ioc)
        print(f"{result['ioc']}: {result['score']} ({result['reason']})")


if __name__ == "__main__":
    main()
