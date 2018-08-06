from mongoengine import *
import pytz
from datetime import datetime

_datetime = datetime.now(tz=pytz.timezone('Asia/Shanghai'))

# mongodb
connect('reptile', host='123.58.244.170', port=27017, username='yangjiajia', password='SYHXsqq@1233')


class Recruit(Document):
    create_at = DateTimeField(default=_datetime)
    # 职位的名称
    name = StringField(max_length=80, null=False)
    # 薪水
    salary = StringField(max_length=12, null=False)
    # 工作地点
    address = StringField(max_length=100, null=False)
    # 学历
    education = StringField(max_length=10, null=False)
    # 工作年限
    work_time = StringField(max_length=12)
    # 福利待遇
    welfare = ListField()
    # 是否全职
    emplType = StringField(max_length=10)
    # 公司的名称
    company = StringField(max_length=100)
    # 公司性质
    company_nature = StringField(max_length=20)
    # 公司规模
    company_size = StringField(max_length=20)
    # 岗位职责
    responsibility = ListField()
    # 任职要求
    tenure = ListField()
    # 工作职责
    work_responsibility = ListField()

    def __str__(self):
        return self.name

    meta = {
        'indexes': [
            'create_at', 'name'
        ],
        'ordering': ['-create_at']
    }
