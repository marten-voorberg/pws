import time


def timer(function):
    def wrapper():
        t1 = time.time()
        function()
        t2 = time.time()
        # return "Time it took to run the function: " + str((t2 - t1)) + "\n"
        print('It took {} seconds to run the function'.format(t2 - t1))
    return wrapper
