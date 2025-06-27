from django.db import models


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey('List', default=None, on_delete=models.CASCADE, null=True)

class List(models.Model):
    pass
