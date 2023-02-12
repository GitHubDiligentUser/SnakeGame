def check_hit(width: float, height: float, animal) -> bool:
    x, y = animal.coordinates[0]  # these are coordinates of the first body segment - the head
    # when the snake is out of the range, the function returns true
    if x < 0 or x >= width:
        return True
    elif y < 0 or y >= height:
        return True

    for body_part in animal.coordinates[1:]:  # everything after the head of the snake
        if x == body_part[0] and y == body_part[1]:
            return True
    # otherwise - if we come here, it means the snake is still in the range
    return False


"""
def check_hit(animal) -> bool:
    x_head, y_head = animal.coordinates[0]  # these are coordinates of the first body segment - the head
    return crash_or_not.crash(x_head, y_head, GAME_WIDTH, GAME_HEIGHT, animal)
"""