"""
@edsonlb
https://www.facebook.com/groups/pythonmania/
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('copa.views',
    url(r'^salvar/$', 'copaSalvar'),
    url(r'^$', 'copaListar')
)