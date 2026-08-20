UNIT_TO_GRAM = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "oz": 28.3495,
    "lb": 453.592,
}


def Weight_Convert(Unit, froms, to):
    gram = Unit * UNIT_TO_GRAM[froms]
    conversion = gram / UNIT_TO_GRAM[to]
    return conversion


if __name__ == "__main__":
    Unit = 1
    froms = "mg"
    to = "g"
    print(Weight_Convert(Unit, froms, to))
