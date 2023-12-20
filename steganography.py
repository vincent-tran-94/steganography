from PIL import Image
import numpy as np
from cesar import viginere_cypher

image_path = "./images/genshin.png"
image_save_encode_path = "./images/watermarked_image.jpg"
#message = "coucou les loulous" 
message = viginere_cypher("coucou les loulous","Azerty12345") 

def lsb_1(image_path,message):  #Taille de 3 dimensions pour le RGB
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

    #pil_image = Image.fromarray(img_array)
    #pil_image.save(image_save_encode_path )
    #pil_image.show()

    return img_array

def lsb_2(image_path,message):  #Taille de 2 dimensions en nuance gris 
    img = Image.open(image_path)
    img = img.convert("L")
    img_array = np.array(img)
    message_to_binary = [int(bin_number) for bin_number in ''.join(format(ord(char), '08b') for char in message)] #Conversion texte en binaire
    img_array -= img_array % 4*255 #Passage des pixels pour des nombres paires
    #print('Passage des pixels',img_array)
    numbers_rows , numbers_cols = img_array.shape
    index_binary = 0
    for index_row in range(0,numbers_rows):
        for index_cols in range(0,numbers_cols):
                if  index_binary < len(message_to_binary):
                    img_array[index_row,index_cols] = message_to_binary[index_binary]
                else:
                    break
                index_binary += 1
    
    pil_image = Image.fromarray(img_array)
    pil_image.show()
                
    return img_array

def save_img_gray(image_path):
    img = Image.open(image_path)
    img = img.convert("L")
    img.save("images/genshin_gray.jpg")


def decode_message_lsb1(image_path,message):
        img = lsb_1(image_path,message) %2 #Extraire tout les informations en binaire pour récupérer le message dans l'image
    
        numbers_rows , numbers_cols, numbers_color = img.shape
        binary_message_list = []

        for index_row in range(0,numbers_rows):
            for index_cols in range(0,numbers_cols):
                for index_color in range(0,numbers_color):
                    pixel_value = img[index_row,index_cols,index_color] 
                    binary_message_list.append(str(pixel_value))
                    if binary_message_list[-8:] == ['0']*8:
                        binary_message = "".join(binary_message_list)
                        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
                        return message
        


def decode_message_lsb2():
        img = lsb_2(image_path,"coucou les loulous")%4

        numbers_rows , numbers_cols = img.shape
        binary_message = []
        for index_row in range(0,numbers_rows):
            for index_cols in range(0,numbers_cols):
                pixel_value = img[index_row,index_cols] 
                binary_message.append(str(pixel_value))
        binary_message = "".join(binary_message)

        # Convertir la séquence binaire en une chaîne de caractères
        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
        
        # Trouver l'indice de la marque de fin de message ('\x00')
        end_index = message.find('\x00')

        return message[:end_index] if end_index != -1 else message


#save_img_gray(image_path)
#print(lsb_1(image_path,message))
#print(lsb_2(image_path,message))
print(decode_message_lsb1(image_path,message)) 
#print(decode_message_lsb2()) 


