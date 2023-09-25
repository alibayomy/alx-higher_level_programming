#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a // b
    except (UnboundLocalError, ZeroDivisionError):
        result = None
    finally:
        if result is None:
            print("Inside result: None")
            return result
        print("Inside result: {:.01f}".format(result))
        return result
