# define function
def check_duplicate(data):
    if len(data) == set(data):
        return True
    else:
        return False


# calling function
print(check_duplicate([1, 2, 3, 4, 5]))
