from decimal import Decimal 
from django.conf import settings
from .models import ActiveList

class Cart(object):
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, ActiveList):
		item = str(activelist.id)
		if item not in self.cart:
			self.cart[activelist] = {'bid':str()}



	def save(self):
		self.session.modified = True
