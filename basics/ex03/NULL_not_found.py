def NULL_not_found(object: any) -> int:
    dict = {
        "NoneType": "Nothing",
        "str": "Empty",
        "int": "Zero",
        "bool": "Fake",
    }

    prefix = dict.get(type(object).__name__)
    if object != object:
        prefix = "Cheese"
    elif bool(object) or prefix is None:
        print("Type not found")
        return 1
    print(f"{prefix}: {object} {type(object)}")
    return 0
