import unittest,logging
logging.basicConfig(level=logging.INFO)

from myDict import Dict

class TestDIct(unittest.TestCase):

    def setUp(self):
        print("setUP")
        return

    def tearDown(self):
        print("tearDown")
        return

    # 测试初始化方法
    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))


    def test_key(self):
        d = Dict()
        # 这个语句不是取值，而是设值，表示我往d里放了一个值，key是'key',值是'value'
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

        # 如果看不懂上面的。我这么写。你应该就懂了
        d['a']=4
        self.assertEqual(d.a, 4)


if __name__ == '__main__':
    unittest.main()