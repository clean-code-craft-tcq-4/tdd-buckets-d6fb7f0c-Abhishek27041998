from detect_range_and_count_readings import detect_range_and_count_readings
from display_ranges import display_range


def main():
    inputs = [3, 3, 5, 4, 10, 11, 12]

    result = detect_range_and_count_readings(inputs)

    display_range(result)


if __name__ == '__main__':
    main()