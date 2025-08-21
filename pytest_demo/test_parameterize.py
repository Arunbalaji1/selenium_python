import pytest

@pytest.mark.parametrize("input,output",[(2,10),(3,15),(4,202),(5,255)])
def test_allval(input,output):
  assert input*5==output
