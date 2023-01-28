import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff("asdfas")
        self.assertIsInstance(result, ValueError)

unittest.main()


