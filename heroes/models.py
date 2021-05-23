from django.db import models
from django.utils import timezone
from django.urls import reverse



class Article(models.Model):
	STATUS_CHOICES = (
         ('draft','Draft'),
         ('published','Published'),


	)


	CATEGORY_CHOICES = (
         ('technology','Technology'),
         ('gadgets','Gadgets'),
         ('design','Design'),
         ('development','Development'),
         ('article','Article'),



	)

	title = models.CharField(max_length=250)
	
	author = models.ForeignKey('users.CustomUser',
		                     on_delete=models.CASCADE,
		                     related_name='heroes_articles')
	category = models.CharField(max_length=250,
		                        choices=CATEGORY_CHOICES,
		                        default='article')
	about = models.CharField(max_length=250,null=True,blank=True)
	body = models.TextField()
	image = models.ImageField(null=True,blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,
		                      choices=STATUS_CHOICES,
		                      default='draft')


	class Meta:
		ordering = ('-publish',)


	def __str__(self):
		return self.title





class Comment(models.Model):
	articles = models.ForeignKey(Article,
		                         on_delete=models.CASCADE,
		                         related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField(null=True, blank=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
		return self.article


	def get_absolute_url(self):
		return reverse('home', args=[str(self.id)])