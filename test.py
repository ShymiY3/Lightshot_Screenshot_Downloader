import unittest
import screendown
import os
from unittest.mock import patch, Mock, mock_open
from screendown import ScreenshotDownload as SSD
from freezegun import freeze_time


class TestScreenshotDownload(unittest.TestCase):
    
    def test_urls_attribute_creation_string(self):
        obj = SSD('https://example.com/')
        self.assertIsInstance(obj.urls, list)
        
    def test_urls_attribute_creation_iterable(self):
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        self.assertIsInstance(obj.urls, list)
    
    @freeze_time('2023-10-14')
    @patch('screendown.os.listdir')
    def test_get_dir_name_no_same_date(self, mock_oslistdir):
        mock_oslistdir.return_value = ['2022-10-14']
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        self.assertEqual(obj.get_dir_name(), '2023-10-14')
    
    @freeze_time('2023-10-14')
    @patch('screendown.os.listdir')
    def test_get_dir_name_single_same_date(self, mock_oslistdir):
        mock_oslistdir.return_value = ['2023-10-14']
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
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
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        self.assertEqual(obj.get_dir_name(), '2023-10-14_4')
    
    @patch('screendown.requests.get')
    def test_make_request_valid(self, mock_get):
        text = "<html><img id='screenshot-image', src='fake_image.png'></html>"
        mock_response = Mock(status_code = 200, text=text) 
        mock_get.return_value = mock_response
        
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        request = obj.make_request('https://example.com/')
        
        self.assertEqual(request, mock_response)
        
    @patch('screendown.requests.get')
    def test_make_request_error(self, mock_get):
        text = "<html><img id='screenshot-image', src='fake_image.png'></html>"
        mock_response = Mock(status_code = 400, text=text) 
        mock_get.return_value = mock_response
        
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
    
        with self.assertRaises(screendown.SSDownloadException):
            obj.make_request('https://example.com/')
    
    def test_scrape_image_valid(self):
        text = "<html><img id='screenshot-image', src='fake_image.png'></html>"
        img_source = 'fake_image.png'
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        img_return = obj.scrape_image(text)
        self.assertEqual(img_source, img_return)
        
    def test_scrape_image_error(self):
        text = "<html><img id='screenshot-image'></html>"
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        with self.assertRaises(screendown.SSDownloadException):
            obj.scrape_image(text)
            
    def test_fetch_image_sources_valid(self):
        images = ['fake_image.png', 'fake_image_1.png']
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        obj.make_request = Mock()
        obj.scrape_image = Mock()
        obj.scrape_image.side_effect = images
        img_sources = obj.fetch_image_sources()
        self.assertEqual(img_sources, images)
    
    def test_fetch_image_sources_error(self):
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        obj.make_request = Mock()
        obj.scrape_image = Mock()
        obj.scrape_image.side_effect = [screendown.SSDownloadException, 'fake_image.png']
        img_sources = obj.fetch_image_sources()
        self.assertEqual(img_sources, ['fake_image.png'])
    
    def test_save_image(self):
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        img_title = 'title'
        img_content = b'content'
        obj.dir_name = 'path'

        with patch('builtins.open', mock_open(),) as m_open:
            obj.save_image(img_title, img_content) 
            m_open.assert_called_once_with(os.path.join(obj.dir_name, f'{img_title}.png'), 'wb')
            m_open().write.assert_called_once_with(img_content)

    @patch('screendown.requests.get')
    def test_download_and_save(self, mock_get):
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        img_sources = ['fake_image.png', 'fake_image_1.png']
        obj.save_image = Mock()
        mock_response_1 = Mock()
        mock_response_2 = Mock()
        mock_response_1.status_code = 400
        mock_response_2.status_code = 200
        mock_response_2.content = b'content'
        mock_get.side_effect = [mock_response_1, mock_response_2]
        obj.download_and_save(img_sources)
        
        obj.save_image.assert_called_once_with('image_1', b'content')
    
    @patch('screendown.os.mkdir')
    def test_run_empty_image_sources(self, mock_mkdir):
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        obj.fetch_image_sources = Mock(return_value=[])
        obj.download_and_save = Mock()
        return_value = obj.run()

        mock_mkdir.assert_not_called
    
    @patch('screendown.os.mkdir')
    def test_run_empty_image_sources(self, mock_mkdir):
        obj = SSD(['https://example.com/', 'https://another-example.com/'])
        obj.fetch_image_sources = Mock(return_value=['fake_image.png'])
        obj.download_and_save = Mock()
        obj.run()

        mock_mkdir.assert_called_once_with(obj.dir_name)
        
if __name__ == '__main__':
    unittest.main()
