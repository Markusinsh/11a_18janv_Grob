#izveidot Python programmu, kur lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs. Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas! 

def lasit_failu():
    # Sakums, prasa nosaukumu un paplasinajum
    faila_nosaukums = input("Ievadi faila nosaukumu: ")
    faila_paplasinajums = input("Ievadi faila paplašinājumu: ")

    # apvieno nosaukumu
    pilns_faila_nosaukums = f"{faila_nosaukums}.{faila_paplasinajums}"

    try:
        # Atver failu un nolasa tā saturu
        with open(pilns_faila_nosaukums, 'r') as f:
            print(f"Faila {pilns_faila_nosaukums} teksts:")
            print(f.read())
    except Exception as e:
        print(f"Nevar atvērt failu {pilns_faila_nosaukums}. Kļūda: {e}")
lasit_failu()
#Ir jaievada tas paplašinājums bez punktina jo savādaķ nezidosies atvērt
