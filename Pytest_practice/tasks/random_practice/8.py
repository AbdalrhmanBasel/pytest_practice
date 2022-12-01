list = ["Hello", "this", "is", "Abdelrhman!"]


def stringify(list):
    return ' '.join(str(e) for e in list)


print(stringify(list))
