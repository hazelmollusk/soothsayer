"""Test fortune_file class"""
from vaticinator.libs import fortune_file as FF


def test_amodule():
    """Test amodule.hello()."""
    amodule.hello()


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    s = SM.SampleClass()
    assert s.true() is True


def test_sampleclass_false():
    """Test samplemodule SampleClass false classmethod."""
    assert SM.SampleClass.false() is False


def test_undoc_func():
    """Test the undocumented function."""
    SM.this_is_and_undocumented_function("some")
