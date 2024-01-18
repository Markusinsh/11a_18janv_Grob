#Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila. 

import csv
# Atver failu kuru vajag w
with open('faila_nosaukums.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Drukā tikai otrās kolonnas datus un sākas ar 0 tādēļ 1 un neesu drošs par for row in reader lietošanu
        print(row[1])

#nezināju kā testēt.... :(
