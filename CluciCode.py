import OnlineManager as m
# -*- coding: utf-8 -*-

def app(x):

    print("""Willst du ein Quiz erstellen oder rechnen?
        Wenn du rechnen willst schreibe a.
        Wenn du eines erstellen willst schreibe b.""")

    print("Gib hier deine Antwort ein:")
    answer = input()


    if answer == "a":

        print("coming soon")


    elif answer == "b":
        x = klasse(x)
    else:
        print("Error")

    return(x)
            
def klasse(x):
    
    print("""Welche Klasse bist du?
              1.Klasse
              2.Klasse
              3.Klasse
              4.Klasse
              5.Klasse""")
    
    antwort = input()
    
    if antwort=="1.Klasse":
        x.append("1.Klasse")
        
    elif antwort=="2.Klasse":
        x.append("2.Klasse")
        
    elif antwort=="3.Klasse":
        x.append("3.Klasse")
        
    elif antwort=="4.Klasse":
        x.append("4.Klasse")
        
    elif antwort=="5.Klasse":
        x.append("5.Klasse")
        
    else:
        print("Error")
    x = katerst(x)
    return(x)

def katerst(x):

    print("Kategorie?")
    print("""
    Mathematik
    Englisch
    Antwort:""")
    
    answer = input()
    
    if answer == "Mathematik":
          x.append("Mathematik")


    elif answer == "Englisch":
          x.append("Englisch")

    x = schwierigkeit(x)

    return(x)
    
def schwierigkeit(x):
    
    print("Schreibe einen Schwierigkeitsgrad von 1-5 auf:")
    antwort = input()
    if antwort < 1 or antwort > 5:
        print("Error")
    x.append(antwort)
    x = aufgabenname(x)
    return(x)   
    
    
def aufgabenname(x):
    print("Name von Thema: ")
    answer = input()
    x.append(answer)
    x = text(x)
    return(x)

def text(x):
    print("Aufgabenstellung:")
    answer = input()
    x.append(answer)
    x = anzahllösung(x)
    return(x)

def anzahllösung(x):
    print("Anzahl der Lösung: ")
    answer = input()
    x.append(answer)
    x = lösung(x)
    return(x)

def lösung(x):
    print("Schreibe die Lösung/en hier ein:")
    answer = input()
    x.append(answer)
    x = userid(x)
    return(x)

def userid(x):
    
    print("Userid:")
    antwort = int(input())
    x.append(antwort)
    x = likes(x)
    
    return(x)

def likes(x):
    print("Likes:")
    
    antwort = 5
    
    x.append(antwort)
    
    return(x)
    
def testForInt(x):
    try:
        int(x)
        return True
    except:
        return False
    


x = []

#x = app(x)

print(x)


c = m.getClient()


s = m.getSheet("Testing 2018",c,0)
s2 = m.getSheet("Testing 2018",c,1)

name = "Chris"
nameCol = 3

IdCol = 1
Id = 0
#update id
Id = m.getCell(2,IdCol,s2)
m.setCell(2,IdCol,(int(Id)+1),s2)
#addName
m.setCell(2,nameCol,name,s2)



#############################################################################
                        #lösen
#############################################################################
def anzahllösung2(z):
    
    nz = []
    for i in range(len(z)-6):
        c = z.pop()
    b = z.pop()    
    
    
    for anl in range(b):
        anl +=1
        print(anl, "Lösung")
        lo = int(input())
        nz.append(lo)
        print(nz)
    richtigfalsch(nz,c)    
    return

def richtigfalsch(nz,c):
    
    print(nz)
    print(c)
    if c in nz:
        print("True")
    else:
        print("False")
    







print(x)