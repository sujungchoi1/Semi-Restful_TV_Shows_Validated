from django.db import models

class ShowManager(models.Manager):
    def getErrors(self, postData):
        # returns a dict with erros
        errors = {}
        
        if len(postData["title"]) < 2:
            errors['title'] = "Title must be at least 2 characters"
        
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        
        if len(postData['description']) < 10:
            errors['description'] = "Description must have at least 10 characters"
        
        if len(postData['release_date']) == 0:
            errors['release_date'] = "Due date cannot be blank"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 
    
    def __repr__(self):
        return f"Show: {self.title} {self.network}"