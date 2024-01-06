import os


def read_file_to_list(rel_path: str) -> list[str]:

    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, rel_path)
    try:
        # Read input file and save separate lines into a list.
        with open(abs_file_path, 'r') as f:
            lines = []
            for line in f:
                lines.append(line)

        return lines

    except FileNotFoundError as e:
        print(f"File not found: {e}")
