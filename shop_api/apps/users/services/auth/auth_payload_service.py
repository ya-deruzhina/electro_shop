class AuthPayloadService:
    @classmethod
    def _get_user_payload(cls, user):
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'status': user.status,
        }

    @classmethod
    def call(cls, user, token):
        return {
            'user': cls._get_user_payload(user),
            'token': token,
        }
