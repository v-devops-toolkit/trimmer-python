import pytest

from DataTransformer import *

test_items = [
    [[], []],
    [['one'], ['one']],
    [['one '], ['one']],
    [['one\n'], ['one']],
    [['one\r'], ['one']],
    [['one \r \n \r \n'], ['one']],
    [['one \r \n \r \n'], ['one']],
    [['a ', 'b \r', 'c \n'], ['a', 'b', 'c']],
]


@pytest.fixture(params=test_items)
def next_item(request):
    return request.param


def test_data_transformer(next_item):
    transformer = DataTransformer()
    result = transformer.transform(next_item[0])
    assert result == next_item[1]
