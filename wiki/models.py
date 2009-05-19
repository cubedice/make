from django.db import models

class Page(models.Model):
	title = models.CharField(max_length = "80", primary_key = True)
	content = models.TextField(blank=True)
