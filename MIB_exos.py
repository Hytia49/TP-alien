
class Responsable:
        def __init__(self, NoAllee, Nom):
                self.NoAllee = NoAllee
                self.Nom = Nom
                
 
class Miam:
        def __init__(self, NomAlien, Aliment):
                self.NomAlien = NomAlien
                self.Aliment = Aliment
                
 
class Agent:
        def __init__(self, Nom, Ville):
                self.Nom = Nom
                self.Ville = Ville
                
 
class Gardien:
        def __init__(self, Nom, NoCabine):
                self.Nom = Nom
                self.NoCabine = NoCabine
        
                
class Alien:
        def __init__(self, Nom, Sexe, Planete, NoCabine):
                self.Nom = Nom
                self.Sexe = Sexe
                self.Planete = Planete
                self.NoCabine = NoCabine
                
 
class Cabine:
        def __init__(self, NoCabine, NoAllee):
                self.NoCabine = NoCabine
                self.NoAllee = NoAllee
                
 
BaseResponsables = { Responsable('1', 'Seldon'), Responsable('2', 'Pelorat') }
 
BaseMiams = { Miam('Zorglub', 'Bortsch'), Miam('Blorx', 'Bortsch'), Miam('Urxiz', 'Zoumise'), Miam('Zbleurdite', 'Bortsch'), Miam('Darneurane', 'Schwanstucke'), Miam('Mulzo', 'Kashpir'), Miam('Zzzzzz', 'Kashpir'), Miam('Arghh', 'Zoumise'), Miam('Joranum', 'Bortsch') }
 
BaseAgents = { Agent('Branno', 'Terminus'), Agent('Darell', 'Terminus'), Agent('Demerzel', 'Uco'), Agent('Seldon', 'Terminus'), Agent('Dornick', 'Kalgan'), Agent('Hardin', 'Terminus'), Agent('Trevize', 'Hesperos'), Agent('Pelorat', 'Kalgan'), Agent('Riose', 'Terminus') }
 
BaseGardiens = { Gardien('Branno', '1'), Gardien('Darell', '2'), Gardien('Demerzel', '3'), Gardien('Seldon', '4'), Gardien('Dornick', '5'), Gardien('Hardin', '6'), Gardien('Trevize', '7'), Gardien('Pelorat', '8'), Gardien('Riose', '9') }
 
BaseAliens = { Alien('Zorglub', 'M', 'Trantor', '1'), Alien('Blorx', 'M', 'Euterpe', '2'), Alien('Urxiz', 'M', 'Aurora', '3'), Alien('Zbleurdite', 'F', 'Trantor', '4'), Alien('Darneurane', 'M', 'Trantor', '4'), Alien('Mulzo', 'M', 'Helicon', '6'), Alien('Zzzzzz', 'F', 'Aurora', '7'), Alien('Arghh', 'M', 'Nexon', '8'), Alien('Joranum', 'F', 'Euterpe', '9') }
##Question 1
Gardiens = {Gardiens.Nom for Gardiens in BaseGardiens}
print("Le nom des gardiens sont: ",Gardiens)
##Question 2
Agents = { Agents.Ville for Agents in BaseAgents }
print(" Les villes agents sont: ",Agents)
##Question 3
triples = { (Alien.NoCabine, Alien.Nom, Gardiens.Nom) for Alien in BaseAliens for Gardiens in BaseGardiens if (Gardiens.NoCabine == Alien.NoCabine)}
print(" Le numéro de cabine, le nom du l'alien et le nom du gardien sont: ",triples)
##Question 4
couple = { (Alien.Nom, Responsable.NoAllee ) for Alien in BaseAliens for Responsable in BaseResponsables }
print( " Le nom de l'alien et son allée sont: ", couple )
##Question 5
allee2 = { ( Alien.Nom, Responsable.NoAllee ) for Alien in BaseAliens for Responsable in BaseResponsables if ( int(Responsable.NoAllee)==2)}
print( " Voici tous les aliens dans l'allée 2: ", allee2)
##Question 6
alienplanete2 = { ( Alien.Planete ) for Alien in BaseAliens for Responsable in BaseResponsables if ( int(Responsable.NoAllee)==2)}
print( " Voici tous les aliens dans l'allée 2: ", alienplanete2)
##Question 7
