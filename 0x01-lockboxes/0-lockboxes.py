#!/usr/bin/python3

'''
    Determines if all boxes can be opened.

    Args: boxes (list): A list of lists representing the boxes.

    Returns: bool: True if all boxes can be opened, False otherwise.
'''

def canUnlockAll(boxes):
    
''' Check if the boxes list is empty '''
    if len(boxes) == 0:
        return False

''' Start with the key to the first box '''

    keys = [0]
 
'''Track visited boxes ''' 
    visited = [False] * len(boxes) 

    while keys:
        box = keys.pop()
        visited[box] = True

        for key in boxes[box]:
            if key < len(boxes) and not visited[key]:
                keys.append(key)

    return all(visited)

