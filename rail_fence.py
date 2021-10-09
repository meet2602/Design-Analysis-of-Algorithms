plain_text, a = "Welcome to CG Patel Institute of Technology", ""
depth = 3
cipher_text = []
plain_text = plain_text.replace(" ", "")
print("Plain text: "+plain_text)

for i in range(0, len(plain_text), depth):
    if i == len(plain_text)-depth:
        cipher_text.append(plain_text[i])
        break
    else:
        cipher_text.append(plain_text[i:i+depth])

if len(cipher_text[-1]) != depth:
    cipher_text[-1] += "x"*(depth-len(cipher_text[-1]))

new_str = []

for j in range(depth):
    str1 = ""
    str1 += " "*j
    for i in range(len(cipher_text)):
        str1 += " " + cipher_text[i][j]
    new_str.append(str1)

for i in new_str:
    print(i)

for j in range(depth):

    for i in range(len(cipher_text)):
        a += (cipher_text[i][j])


print("Cipher text:"+a)
