import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):             #NameTestCase名字可以随意取，但它继承unittest.TestCase类
    """测试name_function.py"""

    def test_first_last_name(self):        #所有test_打头的方法都将自动运行，所以测试的方法都必须以test_打头
        """能够正确处理像Janis Joplin这样的名字吗"""
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_middle_last_name(self):
        """能够正确处理像wang xin hao这样的名字吗"""
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()
