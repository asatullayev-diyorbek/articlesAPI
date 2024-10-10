from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    path('hotel/list/', views.HotelListView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/detail/', views.HotelDetailView.as_view(), name='hotel_detail'),

    path('class/list/', views.ClassListView.as_view(), name='class_list'),
    path('class/<int:pk>/detail/', views.ClassDetailView.as_view(), name='class_detail'),

    path('travel/list/', views.TravelListView.as_view(), name='travel_list'),
    path('travel/<int:pk>/detail/', views.TravelDetailView.as_view(), name='travel_detail'),
]