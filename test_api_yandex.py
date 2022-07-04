import unittest
import yandex_service

class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    # метод: тестирование создания папки на яндекс диске
    def test_create_folder(self):
        self.assertEqual(yandex_service.create_folder('test_folder'), 201)
    
    # метод: тестирование неправильной аунтефикации на яндекс диске (отсутсвие токена)
    @unittest.expectedFailure
    def test_create_folder_fail(self):
        self.assertEqual(yandex_service.create_folder('test_passed'), 401)

    def tearDown(self):
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()