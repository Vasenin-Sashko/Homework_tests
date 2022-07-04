from lib2to3.pgen2 import token
import requests

token = ''
url = "https://cloud-api.yandex.net/v1/disk/resources"

 # метод  аутентификации на яндекс диске
def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }

 # метод  создания папки на яндекс диске
def create_folder(folder_name):
    headers = get_headers()
    params = {"path": folder_name}
    request = requests.get(url=url, params=params, headers=headers)
    if request.status_code != 200:
        response = requests.put(url=url, params=params, headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print(f"Added new folder \"{folder_name}\"")
            return response.status_code




if __name__ == "__main__":
    create_folder('test_folder')