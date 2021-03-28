import divisibility_by_13_mod, pytest

@pytest.mark.parametrize(
    "i, eo", [(8529, 79),(85299258, 31), (5634, 57), (1111111111, 71), (987654321, 30)])
def test_thirt(i, eo):    
    assert divisibility_by_13_mod.thirt(i) == eo

# Use : pytest -v
