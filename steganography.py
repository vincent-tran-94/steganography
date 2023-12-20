from PIL import Image
import numpy as np

image_path = "./images/genshin.png"

def lsb_1(image_path,message):  #Taille de 3 dimensions pour le RGB
    img = Image.open(image_path)
    img_array = np.array(img)
    message_to_binary = [int(bin_number) for bin_number in ''.join(format(ord(char), '08b') for char in message)] #Conversion texte en binaire
    img_array -= img_array % 2 #Passage des pixels pour des nombres paires
    print('Passage des pixels',img_array)
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

def lsb_2(image_path,message):  #Taille de 2 dimensions en nuance gris 
    img = Image.open(image_path)
    img = img.convert("L")
    img_array = np.array(img)
    message_to_binary = [int(bin_number) for bin_number in ''.join(format(ord(char), '08b') for char in message)] #Conversion texte en binaire
    img_array -= img_array % 2 #Passage des pixels pour des nombres paires
    print('Passage des pixels',img_array)
    numbers_rows , numbers_cols = img_array.shape

    index_binary = 0
    for index_row in range(0,numbers_rows):
        for index_cols in range(0,numbers_cols):
                if  index_binary < len(message_to_binary):
                    img_array[index_row,index_cols] = message_to_binary[index_binary]
                else:
                    break
                index_binary += 1
                
    return img_array

def save_img_gray(image_path):
    img = Image.open(image_path)
    img = img.convert("L")
    img.save("images/genshin_gray.jpg")

def decode_message_lsb1():
        img = lsb_1(image_path,'coucou les loulous')%2 #Extraire tout les informations en binaire pour récupérer le message dans l'image
        print(img)
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
        return message

def decode_message_lsb2():
        img = lsb_2(image_path,'coucou les loulous')%2 
        print(img)
        numbers_rows , numbers_cols = img.shape
        binary_message = []
        for index_row in range(0,numbers_rows):
            for index_cols in range(0,numbers_cols):
                pixel_value = img[index_row,index_cols] 
                binary_message.append(str(pixel_value))
        binary_message = "".join(binary_message)

        # Convertir la séquence binaire en une chaîne de caractères
        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
        return message


save_img_gray(image_path)
#print(lsb_1(image_path,'coucou les loulous'))
#print(lsb_2(image_path,'coucou les loulous'))
#print(decode_message_lsb1()) 
#print(decode_message_lsb2()) 


