from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ProfileDate(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile_data/")
    body = models.TextField()

    def __str__(self):
        return self.full_name


class Post(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post/")
    body = models.TextField()
    views_count = models.IntegerField()

    def __str__(self):
        return self.title


class Service(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="service/")
    description = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.title


class About(BaseModel):
    text = models.TextField(max_length=255)
    donation = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    volunteers = models.PositiveIntegerField()

    def __str__(self):
        return f"self.donation"


class Tool(BaseModel):
    skill = models.TextField(max_length=255)
    persentage = models.PositiveIntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f"{self.skill} - {self.persentage}"


class SocialLink(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.CharField(max_length=50)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(BaseModel):
    name = models.CharField(max_length=255)
    link = models.URLField()
    discription = models.TextField()
    used_tools = models.ManyToManyField(Tool)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name