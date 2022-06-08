from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns=[
    path ('',views.login_user,name = 'login'),
    path('register',views.register,name='register'),
    path('logout',views.log_out,name='logout'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('comment/image/<id>',views.post_comment,name='comment'),
    path('user_profile/<username>/',views.user_profile,name='user_profile'),
    path('upload_photo',views.upload_photo,name='upload_photo'),
    path('search', views.search_profile, name='search'),
    path('update_profile', views.update_profile, name='update_profile'),
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
