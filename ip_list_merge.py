"""
ip_list_merge.py

Merge multiple IP list files, normalize entries, remove duplicates,
and write the result to a single output file.

Usage:
    python ip_list_merge.py input1.txt input2.txt ... output.txt
"""

import sys
from typing import Set


def load_ips_from_file(path: str) -> Set[str]:
    ips: Set[str] = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            value = line.strip()
            if not value or value.startswith("#"):
                continue
            ips.add(value)
    return ips


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python ip_list_merge.py input1.txt input2.txt ... output.txt")
        sys.exit(1)

    *input_files, output_file = sys.argv[1:]

    all_ips: Set[str] = set()
    for path in input_files:
        print(f"Loading IPs from: {path}")
        all_ips |= load_ips_from_file(path)

    print(f"Total unique IPs: {len(all_ips)}")

    with open(output_file, "w", encoding="utf-8") as out:
        for ip in sorted(all_ips):
            out.write(ip + "\n")

    print(f"Merged IP list written to: {output_file}")


if __name__ == "__main__":
    main()
