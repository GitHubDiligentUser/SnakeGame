def move(set_direction: str, way: str) -> str:
    if set_direction == 'left' and way != 'right':
        way = set_direction
    elif set_direction == 'right' and way != 'left':
        way = set_direction
    elif set_direction == 'up' and way != 'down':
        way = set_direction
    elif set_direction == 'down' and way != 'up':
        way = set_direction
    return way
