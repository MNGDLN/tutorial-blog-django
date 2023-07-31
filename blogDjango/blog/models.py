from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=255)
    tutorial_category = models.ForeignKey('TutorialCategory', on_delete=models.CASCADE)
    series_summary = models.TextField()
    series_slug = models.SlugField()
    series_img = models.ImageField(upload_to='./media/series_img',blank=True)

    def __str__(self):
        return self.tutorial_series


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=255)
    category_summary = models.TextField()
    category_slug = models.SlugField()
    category_img = models.ImageField(upload_to='./media/category_img',blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'svg'])])

    def __str__(self):
        return self.tutorial_category


class Tutorial(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    tutorial_title = models.CharField(max_length=255,unique=True)
    tutorial_description = models.CharField(max_length=160)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(default=timezone.now)
    tutorial_series = models.ForeignKey('TutorialSeries', on_delete=models.CASCADE)
    tutorial_slug = models.SlugField(unique=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.PUBLISHED)
     

    def __str__(self):
        return self.tutorial_title
    
    def get_absolute_url(self):
        return reverse('blog:tutorial_detail',
                       args=[self.tutorial_slug])
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
    