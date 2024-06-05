from django.http import JsonResponse
from functools import wraps
from .utils import verify_token

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        request = args[1] 
        try:
            token = request.headers.get('token')
        except:
            token = ''
        
        tk = verify_token(token)
        if tk['status'] == 'fail':
            return JsonResponse({'status': 'fail', 'message': 'Invalid Login Token'})
        request.session['user_id'] = tk['user_id']
        return func(*args, **kwargs)
    return decorated
