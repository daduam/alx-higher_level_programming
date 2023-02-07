#!/usr/bin/python3
"""101-stats"""


def display_stats(stats):
    """Print stats so far"""
    print("File size: {}".format(stats['fsize']))
    for status_code in sorted(stats['status_codes']):
        print("{}: {}".format(status_code, stats['status_codes'][status_code]))


if __name__ == "__main__":
    import sys

    lineno = 0
    stats = {'fsize': 0, 'status_codes': {}}

    try:
        for line in sys.stdin:
            lineno += 1
            line = line.split()
            file_size, status_code = int(line[-1]), line[-2]
            stats['fsize'] += file_size
            if not status_code in stats['status_codes']:
                stats['status_codes'][status_code] = 0
            stats['status_codes'][status_code] += 1
            if lineno == 10:
                display_stats(stats)
                lineno = 0
    except KeyboardInterrupt:
        display_stats(stats)
        raise
