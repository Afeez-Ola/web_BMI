def sum_of_even(n):
    try:
        result = None
        if isinstance(n, int):
            result = n * (n+1)
        return result
    except ValueError as error:
        return str(error)


print(sum_of_even(20))
