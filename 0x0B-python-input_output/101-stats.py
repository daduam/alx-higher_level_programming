#!/usr/bin/python3
"""101-stats"""


def display_stats(fsize, status_codes):
    """Print stats so far"""
    print("File size: {}".format(fsize))
    for k, v in sorted(status_codes.items()):
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    import sys

    lineno = 0
    fsize = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            lineno += 1
            line = line.split()
            try:
                file_size, status_code = int(line[-1]), line[-2]
                fsize += file_size
                if status_code not in status_codes:
                    status_codes[status_code] = 0
                status_codes[status_code] += 1
                if lineno == 10:
                    display_stats(fsize, status_codes)
                    lineno = 0
            except (IndexError, ValueError):
                pass
        display_stats(fsize, status_codes)
    except KeyboardInterrupt:
        display_stats(fsize, status_codes)
        raise
