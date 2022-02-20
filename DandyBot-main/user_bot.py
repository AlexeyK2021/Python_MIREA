def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y) > 0:
            return "take"

        if check("wall", x + 2, y):
            return "down"

        return "right"

    elif check("level") == 2:
        if check("gold", x, y) > 0:
            return "take"

        elif check("gold", x, y + 1) or check("gold", x, y + 2):
            return "down"

        elif check("gold", x, y - 1) or check("gold", x, y - 2):
            return "up"

        elif check("gold", x - 1, y) or check("gold", x - 2, y):
            return "left"

        elif check("gold", x + 1, y) or check("gold", x + 2, y):
            return "right"

        elif x < 1:
            return "right"

        elif y > 5:
            return "up"

    elif check("level") == 3:
        if check("gold", x, y) > 0:
            return "take"

        elif (check("wall", x, y + 1) or check("wall", x - 1, y + 1)) and not check("wall", x - 1, y):
            return "left"

        elif (check("wall", x, y - 1) or check("wall", x + 1, y - 1)) and not check("wall", x + 1, y):
            return "right"

        elif check("wall", x - 1, y) or check("wall", x - 1, y - 1) and not check("wall", x, y - 1):
            return "up"

        elif check("wall", x + 1, y) or check("wall", x + 1, y + 1) or check("wall", x + 1, y - 1):
            return "down"

    elif check("level") == 4:
        print(f"x={x}; y={y}")
        if check("gold", x, y) > 0:
            return "take"
        elif check("wall", x + 1, y):
            return "up"
        elif check("wall", x, y + 1) or check("wall", x + 2, y + 1) and check("wall", x + 2, y + 2):
            return "right"
        elif check("wall", x - 1, y+1) and not check("wall", x, y + 1):
            return "down"
