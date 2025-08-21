import pytest

def test_file_example():
  input_val=5
  assert input_val*9==45
@pytest.mark.setexample
def test_file_example3():
  input_val=6
  assert input_val*9==45