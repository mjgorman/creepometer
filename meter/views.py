from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from django import forms
from models import nominate_post, list_nominees, get_creepy, add_creepy, reduce_creepy

def meter_index(request):
    form = Nominee()
    template = loader.get_template('index.html')
    nominees = {}
    for nominee in list_nominees():
        nominees[nominee] = get_creepy(nominee)
    context = {
              'form':form, 
              'nominees':nominees
              }
    context.update(csrf(request))
    return HttpResponse(template.render(context))

def nominate(request):
    form = Nominee(request.POST)
    if form.is_valid():
        nominate_post(form.cleaned_data['nominee_name'])
    html = "<h1>Thanks!</h1></a></a>Reloading to Creep-O-Meter... <script>setTimeout(function(){window.location.href='/'},3000);</script>"
    return HttpResponse(html)

class Nominee(forms.Form):
    nominee_name = forms.CharField(label='Who is giving you the creeps?', max_length=100)
