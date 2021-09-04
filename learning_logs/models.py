from django.db import models

#Model for Topic Head
class Topic(models.Model):
    '''A topic the user is learning about.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.text

#Model for Topic Entry
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if(len(self.text)>=50):
            return self.text[:50] + "..."
        else:
            return self.text