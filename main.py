from __future__ import print_function


## Below are the rudimentary controls for the variables.
faithfulness = 4
generations = 4
transformation = 0


## Building a basic text network

for gen in range(generations):

    print("\n|")
    ## print(gen)

    for mark in range(gen + 1):
        
        for faith in range(faithfulness):
            print("x", end = ' ')
   