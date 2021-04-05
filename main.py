import json
import time
import hashlib

class Iterator:
    def __init__(self, file_name):
        with open(file_name) as f:
            self.content = json.load(f)
        self.file_name = file_name
        self.item = -1
        self.max = len(self.content)

    def __iter__(self):
        return self

    def __next__(self):
        self.item += 1
        if self.item == self.max:
            raise StopIteration
        return self.item

    def get_list(self):
        countries_and_urls = []
        for i in self:
            name = self.content[i]['name']['common']
            url = name.split(' ')
            url = 'https://en.m.wikipedia.org/wiki/' + '_'.join(url)
            string = name + " - " + url
            countries_and_urls.append(string)
        return countries_and_urls

    def write_in_file(self, file_name):
        content = '\n'.join(self.get_list())
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)

def doc_range(file_name):
  with open(file_name) as f:
    max = len(f.readlines())
  item = 0
  while item < max:
    yield item
    item += 1

def hasher(file_name, encoding='utf-8'):
    with open(file_name) as f:
        doc = f.readlines()
        result_data = ''
        for i in doc_range(file):
            hasher = hashlib.md5()
            hasher.update(doc[i].encode(encoding))
            result = str(hasher.hexdigest()) + '\n'
            result_data += result
    with open(f'hashed_{file_name}', 'w') as f:
        f.write(result_data)




start = time.time()
a = Iterator('countries.json')
a.write_in_file('got_it.txt')



file = 'got_it.txt'

hasher(file)
