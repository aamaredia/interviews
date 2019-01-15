def reverse_index(list_, element):
    return len(list_) - list_[::-1].index(element) - 1

def find_rectangle(image):
    for x_position, row in enumerate(image):
        if sum(row) != len(row):
            first_y_position = row.index(0)
            first = (x_position, first_y_position)
            break
    else:
        # Even though problem given assumed a rectangle always exists
        raise Exception('No rectangle found')

    for x_position, row in enumerate(image[first[0]:], start=first[0]):
        if sum(row) != len(row):
            last = (x_position, reverse_index(row, 0))
        else:
            break

    return first, last
