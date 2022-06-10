from program import app

def test_func():
    assert app.func(4) ==8
    assert app.func(3) ==6
    assert app.func(10) ==20
    assert app.func(9) ==18
