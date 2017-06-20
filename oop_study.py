#создаем абстрактные классы
from abc import ABCMeta, abstractmethod
import pickle
import json
import os

source = './file.txt'

#1 - абстрактный класс
class ParamHandlerException(Exception):
    pass


class ParamHandler(metaclass=ABCMeta):

    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params
    
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass
    
    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"

        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        
        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))

        return klass(source, *args, **kwargs)
    
##    @staticmethod
##    def get_instance(source):
##        _, ext = os.path.splitext(str(source).lower())
##
##        if ext == '.xml':
##            return XmlParamHandler(source)
##
##        return TextParamHandler(source)

#2 конкретные реализации
    
class JsonParamHandler(ParamHandler):

    def read(self):
    #Чтение из текстового файла и присвоение значений в self.params
        with open(source, 'r') as f:
            self.params = json.load(f)
                
    def write(self):
    #Запись в текстовый файл параметров self.params
        with open(source, 'w') as f:
            self.params = json.dump(data, f)

class PickleParamHandler(ParamHandler):
    def write(self):
    #Чтение в формате XML и присвоение значений в self.params
        with open(source, 'wb') as f:
            self.params = pickle.dump(data, f)

    def read(self):
    #Запись в формате XML параметров self.params
        with open(source, 'rb') as f:
            self.params = pickle.load(f)

class TextParamHandler(ParamHandler):

    def write(self):
    #Чтение в формате XML и присвоение значений в self.params
        with open(source, 'w') as f:
            for key, value in self.params.items():
                f.write(str(key) + ":" + str(value) + '\n')

    def read(self):
    #Запись в формате XML параметров self.params
        with open(source, 'r') as f:
            f.read()

class XmlParamHandler(ParamHandler):

    def read(self):
    #Чтение в формате XML и присвоение значений в self.params
        with open(source, 'w') as f:
            for key, value in self.params.items():
                f.write(str(key) + ":" + str(value) + '\n')
    def write(self):
    #Запись в формате XML параметров self.params
        with open(source, 'r') as f:
            f.read()    

ParamHandler.add_type('json', JsonParamHandler)
ParamHandler.add_type('pickle', PickleParamHandler)
ParamHandler.add_type('txt', TextParamHandler)
ParamHandler.add_type('xml', XmlParamHandler)

config = ParamHandler.get_instance(source)

config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.add_param('key4', 'val4')


config.write() # запись файла в XML формате
config = ParamHandler.get_instance(source)
config.read() # читаем данные из текстового файла
