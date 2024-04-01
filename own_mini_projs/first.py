#Function verifying input only numbers
def inp():
    return input("Enter value please: ")


# print(type(ent_val))
# print(type(ent_val))


while not isinstance(ent_val, int):
    try:
        ent_val = int(inp())
        break
    except:
        print("Enter one more time")
        ent_val = int(inp())


