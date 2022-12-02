import pytest

import boa

source_code = """
A: public(constant(uint256)) = 10
B: constant(uint256) = 20

@external
def __init__():
    pass

@external
def show() -> uint256:
    return B

@external
@payable
def show_payable() -> uint256:
    return B
"""


@pytest.fixture(scope="module")
def contract():
    c = boa.loads(source_code)
    return c


def test_show(contract):
    assert contract.show() == 20


def test_show_payable(contract):
    assert contract.show_payable() == 20


def test_get_public_constant_var(contract):
    A = contract.eval("A")
    assert A == 10


def test_get_constant_var(contract):
    A = contract.eval("B")
    assert A == 20
