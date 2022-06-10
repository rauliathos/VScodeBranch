import pytest
from program import vowels


def test_no_vowels():
    assert vowels.vowels("ctrsr")==0

def test_one():
    assert vowels.vowels("car")==1

def test_many():
    assert vowels.vowels("aaeeii ouou")==10