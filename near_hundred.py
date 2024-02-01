
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

# in range will include the first int but not the second
def near_hundred(n):
    if n  in range(90,111):
        return True
    elif n in range(190,211):
        return True
    else:
        return False