# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import src.display_number as module_0


def test_case_0():
    int_0 = -115
    none_type_0 = None
    number_display_0 = module_0.NumberDisplay(int_0, none_type_0)
    var_0 = number_display_0.clone()
    var_1 = var_0.str()
    assert var_1 == "0-115"


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -166
    bool_0 = True
    dict_0 = {int_0: int_0, int_0: int_0, bool_0: int_0}
    number_display_0 = module_0.NumberDisplay(dict_0, dict_0)
    float_0 = 513.06382
    number_display_1 = module_0.NumberDisplay(float_0, float_0)
    var_0 = number_display_1.str()
    assert var_0 == "513.06382"
    var_1 = number_display_1.reset()
    assert number_display_1.value == 0
    var_2 = number_display_1.reset()
    var_3 = number_display_1.reset()
    var_4 = number_display_1.clone()
    assert var_4.value == 0
    var_5 = number_display_1.invariant()
    assert var_5 is True
    var_5.str()


def test_case_2():
    str_0 = "+9Kg_Y@n\r'.Zn>A"
    number_display_0 = module_0.NumberDisplay(str_0, str_0)


def test_case_3():
    bool_0 = True
    number_display_0 = module_0.NumberDisplay(bool_0, bool_0)
    var_0 = number_display_0.increase()
    assert var_0 is True
    assert number_display_0.value == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    number_display_0 = module_0.NumberDisplay(tuple_0, tuple_0)
    var_0 = number_display_0.reset()
    assert number_display_0.value == 0
    var_0.str()


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    number_display_0 = module_0.NumberDisplay(none_type_0, none_type_0)
    var_0 = number_display_0.clone()
    var_0.invariant()
