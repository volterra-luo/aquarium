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

def view_stat(request):
    return render_to_response('carriage/stat.html',)

def _get_referer_url(request):
    referer_url = request.META.get('HTTP_REFERER', '/')
    host = request.META['HTTP_HOST']
    if referer_url.startswith('http') and host not in referer_url:
        referer_url = '/'
    return referer_url

import urllib
def google_login(request):
    google_auth_url = '%s?%s' % ('https://accounts.google.com/o/oauth2/auth',
                             urllib.urlencode({
                                 'response_type': 'code',
                                 'client_id': '554792660883-l7mvvejqvkev3qaa23bmlv13ivfg2mil.apps.googleusercontent.com',
                                 'redirect_uri': 'http://localhost:8000/carriage/',
                                 'scope': 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile',
                                 'state': _get_referer_url(request)
                             }))
    return HttpResponseRedirect(google_auth_url)

import urllib2
def get_access_token(code):
    auth_url = 'https://accounts.google.com/o/oauth2/token'
    body = urllib.urlencode({
                'code': code, # 授权码
                'client_id': '554792660883-l7mvvejqvkev3qaa23bmlv13ivfg2mil.apps.googleusercontent.com',
                'client_secret': 'kROd_3tyYvXHxjHiXwUD0EtP',
                'redirect_uri': 'http://localhost:8000/carriage/',
                'grant_type': 'authorization_code' # 必须是这个值
                })
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    req = urllib2.Request(auth_url, body, headers)
    resp = urllib2.urlopen(req)
     
    data = json.loads(resp.read())
     
    return data['access_token']

def get_user_info(access_token):
    if access_token:
        userinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        query_string = urllib.urlencode({'access_token': access_token})
         
        resp = urllib2.urlopen("%s?%s" % (userinfo_url, query_string))
        data = json.loads(resp.read())
         
        return data
    
def google_auth(request):
    if 'blog_user' in request.session:
        return HttpResponseRedirect('/')
     
    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponseRedirect('/')
     
    code = request.GET['code']
     
    access_token = get_access_token(code)
    blog_user = get_blog_user(get_user_info(access_token))
     
    request.session['blog_user'] = blog_user
     
    next = '/'
    if 'state' in request.GET:
        next = request.GET['state']
     
    return HttpResponseRedirect(next)