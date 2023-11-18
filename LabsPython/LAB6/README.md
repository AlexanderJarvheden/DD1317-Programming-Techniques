### Innehåller uppgifterna för LAB 4, 5 och 6 då de bygger på varandra

## Uppgift LAB4
Definiera en klass “Student” som har minst tre attribut: förnamn, efternamn och personnummer. Klassen ska ha minst två metoder, __init__ och __str__.

Skapa minst tre objekt av typen “Student” genom att be användaren skriva in information om studenter. Fundera på bästa sättet att spara ner de skapade objekten.

När alla objekt är skapade ska programmet skriva ut alla skapade objekt.

### Frivilliga extrauppgifter
#### Redigera listan
I grunduppgiften kan vi endast lägga till objekt av typen Student. Lägg till så att användaren kan ändra och ta bort objekt från listan.

##### Exempelutskrift
Vill du lägga till (l), ändra (a) eller ta bort (t) ett objekt? a

Skriv in personnumret på objektet du vill ändra: 0101010000
Vill du ändra namn på Emma Löv (j/n)? j
Skriv in det nya namnet: Ebba Löv

Nu är namnet för 0101010000 ändrat till Ebba Löv!

#### Lägga till många studenter
Ändra så att programmet kan fråga efter 
 studenter istället för bara tre.

##### Exempelutskrift
Hur många studenter vill du lägga till? 2

Vad heter studenten? Jan Jansson
Vad är studentens personnummer? 0404040010

Objektet skapat!

Vad heter studenten? Per Persson
Vad är studentens personnummer? 0303030030

Objektet skapat!

Här är alla sparade objekt:
Namn: Jan Jansson Personnr: 0404040010
Namn: Per Persson Personnr: 0303030030

## Uppgift LAB5
Nu ska vi skriva en klass “School” som har minst ett attribut students.

Skapa ett objekt av typen School. Låt igen användaren skriva in information om minst tre studenter och skapa objekt av typen Student.

Spara objekten i School-objektets attribut students.

Fundera på vad som är den bästa typen av behållare för att spara objekten. Vilka nackdelar och fördelar finns det med olika behållare?

Lägg nu till en metod i klassen School som låter användaren söka efter en elev som går på skolan och som skriver ut om eleven finns 
och det funna Student-objektet. Du får välja själv om du ska söka med hjälp av förnamn, efternamn eller personnummer.

### Frivilliga extrauppgifter
Hantera lärare
Lägg till en klass Person som klassen Student ärver ifrån, se arvLinks to an external site.. Skapa en till klass Teacher som också ärver från Person. Lägg till så att klassen Skola har två attribut, en för studenter och en för lärare, alternativt hitta på ett eget sätt att hålla isär elever och lärare i ditt program.

##### Exempelutskrift
...
Vad för roll har personen? Lärare
Vad heter personen? Albert Einstein
Vad är personens personnummer? 7903140050

Personen tillagd!

Här är alla studenter på KTH:
Namn: Jan Jansson Personnr: 0404040010
Namn: Per Persson Personnr: 0303030030
Namn: Emma Emilsson Personnr: 0101010000

Här är alla lärare på KTH:
Namn: Albert Einsten Personnr: 7903140050

## Uppgift LAB6
I denna laboration ska du låta användaren mata in namnet på en fil som innehåller alla studenters uppgifter. Därefter läser du in uppgifterna på filen och använder dem i ditt program som du skrev i förra laborationen. Om filen inte finns ska användaren mata in ett nytt filnamn.

##### Exempelutskrift
Vad heter filen med alla studenter? students.cs
Den filen fanns inte! Skriv in en ny fil: students.csv

Dessa studenter är skrivna på KTH:
Namn: Johan Tierney Personnr: 8411285597
Namn: Erik Bolin Personnr: 9910247016
Namn: Per Edenström Personnr: 8410024155

...

Vilken student vill du söka efter? Jan

Den studenten läser på KTH:
Namn: Jan Jansson Personnr: 0404040010

### Krav
Användaren ska få mata in ett nytt filnamn om filen inte hittas.
Kraven för laboration 5 ska vara uppfyllda. 
Din kod ska uppfylla kraven i rättningsmatrisen.

### Redovisning
Denna laboration ska redovisas för en lärarassistent på ett laborationstillfälle. Information om bokning av redovisningstillfälle kommer komma upp på Canvas. På redovisningen ska du kunna köra ditt program och beskriva din kod detaljerat.

### Frivillig extrauppgift: Redigera
Ge användaren möjlighet att lägga till, ändra eller ta bort objekt. I slutet av programmet ska alla objekt läsas tillbaka till en fil som användaren får skriva in namnet på.

##### Exempelutskrift
Vad heter filen med alla studenter? students.cs
Den filen fanns inte! Skriv in en ny fil: students.csv

Dessa studenter är skrivna på KTH:
Johan Tierney 8411285597
Erik Bolin 9910247016
Per Edenström 8410024155
...

Vill du lägga till (l), ändra (a) eller ta bort (t) ett objekt? a

Skriv in personnumret på objektet du vill ändra: 0101010000
Vill du ändra namn på Emma Löv (j/n)? j
Skriv in det nya namnet: Ebba Löv

Nu är namnet för 0101010000 ändrat till Ebba Löv!

Ange namn på den fil som uppgifterna ska sparas på: students.csv

Nu är alla uppgifter sparade på filen students.csv
