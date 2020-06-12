class Car:

    def __init__(self, model=None,
                 brand=None, year=None, oil=None, filtr=None, insurance=None, tech_check=None, air_tires=None):
        self.model = model
        self.brand = brand
        self.year = year
        self.brand = brand

    def __repr__(self):
        dic = self.__dict__

        return 'Car object:\n' + \
               '\n'.join([str(key) + ': ' + str(dic[key])
                          for key in dic])
