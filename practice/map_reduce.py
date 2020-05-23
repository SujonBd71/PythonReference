
    #The built-in function map() takes a function as a first 
    # argument and applies it to each of the elements of its 
    # second argument, an iterable
def map_test():
    def capitalize(x):
         return x.capitalize()
    
    # l = list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
    l = list(map(capitalize, ['cat', 'dog', 'cow']))
    print(l)


#filter is used to validate data
#since always return true false

def filter_test():
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

    def is_A_student(score):
        return score > 75

    over_75 = list(filter(is_A_student, scores))
    print(over_75)


#reduce applies a function of two
#arguments cumulatively to the elements of an iterable,
def reduce_test():
    # Python 3
    from functools import reduce
    numbers = [1, 3, 5, 6]

    def custom_sum(first, second):
        return first * second

    result = reduce(custom_sum, numbers)
    print(result)



map_test()
filter_test()
reduce_test()



