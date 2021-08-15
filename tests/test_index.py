import unittest
from server import RarejobBooker
from datetime import datetime, timedelta
from pytz import timezone

class TestSample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_timezone(self):
        tomorrow = datetime.now(timezone('Asia/Tokyo')) + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%Y/%m/%d')
        print(tomorrow_str)
        



if __name__ == "__main__":
    unittest.main()
