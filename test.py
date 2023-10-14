import unittest
import datetime
from unittest.mock import patch
from screendown import ScreenshotDownload
from freezegun import freeze_time

class TestScreenshotDownload(unittest.TestCase):
    

    @freeze_time('2023-10-14')
    @patch('screendown.os.listdir')
    def test_get_dir_name_no_same_date(self, mock_oslistdir):
        mock_oslistdir.return_value = ['2022-10-14']
        obj = ScreenshotDownload('')
        self.assertEqual(obj.get_dir_name(), '2023-10-14')
    
    @freeze_time('2023-10-14')
    @patch('screendown.os.listdir')
    def test_get_dir_name_single_same_date(self, mock_oslistdir):
        mock_oslistdir.return_value = ['2023-10-14']
        obj = ScreenshotDownload('')
        self.assertEqual(obj.get_dir_name(), '2023-10-14_1')
        
    @freeze_time('2023-10-14')
    @patch('screendown.os.listdir')
    def test_get_dir_name_multiple_same_date(self, mock_oslistdir):
        mock_oslistdir.return_value = [
            '2023-10-14_1', 
            '2023-10-14', 
            '2023-10-14_3', 
            '2023-10-14_xyz'
            ]
        obj = ScreenshotDownload('')
        self.assertEqual(obj.get_dir_name(), '2023-10-14_4')
        
if __name__ == '__main__':
    unittest.main()