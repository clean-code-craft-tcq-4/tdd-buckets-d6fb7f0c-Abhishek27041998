from detect_range_and_count_readings import detect_range_and_count_readings, reset_values, check_if_inputs_valid


def test_2_inputs_numbers():
    inputs = [4, 5]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[(4, 5)] == 2


def test_1_input_number():
    inputs = [1]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[(1, 1)] == 1


def test_reset_values():
    inputs = [5, 3, 2]
    index= 2

    start, end , num = reset_values(inputs, index)

    assert start == 2
    assert end == 2
    assert num == 1


def test_many_values():
    inputs = [3, 3, 5, 4, 10, 11, 12]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[(3, 5)] == 4
    assert outputs[(10, 12)] == 3


def test_no_values():
    inputs = []

    outputs = detect_range_and_count_readings(inputs)

    assert outputs == {}


def test_check_if_inputs_valid():
    assert check_if_inputs_valid([]) == False
    assert check_if_inputs_valid(None) == False
    assert check_if_inputs_valid([1,2]) == True
