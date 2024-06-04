#!/usr/bin/env python3
import sys


def reducer():
    current_node = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        #If the line is empty or consists of whitespace characters, the condition evaluates to True.
        if not line:
            continue

        node_id, count = line.split()
        print(f"{node_id} {count}")



if __name__ == "__main__":
    reducer()