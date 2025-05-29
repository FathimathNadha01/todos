from django.db import models



from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Todo(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    options  = {
    'pending' : 'pending',
    'completed' : 'completed',
    'ongoing' : 'ongoing'
}
    status = models.CharField(max_length=50,choices=options)
    created_date = models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    



# Create your models here.
