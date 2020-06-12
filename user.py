"""
AUTO_BOT OOP file

Developers: Andrey Kozlovsky, Stanislav Ermokhin

"""


class User:

    def __init__(self, email=None, name=None,
                 _password=None, phone=None,
                 registered_at_time=None,
                 city=None):
        self.email = email
        self.name = name
        self.password = _password
        self.phone = phone
        self.registered_at_time = registered_at_time
        self.city = city or 'Novosibirsk'

    def get_notification(self):
        pass

    def __repr__(self):
        dic = self.__dict__

        return 'User object:\n' + \
               '\n'.join([str(key) + ': ' + str(dic[key])
                          for key in dic])
