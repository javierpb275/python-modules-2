#from utility import *
from utility import multiply, divide
from shopping.more_shopping import shopping_cart
print(__name__)#__main__

if __name__ == '__main__':
    print(divide(4, 2))
    print(multiply(2, 2))
    print(shopping_cart.buy('apple'))

    print(max([1, 2, 3]))