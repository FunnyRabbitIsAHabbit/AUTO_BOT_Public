class Payment:

    def __init__(self, payment_time=None):
        self.payment_time = payment_time

    def __repr__(self):
        dic = self.__dict__

        return 'Payment object:\n' + \
               '\n'.join([str(key) + ': ' + str(dic[key])
                          for key in dic])
