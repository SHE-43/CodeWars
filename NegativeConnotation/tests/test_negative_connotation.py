import pytest
from negative_connotation_script import connotation as cn

list_of_tests =     [   
        ("A big brown fox caught a bad bunny", True),
        ("Xylophones can obtain Xenon.", False),
        ("CHOCOLATE MAKES A GREAT SNACK", True),
        ("", True),
        (" ", True),
        ("a z", True),
        ("a zz zz", False)
                    ] 

@pytest.mark.parametrize(
    'str_input, bool_output',
    list_of_tests )
def test_2(str_input, bool_output):
    assert cn(str_input) == bool_output





