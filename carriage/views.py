#!/usr/bin/env python
# -*- coding: utf-8 -*-
from carriage.models import Group,Project,Transport
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views import generic
from django import forms

class SearchForm(forms.Form):
    plate_num = forms.CharField(label="请输入需要查询的车号")
    
def search_page(request):
    if request.method == "POST":
        f = SearchForm(request.POST)
        if not f.is_valid():
            return render_to_response("carriage/search.html",{"form":f},context_instance=RequestContext(request))
        else:
            trspts=[]
            trspts = Transport.objects.filter(tanker__lpn__contains = f.cleaned_data['plate_num'])
            return render_to_response("carriage/search.html",{"form":f,"trspts":trspts},context_instance=RequestContext(request))
    f = SearchForm()
    return render_to_response("carriage/search.html",{"form":f},context_instance=RequestContext(request))

class IndexView(generic.ListView):
    template_name = 'carriage/index.html'
    context_object_name = 'latest_transport_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Transport.objects.order_by('-date')[:5]

specialPages = {"SearchPage":search_page} 

def view_page(request,crg_id):
    if crg_id in specialPages:
        return specialPages[crg_id](request)
    return render_to_response("view.html",
            )
