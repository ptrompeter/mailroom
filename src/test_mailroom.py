# _*_ coding: utf-8 _*_

import pdb
import pytest
data = {('Roberts', 'John'): [20.00, 15.00],
        ('Edwards', 'Mary'): [5.00, 30.50],
        ('asdf', 'brice'): [2.35],
        }

NAME_CHECK_DATA = ['Bob Smith, Bob Smith', 'Bob Joe Smith, Bob Joe Smith', '333, None']


DONATION_CHECK_DATA = ['33, 33', '45.52, 45.52', 'Buster, None']


MENU_CHECK_DATA = ['1, 1', '2, 2', 'q, q', 'quit, quit', 'list, None']


@pytest.mark.parametrize('input, result', NAME_CHECK_DATA)
def test_check_data(input, result):
    from mailroom import name_check
    assert name_check(input) == result


@pytest.mark.parametrize('input, result', DONATION_CHECK_DATA)
def test_check_data(input, result):
    """Test check_"""
    from mailroom import donation_check
    assert donation_check(input) == result


@pytest.mark.parametrize('input, result', MENU_CHECK_DATA)
def test_check_data(input, result):
    """Test menu_check function"""
    from mailroom import menu_check
    assert menu_check(input) == result


def test_sortbydonation():
    """Test Sort By donation function in mailroom"""
    from mailroom import sort_by_donation
    assert type(sort_by_donation(data)) == list
    assert len(sort_by_donation(data)) == 3
    data2 = sort_by_donation(data)
    for i in range(len(data2) - 1):
        assert data2[i] > data2[i + 1]  or len(data2) < 2


def test_getname():
    """Test Get Name function in mailroom"""
    from mailroom import get_name
    name = 'Mike Kang Harrison'
    assert type(get_name(name)) == tuple
    assert len(get_name(name)) == 2


def test_menuprompot():
    """ Test menu prompt"""
    from mailroom import menu_prompt
    assert menu_prompt('2') == '2'


def test_getdonation():
    """Test Get Donation"""
    from mailroom import get_donation
    assert get_donation('2') == 2.0

    