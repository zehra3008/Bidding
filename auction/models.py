from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActiveList(models.Model):
	CATEGORY = (
		('Cars', 'Cars'),
		('Paintings','Paintings'),
		('Vintage glassware','Vintage glassware'),
		('Musical instruments','Musical instruments'),
		('Collectibles','Collectibles'),
		('Books','Books'),
		('Other','Other'))
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 62)
	bid = models.IntegerField(default = 0)
	category = models.CharField(max_length = 62, choices=CATEGORY)
	note = models.CharField(max_length = 500, null=True)
	created_on = models.DateTimeField(auto_now=True, null=True)
	product_img = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		return f"{self.name} - {self.category}"

class UserBid(models.Model):
	product = models.ForeignKey(ActiveList, on_delete=models.CASCADE)
	userbid = models.IntegerField()
	bider = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.product} - {self.userbid} {self.bider}"


class UserComment(models.Model):
	item = models.ForeignKey(ActiveList, on_delete=models.CASCADE)
	commenter = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length=100, null=True)

	def __str__(self):
		return f"{self.id} {self.commenter} comment's at {self.item.name}  " 

class WatchList(models.Model):
	user_watchlist = models.ForeignKey(User, on_delete=models.CASCADE)
	watchlist = models.ManyToManyField(ActiveList)

	def __str__(self):
		return f"{self.user_watchlist}"