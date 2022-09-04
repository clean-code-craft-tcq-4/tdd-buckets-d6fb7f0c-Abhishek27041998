from typing import List
from read_config import parse_config
from detect_range_and_count_readings import detect_range_and_count_readings


def a2d_convert_and_detect_range(inputs: List[int], bit: int):
    digital_values = a2d_converter(inputs, bit)

    ranges_count = detect_range_and_count_readings(digital_values)

    return ranges_count


def a2d_converter(input_arr: List[int], bit: int):
    config = get_relevant_config(bit)

    digital_array = []

    for value in input_arr:
        if is_value_in_range(value, config["lower_limit_in_bit"], config["upper_limit_in_bit"]):
            digital_value = convert_value_to_digital(value, config["upper_limit_in_bit"], config["upper_limit_amps"])

            digital_array.append(digital_value)

    return digital_array


def get_relevant_config(bit: int):
    config = parse_config("a2d_config.yml")

    key = f"{bit}_bit"

    return config["Sensor"][key]


def convert_value_to_digital(value: int, upper_limit_bits: int, upper_limit_amps: int):
    digital_val = upper_limit_amps * (value / upper_limit_bits)

    return round(digital_val)


def is_value_in_range(value: int, lower_limit: int, upper_limit: int):
    if lower_limit <= value <= upper_limit:
        return True
    else:
        return False
