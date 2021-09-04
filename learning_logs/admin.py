from django.contrib import admin

from learning_logs.models import Entry, Topic
admin.site.register(Topic)
admin.site.register(Entry)