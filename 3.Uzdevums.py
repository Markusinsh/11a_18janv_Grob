#Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu.

def izdrukat_treso_rindu(faila_nosaukums):
    with open(faila_nosaukums, 'r') as f:
        rindas = f.readlines()
        print(rindas[2])
izdrukat_treso_rindu('test.txt')
#Rindas sak skaitit ar 0
