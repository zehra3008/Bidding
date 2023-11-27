from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),

	path('', views.index, name='index'),
	path('categories/<str:category>', views.categories, name='categories'),
	path('detail/<int:pk>', views.detail, name='detail'),
	path('watchlist/', views.watchlist, name='WatchList'),
	path('watchlist/<int:pk>', views.watchlist, name='Add-watchlist'),
	path('createList/', views.createList, name='create'),
	
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)