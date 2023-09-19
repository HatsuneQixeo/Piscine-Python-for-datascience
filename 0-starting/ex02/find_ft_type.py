def all_thing_is_obj(object: any) -> int:
    typename = type(object)
    name = typename.__name__

    if name in ("list", "tuple", "set", "dict"):
        prefix = name.capitalize()
    elif name == "str":
        prefix = f"{object} is in the kitchen"
    else:
        print("Type not found")
        return 42
    print(f"{prefix} : {typename}")
    return 42
