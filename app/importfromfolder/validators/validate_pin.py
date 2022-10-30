def validate_pin(pin):
    if not pin.isdigit():
        return False
    if len(pin) != 4:
        return False
    return True