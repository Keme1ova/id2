from django.urls import path
from . import views

urlpatterns = [
   path('', views.View_user_notes.as_view()),
   path('notes/', views.View_user_notes.as_view(), name='notes'),
   path('notes/<int:id>/update_note/',
        views.View_update_note.as_view(), name='update'),
   path('notes/<int:id>/delete_note/',
        views.View_delete_note.as_view(), name='delete'),
   path('notes/add_note/', views.View_create_note.as_view(), name='add'),

]