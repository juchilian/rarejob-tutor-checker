import unittest


class TestSample(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_sample(self):
        self.assertEqual("1", "1")


if __name__ == "__main__":
    unittest.main()
