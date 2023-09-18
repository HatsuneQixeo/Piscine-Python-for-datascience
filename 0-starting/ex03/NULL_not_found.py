def NULL_not_found(object: any) -> int:
    if object != object:
        prefix = "Cheese"
    elif object is None:
        prefix = "Nothing"
    elif object is False:
        prefix = "Fake"
    elif object == 0:
        prefix = "Zero"
    elif isinstance(object, str) and not (object and object.isprintable()):
        prefix = "Empty"
    else:
        print("Type not found")
        return 1
    print(f"{prefix}: {object} {type(object)}")
    return 0
