from user_auth.models import LoginRecord 

def verify_token(token):
    login_data = LoginRecord.objects.filter(token=token).first()
    if login_data :
        return {'status':'success','user_id':login_data.user_id}
    
    return {'status':'fail'}