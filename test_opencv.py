import cv2
from cesar import viginere_cypher


class GenerateImage(): 

    def load_image(path_image):
        return cv2.imread(path_image)
    
    def display_image(image):
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
        # Obtenir les valeurs des pixels à une position spécifique (x, y)
    def get_pixel_value(image, x, y):
        return image[y, x]
    
        # Convertir un texte en binaire
    def text_to_binary(text):
        return ''.join(format(ord(char), '08b') for char in text)

    # Convertir tous les pixels de l'image en valeur paire
    def convert_pixels_to_even(image):
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                if (image[row][col] % 2 != 0).any():
                    image[row][col] -= 1  # Si au moins un élément du pixel est impair, le rendre pair en soustrayant 1
        return image

    # Encoder un message binaire dans l'image avec des coefficients pairs
    def encode_message(image, binary_message):
        binary_message += '1111111111111110'  # Marque de fin de message
        data_index = 0

        img_encoded = image.copy()

        for row in range(img_encoded.shape[0]):
            for col in range(img_encoded.shape[1]):
                if data_index < len(binary_message):
                    img_encoded[row][col] = image[row][col] | int(binary_message[data_index]) #On va faire un OU Binaire  entre un pixel de l'image originale (image[row][col]) et un bit extrait du message binaire (int(binary_message[data_index])).
                    data_index += 1

                if data_index >= len(binary_message):
                    break
            if data_index >= len(binary_message):
                break

        return img_encoded
    

    "Problème de fonction sur le décodage"
    def decode_message(image):
        binary_message = ''
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                pixel_value = image[row][col] & 1
                binary_message += str(pixel_value)

        # Convertir la séquence binaire en une chaîne de caractères
        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

        # Trouver l'indice de la marque de fin de message ('\x00')
        end_index = message.find('\x00')

        return message[:end_index] if end_index != -1 else message


#Chemins d'accès
path_image = "images/genshin.png"
path_image_encode = "images/genshin_encode.png"

#Import l'image pris
original_image = GenerateImage.load_image(path_image)
print("Original Image",original_image)
GenerateImage.display_image(original_image)

#Obtenir le nombre de pixels en (x,y)
pixel_value = GenerateImage.get_pixel_value(original_image, 10, 20)  # Remplacez 10 et 20 par les coordonnées x, y souhaitées
print(f"Valeur du pixel à la position (10, 20) : {pixel_value}")

#Encoder un message binaire dans l'image avec des coefficients paires 
#message_to_encode = "Bonjour Vincent." 
message_viginere = viginere_cypher("le chocolat est bon","Azerty12345")
binary_message = GenerateImage.text_to_binary(message_viginere)
print("Message binaire",binary_message)


modified_image = GenerateImage.convert_pixels_to_even(original_image)
GenerateImage.display_image(modified_image)  #Image en full gris
print("Image convertie en pixel:",modified_image)

# Convertir l'image en niveaux de gris (pour simplifier le processus de codage)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) #Image avec du nuance en gris

encoded_image = GenerateImage.encode_message(gray_image, binary_message)
print("Image encodée : ",encoded_image)
cv2.imwrite(path_image_encode, encoded_image)  # Sauvegarder l'image encodée


"""
Import Image décodée
"""

load_image_gray = GenerateImage.load_image(path_image_encode)
GenerateImage.display_image(load_image_gray)

"""
# Exemple d'utilisation pour décoder un message depuis une image encodée avec OpenCV
encoded_image = cv2.imread(path_image_encode)

decoded_message = GenerateImage.decode_message(encoded_image)
print(f"Message décodé : {decoded_message}")
"""