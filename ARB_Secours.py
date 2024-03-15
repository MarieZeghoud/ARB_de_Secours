class Noeud:
  def __init__(self, question, oui = None, non = None):
    """
    Cette fonction définit les attributs de la classe Noeud.
    IN: L'instance actuelle self de la classe, et les attributs question, oui et non.
    OUT: Associe la valeur contenue dans chaque variable à leur instance spécifique en self.
    """
    self.question = question
    self.oui = oui
    self.non = non
#

class ArbreDeDecision:
  def __init__(self, racine):
    """
    Cette fonction définit les attributs de la classe ArbreDeDecision.
    IN: L'instance actuelle self de la classe, et l'attribut racine.
    OUT: Associe la valeur contenue dans chaque variable à leur instance spécifique en self.
    """
    self.racine = racine
#
  
  def parcourir(self, racine):
    """
    Cette fonction permet de parcourir l'arbre de décision de la situation d'urgence choisie.
    IN: La racine de l'arbre de décision choisi.
    OUT: La branche gauche du sous-arbre si Q.lower() ==  'oui', et la branche droite si Q.lower() == 'non'.
    """
    #On permet à la méthode de redémarrer en cas d'erreur
    while True:
      #L'interface de réponse de l'utilisateur 
      Q = input(racine.question)
      #La réponse est oui / pas de réponse non
      if Q.lower() == "oui" and racine.oui is not None:
        racine = racine.oui
        print()
      #La réponse est non / pas de réponse oui
      elif Q.lower() == "non" and racine.non is not None:
        racine = racine.non
        print()
      #Pas de réponse oui / pas de réponse non
      elif racine.oui is None and racine.non is None:
        break
      #Réponse erronée
      else:            
        print("Veuillez répondre par oui ou par non.")
        print()
#


#######################################
END = Noeud("La session d'entraînement est terminée. (oui)")

#On crée les différents noeuds de l'Arbre de Situation d'Inconscience
N_END = Noeud("Continuez de vérifier la respiration de la victime en attendant les secours. (oui)", END)
NCI_A = Noeud("Si la victime reprend conscience, mettez-la dans une position confortable de son choix (assise, semi-assise ou allongée). Posez-lui des questions: est-ce la 1ère fois ? Sinon, depuis combien de temps cela dure ? Est-elle hospitalisée, ou prend-elle des médicaments pour cela ? (oui)", N_END)
#Méthodes de l'insufflation 
NCI5 = Noeud("Couvrez entièrement la bouche de la victime avec la votre. Insufflez lentement et continuellement de l'air pendant 1s, en vérifiant que sa poitrine se soulève. Après insufflation, maintenez la tête de la victime dans la position d'insufflation et vérifiez si sa poitrine s'abaisse à l'expiration. (oui)", NCI_A)
NCI4 = Noeud("Avec une main, pincez son nez avec le pouce et l'index. Avec l'autre, maintenez son menton pour que sa bouche reste ouverte. (oui)", NCI5)
NCI3 = Noeud("Méthode de l'insufflation: faites basculer sa tête en arrière en soulevant son menton avec l'extrémité des doigts d'une main, l'extrémité des doigts de l'autre sur son front. (oui)", NCI4)
#Méthode des compressions 
NCI2 = Noeud("Comprimez verticalement le sternum de la victime avec les bras tendus et un enfoncement de 5-6cm. Après chaque pression, laissez la poitrine reprendre sa position initiale. (oui)", NCI3)
NCI1 = Noeud("Méthode des compressions : agenouillez vous près de la victime. Penchez-vous au-dessus d'elle et placez vos deux mains solidarisées au milieu de sa poitrine nue ( talon de la 1ère main sur la poitrine, talon de l'autre main sur la première ). (oui)", NCI2)
#Respiration irrégulière et D.A.E / Respiration irrégulière et pas de D.A.E
NCI = Noeud("Alternez entre 30 compressions pulmonaires ( 2 par seconde, avec une durée de la compression équivalente à la durée de relâchement ) et deux insufflations, jusqu'à ce que la victime reprenne conscience ou que les secours arrivent. (oui)", NCI1)
#Respiration irrégulière et D.A.E
NDAE = Noeud("Si vous êtes entouré d'une ou plusieurs personnes, demandez-leur de le chercher immédiatement. Si vous êtes seul, faites-le par vous-même. Suivez les instructions du D.A.E. Si cela ne fonctionne pas, passez à une réanimation cardio-pulmonaire. (oui)", NCI)
#Respiration irrégulière
N1B = Noeud("Si vous êtes entouré d'une ou plusieurs personnes, demandez-leur d'appeler les secours (15 ou 18). Sinon, contactez-les par vous-même. Un D.A.E se trouve-t-il à proximité ? (oui/non)", NDAE, NCI)
#Respiration régulière / FIN
N4_END = Noeud("Continuez de surveiller sa respiration jusqu'à l'arrivée des secours. (oui)")
N4F = Noeud("Si vous êtes entouré d'une ou plusieurs personnes, demandez-leur d'appeler les secours (15 ou 18). Si vous êtes seul, allez chercher de l'aide, et contactez les secours par vous-même. (oui)", N4_END) 
#PLS
N4E = Noeud("Ouvrez-lui la bouche afin de laisser les liquides s'écouler. (oui)", N4F) 
N4D = Noeud("Avec l'autre main, relevez la jambe la plus éloignée et faites roulez la victime vers vous en tirant lentement cette jambe, jusqu'à-ce que son genou touche le sol. L'autre pied doit rester au sol. (oui)", N4E)
N4C = Noeud("Saisissez l autre bras, et maintenez le dos de la main de ce bras contre son oreille avec votre main gauche. (oui)", N4D)
N4B = Noeud("Ramenez son bras le plus proche vers vous, en angle droit avec la paume de la main tournée vers le haut. (oui)", N4C)
N4A = Noeud("Mettez la victime dans une Position Latérale de Sécurité. (oui)", N4B)
N4 = Noeud("Enlevez les lunettes de la personne si elle en porte: effectuez une Position Latérale de Sécurité. (oui)", N4B)
#La victime respire 
N3 = Noeud("Vérifiez la respiration de la personne: sa poitrine se soulève-t-elle régulièrement ? (oui/non)", N4, N1B)
N2 = Noeud("Faites basculer sa tête en arrière en soulevant son menton avec l'extrémité des doigts d'une main, l'extrémité des doigts de l'autre sur son front. (oui)", N3)
N1AA = Noeud("Desserez le col, la cravate et la ceinture de la victime pour faciliter sa respiration. (oui)", N2)
#La personne est consciente
N1 = Noeud("La personne respire-t-elle ? (oui/non)", N1AA, N1B)
N0 = Noeud("La personne est consciente ? (oui/non)", N1, N1B)
#On initialise l'Arbre 
ARB_Inc = ArbreDeDecision(N0)




#On crée les différents noeuds de l'Arbre de Situation d'Hémorragie
#Saignement qui continue
H_END = Noeud("Lorsque la victime est hors de danger, prenez-soin de bien vous laver les mains. (oui)", END)
#Saignement stable / stoppé
H2B = Noeud("Continuez de comprimer la plaie jusqu'à ce que les secours arrivent. (oui)", H_END)
H2A = Noeud("Comprimez plus fermement la plaie, et ce jusqu'à-ce que les secours arrivent. (oui)", H_END)
#Une ou plusieurs personnes pour vous assister
H2 = Noeud("Demandez à la personne de contactez immédiatement les secours (15 ou 18). La plaie continue-t-elle de saigner ? (oui/non)", H2A, H2B)
#Aucune personne pour vous assister
H1D = Noeud("Si vous avez réussi et que le saignement s'est stoppé, contactez immédiatement les secours (15 ou 18). Dans le cas contraire, continuez de comprimez manuellement et fermement la plaie jusqu'à-ce que le saignement diminue et que vous soyez en capacité de chercher de l'aide. (oui)", H_END)
H1C = Noeud("Entourez ce tampon d'un lien assez large pour le recouvrir entièrement et faire 2 fois le tour du bras de la victime. Le lien doit être assez serré pour que le saignement s'arrête. (oui)", H1D)
H1B = Noeud("Substituez très rapidement le moyen précédent de compression avec un tampon recouvrant toute la plaie. Si le tampon n'est pas suffisant, ajoutez-en un deuxième par-dessus. (oui)", H1C) 
H1A = Noeud("Vous allez devoir appliquer un tampon relai avant de contacter les secours. (oui)", H1B)
H1 = Noeud("Êtes-vous seul ?", H1A, H2)
#La Victime ne peut pas compresser sa blessure
H0B = Noeud("Protégez vos mains avec un tissu, un sac plastique, des gants ou n'importe quel autre tissu vous protégeant du contact du sang. Exercez une pression sur la plaie. (oui)", H1)
#La Victime peut compresser sa blessure
H0A = Noeud("Demandez-lui de compresser sa blessure, et allongez-la en position horizontale. (oui)", H1)
H0 = Noeud("Si possible, ne rentrez pas en contact avec le sang de la victime. Peut-elle compresser sa blessure elle-même ? (oui/non)", H0A, H0B)
#On initialise l'Arbre 
ARB_Hem = ArbreDeDecision(H0)




#On crée les différents noeuds de l'Arbre de Situation d'Étouffement 
#Perte de Conscience, entouré
E3_END = Noeud("Continuez la réanimation cardio-pulmonaire jusqu'à-ce que la victime reprenne conscience ou que les secours arrivent. (oui)", END)
#La victime peut tousser / respirer / émettre du bruit
E0_END = Noeud("Si la toux persiste après la sortie du corps étranger, demandez conseil à votre médecin ou aux secours. (oui)", END)
#La victime peut tousser / respirer / émettre du bruit
E0B = Noeud("Encouragez la personne à tousser afin de faire sortir le corps étranger. Ne lui administrez pas de claques, et ne lui faites pas boire. (oui)", E0_END)
#Méthodes de l'insufflation 
E3B5 = Noeud("Couvrez entièrement la bouche de la victime avec la votre. Insufflez lentement et continuellement de l'air pendant 1s, en vérifiant que sa poitrine se soulève. Après insufflation, maintenez la tête de la victime dans la position d'insufflation et vérifiez si sa poitrine s'abaisse à l'expiration. (oui)", E3_END)
E3B4 = Noeud("Avec une main, pincez son nez avec le pouce et l'index. Avec l'autre, maintenez son menton pour que sa bouche reste ouverte. (oui)", E3B5)
E3B3 = Noeud("Méthode de l'insufflation: faites basculer sa tête en arrière en soulevant son menton avec l'extrémité des doigts d'une main, l'extrémité des doigts de l'autre sur son front. (oui)", E3B4)
#Méthode des compressions 
E3B2 = Noeud("Comprimez verticalement le sternum de la victime avec les bras tendus et un enfoncement de 5-6cm. Après chaque pression, laissez la poitrine reprendre sa position initiale. (oui)", E3B3)
E3B1 = Noeud("Méthode des compressions : agenouillez vous près de la victime. Penchez-vous au-dessus d'elle et placez vos deux mains solidarisées au milieu de sa poitrine nue ( talon de la 1ère main sur la poitrine, talon de l'autre main sur la première ). (oui)", E3B2)
#Perte de Conscience, entouré
E3B = Noeud("Demandez aux personnes présentes de contacter immédiatement les secours (15 ou 18). Alternez entre une série de 30 compressions thoraciques ( 2 par seconde, avec une durée de la compression équivalente à la durée de relâchement )et 2 insufflations. (oui)", E3B1)
#Perte de Conscience, seul
E3A = Noeud("Contactez immédiatement les secours (15 ou 18), et alternez entre une série de 30 compressions thoraciques ( 2 par seconde, avec une durée de la compression équivalente à la durée de relâchement )et 2 insufflations. (oui)", E3_END)
#Perte de Conscience 
E3 = Noeud("Si la victime a perdu connaissance, installez-la doucement au sol. Êtes-vous seul ? (oui/non)", E3A, E3B)
#Compressions Abdominales / Claques
E2A = Noeud("Alternez les 5 claques et les 5 compressions abdominales. Les choses sont-elles rentrées dans l'ordre ? (oui/non)", E0_END, E3)
E2 = Noeud("Enfoncez 5 fois votre poing vers vous, vers le haut. Les choses sont-elles rentrées dans l'ordre ? (oui/non)", E0_END, E2A)
#Compressions Abdominales
E1B = Noeud("Maintenez votre poing fermé entre le nombril et l'extrémité inférieure du sternum avec l'autre main. (oui)", E2)
E1A = Noeud("Prenez la victime par derrière, vos bras autour de la partie supérieure de son abdomen. (oui)", E1B)
E1 = Noeud("Vous allez effectuer 5 compressions abdominales. (oui)", E1A)
#La victime ne peut pas tousser / respirer / émettre du bruit
E0A = Noeud("Donnez 5 claques dans le dos de la victime, en vérifiant après chaque claque si la personne ne s'étouffe plus. Les choses sont-elles rentrées dans l'ordre ? (oui/non)", E0_END, E1)
E0 = Noeud("La victime peut-elle parler, respirer ou émettre du bruit en toussant ? (oui/non)", E0B, E0A)
#On initialise l'Arbre 
ARB_Et= ArbreDeDecision(E0)




#On crée les différents noeuds de l'Arbre de Situation de Noyade 
#Victime inconsciente / Respiration normale / PLS
O5_END = Noeud("Continuez de surveiller sa respiration jusqu'à l'arrivée des secours. (oui)", END)
O5D = Noeud("Ouvrez-lui la bouche afin de laisser les liquides s'écouler. (oui)", O5_END)
O5C = Noeud("Avec l'autre main, relevez la jambe la plus éloignée et faites roulez la victime vers vous en tirant lentement cette jambe, jusqu'à-ce que son genou touche le sol. L'autre pied doit rester au sol. (oui)", O5D)
O5B = Noeud("Saisissez l'autre bras, et maintenez le dos de la main de ce bras contre son oreille avec votre main gauche. (oui)", O5C)
O5A = Noeud("Ramenez son bras le plus proche vers vous, en angle droit avec la paume de la main tournée vers le haut. (oui)", O5B)
O5 = Noeud("Mettez la victime dans une Position Latérale de Sécurité. (oui)", O5A)
#Respiration anormale
O3DB = Noeud("Si la victime reprend conscience, mettez-la en Position Latérale de Sécurité. (oui)", O5A)
#Méthodes des compressions 
O3DA5 = Noeud("Comprimez verticalement le sternum de la victime avec les bras tendus et un enfoncement de 5-6cm. Après chaque pression, laissez la poitrine reprendre sa position initiale. (oui)", O3DB)
O3DA4 = Noeud("Méthode des compressions : agenouillez vous près de la victime. Penchez-vous au-dessus d'elle et placez vos deux mains solidarisées au milieu de sa poitrine nue ( talon de la 1ère main sur la poitrine, talon de l'autre main sur la première ). (oui)", O3DA5)
O3DA3 = Noeud("Couvrez entièrement la bouche de la victime avec la votre. Insufflez lentement et continuellement de l'air pendant 1s, en vérifiant que sa poitrine se soulève. Après insufflation, maintenez la tête de la victime dans la position d'insufflation et vérifiez si sa poitrine s'abaisse à l'expiration. (oui)", O3DA4)
#Méthode de l'insufflation 
O3DA2 = Noeud("Avec une main, pincez son nez avec le pouce et l'index. Avec l'autre, maintenez son menton pour que sa bouche reste ouverte. (oui)", O3DA3)
O3DA1 = Noeud("Méthode de l'insufflation: faites basculer sa tête en arrière en soulevant son menton avec l'extrémité des doigts d'une main, l'extrémité des doigts de l'autre sur son front. (oui)", O3DA2)
#Respiration anormale
O3DA = Noeud("Débutez par 5 insufflations, puis alternez entre 30 compressions pulmonaires ( 2 par seconde, avec une durée de la compression équivalente à la durée de relâchement ) et deux insufflations, jusqu'à ce que la victime reprenne conscience ou que les secours arrivent. (oui)", O3DA1 )
O3D = Noeud("Si vous êtes entouré d'une ou plusieurs personnes, demandez-leur de le chercher immédiatement. Si vous êtes seul, faites-le par vous-même. Suivez les instructions du D.A.E. Si cela ne fonctionne pas, passez à une réanimation cardio-pulmonaire. (oui)", O3DA)
O3 = Noeud("Si vous êtes entouré d'une ou plusieurs personnes, demandez-leur d'appeler les secours (15 ou 18). Sinon, contactez-les par vous-même. Un D.A.E se trouve-t-il à proximité ? (oui/non)", O3D, O3DA)
#Victime inconsciente
O4B = Noeud("Penchez-vous pour écouter sa respiration: percevez-vous une respiration régulière pendant au moins 10 secondes d'affilée ?, (oui/non)", O5, O3)
O4A = Noeud("Faites basculer sa tête en arrière en soulevant son menton avec l'extrémité des doigts d'une main, l'extrémité des doigts de l'autre sur son front. (oui)", O4B)
O4 = Noeud("Vous devez vous assurer que la victime respire. (oui)", O4A)
#Victime consciente / Respiration normale
O2_END = Noeud("Rassurez la victime et demandez-lui de se calmer. Allongez-là dans une position confortable, couvrez-là et appelez les secours. (oui)")
#Victime consciente
O2 = Noeud("Est-ce que la victime respire ? (oui/non)", O2_END, O3)
O1 = Noeud("Une fois hors de l'eau, posez des questions à la victime: est-elle consciente ? (oui/non)", O2, O4)
#Seul 
OB = Noeud("Ne prenez pas de risque: envoyez à la victime un objet flottant s'il y en a à proximité, et allez chercher de l'aide. (oui)", O1)
#Environnement surveillé 
OA = Noeud("Alertez immédiatement la personne en charge. (oui)", O1)
O = Noeud("Êtes-vous dans un environnement surveillé, avec un maître nageur ou un surveillant de baignade ? (oui/non)", OA, OB)
#On initialise l'Arbre 
ARB_Noy= ArbreDeDecision(O)




#On crée les différents noeuds de l'Arbre de Situation de Brûlure 
#Vêtements collés 
B3 = Noeud("Appliquez un pansement ou un tissu propre sur la brûlure afin de la protéger. Si vous voyez des ampoules sur la plaie, ne les percez pas. (oui) ", END)
#Vêtements non-collés
B2A = Noeud("Retirez ces vêtements / bijoux. (oui)", B3)
B2 = Noeud("La victime porte-elles des vêtements / des bijoux au niveau de la brûlure qui ne sont pas collés à la peau ? (oui/non)", B2A, B3)
#Brûlure légère 
B1 = Noeud("Refroidissez la brûlure pendant 15min par un ruissellement d'eau entre 15 et 25°C. L'eau doit couler sur le membre affecté et ruisseler sur la plaie: n'appliquez pas directement le flux d'eau sur la plaie. (oui)", B2)
#Brûlure grave
BA = Noeud("Contactez immédiatement les secours(15 ou 18). (oui)", B1)
B = Noeud("La brûlure est-elle grave, avec une surface supérieure à la moitié de la paume de la main et/ou une couleur noirâtre ?, (oui/non)", BA, B1)
#On initialise l'Arbre 
ARB_Br= ArbreDeDecision(B)



#On rassemble tous les scénarios dans un arbre principal 
T5 = Noeud("La victime n'est pas en situation de danger. (oui)", END)
T4 = Noeud("Est-elle en train de faire un malaise ? (oui/non)", N0, T5)
T3 = Noeud("Est-elle en train de s'étouffer ? (oui/non)", E0, T4)
T2 = Noeud("Est-elle en train de se noyer ? (oui/non)", O, T3)
T1 = Noeud("Présente-elle des signes de brûlure ? (oui/non)", B, T2)
T = Noeud("La victime saigne-t-elle abondament ? (oui/non)", H0, T1 )
#On initialise l'Arbre Principal 
ARB_MAIN = ArbreDeDecision(T)

#######################################

print("Cet arbre de décision vise à vous entrainer à agir de façon décisive et appropriée face à des scénarios d'urgence. Répondez par oui ou par non. Cinq situations différentes seront proposées.")
print("La session commence dès maintenant.")
print()
#On parcourt l'arbre principal 
ARB_MAIN.parcourir(T)