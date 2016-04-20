from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey


class Question(Model):
    question_text = CharField(max_length=200)
    is_active = BooleanField()

    def __str__(self):
        return self.question_text


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
