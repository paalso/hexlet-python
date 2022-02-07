from hexlet_pytest.without import without

def test_without():
    assert without([2, 1, 2, 3, 4], 2, 3) == [1, 4]

def test_without_no_change():
    assert without([2, 1, 2, 3, 4], 5, 6) == [2, 1, 2, 3, 4]

def test_without_empty_coll():
    assert without([], 1, 2) == []

def test_without_all_empty():
    assert without([]) == []
