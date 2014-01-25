from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Join
from .forms import JoinForm

def index():
    pass

def thanks():
    pass

def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        zip_code = form.cleaned_data['zip_code']

        new_join = form.save(commit=False)
        new_join.save()

        return render_to_response('join/thanks.html')

    return render_to_response('join/home.html', locals(), context_instance=RequestContext(request))