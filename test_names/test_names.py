from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Sally Sue','Brown') == 'Brown; Sally Sue'
    assert make_full_name('','Washington') == 'Washington; '
    assert make_full_name('Trent','') == '; Trent'
    assert make_full_name('Takota','Johnson') == 'Johnson; Takota'
    assert make_full_name('Sam','Thompson-Graves') == 'Thompson-Graves; Sam'

def test_extract_family_name():
    assert extract_family_name('Johnson; Takota') == 'Johnson'
    assert extract_family_name('Brown; Sally Sue') == 'Brown'
    assert extract_family_name('Thompson-Graves; Sam') == 'Thompson-Graves'

def test_extract_given_name():
    assert extract_given_name('Johnson; Takota') == 'Takota'
    assert extract_given_name('Brown; Sally Sue') == 'Sally Sue'
    assert extract_given_name('Thompson-Graves; Sam') == 'Sam'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])