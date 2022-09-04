from typing import List, Dict, Tuple


def reset_values(inputs, index):
    start = inputs[index]
    end = inputs[index]
    num = 1
    return start, end, num


def check_if_inputs_valid(inputs: List[int]):
    if inputs is None or len(inputs) == 0:
        return False

    return True


def detect_range_and_count_readings(inputs: List[int]):
    # Output variable to store list of ranges along with number of readings
    output: Dict[Tuple[int, int], int] = {}

    # If inputs lenght is 0 or is empty return {}
    if not check_if_inputs_valid(inputs):
        return output

    # Sort inputs
    inputs.sort()

    # Define placeholders for range identification and count
    start_range, end_range, num = reset_values(inputs, 0)

    for i in range(1, len(inputs)):
        eval = (inputs[i] == end_range + 1) | (inputs[i] == end_range)

        if eval:
            end_range = inputs[i]
            num += 1
            continue
        else:
            key = (start_range, end_range)
            output[key] = num
            start_range, end_range, num = reset_values(inputs, i)

    key = (start_range, end_range)
    output[key] = num

    return output




