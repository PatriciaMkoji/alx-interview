#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes_count = {}


def print_statistics():
    """
    A script that prints statistics including total file size and counts for each status code.
    """
    try:
        print(f"File size: {total_size}")
        for code in sorted(status_codes_count):
            print(f"{code}: {status_codes_count[code]}")
        print()

        sys.stdout.flush()
    except BrokenPipeError:
        # Ignore BrokenPipeError when writing to a closed pipe
        pass


def signal_handler(sig, frame):
    """
    It handles SIGINT signal by printing statistics and exiting.
    """
    print_statistics()
    sys.exit(0)

    # Register the signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    line_count = 0
    for line in sys.stdin:
        line = line.strip()

        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                total_size += file_size
                status_codes_count[status_code] = status_codes_count.get(status_code, 0) + 1
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics()
        except (ValueError, IndexError):
            # Skip lines with incorrect format
            pass

