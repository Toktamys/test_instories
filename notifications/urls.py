from django.urls import path

from .views import (
    PushListView,
    PushDetailView,
    PushCreateView,
    PushUpdateView,
    PushDeleteView,
    OptionListView,
    OptionCreateView,
    OptionDetailView,
    OptionUpdateView,
    OptionDeleteView,
    login_user,
    logout_user)

urlpatterns = [
    path('', login_user, name='login_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('pushes/', PushListView.as_view(), name='push_list'),
    path('pushes/<int:pk>/', PushDetailView.as_view(), name='push_detail'),
    path('pushes/<int:pk>/update/', PushUpdateView.as_view(), name='push_update'),
    path('pushes/<int:pk>/delete/', PushDeleteView.as_view(), name='push_delete'),
    path('pushes/add-push/', PushCreateView.as_view(), name='push_create'),
    path('options/', OptionListView.as_view(), name='option_list'),
    path('options/<int:pk>/', OptionDetailView.as_view(), name='option_detail'),
    path('options/<int:pk>/update/', OptionUpdateView.as_view(), name='option_update'),
    path('options/<int:pk>/delete/', OptionDeleteView.as_view(), name='option_delete'),
    path('options/add-option/', OptionCreateView.as_view(), name='option_create'),
]
