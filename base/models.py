from django.db import models


# About Model
class About(models.Model):
    name = models.CharField(max_length=30, null=False, default="Bibek Poudel")
    work = models.CharField(max_length=30, null=False, default="Programmer")
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill name")
    description = models.TextField(verbose_name="Skill description")
    knowledge = models.IntegerField(verbose_name="percentage")

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    link = models.CharField(max_length=100, verbose_name="Link", null = True)

    def __str__(self):
        return self.title


class VisitorMessage(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name", name='name')
    email = models.EmailField(max_length=30, verbose_name="Visitor Email", name='email')
    message = models.TextField(verbose_name="Visitor Message", name='message')

    def __str__(self):
        return self.name