# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

from sample import sample_code

def test_success():
    assert True

class TestSample(unittest.TestCase):

    def setUp(self):
        self.hello_message="Hello Pyohio"

    def test_prints(self):
        output=sample_code.hello_Milan()
        assert (output==self.hello_message)