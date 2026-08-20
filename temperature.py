def Celsius_Convert(value, to_unit):
    if to_unit == "F":
        return (value * 9 / 5) + 32
    elif to_unit == "K":
        return value + 273.15
    else:
        return value


def Fahrenheit_Convert(value, to_unit):
    if to_unit == "C":
        return (value - 32) * 5 / 9
    elif to_unit == "K":
        return (value - 32) * 5 / 9 + 273.15
    else:
        return value


def Kelvin_Convert(value, to_unit):
    if to_unit == "C":
        return value - 273.15
    elif to_unit == "F":
        return (value - 273.15) * 9 / 5 + 32
    else:
        return value


def Temperature_Convert(value, from_unit, to_unit):
    if from_unit == "C":
        return Celsius_Convert(value, to_unit)

    elif from_unit == "F":
        return Fahrenheit_Convert(value, to_unit)

    elif from_unit == "K":
        return Kelvin_Convert(value, to_unit)


if __name__ == "__main__":
    print(Temperature_Convert(0, "C", "F"))
    print(Temperature_Convert(32, "F", "C"))
    print(Temperature_Convert(0, "C", "K"))
