# Adds 5 to desired function
def add_five(function):
    def wrapper(*args):
        return function(*args) + 5
    return wrapper


@add_five
def multiply(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    print 'Please enter two numbers to multiply.' 
    num1 = int(raw_input('Number 1: '))
    num2 = int(raw_input('Number 2: '))
    print 'Before decorator: {0}'.format((num1 * num2))
    print 'After add5 decorator: {0}'.format(( multiply(num1, num2)))
