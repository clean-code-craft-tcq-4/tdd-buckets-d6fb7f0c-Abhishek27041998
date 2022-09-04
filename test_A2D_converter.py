from A2D_converter import *


def test_get_relevant_config_12_bit():
    config = get_relevant_config(12)

    assert config["lower_limit_in_bit"] == 0
    assert config["lower_limit_amps"] == 0
    assert config["upper_limit_in_bit"] == 4094
    assert config["upper_limit_amps"] == 10


def test_convert_value_to_digital_12_bit():
    assert convert_value_to_digital(1146, 4094, 10, 0, 0) == 3
    assert convert_value_to_digital(4094, 4094, 10, 0, 0) == 10
    assert convert_value_to_digital(0, 4094, 10, 0, 0) == 0
    assert convert_value_to_digital(2050, 4094, 10, 0, 0) == 5


def test_is_value_in_range_12_bit():
    assert is_value_in_range(0, 0, 4094) == True
    assert is_value_in_range(4094, 0, 4094) == True
    assert is_value_in_range(4095, 0, 4094) == False
    assert is_value_in_range(20, 0, 4094) == True


def test_a2d_converter_12_bit():
    assert a2d_converter([0, 4094, 4095, 2050], 12) == [0, 10, 5]
    assert a2d_converter([4096, 10000, -1, -100, 44444], 12) == []
    assert a2d_converter([1000, 1000, 1000], 12) == [2, 2, 2]


def test_a2d_convert_and_detect_range():
    assert a2d_convert_and_detect_range([0, 4094, 4095, 2050], 12) == {(0, 0): 1, (5, 5): 1, (10, 10): 1}
    assert a2d_convert_and_detect_range([4096, 10000, -1, -100, 44444], 12) == {}
    assert a2d_convert_and_detect_range([1000, 1000, 1000], 12) == {(2, 2): 3}

# 10 Bit testing


def test_get_relevant_config_10_bit():
    config = get_relevant_config(10)

    assert config["lower_limit_in_bit"] == 0
    assert config["lower_limit_amps"] == -15
    assert config["upper_limit_in_bit"] == 1022
    assert config["upper_limit_amps"] == 15


def test_convert_value_to_digital_10_bit():
    assert convert_value_to_digital(511, 1022, 15, 0, -15) == 0
    assert convert_value_to_digital(1022, 1022, 15, 0, -15) == 15
    assert convert_value_to_digital(0, 1022, 15, 0, -15) == -15
    assert convert_value_to_digital(700, 1022, 15, 0, -15) == 6


def test_a2d_converter_10_bit():
    assert a2d_converter([0, 511, 1022, 700], 10) == [-15, 0, 15, 6]
    assert a2d_converter([4096, 10000, -1, -100, 44444], 10) == []
    assert a2d_converter([1000, 1000, 1000], 10) == [14, 14, 14]


def test_a2d_convert_and_detect_range_10_bit():
    assert a2d_convert_and_detect_range([0, 511, 1022, 700], 10) == {(0, 0): 1, (6, 6): 1, (15, 15): 2}
    assert a2d_convert_and_detect_range([4096, 10000, -1, -100, 44444], 10) == {}
    assert a2d_convert_and_detect_range([1000, 1000, 1000], 10) == {(14, 14): 3}

