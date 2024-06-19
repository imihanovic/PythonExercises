import random
class Spil:
    NUMBERS = list(range(1,8)) + [11,12,13]
    SUIT = [ "K", "S", "B", "D" ]
    def __init__(self):
        self.deck = [ (n, s) for n in self.NUMBERS for s in Spil.SUIT ]
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def dealHand(self):
        hand, self.deck = self.deck[:3], self.deck[3:]
        return hand
    
    def dealCard(self):
        if(len(self.deck)!=0):
            card = self.deck.pop(0)
            return card
    
    def getBriskula(self):
        briskula = self.deck.pop(0)
        self.deck.append(briskula)
        return briskula
    
class Igrac:
    def __init__(self, ime):
        self.ime = ime
        self.ruka = None
        self.bodovi = 0
        self.dobivene = []
        
    def akcija(self, stanjeIgre):
        return random.randint(0, len(stanjeIgre["ruka"]) - 1)
    
class Human(Igrac):
    def __init__(self):
        name = input("Enter your name: ")
        super().__init__(name)
    def akcija(self, stanjeIgre): 
        odabrana = int(input("Choose card you want to throw (1,2,3) or 0 for random: "))
        if(odabrana > len(self.ruka)):
            print("Pogresan unos!")
            return self.akcija(stanjeIgre)
        elif(odabrana == 0):
            return super().akcija(stanjeIgre)
        elif(odabrana in [1,2,3]):
            return odabrana-1
            

class Bot(Igrac):
    def __init__(self):
        super().__init__("Bot")
        
    def akcija(self, stanjeIgre):
        ruka = stanjeIgre["ruka"][:]
        karteDrugogZoga = []
        karteBriskula = []
        for i in ruka:
            if(i[1] != stanjeIgre["briskula"][1]):
                if(i[0] not in [1,3]):
                    karteDrugogZoga.append(i)
            else:
                karteBriskula.append(i)
                
        if(len(stanjeIgre["stol"])==0):
            if len(karteDrugogZoga) != 0:
                return stanjeIgre["ruka"].index(sorted(karteDrugogZoga, key=lambda karta : Briskula.SNAGA[karta[0]])[0])
            return stanjeIgre["ruka"].index(sorted(ruka, key=lambda karta : Briskula.SNAGA[karta[0]])[0])
        
        else:
            bacena = stanjeIgre["stol"][0]
            karteIstogZoga = []
            for i in ruka:
                if(i[1] == bacena[1] and Briskula.SNAGA[i[0]]>Briskula.SNAGA[bacena[0]]):
                    karteIstogZoga.append(i)
            if(len(karteIstogZoga)>0):
                print("KARTE ISTOG ZOGA",karteIstogZoga)
                
            if bacena[1] == stanjeIgre["briskula"][1]:
                if(bacena[0] == 3 and (1,stanjeIgre["briskula"][1]) in stanjeIgre["ruka"]):
                  return stanjeIgre["ruka"].index((1,stanjeIgre["briskula"][1]))
                
                if (len(karteDrugogZoga)>0):
                    return stanjeIgre["ruka"].index(sorted(karteDrugogZoga, key=lambda karta : Briskula.SNAGA[karta[0]])[0])
                return stanjeIgre["ruka"].index(sorted(ruka, key=lambda karta : Briskula.SNAGA[karta[0]])[0])
            
            else:
                if(len(karteIstogZoga)>0):
                    return stanjeIgre["ruka"].index(sorted(karteIstogZoga, key=lambda karta : Briskula.SNAGA[karta[0]])[-1])   
                
                elif (len(karteBriskula) > 0 and bacena[0] in [1,3]) or len(karteBriskula)==3:
                    return stanjeIgre["ruka"].index(sorted(karteBriskula, key=lambda karta : Briskula.SNAGA[karta[0]])[0])
                
                elif(len(karteDrugogZoga)>0):
                     stanjeIgre["ruka"].index(sorted(karteDrugogZoga, key=lambda karta : Briskula.SNAGA[karta[0]])[0])
        
            return stanjeIgre["ruka"].index(sorted(ruka, key = lambda karta: Briskula.SNAGA[karta[0]])[0])
        
class Briskula:
    BODOVI = {1:11, 2:0, 3:10, 4:0, 5:0, 6:0, 7:0, 11:2, 12:3, 13:4}
    SNAGA = {1:10, 2:1, 3:9, 4:2, 5:3, 6:4, 7:5, 11:6, 12:7, 13:8}
   
    def __init__(self, agent1, agent2):
        self.spil = Spil()
        self.spil.shuffle()
        self.igrac1 = agent1
        
        self.igrac1.ruka = self.spil.dealHand()
        
        self.bot = agent2
        self.bot.ruka = self.spil.dealHand()
        
        self.briskula = self.spil.getBriskula()
        self.stol = []
        
    
    def odigraj_partiju(self):
        
        igrac1Turn = True
        while(len(self.spil.deck)!=0 or len(self.igrac1.ruka)!=0):
            #print("*"*40)
            #print(self)
            dobivena = None
            
            if(igrac1Turn):
                #print(self.stanje(self.igrac1))
                kartaIgrac1IND = self.igrac1.akcija(self.stanje(self.igrac1))
                kartaIgrac1 = self.igrac1.ruka[kartaIgrac1IND]
                
                self.stol = [kartaIgrac1]
                # print(self)
                # print("-"*40)
                kartaBotIND = self.bot.akcija(self.stanje(self.bot))
                kartaBot = self.bot.ruka[kartaBotIND]
                # print()
                # print("BOT BACIO", kartaBot)
                self.stol.append(kartaBot)
                print(self)
                self.igrac1.ruka.pop(kartaIgrac1IND)
                self.bot.ruka.pop(kartaBotIND)
                # print()
                # print("STOL:",self.stol)
                
                dobivena = self.checkHand(kartaIgrac1, kartaBot)
            else:
                
                kartaBotIND = self.bot.akcija(self.stanje(self.bot))
                kartaBot = self.bot.ruka[kartaBotIND]
                self.stol = [kartaBot]
                # print(self)
                # print("-"*40)
                # print()
                # print("BOT BACIO", kartaBot)
                
                # print()
                # print("STOL",self.stol)
          
                kartaIgrac1IND = self.igrac1.akcija(self.stanje(self.igrac1))
                kartaIgrac1 = self.igrac1.ruka[kartaIgrac1IND]
                
                self.stol.append(kartaIgrac1)
                #print(self)
                self.igrac1.ruka.pop(kartaIgrac1IND)
                self.bot.ruka.pop(kartaBotIND)
            
                dobivena = self.checkHand(kartaBot, kartaIgrac1)
                
            if dobivena == kartaIgrac1:
                self.igrac1.bodovi+=Briskula.BODOVI[kartaIgrac1[0]]
                self.igrac1.bodovi+=Briskula.BODOVI[kartaBot[0]]
                
                self.igrac1.dobivene.append([kartaIgrac1, kartaBot])
                if(len(self.spil.deck)!=0):
                    self.igrac1.ruka.append(self.spil.dealCard())
                    self.bot.ruka.append(self.spil.dealCard())
                igrac1Turn = True
            else:
                self.bot.dobivene.append([kartaIgrac1, kartaBot])
                self.bot.bodovi+=Briskula.BODOVI[kartaIgrac1[0]]
                self.bot.bodovi+=Briskula.BODOVI[kartaBot[0]]
                if(len(self.spil.deck)!=0):
                    self.bot.ruka.append(self.spil.dealCard())
                    self.igrac1.ruka.append(self.spil.dealCard())
                igrac1Turn = False
                
           # print("*"*40) 
            self.stol = []   
        print(self)
        return(self.rezultat())
    
    def checkHand(self, karta1, karta2):
        if(karta1[1] == karta2[1]):
            if(self.SNAGA[karta1[0]]>self.SNAGA[karta2[0]]):
                return karta1
            else:
                return karta2
        elif(karta1[1] == self.briskula[1]):
            return karta1
        elif(karta2[1] == self.briskula[1]):
            return karta2
        return karta1
    
        
    def __str__(self):
        return """Broj karata u špilu: {brSpil}
Briškula: {bris}
Karte na stolu:{stol}
Karte u igraca: {ruka1}
Karte u bota: {ruka2}
Bodovi igrac: {bodovi1}
Bodovi bot: {bodovi2}
""".format(brSpil=str(len(self.spil.deck)), bris=self.briskula, stol=self.stol, ruka1=self.igrac1.ruka, ruka2=self.bot.ruka, bodovi1=self.igrac1.bodovi, bodovi2=self.bot.bodovi)

    def rezultat(self):
        if(self.igrac1.bodovi == 60):
            return 0
        elif(self.igrac1.bodovi > self.bot.bodovi):
            return 1
        return 2
    
    def stanje(self, trenutniIgrac):
        if trenutniIgrac == self.igrac1:
            ruka = self.igrac1.ruka
            dobivene = self.igrac1.dobivene
            dobivene_protivnik = self.bot.dobivene
        else:
            ruka = self.bot.ruka
            dobivene = self.bot.dobivene
            dobivene_protivnik = self.igrac1.dobivene
        return {"briskula":self.briskula,"ruka":ruka,"stol":self.stol,"dobivene":dobivene,"dobivene_protivnik":dobivene_protivnik}
        

def main():
    briskula = Briskula("Ivana")
    briskula.odigraj_partiju()
    
if __name__ == '__main__':
    main()
