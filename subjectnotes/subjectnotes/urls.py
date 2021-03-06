from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject_list/', views.subject_list, name='subject_list'),
    path('note_list/<int:subject_id>/', views.note_list, name='note_list'),
]
