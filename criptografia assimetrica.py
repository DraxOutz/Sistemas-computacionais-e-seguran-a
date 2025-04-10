import rsa

#Gerar par de chaves pública e privada.
public_key, private_key = rsa.newkeys(512) #Tamanho da chave em bits.

#Criptografar mensagem.
mensagem = "INSIRA ELA AQUI"
mensagem_bytes = mensagem.encode()

#Criptografar com a chave pública
criptografada = rsa.encrypt(mensagem_bytes, public_key)

#Descriptografar com a chave privada
descriptografada = rsa.decrypt(criptografada, private_key)

print("Criptografada:", criptografada)
print("Descriptografada:", descriptografada.decode())