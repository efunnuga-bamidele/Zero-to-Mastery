import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('about to test a function')
        return super().setUp()

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff_2(self):
        test_param = 'string'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stpp_4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self) -> None:
        print('cleaning up')
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()