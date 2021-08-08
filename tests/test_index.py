import unittest

class TestSample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ok(self):
        self.assertEqual(3, 3)
    
    @unittest.skip("demonstrating skipping")
    def test_wrong(self):
        self.assertEqual(3, 4)


if __name__ == "__main__":
    unittest.main()
