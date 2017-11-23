# -*- coding: utf-8 -*-

import openpyxl, time,os

from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook
'''
TODO 
ca ce 
create automatique if not exist
index par insertion

1 couche:
    tested with r'/home/bo/桌面/test/final test/5. 2016.03.07 LRP Mentions Légales et Données Personnelles.txt'
    4.12
    5.44
    5.59
    5.49
    tested with /home/bo/桌面/test/final test/2015_THE_MAKEUP_BOOK.txt
    32.02
    54.42
    33.68
    test with whole "final test"
    791.40
    
    
    
2 couches :
    tested with r'/home/bo/桌面/test/final test/5. 2016.03.07 LRP Mentions Légales et Données Personnelles.txt'
    9.01
    6.94
    6.94
    7.09
    tested with /home/bo/桌面/test/final test/2015_THE_MAKEUP_BOOK.txt
    16.10
    18.32
    37.54
    19.06
    test with whole "final test"
     test1  par simple add then sorted 619.93
     test2  par insertion 114.03
     test3  par insertion 157
     test4 failed with wrong code (302.7)
     test5 successful 129.90  (file '0' correctly registered)

    test /Google pour les pros/1. Ateliers GPLP
     test1: 356.33
    test Google pour les pros
    test1 1552.72
     
    test CAUDALIE
     tes1 223
     
    test Twitter
     test1 25.95 
'''
li = ['a', 'b','c']
print(li.pop())