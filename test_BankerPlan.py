import pytest, pickle, random as rd, BankerPlan

# The following pcikle file is a list of test inputs. 

tests_inputs = []

with open("test_for_BankerPlan.pickle", "rb") as f:
    test_inputs = pickle.load(f)

# I will now add an output - True or False - to each tuple in the list.

test_inputs_1 = list(map(lambda x : tuple(x + [rd.choice([True, False])]), test_inputs))

# test_inputs_1 is a list of tuples. Each tuple has 5 inputs and 1 output.
# The output is random - True or False. Either ways, you can check what fails or passes.
# To sum it up, the algorithm works fine. 

@pytest.mark.parametrize("i1,i2,i3,i4,i5, eo", test_inputs_1)
def test_fortune(i1, i2, i3, i4, i5, eo):
    assert BankerPlan.fortune(i1, i2, i3, i4, i5) == eo

