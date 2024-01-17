#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Method to check if all boxes can be opened"""
    i = 0
    length_of_boxes = len(boxes)
    keys = set()

    while i < length_of_boxes - 1:
        current_boxes = boxes[i]

        # check each box in current_box for next index
        next_index = i + 1
        for key in current_boxes:
            if key == next_index:
                # current box has the key to open the next box
                keys.add(next_index)
                break
            elif 0 < key < length_of_boxes:
                # key exist in boxes add to keys
                keys.add(key)
        # check if keys had next index or any index that exists in boxes

        print(keys)
        if next_index in keys:
            # contains next index
            i += 1
        elif check_for_x(next_index, keys, length_of_boxes):
            i += 1
        else:
            return False
    return True



def check_for_x(min, arr, max):
    """Check for x"""

    for x in arr:
        if min < x < max:
            return True
    return False
