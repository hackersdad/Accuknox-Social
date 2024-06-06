# api/urls.py
from django.urls import path
from .views import UserSignupView, UserLoginView, UserSearchView, FriendRequestView, FriendsListView, FriendRequestActionView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='search'),
    path('friend-request/', FriendRequestView.as_view(), name='friend-request'),
    path('friend-request-action/', FriendRequestActionView.as_view(), name='friend-request-action'),
    path('friends/', FriendsListView.as_view(), name='friends'),
]
