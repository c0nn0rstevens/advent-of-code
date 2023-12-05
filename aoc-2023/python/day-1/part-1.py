# List of digits for comparison.
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Read input file and save separate lines into a list.
with open('input.txt') as f:
    lines = []
    for line in f:
        lines.append(line)

calibration_values = []

for line in lines:
    # print('Line: ' + line)
    # Iterate over each character in the string.
    for char in line:
        if char in DIGITS:
            first_digit = char
            # print('First number: ' + first_digit)
            break
        else:
            continue

    for char in reversed(line):
        if char in DIGITS:
            second_digit = char
            # print('Second number: ' + second_digit + '\n')
            break
        else:
            continue

    calibration_values.append(int(first_digit + second_digit))

calibration_sum = sum(calibration_values)
print(calibration_sum)
