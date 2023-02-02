from django.db import models

# Create your models here.

class TodoItem(models.Model):
    # Creating a table in the database with the columns text, isCompleted, and created_on.
    text = models.CharField(max_length=255)
    isCompleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returning the text of the item.
        return self.text