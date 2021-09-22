from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors
    def __repr__(self) -> str:
        return f'{self.id}: {self.title}'
    #el self id corresponde a la llave con que se accederá en el shell                  

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Books,related_name= 'authors')
    notas = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __repr__(self) -> str:
        return f'{self.id}: {self.first_name}'

