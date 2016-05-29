# coding: utf-8
import json

from django.views.generic import View
from django.http import HttpResponse

from .models import Comment


class CommentsApiView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps([dict(author=i.author,
                                             text=i.text,
                                             id=i.id)
                                        for i in Comment.objects.all()]),
                            content_type='application/json; charset=utf8')
