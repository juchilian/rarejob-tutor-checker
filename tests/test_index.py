import unittest
from server.index import Sample

class TestSample(unittest.TestCase):
    def setUp(self):
        self.testSample = Sample(1,2)
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_ok(self):
        self.assertEqual(self.testSample.addition(), 3)
    
    def test_wrong(self):
        self.assertEqual(self.testSample.addition(), 4)


if __name__ == "__main__":
    unittest.main()
