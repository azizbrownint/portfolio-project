from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images/')
    pubdate = models.DateTimeField()
    bodytext = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.bodytext[:100] + "..."

    def pubdate_pretty(self):
        return self.pubdate.strftime('%b %e %Y')



# Create a blog models
#title, publication date, some actual text(body), and finally an image.

# Add the blog app to the settings

# create a migration

# migrate

# add to the admin
