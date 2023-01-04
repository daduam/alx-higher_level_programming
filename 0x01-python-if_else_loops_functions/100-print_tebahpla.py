#!/usr/bin/python3
for i in range(ord("z"), ord("a") - 1, -1):
    c = i
    if i % 2 == 1:
        c = c - ord("a") + ord("A")
    print(f"{c:c}", end="")
