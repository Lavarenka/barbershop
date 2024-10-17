from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    is_published = models.BooleanField(default=False, verbose_name='Published')
    image = models.ImageField(upload_to="photos/posts", verbose_name="Image")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Order")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Application(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First Name")
    last_name = models.CharField(max_length=150, verbose_name="Last Name")
    message = models.TextField(blank=True, verbose_name="Message")
    # number = models.IntegerField(verbose_name="Number", null=True)
    number = models.CharField(max_length=30, verbose_name="Number")
    date_of_birth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    time_of_death = models.TimeField(verbose_name="Time of Death", blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Service")

    def __str__(self):
        return self.first_name


class ContactDetails(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title", )
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.title


class SocialItem(models.Model):
    """social links on footer"""

    name = models.CharField(max_length=50, unique=True, verbose_name="Social name")
    icon = models.CharField(max_length=100, verbose_name="Font Awesome Icon")
    link = models.TextField(verbose_name="link")
