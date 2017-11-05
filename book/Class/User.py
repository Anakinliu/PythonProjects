class User:
    """

    """

    def __init__(self, first_name, last_name, age, nick_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nick_name = nick_name
        self.login_attempts = 0

    def describe(self):
        print("nick name: %s, name: %s-%s, age: %d" %
              (self.nick_name, self.first_name, self.last_name, self.age))

    def greet_user(self):
        print("hi, " + self.nick_name + " !")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


me = User("yin quan", "liu", 20, "aa")
me.greet_user()
me.describe()
me.increment_login_attempts()
print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)