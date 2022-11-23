from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank = True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self): #after someone creates a post, where should the wubsite take them
        #must be called get_absolute_url 
        return reverse("post_detail", kwargs={'pk': self.pk}) #once we click on publish button, website will bring us to post_detail page with primary key of the post created

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'comments') #thisline will connect each comment to an Post
    author = models.CharField(max_length= 200)  #this is not related to the author field of post. The author here is manually inputted by the person
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False) #approved_comment should match xxxx of line 18 filter(xxxx) 

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('post_list') #when comments approved, it will bring the superuser to a list of the post


    def __str__(self):
        return self.text