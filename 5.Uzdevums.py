# Prasa lietotājam ievādīt savu vārdu 
vards = input("Lūdzu, ievadiet savu vārdu: ")

# Veido teksta failu un ieraksta lietotāja vārdu
with open("lietotajs.txt", "w") as faila_objekts:
    faila_objekts.write(vards) 
