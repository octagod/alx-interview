#!/usr/bin/python3
""" Minimum operations"""



def minOperations(n):
    """Minimum operations
    Actions: copyAll & paste
    copyAll -> Gets existing character(s) and save in a variable e.g copy_all
    paste -> gets chars in copy_all and appends to original chars value
    """
    chars = "H"
    action_counter = 0
    # operatons: copyAll and paste
    # * paste => paste = copy_all => chars = chars + paste 

    # determine if n is odd or even
    is_odd = isNOdd(n)

    if n > 1:
        if is_odd:
            action_counter = handle_odd(chars, n)
            return action_counter
        else:
            action_counter = handle_even(chars, n)
            return action_counter
    else:
        return 0


def handle_even(chars, n):
    """Handle even n"""
    counter = 0
    # to get res for odd numbers actions required CPPCPPi
    # where C is copy all action and P is paste action and i is the sumation 1 to infinity
    copy_all = copyAll(chars=chars)
    counter += 1
    res = pasteAction(copy_all=copy_all, chars=chars)
    counter += 1
    copy_all = copyAll(chars=res)
    counter += 1
    if len(res) == 2:
        while True:
            res = pasteAction(copy_all=copy_all,chars=res)
            counter += 1
            if len(res) == n:
                return counter
            elif len(res) > n:
                return 0



def handle_odd(chars, n):
    """Handle odd n"""
    counter = 0
    # to get res for even numbers actions required CPCPi
    # where C is copy all action and P is paste action and i is the sumation 1 to infinity
    copy_all = copyAll(chars=chars)
    counter += 1
    res = pasteAction(copy_all=copy_all, chars=chars)
    counter += 1
    res = pasteAction(copy_all=copy_all, chars=res)
    counter += 1
    copy_all = copyAll(chars=res)
    counter += 1
    if len(res) == 3:
        while True:
            res = pasteAction(copy_all=copy_all,chars=res)
            counter += 1
            res = pasteAction(copy_all=copy_all,chars=res)
            counter += 1
            if len(res) == n:
                return counter
            elif len(res) > n:
                return 0



def copyAll(chars):
    """Copy All action"""
    return chars


def pasteAction(copy_all, chars):
    """Paste Action"""
    paste = copy_all
    chars = chars + paste
    return chars


def isNOdd(n):
    """Check if n is odd"""
    if n % 2 == 1:
        return True
    return False
