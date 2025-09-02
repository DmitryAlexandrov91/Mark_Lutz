def adder(*args):
    if not args:
        return None
    if len(args) == 1:
        return args[0]
    res = args[0]
    for x in args[1:]:
        res += x
    return res
