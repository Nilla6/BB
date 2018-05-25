from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('website:products_list_by_category', args=[self.slug])

class Product(models.Model):
	description = models.CharField(max_length = 50)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=0)
	image = models.ImageField(null=True, blank=True)
	available = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=200, db_index=True)
	category = models.ForeignKey(Category, related_name='products')

	class Meta:
		ordering = ('-created',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('website:product_detail', args=[self.id, self.slug])
