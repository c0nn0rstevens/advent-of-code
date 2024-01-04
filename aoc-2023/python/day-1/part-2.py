
# List of digits for comparison.
DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

FIRST_LETTERS = {'o', 't', 'f', 's', 'e', 'n'}

LAST_LETTERS = {'e', 'o', 'r', 'x', 'n', 't'}

NUMBER_WORDS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_calibration_value(line: str, reversed: bool = False) -> int:

    char_list = []
    if reversed:
        line = line[::-1]  # Reverse order of string.

    for char in line:

        if char == '\n':
            continue

        elif char in DIGITS:
            return int(char)

        elif reversed:
            char_list.insert(0, char)

        else:
            char_list.append(char)

        if len(char_list) > 2:
            print(char_list)
            word = ''.join(map(str, char_list))
            for number_word in NUMBER_WORDS.keys():
                word_start_index = word.find(number_word)
                if word_start_index != -1:
                    return int(NUMBER_WORDS[number_word])

        else:
            continue


def main():

    # Read input file and save separate lines into a list.
    with open('input.txt') as f:
        lines = []
        for line in f:
            lines.append(line)

    calibration_values = []

    for line in lines:
        calibration_value = (
            get_calibration_value(line)
            + get_calibration_value(line, reversed=True)
        )
        calibration_values.append(calibration_value)
    print(sum(calibration_values))
    return 0


if __name__ == "__main__":
    main()
