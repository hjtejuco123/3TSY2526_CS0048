class NameErrorCustom(Exception):
    pass

try:
    name = ""

    if name.strip() == "":
        raise NameErrorCustom("Name cannot be empty.")

except NameErrorCustom as e:
    print(e)