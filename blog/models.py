from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images/')
    pubdate = models.DateTimeField()
    bodytext = models.TextField()



# Create a blog models
#title, publication date, some actual text(body), and finally an image.

# Add the blog app to the settings

# create a migration

# migrate

# add to the admin
