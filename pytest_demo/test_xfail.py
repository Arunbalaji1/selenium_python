import pytest

def test_exe():
  input_val=3
  assert input_val*6==18
@pytest.mark.xfail
def test_exe1():
  input_val=3
  assert input_val*5==18
@pytest.mark.skip  
def test_exe2():
  input_val=3
  assert input_val*8==18