from datetime import datetime

def limit(g):
    def wrapper():
        if 9 < datetime.now().hour < 22:
            print('ok')
            g()
        else:
            print('not now')
    return wrapper

@limit
def game():
    print("gaming")

game()

