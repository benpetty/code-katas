import pytest
from .prefill_an_array import prefill


@pytest.mark.parametrize('param1, param2, answer', [
    [3, 1, [1, 1, 1]],
    [2, 'abc', ['abc', 'abc']],
    ['1', 1, [1]],
    [3, prefill(2, '2d'), [['2d', '2d'], ['2d', '2d'], ['2d', '2d']]],
])
def test_prefill(param1, param2, answer):
    from .prefill_an_array import prefill
    assert prefill(param1, param2) == answer

@pytest.mark.parametrize('param1, param2, message', [
    ['xyz', '1', 'xyz is invalid'],
    [None, None, 'None is invalid'],
])
def test_prefill_exception(param1, param2, message):
    from .prefill_an_array import prefill
    with pytest.raises(TypeError, match=message):
        prefill(param1, param2)
