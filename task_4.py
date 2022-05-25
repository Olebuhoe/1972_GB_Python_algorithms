"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4


class WebCache:
    def __init__(self):
        self.urls_hashes = {}

    def make_hash(self, url):
        salt = uuid4().hex
        hash = hashlib.md5(salt.encode() + url.encode()).hexdigest()  # взял алгоритм md5, чтоб хеши были покороче
        return hash

    def into_cache(self, url):
        url_hashe = self.make_hash(url)
        return self.urls_hashes.setdefault(url, url_hashe)


if __name__ == '__main__':
    dct_urls = WebCache()
    dct_urls.into_cache('gb.ru')
    dct_urls.into_cache('yandex.ru')
    print(dct_urls.urls_hashes)
    print(dct_urls.into_cache('vk.com'))
    print(dct_urls.urls_hashes)
    print(dct_urls.into_cache('gb.ru'))
    print(dct_urls.urls_hashes)
