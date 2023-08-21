my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 100, 'k': 110, 'l': 120, 'm': 130, 'n': 140, 'o': 150, 'p': 160, 'q': 170, 'r': 180, 's': 190, 't': 200, 'u': 210, 'v': 220, 'w': 230, 'x': 240, 'y': 250, 'z': 260}
keys_to_lookup = [3,150,4,5]

for key in keys_to_lookup:
    str_key = str(key)  # Convert integer key to a string
    corresponding_key = next((k for k, v in my_dict.items() if v == key), None)
    
    if corresponding_key:
        value = my_dict[corresponding_key]
        print(corresponding_key)
    else:
        print(f"No key with value {key} exists in the dictionary.")
