#!/usr/bin/python3
"""Log parsing"""


def compute_metrics(lines):
    """Compute metrics from log lines"""
    total_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        try:
            parts = line.split()
            file_size = int(parts[-2])
            status_code = int(parts[-3])

            # Update total file size
            total_size += file_size

            # Update status code counts
            status_counts[status_code] += 1
        except (IndexError, ValueError):
            # Skip lines with incorrect format
            continue

    return total_size, status_counts


def print_statistics(total_size, status_counts):
    """Print statistics"""
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")
