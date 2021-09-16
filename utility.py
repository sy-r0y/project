

def find_max(list):

    maximum = list[0]

    for item in list:
        if item > maximum:
            maximum = item

    return maximum

