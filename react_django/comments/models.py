# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()

