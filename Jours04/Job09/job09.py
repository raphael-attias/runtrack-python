l = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
max_ = None
for num in l:
    if (max_ is None or num > max_):
        max_ = num
l.index(max_)
print('Max:', max_, "position : ", l.index(max_)+1)
min_ = None
for nim in l:
    if (min_ is None or nim < min_):
        min_ = nim
l.index(min_)
print('min:', min_, "position : ", l.index(min_)+1)
