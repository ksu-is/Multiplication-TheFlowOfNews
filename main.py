from __future__ import print_function
import random


## Below are the rudimentary controls for the variables.
faithfulness = 1
generations = 4
diversion = 2
count = 0
base = 1
health = "L"
healthfile = open("healthline.txt", "w")


## Building a basic text network

for gen in range(generations):

    ## count = 0
    print("\n| -- Gen:", gen + 1)
    healthfile = open("healthline.txt", "a+")


    ## here, had to study about how 'to the power of' can be done in python.
    for mark in range(base ** faithfulness):
        
        health = ord(health)
        unhealth = random.randint((-1 * diversion), diversion)
        health = health + unhealth
        health = chr(health)
        count += 1
        ## print(health, end = '')
        ## print("(" + str(count) + ")", end = '')
        ## healthfile.write(health)
        healthfile.write("(" + health + ", #" + str(count) + ") ")
        base += 1
        

    healthfile = open("healthline.txt", "r")
    flow = healthfile.read()
    print()
    print(flow)
    print("here")

    ##for mark in range(gen + 1):
        
        ##for faith in range(faithfulness * (mark + 1)):
            ##print("x", end = ' ')

## possibility: create text file, store variables change, call in each generation, then append new adds.
   


healthfile.close()