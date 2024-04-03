from django.db import models

# Create your models here.
class list_of_category(models.Model):
    list = models.CharField(max_length=5000)

    def __str__(self):
        return self.list

class table(models.Model):
    task_name = models.CharField(max_length=5000)
    category = models.ForeignKey(list_of_category, on_delete=models.CASCADE)
    due_date = models.DateField()
