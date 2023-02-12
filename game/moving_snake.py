def move_body_parts(way: str, a: float, pix: float) -> float:
    if way == "up" or way == "left":
        a -= pix
        return a
    elif way == "down" or way == "right":
        a += pix
        return a


"""
    if way == "up":
        y -= PIXEL
    elif way == "down":
        y += PIXEL
    elif way == "left":
        x -= PIXEL
    elif way == "right":
        x += PIXEL
"""