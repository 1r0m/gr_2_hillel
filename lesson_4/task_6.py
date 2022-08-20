lst = [-9, 29, -100, 64, 26, 73, -96, 28, -92, 11, -14, -86, -54, -67]
print([(x, (lst[i], lst[i+2])) for i, x in enumerate(lst[1:-1]) if x > lst[i] and x > lst[i+2]])