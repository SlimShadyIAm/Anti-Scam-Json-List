import json

antiscamjson = open('antiscam.json')
data = json.load(antiscamjson)
scamjburls = sorted(data["scamjburls"])
scamideviceunlockurls = sorted(data["scamideviceunlockurls"])
antiscamjson.close()

f = open("antiscam.json", "w")
f.write('{\n\t"scamjburls": ')
f.write(str(scamjburls).replace("'", '"').replace("[", "[\n\t\t").replace("]", "\n\t],").replace(", ", ",\n\t\t"))
f.write('\n\t"scamideviceunlockurls": ')
f.write(str(scamideviceunlockurls).replace("'", '"').replace("[", "[\n\t\t").replace("]", "\n\t]").replace(", ", ",\n\t\t"))
f.write('\n}')
f.close()

for i in scamjburls:
    for z in i:
        if z.isupper():
            print("Capital:", i)

for i in scamideviceunlockurls:
    for z in i:
        if z.isupper():
            print("Capital:", i)

for i in range(len(scamjburls)):
    for j in range(i + 1, len(scamjburls)):
        if scamjburls[i] == scamjburls[j]:
            print("Duplicate:", scamjburls[i])

for i in range(len(scamideviceunlockurls)):
    for j in range(i + 1, len(scamideviceunlockurls)):
        if scamideviceunlockurls[i] == scamideviceunlockurls[j]:
            print("Duplicate:", scamideviceunlockurls[i])

print("Done")