#from utility import *
#from utility import multiply, divide
#from shopping.more_shopping import shopping_cart
#print(__name__)#__main__
#import random as m_random
#from random import shuffle
#import sys
#import pyjokes
#from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

if __name__ == '__main__':
    print(datetime.time())#00:00:00
    print(datetime.time(10,36,15))#10:36:15
    print(datetime.date.today())#2021-11-14
    arr = array('i', [1,2,3])
    print(arr[0])#1
    '''
    li = [1,2,3,4,5,6,7,7]
    sentence = 'blah blah blah whatever you want'
    print(Counter(li)) #Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
    print(Counter(sentence))#Counter({'a': 5, ' ': 5, 'h': 4, 'b': 3, 'l': 3, 'w': 2, 't': 2, 'e': 2, 'v': 1, 'r': 1, 'y': 1, 'o': 1, 'u': 1, 'n': 1})
    dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
    print(dictionary['c'])#does not exist
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d2 = OrderedDict()
    d2['a'] = 2
    d2['b'] = 1
    print(d2 == d) #False
    print(pyjokes.get_joke('en', 'neutral'))
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    print(f'hello {first_name} {last_name}')
    my_list = [1,2,3,4,5]
    shuffle(my_list)
    print(my_list)
    print(divide(4, 2))
    print(multiply(2, 2))
    print(shopping_cart.buy('apple'))
    print(max([1, 2, 3]))
    '''