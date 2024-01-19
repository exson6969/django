from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView, UserRegistrationView, CustomObtainAuthToken

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomObtainAuthToken.as_view(), name='user-login'),
]