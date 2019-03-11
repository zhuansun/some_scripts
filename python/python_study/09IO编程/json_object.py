import json

# 把dict转成json
# d = dict(name='bob',age=23,socre=90)
# print(json.dumps(d))


class Teacher(object):
    def __init__(self,__name,__age,__score):
        self.__name = __name
        self.__age = __age
        self.__score = __score

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getScore(self):
        return self.__score


def teachet2dict(teacher):
    return {
        'name':teacher.getName(),
        'age':teacher.getAge(),
        'score':teacher.getScore()
    }


def dict2teacher(d):
    return Teacher(d['name'],d['age'],d['score'])

s = Teacher("张老师",23,45)
json_str = json.dumps(s,default=teachet2dict)
print(json.loads(json_str,object_hook=dict2teacher))