from stack import Stack

def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{"