#!/usr/bin/env python3

# This is a sample input validator, written in Python 3.

# Please refer to the comments in README.md for a description of the syntax it
# is validating. Then, change it as you need.

import sys
import re

dims_line = sys.stdin.readline().strip()
print(repr(dims_line))
assert re.match(
    "^[1-9][0-9]* [1-9][0-9]*$", dims_line
), "First line does not match format 'R C'."
inp = dims_line.split(" ")
r, c = int(inp[0]), int(inp[1])
assert 1 <= r <= (2**32) - 1, f"Rows value {r} is not between 1 and 2^32 - 1."
assert 1 <= c <= (2**32) - 1, f"Columns value {c} is not between 1 and 2^32 - 1."

for i in range(r):
    case_line = sys.stdin.readline()

    if case_line == "":
        raise AssertionError(
            f"Expected {r} row{"s" if r > 1 else ""} of matrix data, but found only {i}."
        )

    if i == r - 1:
        assert not case_line.endswith(
            "\n"
        ), "There should be no more lines after the last line of expected input."

    x = case_line.split(" ")

    assert len(x) == c

    for num in x:
        assert re.match(
            r"^-?([1-9][0-9]*)$", num
        ), f"Matrix value '{num}' is not an integer."
        assert (int(num) == -1) or (
            1 <= int(num) <= 10000
        ), f"'{num}' is either not -1, or not between 1 and 10000."

# ensure no extra input
assert (
    sys.stdin.readline() == ""
), "There should be no more lines after the last line of expected input."

# if we get here, all is well; use exit code 42.
sys.exit(42)
