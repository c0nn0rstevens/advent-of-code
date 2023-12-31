"""
This module runs the AoC implementation multiple times to get a
representative sample of its performance.
"""
from time import time
import subprocess


def benchmark(runner: str, program: str, n: int) -> list[float]:

    durations: list[float] = []
    for _ in range(0, n):
        start = time()
        try:
            result = subprocess.run([runner, program])

        except subprocess.SubprocessError as err:
            print(
                f"Unable to run 'program' successfully."
                f"Result: {result}, Error: {err}."
            )

        end = time()
        duration = end - start
        durations.append(duration)

    return durations
