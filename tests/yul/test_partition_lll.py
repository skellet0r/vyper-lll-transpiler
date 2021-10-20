import pytest
import vyper
from vyper.old_codegen.lll_node import LLLnode

from transpiler.yul import YulObject


@pytest.fixture(scope="module")
def vyper_lll():
    code = """
@external
def foo():
    pass
"""
    return vyper.compile_code(code, output_formats=["ir"])["ir"]


def test_partition(vyper_lll):
    root_lll, sub_lll = YulObject.partition_lll(vyper_lll)

    # check root partition is an LLLnode instance
    assert isinstance(root_lll, LLLnode)
    # and the original does not equal are new root
    assert root_lll != vyper_lll

    # check all sub lll nodes are instances of LLLnode
    for v in sub_lll.values():
        assert isinstance(v, LLLnode)
