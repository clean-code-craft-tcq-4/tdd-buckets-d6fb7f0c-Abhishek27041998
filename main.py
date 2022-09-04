from detect_range_and_count_readings import detect_range_and_count_readings
from display_ranges import display_range
from A2D_converter import a2d_converter


def main():
    inputs = [0, 10, 121, 4094, 1024, 2048, 4095, 5000]

    bit = 12

    digital_values = a2d_converter(inputs, bit)

    result = detect_range_and_count_readings(digital_values)

    display_range(result)


if __name__ == '__main__':
    main()