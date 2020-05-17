from django.contrib.postgres.fields import JSONField
from django.db.models import *


class Dashboard(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=80)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    user_id = IntegerField(default=0)

    def __str__(self):
        return str(self.title)


class Figure(Model):
    id = AutoField(primary_key=True)
    dashboard = ForeignKey(Dashboard, on_delete=CASCADE)
    tag = CharField(max_length=80)
    data = JSONField()
    params = JSONField()
    modify_at = DateTimeField('creation timestamp', auto_now_add=True)
    
    def __str__(self):
        return str(self.tag)
