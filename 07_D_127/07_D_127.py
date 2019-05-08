#nomer 1
import re
f = open('Indonesia.txt', 'r', encoding='latin1')

teks = f.read()
f.close()
h = r'me\w+'
tampil = re.findall(h, teks)

print(tampil)


#nomer 2
import re
f = open('Indonesia.txt', 'r', encoding='latin1')

teks = f.read()
f.close()
i = r'di\w+'
tampil = re.findall(i, teks)

print(tampil)

#nomer 3
import re
f = open('Indonesia.txt', 'r', encoding='latin1')

teks = f.read()
f.close()
j = r'di \w+'
tampil = re.findall(j, teks)

print(tampil)




#nomer 4
import re
f = open('KEI.html', 'r', encoding='latin1')

teks = f.read()

strings = re.findall(r'title="([\w+]+)">', teks)
strings= re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
a = []
for i in strings:
    a.append((i[0], float(i[1])))

print(a)
