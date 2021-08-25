# Django Practice Polling app

## Description

The app is followed on the documentation of Django.
For now have completed the setup of the project and app, created the view and models.

## Code

A view function that returns a HTTP Response when called in the views.py

```Python
def index(request):
    return HttpResponse('Hello world, your at the polls index.')
```

A url defined in the polls url.py file

```Python
urlpatterns = [
    path('', views.index, name='index'),
]
```

The models in the polls models.py file

```Python
# One to one relationship set between question and choice model
# Question model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```
