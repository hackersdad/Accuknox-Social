from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import SocialUser, LoginRecord, FriendRequest, Friendship

from accuknox_social.decorators import token_required

class UserSignupView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')
        
        if SocialUser.objects.filter(email__iexact=email).exists():
            return JsonResponse({'status':'error', 'message' : 'Email already exists'})

        new_user = SocialUser()
        new_user.email = email
        new_user.name = name
        new_user.password = password
        new_user.status = 1
        new_user.save()

        return JsonResponse({'status':'success', 'message' : 'User created successfully'})

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = SocialUser.objects.filter(email__iexact=email).first()
        
        if user and user.password == password:
            import secrets
            import string
            alphabet = string.ascii_letters + string.digits
            token = ''.join(secrets.choice(alphabet) for _ in range(64))
            login_record = LoginRecord()
            login_record.user_id = user.id
            login_record.token = token
            login_record.save()

            return JsonResponse({'status':'success', 'message': 'Login successful','token': token})
        
        return JsonResponse({'status':'error', 'message':'Invalid credentials'})

class UserSearchView(APIView):
    @token_required
    def get(self, request, *args, **kwargs):
        query = request.data.get('q', '')
        users = SocialUser.objects.filter(email__iexact=query) | SocialUser.objects.filter(name__icontains = query)
        user_data = [{'id': user.id, 'email': user.email, 'name': user.name} for user in users]
        
        return JsonResponse({'status':'success', 'message': 'Search results','data': user_data})

class FriendRequestView(APIView):
   
    @token_required
    def post(self, request, *args, **kwargs):
        to_user_id = request.data.get('to_user_id')
        from_user_id = request.session.get('user_id')
        raw_query = "SELECT * FROM friend_request WHERE from_user_id = %s and timestamp > NOW() - INTERVAL 1 MINUTE;"
        recent_requests = FriendRequest.objects.raw(raw_query, [from_user_id])
        count = len(list(recent_requests))
        if count > 3:
            return JsonResponse({'status': 'fail', 'message': "You cannot send more than 3 requests in a minute"})

        req = FriendRequest()
        req.from_user_id = from_user_id
        req.to_user_id = to_user_id
        req.status = 'pending'
        req.save()

        return JsonResponse({'status': 'success', 'message': f"Current time: {now}"+'Friend request sent'+str(timezone.get_current_timezone_name())})
    @token_required
    def get(self, request, *args, **kwargs):
        user = request.session.get('user_id')
        pending_requests = FriendRequest.objects.filter(to_user_id = user,status='pending')
        requests_data = [{'id': req.id, 'from_user': req.from_user.id, 'timestamp': req.timestamp} for req in pending_requests]
        
        return JsonResponse({'status':'success', 'message':'Pending friend requests', 'data':requests_data})

class FriendsListView(APIView):
    @token_required

    def get(self, request, *args, **kwargs):
        user = request.session.get('user_id')
        raw_query = "SELECT t.*, social_user.* FROM ( SELECT USER1_id as u_id FROM friendship WHERE USER2_id =2 UNION ALL SELECT USER2_id AS u_id FROM friendship WHERE USER1_id = 2 )  t LEFT JOIN social_user ON t.u_id = social_user.id;"
        friends = Friendship.objects.raw(raw_query)
        friends_data = [{'id': friend.id, 'email': friend.email, 'name': friend.name} for friend in friends]
        
        return JsonResponse({'status':'success', 'message':'Friends list', 'data':friends_data})


class FriendRequestActionView(APIView):
    @token_required

    def post(self, request, *args, **kwargs):
        user = request.session.get('user_id')
        
        action = request.data.get('action')

        if action not in ['accept','reject']:
            return JsonResponse({'status':'fail', 'message':'Invalid Action Passed'})

        request_id = request.data.get('request_id')

        req = FriendRequest.objects.filter(id=request_id, to_user_id = user,status='pending')
        


        if len(req) > 0 :
            if action == 'accept':
                req[0].status = 'accepted'

                friendship = Friendship()
                friendship.user1_id = req[0].from_user_id
                friendship.user2_id = req[0].to_user_id
                friendship.save()

            else:
                req[0].status = 'rejected'

            req[0].save()

            

            return JsonResponse({'status':'success', 'message':'Request '+ str(req[0].status)})

        else: 
            return JsonResponse({'status':'fail', 'message':'Invalid Request'})
