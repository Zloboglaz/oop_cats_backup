import requests

class YandexDrive:
    main_url = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}

    def folder_existence(self, folder_name):
        """
        Проверка существования папки на диске
        """
        url = f'{self.main_url}/v1/disk/resources'
        params = {
            'path': folder_name
        }

        response = requests.get(url, headers=self.headers, params=params)
        return response.status_code


    def create_folder(self, folder_name):
        """
        Создание новой папки на диске, если такой еще не существует
        """
        folder_info = self.folder_existence(folder_name)
        if folder_info == 404:
            url = f'{self.main_url}/v1/disk/resources'
            params = {'path': folder_name}
            response = requests.put(url, headers=self.headers, params=params)
            return 'Папка успешно создана.' if response.status_code == 201 else f'Ошибка, код {response.status_code}'

        elif folder_info == 200:
            return f'Папка "{folder_name}" уже существует.'

    def upload_file(self, folder_name, img_name):
        """
        Загрузка файла на диск
        """
        url = f'{self.main_url}/v1/disk/resources/upload'
        params = {'path': f'{folder_name}/{img_name}'}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code in [200, 201]:
            upload_url = response.json()['href']

            with open(f'images/{img_name}', 'rb') as f:
                upload_response = requests.put(upload_url, files={'file': f})
                if upload_response.status_code == 201:
                    return f'Изображение {img_name} успешно загружено на Яндекс диск.'
                else:
                    return f'При загрузке изображения {img_name} произошла ошибка. Код {upload_response}'
        else:
            return f'Изображение {img_name} уже существует на Яндекс диске. Введите другое название.'




