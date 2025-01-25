class User :
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authentication (function) :
    def wrapper_function (*args) :
        if args[0].is_logged_in == True :
            function(args[0])
    return wrapper_function


@is_authentication
def create_blog (user) :
    print(f'This is {user.name} new blog post')

new_user = User('HWT')
new_user.is_logged_in = True
create_blog(new_user)