from django.db.models import *


class Blog(Model):
    title = CharField(max_length=80)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    
    def __str__(self):
        return str(self.title)



class Post(Model):
    blog = ForeignKey(Blog, on_delete=CASCADE)
    subject = CharField(max_length=80)
    text = TextField(max_length=4096)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    updated_at = DateTimeField('update timestamp', auto_now=True)
