from mongoengine import *

connect('student')


class StudentInfo(Document):
    name = StringField(required=True, max_length=20)
    age = IntField(required=True)


class Article(Document):
    content = StringField(required=True, max_length=1000)
    owner = ReferenceField(StudentInfo)

owner = StudentInfo.objects(id="5b9cbc7bbd34d0b7bc4f6ebe")[0]
print(owner)
print(owner.name, owner.age)
a = Article(content='123', owner=owner)
a.save()