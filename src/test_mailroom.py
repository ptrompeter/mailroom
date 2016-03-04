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

def test_getname():
	from mailroom import get_name
	name = 'Mike Kang Harrison'
	assert type(get_name(name)) == tuple
	assert len(get_name(name)) == 2