from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('all-industries/', views.all_industries, name="all-industries"),
    path('fashion-apparel/', views.fashion_apparel, name="fashion-apparel"),
    path('food-drink/', views.food_drink, name="food-drink"),
    path('paid-pricing/', views.paid_pricing, name="paid-pricing"),
    path('organic-pricing/', views.organic_pricing, name="organic-pricing"),
    path('sign-in/', views.sign_in, name="sign-in"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
