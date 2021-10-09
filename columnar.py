from prettytable import PrettyTable

plain_text = "welcome to cgpit"
key = ['d', 'c', 'b', 'a']
# key = [4, 3, 2, 1]
cipher_text, ct = [], []
plain_text = plain_text.replace(" ", "")
enc_text = ""
table = PrettyTable(key)

print("Plain text: "+plain_text)

for i in range(0, len(plain_text), len(key)):
    if i >= len(plain_text)-len(key):
        cipher_text.append(plain_text[i:])
        break
    else:
        cipher_text.append(plain_text[i:i+len(key)])

if len(cipher_text[-1]) != len(key):
    cipher_text[-1] += "x"*(len(key)-len(cipher_text[-1]))

for i in cipher_text:
    new_list = list()
    for a in i:
        new_list.append(a)
    table.add_row(new_list)
print(table)

for j in range(len(key)):
    a = ""
    for i in range(len(cipher_text)):
        a += (cipher_text[i][j])
    ct.append(a)

if type(key[0]) == int:
    for i in key:
        enc_text += ct[i-1]
else:
    for i in sorted(key):
        a = key.index(i)
        enc_text += ct[a]

print("Cipher text: "+str(enc_text))
