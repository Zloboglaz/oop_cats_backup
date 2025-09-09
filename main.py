from cats import Cats
from yandex_drive import YandexDrive

def token_input():
    ya_token = ''
    while not ya_token:
        ya_token = input('Введите токен Вашего Яндекс диска: ').replace(' ', '')
        if not ya_token:
            print('Данное поле не может быть пустым или состоять из пробелов.')
    return ya_token

def text_input():
    txt = ''
    while not txt:
        txt = input('Введите текст, который бдет отображаться на изображении: ').replace(' ', '')
        if not txt:
            print('Данное поле не может быть пустым или состоять из пробелов.')
    return txt

if __name__ == '__main__':

    # Так бедет называться папка на Яндекс диске, в которую будет осуществляться сохранение изображения
    folder_name = 'FPY-134'

    # Ввод токена Яндекс диска
    yandex_token = token_input()

    # Ввод текста для картинки
    txt = text_input()

    cat = Cats()
    disk = YandexDrive(yandex_token)

    # Получение изображения с нуобходимым текстом через GET запрос, сохранеие изображение локально в папке /images,
    # сохранение .json с информацией о файле и возврат имени сохраненного файла
    file_name = cat.save_img(txt, cat.get_img_with_text(txt))

    # Создание папки на Яндекс диске, если её еще нет
    disk.create_folder(folder_name)

    # Загрузка ранее скачанного изображения на Яндекс диск в ранее созданную папку
    print(disk.upload_file(folder_name, file_name))


