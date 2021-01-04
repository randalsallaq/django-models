from django.urls import path,include
from .views import HomePageView,DetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', DetailsView.as_view(), name ='post_detail')
    
]