## Aufgabenbeschreibung

### 1. Erstellen eines UML-Klassendiagramms basierend auf den gegebenen Daten:
- **Analysiere die Struktur des JSON-Dokuments** und identifiziere die relevanten Klassen und ihre Attribute sowie Beziehungen zueinander.
- **Zeichne ein UML-Klassendiagramm**, das die Klassen, ihre Attribute und Methoden sowie die Beziehungen zwischen den Klassen (z.B. Assoziationen, Vererbungen) darstellt.


### 2. Implementierung der Klasse in Python:
- **Erstelle eine Python-Klasse oder Klassen**, die die Struktur des UML-Klassendiagramms widerspiegeln.
- **Definiere die Attribute und Methoden** entsprechend den Daten und Anforderungen aus dem JSON-Dokument.
```python
from typing import List

class member:
    def __init__(self, *, name: str, age: int, secretIdentity: str, powers: List[str]):
        self.name = name
        self.age = age
        self.secretIdentity = secretIdentity
        self.powers = powers

class squad:
    def __init__(self, *, squadName:str, homeTown: str, formed: int, status: str, active: bool, members:List[member]):
        self.squadName = squadName
        self.homeTown = homeTown
        self.formed = formed
        self.status = status
        self.active = active
        self.members = members
```

### 3. Einlesen der JSON-Daten als Objekte der erstellten Klasse(n):
- **Schreibe ein Python-Skript**, das die JSON-Daten einliest.
- **Erstelle Instanzen der zuvor definierten Klasse(n)** und initialisiere sie mit den Daten aus dem JSON-Dokument.
```python
import json
with open("base.json", "r") as my_file:
    content = json.load(my_file)

groups = []
for group in content:
    obj = squad(
        squadName=group.get('squadName', 'N/A'),
        homeTown=group.get('homeTown', 'N/A'),
        formed=group.get('formed', 'N/A'),
        status=group.get('status', 'N/A'),
        active=group.get('active', False),
        members= [
            member(
                name=a_member.get('name', 'N/A'), 
                age=a_member.get('age', 'N/A'),
                secretIdentity=a_member.get('secretIdentity', 'N/A'),
                powers=a_member.get('powers', 'N/A')
                ) for a_member in group.get('members', [])]
        )
    groups.append(obj)
```

### 4. Methode zum Hinzufügen eines Members:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein neues Mitglied zum Team hinzufügt.
- Die Methode sollte die benötigten Informationen (z.B. Name, ID) als Parameter entgegennehmen und ein neues Mitgliedsobjekt erstellen und zur entsprechenden Liste hinzufügen.
```python
class squad:
    ...
    def add_new_member(self, *, name: str, age: int, secretIdentity: str, powers: List[str]):
        self.members.append(member(name=name, age=age, secretIdentity=secretIdentity, powers=powers))
```

### 5. Methode zur Ausgabe des Teams mit den jeweiligen Mitgliedern:
- **Implementiere eine Methode in der entsprechenden Klasse**, die das gesamte Team und deren Mitglieder auf eine lesbare Weise ausgibt.
- Die Methode sollte durch die Mitglieder des Teams iterieren und deren Details anzeigen.
```python
class member:
    ...
    def __repr__(self):
        result = "\n"
        for k, v in self.__dict__.items():
            result += f"{k}: {v}"
        return result

class squad:
    ...
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f"{k}: {v}\n"
        return result

```

### 6. Methode zum Löschen eines Members anhand der ID:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein Mitglied anhand seiner ID löscht.
- Die Methode sollte die Liste der Mitglieder durchsuchen, das Mitglied mit der passenden ID finden und es aus der Liste entfernen.
```python
class member:
    def __init__(self, *, id:int, name: str, age: int, secretIdentity: str, powers: List[str]):
        self.id = id
        self.name = name
        self.age = age
        self.secretIdentity = secretIdentity
        self.powers = powers
    ...

class squad:
    ...
    def del_member(self, *, id: int) -> bool:
        for idx, member in enumerate(self.members):
            if member.id == id:
                del self.members[idx]
                return True
        return False

import json
with open("base.json", "r") as my_file:
    content = json.load(my_file)

groups = []
for group in content:
    ids = iter(range(1 + len(group.get('members', []))))
    obj = squad(
        ...
        members= [
            member(
                id=next(ids),
                ...
                ) for a_member in group.get('members', [])]
        )
    groups.append(obj)
```

# Ganzer Code:
```python
from typing import List
import json

class member:
    def __init__(self, *, id:int, name: str, age: int, secretIdentity: str, powers: List[str]):
        self.id = id
        self.name = name
        self.age = age
        self.secretIdentity = secretIdentity
        self.powers = powers

    def __repr__(self):
        result = []
        for k, v in self.__dict__.items():
            result.append(f"{k}: {v}")

        return "\n" + ', '.join(result)

class squad:
    def __init__(self, *, squadName:str, homeTown: str, formed: int, status: str, active: bool, members:List[member]):
        self.squadName = squadName
        self.homeTown = homeTown
        self.formed = formed
        self.status = status
        self.active = active
        self.members = members
    
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f"{k}: {v}\n"
        return result
    
    def add_new_member(self, **kwargs):
        self.members.append(member(**kwargs))

    def del_member(self, *,  id: int) -> bool:
        for idx, member in enumerate(self.members):
            if member.id == id:
                del self.members[idx]
                return True
        return False



with open("base.json", "r") as my_file:
    content = json.load(my_file)

groups = []
for group in content:
    ids = iter(range(1 + len(group.get('members', []))))
    obj = squad(
        squadName=group.get('squadName', 'N/A'),
        homeTown=group.get('homeTown', 'N/A'),
        formed=group.get('formed', 'N/A'),
        status=group.get('status', 'N/A'),
        active=group.get('active', False),
        members= [
            member(
                id=next(ids),
                name=a_member.get('name', 'N/A'), 
                age=a_member.get('age', 'N/A'),
                secretIdentity=a_member.get('secretIdentity', 'N/A'),
                powers=a_member.get('powers', 'N/A')
                ) for a_member in group.get('members', [])]
        )
    groups.append(obj)

#Testing
for group in groups:
    print(group, "\n")

a_squad = squad(squadName="testname", homeTown="testtown", formed=1000, status="idk", active=True, members=[])
print(a_squad, "\n")

a_squad.add_new_member(id=1, name="test", age=4, secretIdentity="Batman", powers=[])
a_squad.add_new_member(id=2, name="test2", age=43, secretIdentity="Batgirl", powers=[])
print(a_squad)

a_squad.del_member(id=1)
print(a_squad)
```

## Fragen zur Objektorientierung

1. Warum verwendet man Objektorientierung?
-> Abbildung von realen Verhältnissen
-> Durch eigens erstellte Klassen kann man Objekte erstellen, welche bei der Übersichtlichkeit von Daten helfen
-> Man kann funktionen für bestimmte Objekte definieren und in Python auch mit Magic Methods dass verhalten bei bsp dem Vergleich von Objekten definieren

2. Welche weiteren Vorgehensweisen gibt es?
-> Prozeduale Programmierung
-> Funktionale Programmierung

3. Was ist ein Objekt und was eine Klasse?
-> Eine Klasse ist ein Bauplan für ein Objekt welches im Grunde ein eigenst definierter Datentyp ist (Ein Objekt ist eine Instanz einer Klasse)

4. Was versteht man unter Kapselung?
-> Man verbirgt die Attribute und ggf. Methoden einer Klasse und macht es nur für das was man verändern/aufrufen können soll möglich es aufzurufen bzw. zu verändern

5. Was ist Vererbung?
-> Wenn eine Klasse Attribute und/oder Methoden von einer anderen Klasse kopiert

6. Was versteht man unter Refactoring?
-> Umstrukturierung von Code, sodass dieser logischer, übersichtlicher und ggf. performanter läuft
-> Der Code wird auf einen vordefinierten Standard gebracht

7. Welche Rolle spielt das Refactoring bzgl. der Wiederverwendung von Code?
-> Wenn der Code einem bestimmten Standard entspricht und logisch aufgebaut ist, dann ist es einfahc ihn zu verstehen und somit einfach ihn in anderen Code sinnvoll einzubinden

8. Für was gibt es die `__init__`-Funktion in einer Klasse?
-> Die __init__ methode ist der Constructor, er wird bei dem erstellen eines Objekts der Klasse automatisch aufgerufen und setzt die Attribute

9. Für was braucht man den `self` Parameter?
-> Um in Methoden innerhalb der Klasse auf das Objekt für das die Methode angewandt wurde zu refferenzieren
-> Konkret z. B. um Attribute des genannten Objekts zu ändern

10. Wie schreibt man einzeilige und mehrzeilige Kommentare in Python?
-> # <Code> (Einzeilig)
-> """ <Code> """ (Mehrzeilig)

11. Welche weiteren objektorientierten Programmiersprachen neben Python gibt es? (3 Beispiele)
-> Java
-> C++
-> C#

12. Korrigiere die Fehlerhaften Skripte.

### Code 1
```python
class MyClass:
    def __init__(name):
        self.name = name

    def greet():
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()
```

# Korrigiert 1 (self ergänzt)
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()
```


### Code 2
```python
def say_hello():
print("Hello, World!")  

say_hello()
```

# Korrigiert 2 (print statement eingerückt)
```python
def say_hello():
    print("Hello, World!")  

say_hello()
```


### Code 3 
```python
x = 10
if x = 5:   
    print("x is 5")
```

# Korrigiert 3 (= durch == ersätzt, da = für Variablenwertvergebung benutzt wird, Gleichheitsvergleiche werden mit == gemacht)
```python
x = 10
if x == 5:   
    print("x is 5")
```


### Code 4
```python
numbers = (1, 2, 3, 4, 5) 
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```

# Korrigiert 4 (Tuple zu List geändert, da man Tuplewerte nicht verändern kann)
```python
numbers = [1, 2, 3, 4, 5] 
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```


### Code 5
```python
values = [1, 2, 3, 4, 5]
a, b, c = values
```

# Korrigiert 5 (List bis Element mit dem indx 3 (exkl.) gesliced)
```python
values = [1, 2, 3, 4, 5]
a, b, c = values[:3]
```