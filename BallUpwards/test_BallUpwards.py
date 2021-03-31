from BallUpwards import max_ball
import pytest

# 10 test inputs/outputs.
test_input_outputs = [
    ((37), 10),((45), 13), ((99), 28), ((85), 24), ((136), 39), 
    ((52), 15), ((16), 5), ((127), 36), ((137), 39), ((14), 4)
    ]


@pytest.mark.parametrize("i , eo", test_input_outputs)
def test_max_ball(i, eo):
    assert max_ball(i) == eo;



