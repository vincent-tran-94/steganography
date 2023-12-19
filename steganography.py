from PIL import Image
import numpy as np

image_path = "./images/genshin.png"

def lsb_1(image_path,message): 
    img = Image.open(image_path)
    img_array = np.array(img)
    message_to_binary = [int(bin_number) for bin_number in ''.join(format(ord(char), '08b') for char in message)] #Conversion texte en binaire
    img_array -= img_array % 2 #Passage des pixels pour des nombres paires

    numbers_rows , numbers_cols, numbers_color = img_array.shape

    index_binary = 0
    for index_row in range(0,numbers_rows):
        for index_cols in range(0,numbers_cols):
            for index_color in range(0,numbers_color):
                if  index_binary < len(message_to_binary):
                    img_array[index_row,index_cols,index_color] = message_to_binary[index_binary]
                else:
                    break
                index_binary += 1
                
    return img_array


def decode_message():
        img = lsb_1(image_path,'coucou les loulous')%2
        numbers_rows , numbers_cols, numbers_color = img.shape
        binary_message = []
        for index_row in range(0,numbers_rows):
            for index_cols in range(0,numbers_cols):
                for index_color in range(0,numbers_color):
                    pixel_value = img[index_row,index_cols,index_color] 
                    binary_message.append(str(pixel_value))
        binary_message = "".join(binary_message)

        # Convertir la séquence binaire en une chaîne de caractères
        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
        print(message)
        return message

decode_message()
