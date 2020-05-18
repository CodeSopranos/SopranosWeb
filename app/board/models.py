from django.contrib.postgres.fields import JSONField
from django.db.models import *


class Dashboard(Model):
    name = CharField(max_length=80)
    theme = CharField(max_length=80, default='theme')
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    user_id = IntegerField(default=0)
    data = JSONField(default={})

    def __str__(self):
        return str(self.name)



class Figure(Model):
    dashboard = ForeignKey(Dashboard, on_delete=CASCADE)
    tag = CharField(max_length=80)
    data = JSONField()
    params = JSONField()
    modify_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.tag)
