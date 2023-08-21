def create_alphabet_dict():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {}
    for i, char in enumerate(alphabet):
        if(i+1 >= 10):
            alphabet_dict[char] = (i+1)*10
        else:
            alphabet_dict[char] = i+1
            
    return alphabet_dict
    
print(create_alphabet_dict())

def caesar_decrypt(encrypted_text):
    alphabet_dict = create_alphabet_dict()
    decrypted_text = ""
    for num_str in encrypted_text.split():
        if num_str.isdigit():
            num = int(num_str)
    
    print(num)
    
decrypted = caesar_decrypt('315045')

