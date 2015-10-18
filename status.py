def stats(values):
    """Define a function which given an input of values, will return the min, ave, max
        RED GREEN REFACTOR
    """

    least = min(values)
    greatest = max(values)
    average = 0
    for num in values:
        average += num
    average /= float(len(values))
    return [least, average, greatest]  # needs some work

# I assert that if you call stats function with [0,1,0,1] you will get [0, 0.5, 1]
assert stats([0, 1, 0, 1]) == [0, 0.5, 1]
assert stats([0, 1, 100]) == [0, 101.0/3.0, 100]
assert stats([0, 1, 2, 3, 4, 5]) == [0, 2.5, 5]

#print stats([0, 1, 100]);
