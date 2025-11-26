"""
log_filter.py

Simple log filtering helper.

Usage:
    python log_filter.py input.log output.log --ip 192.0.2.10 --keyword ERROR

You can filter by:
    --ip        <ip-address>
    --keyword   <text>
    --since     <substring to match timestamp, e.g. '2025-01-01'>
"""

import sys
from typing import Optional, TextIO


def filter_line(
    line: str,
    ip: Optional[str],
    keyword: Optional[str],
    since: Optional[str],
) -> bool:
    if ip and ip not in line:
        return False
    if keyword and keyword not in line:
        return False
    if since and since not in line:
        return False
    return True


def main() -> None:
    if len(sys.argv) < 3:
        print(
            "Usage: python log_filter.py input.log output.log "
            "[--ip <ip>] [--keyword <text>] [--since <timestamp-substring>]"
        )
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    ip: Optional[str] = None
    keyword: Optional[str] = None
    since: Optional[str] = None

    args = sys.argv[3:]
    it = iter(args)
    for arg in it:
        if arg == "--ip":
            ip = next(it, None)
        elif arg == "--keyword":
            keyword = next(it, None)
        elif arg == "--since":
            since = next(it, None)

    with open(input_path, "r", encoding="utf-8") as inp, open(
        output_path, "w", encoding="utf-8"
    ) as out:
        _filter_log(inp, out, ip, keyword, since)

    print(f"Filtered log written to: {output_path}")


def _filter_log(
    inp: TextIO,
    out: TextIO,
    ip: Optional[str],
    keyword: Optional[str],
    since: Optional[str],
) -> None:
    for line in inp:
        if filter_line(line, ip, keyword, since):
            out.write(line)


if __name__ == "__main__":
    main()
