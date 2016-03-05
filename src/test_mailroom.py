# _*_ coding: utf-8 _*_

data = {('Roberts', 'John'): [20.00, 15.00],
        ('Edwards', 'Mary'): [5.00, 30.50],
        ('asdf', 'brice'): [2.35],
        }


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

    