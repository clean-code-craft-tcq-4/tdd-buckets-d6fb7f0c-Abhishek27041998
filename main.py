from display_ranges import display_range
from A2D_converter import a2d_convert_and_detect_range


def main():
    # inputs = [0, 10, 121, 4094, 1024, 2048, 4095, 5000]

    inputs = [0, 511, 700, 1022]

    bit = 10

    # digital_values = a2d_converter(inputs, bit)
    #
    # result = detect_range_and_count_readings(digital_values)

    result = a2d_convert_and_detect_range(inputs, bit)

    display_range(result)


if __name__ == '__main__':
    main()