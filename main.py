#from utility import *
from utility import multiply, divide
from shopping.more_shopping import shopping_cart
print(__name__)#__main__
#import random as m_random
from random import shuffle

if __name__ == '__main__':
    my_list = [1,2,3,4,5]
    shuffle(my_list)
    print(my_list)
    '''
    print(divide(4, 2))
    print(multiply(2, 2))
    print(shopping_cart.buy('apple'))
    print(max([1, 2, 3]))
    '''