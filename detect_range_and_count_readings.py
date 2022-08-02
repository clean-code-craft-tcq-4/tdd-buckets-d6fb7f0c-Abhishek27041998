from typing import List, Dict, Tuple


def detect_range_and_count_readings(inputs: List[int]):
    # Output variable to store list of ranges along with number of readings
    output: List[Dict[Tuple[int, int], int]] = []

    # Sort inputs
    inputs.sort()

    # Define placeholders for range identification and count
    start_range = inputs[0]
    end_range = inputs[0]
    num = 1
    reset = False
    for i in range(1, len(inputs)):
        if reset:
            start_range = inputs[i]
            end_range = inputs[i]
            num = 1

        if inputs[i] == end_range + 1:
            end_range = inputs[i]
            num += 1
            continue
        else:
            key = (start_range, end_range)
            output.append({key: num})
            reset = True

    key = (start_range, end_range)
    output.append({key: num})

    return output




