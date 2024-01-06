"""
This module runs the AoC implementation multiple times to get a
representative sample of its performance.
"""
from time import time
import subprocess


def benchmark(runner: str, program: str, n: int) -> list[float]:
    """Runs program, using runner, n times and returns a list of durations.

    Args:
        runner (str): The binary to call to run the program.
        program (str): The name of file in to run.
        n (int): The number of times to run the program.

    Returns:
        list[float]: List of n run durations for each run of the program.
    """

    durations: list[float] = []
    for _ in range(0, n):
        start = time()
        try:
            result = subprocess.run([runner, program])

        except subprocess.SubprocessError as err:
            print(
                f"Unable to run {program} successfully."
                f"Result: {result}, Error: {err}."
            )

        end = time()
        duration = end - start
        durations.append(duration)

    return durations
