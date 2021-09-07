''' Defines URL patterns for learning_logs '''

from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    #Show all topics
    url(r'^topics/$', views.topics, name = 'topics'),

    #Detailed page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

    #Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]