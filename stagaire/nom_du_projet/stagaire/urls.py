from django.urls import path
from .views import home, delete_student, student_add, update_student

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("add_student/", student_add),
    path("delete_student/<str:student_id>/", delete_student, name="delete_student"),
    path("update_student/<str:student_id>/", update_student, name="update_student"),  
]
