#!/usr/bin/python3

"""
    Determines if all boxes can be opened.

    Args: boxes (list)- A list of lists representing the boxes.

    Returns: bool- True if all boxes can be opened, False otherwise.
"""

def can_unlock_all(boxes):
   
    # Check if the boxes list is empty
    if len(boxes) == 0:
        return False

    keys = [0]  # Start with the key to the first box
    visited = [False] * len(boxes)  # Track visited boxes

    # Iterate through the keys
    while keys:
        box = keys.pop()
        visited[box] = True

        # Iterate through the keys in the current box
        for key in boxes[box]:
            # Check if the key is within the valid range and the corresponding box is not visited
            if key < len(boxes) and not visited[key]:
                keys.append(key)

    # Check if all boxes are visited
    return all(visited)

