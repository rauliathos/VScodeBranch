import pytest
from program import factorial

def test_fact_zero():
    assert factorial.fact(0)==1

def test_fact_number7():
    assert factorial.fact(7)==5040
    
    
def test_fact_number3():
     assert factorial.fact(3)==6

#def test_fact_negative():
 #   assert factorial.fact(-3)==-6