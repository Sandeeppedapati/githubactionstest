from src.operations import multiply,div


def test_multiply() :
    assert multiply(5,1) ==5
    assert multiply(5,0) ==0
    assert multiply(5,-10) == -50

def test_div() :
    assert div(5,1) ==5
    assert div(5,0) == "invalid input"
    assert div(10,2) == 5
    assert div(10,5) == 2