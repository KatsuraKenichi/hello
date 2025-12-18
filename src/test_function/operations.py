def parse_int(s):
    try:
        return int(s)
    except Exception:
        raise ValueError("invalid integer")


def compute(op, a, b):
    if op == 'mul':
        return a * b
    if op == 'div':
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    raise ValueError("invalid op")
