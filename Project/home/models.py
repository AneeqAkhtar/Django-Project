from django.db import models

# Create your models here.
print('models')
class home_service(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=15)


#Override models.save from real code
    #def save(self):
     #  pass # type: ignore