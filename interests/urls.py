from django.urls import path
from .views import InterestListCreateView

urlpatterns = [
    path('', InterestListCreateView.as_view(), name='interest_list_create'),
]
