import random
def rand_qgen(length, dfilter, date):
    chars = "abcdefghijklnopqrstuvwxyz1234567890_-"
    inurl = ""
    for i in range(length):
        inurl += random.choice(chars)

    if dfilter == True:
        query = f"inurl:{inurl} before:{date}"
    else:
        query = f"inurl:{inurl}"
    return query