UNIT_TO_METER = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}

def Convert(Units:int|float, froms:dict.keys, to):
    meter = Units * UNIT_TO_METER[froms]
    conversion = meter/UNIT_TO_METER[to]

    return conversion

if __name__ == "__main__":
    froms = "km"
    to = "cm"

    print(Convert(0.3, froms, to))