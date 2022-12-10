

def login():
    while True:
        try:
            print('pls insert your password_')
            print('if u are a new user just create one_')
            print('must be at leat a 2 digits number_')
            user = int(input('password_'))

            if len(str(user)) < 2:
                raise ValueError

            return user
        except ValueError:
            print('error!')
