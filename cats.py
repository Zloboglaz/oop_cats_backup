import json
import requests

class Cats:
    main_url = 'https://cataas.com/cat'

    def __init__(self):
        pass

    def get_img_with_text(self, need_text):
        """
        Получение данных через GET запрос
        need_txt - текст, который будет отображаться на картинке
        """
        url = f'{self.main_url}/says/{need_text}'
        response = requests.get(url)
        return response

    def save_img(self, name: object, content: object):
        """
        Сохранение картинки и .json с информацией локально в папку /images
        name - название файла при сохранении
        content - результат GET запроса из метода get_img_with_text(self, need_text)
        """
        extension = content.headers['Content-Type'].split('/')[-1]
        file_name = f'{name}.{extension}'

        with open(f'images/{file_name}', 'wb') as f:
            f.write(content.content)

        image_info = {
            "file_name": file_name,
            "file_size_bytes": content.headers['Content-Length'],
            "file_type": content.headers['Content-Type'],
        }

        with open(f'images/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(image_info, f, ensure_ascii=False, indent=2)

        return file_name