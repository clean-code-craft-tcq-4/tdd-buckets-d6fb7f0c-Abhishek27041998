from detect_range_and_count_readings import detect_range_and_count_readings, reset_values


def test_2_inputs_numbers():
    inputs = [4, 5]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[0][(4, 5)] == 2


def test_1_input_number():
    inputs = [1]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[0][(1, 1)] == 1


def test_reset_values():
    inputs = [5, 3, 2]
    index= 2

    start, end , num = reset_values(inputs, index)

    assert start == 2
    assert end == 2
    assert num == 1




