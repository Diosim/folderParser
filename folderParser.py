#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:45:13 2019

@author: diosim
"""
import os
#Python walks through the current directory and subfolders to scan
x = os.walk('.')

#array of a list with all folders
folders = [ x[0] for x in os.walk('.')]

#name of the file we search for
file = 'New Text Document.txt'

#filesList is a list with all folders containing the file we specified
fileslist = []
for i in folders:
    if file in os.listdir(i):
        fileslist.append(i)



for i in fileslist:
#reset info for each iteration
    t_email = ''
    t_name = ''
    t_zip = ''
    t_in = ''
    t_out = ''
    t_phone = ''
#    t_age = ''
    t_street = ''
    t_city = ''
    t_cuddle = ''
    t_feet = ''
    
#tparse alias and state from folder name
    rkey = i.rfind('/')
    r = i[rkey+1:]
    t_alias = r[:-2].title()
    t_state = r[-2:].upper()
    

#fn is the path of the 'file' which is to be used
    fn = i + "/" + file
#open each 'file'path we specified earlier and assign a useable encoding to it
    with open(fn, encoding="ISO-8859-1") as fp:
        
        for line in fp:
            line = str(line).strip()
            if 'name:' in line.lower():
                colkey = line.rfind(':')
                t_name = line[colkey+1:].strip().title()
            if 'email:' in line.lower():
                colkey = line.rfind(':')
                t_email = line[colkey+1:].strip().lower()
            if 'zip code:' in line.lower():
                colkey = line.rfind(':')
                t_zip = line[colkey+1:].strip()
                t_zip = t_zip[:5]
            if 'incall:' in line.lower():
                colkey = line.rfind(':')
                t_in = line[colkey+1:].strip().title()
            if 'outcall:' in line.lower():
                colkey = line.rfind(':')
                t_out = line[colkey+1:].strip().title()
                
            if 'shoe size:' in line.lower():
                t_feet = 'feet'
                
            if 'person and cuddle with them' in line.lower():
                t_cuddle = 'sb'

#either bugs out or there is varying info in this field
#            if 'age:' in line.lower():
#                colkey = line.rfind(':')
#                t_age = line[colkey+1:].strip()
            
            if 'street address:' in line.lower():
                colkey = line.rfind(':')
                t_street = line[colkey+1:].strip().title()
            if 'phone:' in line.lower():
                colkey = line.rfind(':')
                t_phone = line[colkey+1:].strip()
            if 'city:' in line.lower():
                colkey = line.rfind(':')
                t_city = line[colkey+1:].strip().title()
        
        
        with open('accounts.txt','a') as fa:
            fa.write("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n".format(t_state, t_alias, t_zip, t_name, t_email, t_phone, t_in, t_out, t_street, t_city, t_cuddle, t_feet))
        print("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(t_state, t_alias, t_zip, t_name, t_email, t_phone, t_in, t_out, t_street, t_city, t_cuddle, t_feet))
            

