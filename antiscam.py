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