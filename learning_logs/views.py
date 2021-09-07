from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Topic
from .forms import TopicForm

def index(request):
    ''' Learning Log Home Page '''
    return render(request, 'learning_logs/index.html')

def topics(request):
    ''' Show all topics '''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    ''' Show a single topic and all its entries '''
    topic = Topic.objects.get(id = topic_id)
    entries= topic.entry_set.order_by('-date_added')
    context = { 'topic' : topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new Topic. """
    if request.method != 'POST':
        #No data submitted; Create a blank form.
        form = TopicForm()
    else:
        #POST data submitted; Process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)