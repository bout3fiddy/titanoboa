import pytest

import boa

source_code = """
A: constant(uint256) = 10

@external
def __init__():
    pass
"""


@pytest.fixture(scope="module")
def contract():
    c = boa.loads(source_code)
    return c


def test_get_constant_var(contract):
    A = contract.eval("A")
    assert A == 10
