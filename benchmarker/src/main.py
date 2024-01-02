"""
This module standardises the benchmarking of AoC solutions, records the results
and automatically generates the Markdown code for documenting the results of a
given solution.
"""

import sys
from benchmarker import benchmark
import statistics
import datetime
from py_markdown_table.markdown_table import markdown_table

PRECISION = 5


def main():
    """ Runs the benchmark. """
    testee = sys.argv[1]
    runner = sys.argv[2]
    n = int(sys.argv[3])
    durations = benchmark(runner, testee, n)
    lower_quartile = statistics.median_low(durations)
    minimum = min(durations)
    maximum = max(durations)
    mean = statistics.mean(durations)
    median = statistics.median(durations)
    mode = statistics.mode(durations)
    upper_quartile = statistics.median_high(durations)
    std_dev = statistics.stdev(durations)
    today = datetime.date.today().strftime("%d/%m/%Y")
    data = [
        {
            "mean": f'{mean:.{PRECISION}}',
            "mode": f'{mode:.{PRECISION}}',
            "min": f'{minimum:.{PRECISION}}',
            "q1": f'{lower_quartile:.{PRECISION}}',
            "median": f'{median:.{PRECISION}}',
            "q3": f'{upper_quartile:.{PRECISION}}',
            "max": f'{maximum:.{PRECISION}}',
            "std dev": f'{std_dev:.{PRECISION}}'
        }
    ]
    md_table = markdown_table(data).set_params(row_sep='markdown').get_markdown()
    # Get rid of codeblock backticks.
    md_table = md_table[3:-3]
    markdown_template = f"""Date: {today}{md_table}"""
    print(markdown_template)


if __name__ == "__main__":
    main()
