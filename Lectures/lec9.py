'''
lec 9
define class
'''

import lec4
print(my_car)

#def report_maker(input):
#    return input

class car:
    maker='toyota'
    def __init__(self,input_model):
        self.model=input_model
    def report(self):
        return self.maker,self.model
#my_car_instance=car('highlander')
#print(my_car_instance.maker)
#print(my_car_instance.model)

my_camry=car('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())

my_camry.maker='Ford'
print(my_camry.report())