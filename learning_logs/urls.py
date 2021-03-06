"""Определяет схемы URL для learning_logs."""

from django.urls import path, include
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    # the page with all topics
    path('topics/', views.topics, name='topics'),
    # the page with info on specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # the page to add new TOPICS
    path('new_topic/', views.new_topic, name='new_topic'),
    # the page to add new ENTRIES
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]







