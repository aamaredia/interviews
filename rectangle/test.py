from solution import find_rectangle

#TODO: Auto generated images would be rad
image = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

image1 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

image2 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
]

image3 = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

image4 = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

image5 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
]

image6 = [
    [0],
]

image7 = [
    [0, 0, 0, 0],
]

assert find_rectangle(image) == ((1, 2), (3, 4))
assert find_rectangle(image1) == ((1, 2), (3, 2))

assert find_rectangle(image2) == ((3, 0), (4, 1))
assert find_rectangle(image3) == ((0, 2), (1, 3))
assert find_rectangle(image4) == ((0, 0), (1, 1))
assert find_rectangle(image5) == ((3, 2), (4, 3))

assert find_rectangle(image6) == ((0, 0), (0, 0))
assert find_rectangle(image7) == ((0, 0), (0, 3))
