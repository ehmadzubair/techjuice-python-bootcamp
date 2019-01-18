from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject_list/', views.subject_list, name='subject_list'),
    path('note_list/<int:subject_id>/', views.note_list, name='note_list'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('update_note/<int:note_id>/', views.update_note, name='update_note'),
]
