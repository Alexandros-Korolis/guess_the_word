mylist=['ΠΟΛΥΚΑΤΟΙΚΙΑ','ΣΙΔΗΡΟΔΡΟΜΟΣ','ΑΥΤΟΚΙΝΗΤΟΔΡΟΜΟΣ','ΔΙΑΜΕΡΙΣΜΑ','ΛΕΩΦΟΡΟΣ',
        'ΠΡΩΤΕΥΟΥΣΑ','ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ','ΓΑΤΑ']

import random
x=random.choice(mylist)
word=list(x)

def myfun92(word):    
    gme=word[:]
    for i in range (len(gme)):
        gme[i]='_'
    print(gme)

    cgl= ['Α','B','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Π','Ρ',
          'Υ','Σ','Τ','Φ','Χ','Ψ','Ο','Ω']

    fail=0
    while fail <= 5 :   
        gletter=input('Give me a capital Greek letter : ') 
        
        if gletter in cgl :
            for i in range (len(gme)):
                if gletter == word[i]:
                    gme[i] = gletter
                    print(gme)                               
        else:
                print('Δώσε κεφαλαίο Ελληνικό γράμμα')
            
        if gletter not in word:
            fail += 1
            print ('Αριθμός αποτυχιών :',fail )
        else:
            continue 
    
        if gme == word:
            print('Μπράβο κέρδισες!!')
            break
        
        elif fail == 5:
            print('Δυστυχώς εχασες!! Η λέξη ήταν :' , x)
            break
               
 
        
    
    