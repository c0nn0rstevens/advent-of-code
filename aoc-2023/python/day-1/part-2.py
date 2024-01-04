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

    line = line.rstrip()
    char_list = []
    if reversed:
        line = line[::-1]  # Reverse order of string.

    for char in line:

        if char in NUMBER_WORDS.values():

            try:

                return int(char)

            except ValueError as e:
                print(f"Cannot convert {char} to int. Error: {e}")
                return

        char_list.insert(0, char) if reversed else char_list.append(char)

        if len(char_list) > 2:
            # print(f"{'Second: ' if reversed else 'First: '} \n {char_list}")
            word = ''.join(map(str, char_list))
            for number_word in NUMBER_WORDS.keys():
                word_start_index = word.find(number_word)
                if word_start_index != -1:
                    try:
                        int(NUMBER_WORDS[number_word])

                    except ValueError as e:
                        print(f"Cannot convert {char} to int. Error: {e}")
                        return -1
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
        print("Line: " + line)
        calibration_value_1 = get_calibration_value(line)
        calibration_value_2 = get_calibration_value(line, reversed=True)
        print(f"First value: {calibration_value_1}")
        print(f"Second value: {calibration_value_2}")
        calibration_values.append(calibration_value_1 + calibration_value_2)
    print(sum(calibration_values))
    return 0


if __name__ == "__main__":
    main()
