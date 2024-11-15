class User :
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

user = User(1, 'HWT')
print(user.username)
print(user.user_id)
