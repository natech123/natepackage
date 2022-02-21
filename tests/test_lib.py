from natepackage.lib import try_me

def test_try_me():
    assert type(try_me(23,6)) == str
