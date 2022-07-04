import unittest
import app
from unittest.mock import patch

class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')
    
    @patch('app.input')
    def test_get_doc_owner_name(self, mock_input):
        mock_input.return_value = '10006'
        self.assertEqual(app.get_doc_owner_name(), None)
        return print('test 1 ok!')

    @patch('app.input')
    def test_add_new_doc(self, mock_input):
        mock_input.return_value = '123'
        mock_input.return_value = 'passport'
        mock_input.return_value = 'Alex'
        mock_input.return_value = '1'
        self.assertEqual(app.add_new_doc(), '1')
        return print('test 2 ok!')

    @patch('app.input')
    def test_delete_doc(self, mock_input):
        mock_input.return_value = '10006'
        self.assertEqual(app.delete_doc(), ('10006', True))
        return print('test 3 ok!')

if __name__ == '__main__':
    unittest.main()