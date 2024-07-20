from django.db import models


# class Blog(models.Model):
#     class Status(models.TextChoices):
#         PUBLISH = 'pb', 'Publish'
#         DRAFT = 'df', 'DRAFT'
#
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='blog/blog/')
#     status = models.CharField(max_length=4, choices=Status.choices, default=Status.PUBLISH)
#     comment = models.ManyToManyField(Comments, blank=True)
#     publish = models.DateTimeField(default=datetime.now())
#     updated = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
