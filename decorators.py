from time import time


def authenticated(fn):
    """
    The authenticated decorator only allows the function to run if the user has key 'valid' set to True
    """
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper

def performance(fn):
    """
    The performance decorator measures the time taken to run a function
    """
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        return print(f'Time taken to run {fn} was {t2-t1}s')
    return wrapper

@authenticated
@performance
def message_friends(user):
    print('message sent to {}'.format(user['name']))


@performance
def long_time(num):
    for i in range(num):
        i*5


if __name__ == '__main__':
    # create a user to run the message friends functions
    user1 = {
        'name': 'Bobo',
        'valid': False
    }
    user2 = {
        'name': 'Toto',
        'valid': True
    }

    print()
    message_friends(user1)
    message_friends(user2)
    print()
    long_time(50000000)
    print()