def script(check, x, y):
    if check("gold", x, y) > 0:
        return "take"
    elif check("level") == 1:
        if check("gold", x, y) > 0:
            return "take"

        if check("wall", x + 2, y):
            return "down"

        return "right"

    elif check("level") == 2:
        if check("gold", x, y + 1) or check("gold", x, y + 2):
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
        if (check("wall", x, y + 1) or check("wall", x - 1, y + 1)) and not check("wall", x - 1, y):
            return "left"

        elif (check("wall", x, y - 1) or check("wall", x + 1, y - 1)) and not check("wall", x + 1, y):
            return "right"

        elif check("wall", x - 1, y) or check("wall", x - 1, y - 1) and not check("wall", x, y - 1):
            return "up"

        elif check("wall", x + 1, y) or check("wall", x + 1, y + 1) or check("wall", x + 1, y - 1):
            return "down"

    elif check("level") == 4:
        if not check("wall", x - 1, y) and check('wall', x + 1, y - 1) \
                and check('wall', x + 1, y - 2) and check('wall', x - 2, y - 1) \
                and check('wall', x - 2, y - 2) and check('wall', x - 3, y - 2) and check('wall', x - 3, y - 1):
            return "left"

        elif not check("wall", x + 1, y) and check('wall', x - 1, y + 1) \
                and check("wall", x - 2, y + 1) and check('wall', x - 1, y + 2) \
                and check('wall', x - 2, y + 2) and check("wall", x + 2, y + 1):
            return "right"

        elif check("wall", x + 1, y + 1) and not check("wall", x, y - 1):
            if check("wall", x + 1, y):
                return "up"
            return "right"

        elif check("wall", x - 1, y + 1):
            if not check("wall", x, y + 1):
                return "down"
            return "right"

        elif check("wall", x + 1, y - 1):
            if not check("wall", x, y - 1):
                return "up"
            return "left"

        elif check("wall", x - 1, y - 1):
            if not check("wall", x - 1, y):
                return "left"
            return "down"
