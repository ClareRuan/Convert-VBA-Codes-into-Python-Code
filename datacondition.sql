# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:31:51 2023

@author: cr_ru
"""

"""syntax for mysql here"""
Drop table if exists Customers;
Create table Customers (
    id integer primary key auto-increment,
    name varchart(30) not null,
    age integer,
    score real
    ); 