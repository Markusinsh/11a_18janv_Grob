#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). (3 punkti)
# Atver failu lasīšanai (test.txt vietā ievieto sava faila nosauku ja maina pats izmantoju test failu)
with open('test.txt', 'r') as file:
    print(file.read())
