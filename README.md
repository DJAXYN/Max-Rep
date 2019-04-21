#Calculate the Maximum Weight for Weightlifting exercises

Exercising is important, so is being safe while lifting weights. The idea of a '1 Rep Max' is the maximal weight they could lift safely for one repetition. This can be figured out by increasing weights until you fail. Which is dangerous!! Conversely you can take a users current amount of weights they can lift and the number of reps they did at that weight.

So there will be two *required* arguments ` -w/--weight, -r/--reps` and using a formula will output the 1 rep max weight the user should be lifting.

Formula

'''
Epley formula

    1  RM = w ( 1 + r 30 )

Where w is the weight the user was able to lift and r is the number of reps
'''

#Expected usage:
```
(base) Jasons-MacBook-Air:14-open jasongiles$ ./max_rep.py
usage: max_rep.py [-h] -w str -r str
max_rep.py: error: the following arguments are required: -w/--weight, -r/--reps
```

You will right a program called `max_rep.py`. Which will take the two arguments, incorporate the formula and output the following:

#Expected Behavior

```
(base) Jasons-MacBook-Air:14-open jasongiles$ ./max_rep.py -w 200 -r foo
the value given 'foo' is not a digit
```

```
Based upon your 5 reps at a weight of 200 lbs, your 1 rep max is 233.33 lbs

Happy Lifting
```

The 2nd line `happy lifting` will be printed after a ~time delay.

#Test Suite

The Test suite will check usage, bad input, and combinations of reps and weight. 
