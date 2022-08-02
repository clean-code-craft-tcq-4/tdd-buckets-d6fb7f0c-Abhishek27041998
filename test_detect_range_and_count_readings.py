from detect_range_and_count_readings import detect_range_and_count_readings


def test_2_inputs_numbers():
    inputs = [4, 5]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[0][(4, 5)] == 2

test_2_inputs_numbers()


