from peewee import *

settings = {'host': '127.0.0.1', 'password': 'willian', 'port': 5434, 'user': 'postgres'}

db = PostgresqlDatabase('test', **settings)

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    birthday = DateField()
    is_relative = IntegerField()
    name = CharField()

    class Meta:
        table_name = 'person'

