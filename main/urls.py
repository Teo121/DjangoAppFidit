from django.urls import path
from .views import homepage, add_rezervacija, update_rezervacija, delete_rezervacija

urlpatterns = [
    path('', homepage, name='homepage'),  # This is the homepage URL
    path('add_rezervacija/', add_rezervacija, name='add_rezervacija'),
    path('update_rezervacija/<int:rezervacija_id>/', update_rezervacija, name='update_rezervacija'),
    path('delete_rezervacija/<int:rezervacija_id>/', delete_rezervacija, name='delete_rezervacija'),
    # Add more URLs as needed
]
