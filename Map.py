from queue import PriorityQueue

mappa_romania = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu-Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Craiova': [('Drobeta', 120), ('Rimnicu-Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu-Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Craiova', 138), ('Rimnicu-Vilcea', 97), ('Bucarest', 101)],
    'Bucarest': [('Pitesti', 101), ('Giurgiu', 90), ('Fagaras', 211), ('Urziceni', 85)],
    'Giurgiu': [('Bucarest', 90)],
    'Fagaras': [('Sibiu', 99), ('Bucarest', 211)],
    'Urziceni': [('Bucarest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

def ricerca_costo_uniforme(citta_partenza, citta_arrivo):

    coda_frontiera = PriorityQueue()
    coda_frontiera.put((0, [citta_partenza], [0]))  # Ogni elemento nella coda è salvato come tupla 
    nodi_esplorati = set()

    while not coda_frontiera.empty():
        costo, percorso, costi_intermedi = coda_frontiera.get()
        citta_corrente = percorso[-1]

        if citta_corrente == citta_arrivo:
            return costo, list(zip(percorso, costi_intermedi))  

        if citta_corrente not in nodi_esplorati:
            nodi_esplorati.add(citta_corrente)

            for vicino, distanza in mappa_romania[citta_corrente]:
                if vicino not in nodi_esplorati:
                    nuovo_costo = costo + distanza
                    nuovo_percorso = list(percorso)
                    nuovo_percorso.append(vicino)
                    nuovi_costi_intermedi = list(costi_intermedi)
                    nuovi_costi_intermedi.append(nuovo_costo)
                    coda_frontiera.put((nuovo_costo, nuovo_percorso, nuovi_costi_intermedi))

  
    return None, None


citta_di_partenza = input("Inserisci la città di partenza: ")
citta_di_arrivo = input("Inserisci la città di arrivo: ")


risultato_costo, risultato_percorso = ricerca_costo_uniforme(citta_di_partenza, citta_di_arrivo)


if risultato_costo is not None and risultato_percorso is not None:
    print(f"\nIl percorso più breve da {citta_di_partenza} a {citta_di_arrivo} è:")
    print("-" * 40)
    for citta, costo in risultato_percorso:
        print(f"Città: {citta.ljust(15)} | km: {costo}")
    print("-" * 40)
    print(f"Distanza totale: {risultato_costo} km\n")
else:
    print(f"Percorso non trovato da {citta_di_partenza} a {citta_di_arrivo}\n")