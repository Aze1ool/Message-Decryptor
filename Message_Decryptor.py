#CS574 Homework 3
#Azamat Khafizov
#823503675

import string
import collections

print("Wellcome to the program \n")

#Requesting input of the 4 messages

message_1 = input("Please enter the first message that you would like to decrypt: ")
message_2 = input("Please enter the second message that you would like to decrypt: ")
message_3 = input("Please enter the third message that you would like to decrypt: ")
message_4 = input("Please enter the forth message that you would like to decrypt: ")
number_to_rotate = input("Please enter the number of rotation: ")

#decrypting each message to find the pair

def decryption_1(message_1, number_to_rotate):

    number_to_rotate = 1

    message_1.upper()
    
    message_1.lower()

    message_1.rotate(number_to_rotate)

    message_1 = ''.join(list(message_1))
  
    return message_1.translate(bytes.maketrans(string.message_1, message_1))

def decryption_2(message_2, number_to_rotate):

    number_to_rotate = 2
    
    message_2.upper()
    
    message_2.lower()

    message_2.rotate(number_to_rotate)

    message_2 = ''.join(list(message_1))
  
    return message_1.translate(bytes.maketrans(bytes.message_2, message_2))
    
def decryption_3(message_3, number_to_rotate):

    number_to_rotate = 3
    
    message_3.upper()
    
    message_3.lower()

    message_3.rotate(number_to_rotate)

    message_3 = ''.join(list(message_3))
  
    return message_3.translate(bytes.maketrans(bytes.message_3, message_3))   
    
def decryption_4(message_4, number_to_rotate):

    number_to_rotate = 4
    
    message_4.upper()
    
    message_4.lower()

    message_4.rotate(number_to_rotate)

    message_4 = ''.join(list(message_1))

    return message_4.translate(bytes.maketrans(bytes.message_4, message_4))       

#printing the results

print("The decrypte message 1 is: ",decryption_1(message_1, number_to_rotate))
print("The decrypte message 2 is: ",decryption_2(message_2, number_to_rotate))
print("The decrypte message 3 is: ",decryption_3(message_3, number_to_rotate))
print("The decrypte message 4 is: ",decryption_4(message_4, number_to_rotate))
print("I hope you found some pairs")
    
