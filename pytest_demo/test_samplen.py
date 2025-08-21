import pytest
""" import pytest
def f():
  raise SystemExit(1)
def test_mytest():
  with pytest.raises(SystemExit):
    f()
test_mytest() """

def test_file_exmaple():
    input_value = 5
    assert input_value*6 == 25
