alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

direction = input('Type Encode to encrypt, type decode to decrypt:\n').lower()
text = input('Type Your message : \n').lower()
shift = int(input('Type the shift number : \n'))

def password_creator(text, shift, identifier) :
    chiper_text = ''

    for letter in text :
        if identifier == 'decode' :
            shift *= -1
        else :
            formatted_index = alphabet.index(letter) + shift
            formatted_index = formatted_index % len(alphabet)
            chiper_text += alphabet[formatted_index]
    
    print(chiper_text)

password_creator(identifier=direction, text=text, shift=shift)
    
    

    
    


