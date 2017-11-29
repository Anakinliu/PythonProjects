import unittest
from book.test.formatted_name import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """
    测试formatted_name.pyd的类
    """

    def test_first_last_name(self):
        """测试是否能处理像Janis Joplin这样的姓名"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, '')


unittest.main()
