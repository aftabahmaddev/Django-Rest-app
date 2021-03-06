import jwt
import datetime
from django.conf import settings
 
def generate_access_token(user):
    payload={
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.datetime(minute=60),
        'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

