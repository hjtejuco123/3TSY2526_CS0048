try:
    name = ""

    if name == "":
        raise Exception("Name cannot be empty.")

    print("Name entered:", name)

except Exception as e:
    print("Error:", e)