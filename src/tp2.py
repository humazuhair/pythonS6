arcs = open("/Users/humazuhair/Downloads/graphe_tp2.txt", "r")lignes = arcs.readlines()touslesarc = []for lines in lignes:    touslesarc.append(lines.strip("\r\n"))arcs.close()print(touslesarc)Origine = []Destination = []for unArc in touslesarc:    cetArc = unArc.split("\t")    orig = int(cetArc[0])    Origine.append(orig)    dest = int(cetArc[1])    Destination.append(dest)# print('origine = ', Origine)# print('destination = ', Destination)nbArcs = len(Origine)# print('nb Arcs = ', nbArcs)nbSommets = max(max(Origine), max(Destination)) + 1# print('nb Sommets = ', nbSommets)successeurs = [[] for j in range(nbSommets)]predecesseurs = [[] for j in range(nbSommets)]numArc = [[] for j in range(nbSommets)]for u in range(0, nbArcs):    orig = Origine[u]    dest = Destination[u]    successeurs[orig].append(dest)    predecesseurs[dest].append(orig)    numArc[dest].append(u)def insere_fin(liste, j):    liste.append(j)def insere_debut(liste, j):    liste.insert(0, j)# ex 2Liste_sommets = []Marque = [False for j in range(nbSommets)]Dans_liste = [False for j in range(nbSommets)]Liste_sommets.append(0)Marque[0] = TrueDans_liste[0] = True# lifowhile Liste_sommets:    k = Liste_sommets.pop(0)    # print('k', k)    Marque[k] = True    for l in successeurs[k]:        if not Marque[l] and not Dans_liste[l]:            insere_fin(Liste_sommets, l)            Dans_liste[l] = True# fifowhile Liste_sommets:    k = Liste_sommets.pop(0)    # print('k', k)    Marque[k] = True    for l in successeurs[k]:        if not Marque[l] and not Dans_liste[l]:            insere_debut(Liste_sommets, l)            Dans_liste[l] = Truefor i, j in enumerate(predecesseurs):    if not j:        print(i)for j in range(nbSommets):    if not predecesseurs[j]:        source = jprint(source)# my solutionfor i, j in enumerate(successeurs):    if not j:        print(i)# teacher's solutionfor j in range(nbSommets):    if not successeurs[j]:        source = jprint(source)def cherche_chemin(i, j):    P = []    Liste_sommets = []    Marque = [False for j in range(nbSommets)]    Dans_liste = [False for j in range(nbSommets)]    Liste_sommets.append(0)    Marque[0] = True    Dans_liste[0] = True    trouve = False    while Liste_sommets and trouve:        f = Liste_sommets.pop(0)        Marque[f] = True        if f == j:            trouve = True            for l in successeurs[f]:                if not Marque[l] and not Dans_liste[l]:                    insere_debut(Liste_sommets, l)                    Dans_liste[l] = True                    P[l] = f                    trouve = True    return trouve#cherche_chemin(1, 4)Marque = [0 for j in range(0, nbSommets)]nbConnexite = 1while min(Marque) == 0:    for j in range(nbSommets):        if Marque[j] == 0:            depart = j        List = [depart]        while List != []:            ce_sommet = List[0]            List.remove(ce_sommet)            Marque[ce_sommet] = nbConnexite            for j in successeurs[ce_sommet] + predecesseurs[ce_sommet]:                if Marque[j] == 0:                    List.append(j)        print(" composant connexe = ", nbConnexite)        for j in range(nbSommets):            if Marque[j] == nbConnexite:                print j        nbConnexite = + 1