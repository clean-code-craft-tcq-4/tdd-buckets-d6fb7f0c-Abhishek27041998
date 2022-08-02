
def test_2_inputs_numbers():
    inputs = [4, 5]

    outputs = detect_range_and_count_readings(inputs)

    assert outputs[0][(4, 5)] == 2

