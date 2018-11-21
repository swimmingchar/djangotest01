# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.conf import settings
from django import forms
from io import BytesIO
from PIL import Image, ImageDraw


# Create your views here.
class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(slef, image_format='PNG'):
        height = slef.cleaned_data['height']
        width = slef.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        draw =ImageDraw.Draw(image)
        text = '{0} x {1}'.format(width,height)
        textwidth,textheight=draw.textsize(text)

        if textwidth < width and textheight < height:
            texttop = (height - textheight) // 2
            textleft = (width - textwidth) // 2
            draw.text((texttop,textleft),text,fill=(255,255,255))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content


def placehoder(request, width, height):
    # TODO: Rest of the view will go here
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
        # return HttpResponse('OK\r\n width is:%s\r\n height is:%s' %(width,height))
    else:
        return HttpResponseBadRequest("尺寸错误！")
def index(request):
    example = reverse('placehoder',kwargs={'width':50, 'height':50})
    context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)


def app(request):

    return render(request,"index-3.html")


def app01(request):
    return render(request,'index-2.html')