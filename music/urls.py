from django.conf.urls import url
from haystack.views import SearchView

from . import views
from django.views.generic import RedirectView

urlpatterns = [

   # url(r'^$' , views.search ,name = 'search'),

   url(r'^$' , SearchView() ,name = 'haystack_search'),
   url(r'^song_id/(?P<song_num>[0-9]+)/$',views.song_id, name='song_id'),
   url(r'^search_results/$', views.search_results, name='serach_results'),
]

