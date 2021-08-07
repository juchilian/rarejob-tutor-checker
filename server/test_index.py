import unittest


class TestSample(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_ok(self):
        self.assertEqual("1", "1")
    
    def test_wrong(self):
        self.assertEqual("1", "2")


if __name__ == "__main__":
    unittest.main()
