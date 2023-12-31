"""
This module standardises the benchmarking of AoC solutions, records the results
and automatically generates the Markdown code for documenting the results of a
given solution.
"""

import sys
from benchmarker import benchmark


def main():
    """ Runs the benchmark. """
    testee = sys.argv[1]
    runner = sys.argv[2]
    n = int(sys.argv[3])
    duration = benchmark(runner, testee, n)
    print(duration)


if __name__ == "__main__":
    main()
