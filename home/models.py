from django.db import models


#creatrd thr shema and will make chabges to vies to stor upon hitting submit and exe of POST req
# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
#goto admin and import this Contact oblject and register the model

    def __str__(self):
        return self.name #isse name display hoga object mein in data base
