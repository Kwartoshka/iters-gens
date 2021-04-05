import json
import time
import hashlib

class Iterator:
    def __init__(self, file_name):
        with open(file_name) as f:
            self.content = json.load(f)
        self.file_name = file_name
        self.id = -1
        self.max = len(self.content)

    def __iter__(self):
        return self

    def __next__(self):

        self.id += 1
        if self.id == self.max:
            raise StopIteration
        return self.content[self.id]


    def get_list(self):
        countries_and_urls = []
        for i in self:
            name = i['name']['common']
            url = name.split(' ')
            url = 'https://en.m.wikipedia.org/wiki/' + '_'.join(url)
            string = name + " - " + url
            countries_and_urls.append(string)
        return countries_and_urls

    def write_in_file(self, file_name):
        content = '\n'.join(self.get_list())
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)

def generator(file_name):
    max = sum(1 for line in open(file_name))
    with open(file_name) as f:
        item = 0
        while item < max:
            string = f.readline()
            hasher = hashlib.md5(string.encode('utf-8'))
            result = str(hasher.hexdigest()) + '\n'
            yield result
            item += 1

def hasher(file_name):
    with open(f'hashed_{file_name}', 'w') as f:
        for item in generator(file_name):
          f.write(item)


file = Iterator('countries.json')
where_to_write = 'got_it.txt'

file.write_in_file(where_to_write)
hasher(where_to_write)