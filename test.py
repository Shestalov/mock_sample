import unittest
from main import func, base_func
from unittest.mock import MagicMock, patch

mock_1 = MagicMock(return_value=8)


def new_func():
    return 8


class TestFunc(unittest.TestCase):
    a1 = func(1, 2)
    a2 = func(2, 3)

    def test_func_1(self):
        self.assertEqual(8, func(self.a1, self.a2))

    def test_func_2(self):
        self.assertEqual(8, func(self.a1, self.a2))

    # changing by decorator origin_func -> mock_1/new_func

    @patch('main.original', new_func)
    def test_mock(self):
        self.assertEqual(8, base_func())

    @patch('main.original', mock_1)
    def test_mock_2(self):
        self.assertEqual(8, base_func())
        mock_1.assert_called_with(a1=2)
