from A2D_converter import *


def test_get_relevant_config_12_bit():
    config = get_relevant_config(12)

    assert config["lower_limit_in_bit"] == 0
    assert config["lower_limit_amps"] == 0
    assert config["upper_limit_in_bit"] == 4094
    assert config["upper_limit_amps"] == 10


def test_convert_value_to_digital_12_bit():
    assert convert_value_to_digital(1146, 4094, 10) == 3
    assert convert_value_to_digital(4094, 4094, 10) == 10
    assert convert_value_to_digital(0, 4094, 10) == 0
    assert convert_value_to_digital(2050, 4094, 10) == 5


def test_is_value_in_range_12_bit():
    assert is_value_in_range(0, 0, 4094) == True
    assert is_value_in_range(4094, 0, 4094) == True
    assert is_value_in_range(4095, 0, 4094) == False
    assert is_value_in_range(20, 0, 4094) == True


def test_a2d_converter_12_bit():
    assert a2d_converter([0, 4094, 4095, 2050], 12) == [0, 10, 5]
    assert a2d_converter([4096, 10000, -1, -100, 44444], 12) == []
    assert a2d_converter([1000, 1000, 1000], 12) == [2, 2, 2]
