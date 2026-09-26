import random
# Paramètres
lambda_rate = 1/6 # Taux d'arrivée (1 client toutes les 6 min)
mu_rate = 1/5 # Taux de service (1 client toutes les 5 min)
simulation_time = 60 # 1 heure en minutes
temps_attente = []
# Simulation
temps_actuel = 0
prochain_arrivee = random.expovariate(lambda_rate)
clients = [] # Liste des temps d'arrivée
temps_service_fini = 0
while temps_actuel < simulation_time:
    if prochain_arrivee <= temps_actuel:
        clients.append(prochain_arrivee)
        prochain_arrivee += random.expovariate(lambda_rate)
    if clients and temps_actuel >= temps_service_fini:
        arrivee = clients.pop(0) #Retire le premier client de la file
        attente = max(0, temps_actuel - arrivee)
        temps_attente.append(attente)
        temps_service_fini = temps_actuel + random.expovariate(mu_rate)
        temps_actuel = temps_service_fini #Avance le temps directement à la fin du service,
    else:
        temps_actuel += 0.1
# Résultat
if temps_attente:
    print(f"Temps d'attente moyen : {sum(temps_attente)/len(temps_attente):.2f} minutes")
else:
    print("Aucun client servi.")