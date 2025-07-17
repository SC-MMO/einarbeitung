## Aufgabenbeschreibung
Die Daten sollen in einer Datenbank gespeichert werden.

1. **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.
2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.
3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.
4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
   a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
   b) **Löschen**: Daten werden aus der Datenbank gelöscht.
   c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
   d) **Auslesen**: Daten werden aus der Datenbank abgerufen.

-> ./ER Diagramm.png & ./04_Aufgaben.py

### Fragen:

- Welche Datenbanken gibt es? SQL, SQLite
-> Hierarchische Datenbanken:
   -> Sitemaps
   -> XML
-> Relationale Datenbanken (SQL):
   -> MySQL
   -> SQLite
-> Nicht-relationale Datenbanken (NoSQL)
   -> MongoDB 
   -> CouchDB
-> Objektorientierte Datenbanken:
   -> ObjektDB
   -> Db4o
-> Netzwerkdatenbanken:
   -> IDS 
   -> EDMS
-> Zeitreihen-Datenbanken:
   -> InfluxDB
   -> TimescaleDB

- Wann macht welcher Typ Sinn? SQL bei gleichbleibenden Attributen.
-> Wenn sich die Struktur der Datenbank nicht wirklich verändert, dann macht eine Relationale Datenbank Sinn

- Was ist ein Primary Key und was ein Foreign Key?
-> Primary Key: Object id des des Objekts selbst
-> Foreign Key: Object id eines referrenzierten Objekts

- Was ist ein nativer und was ein künstlicher Primary Key?
-> Falls man keine eigene Logik für die Erstellung eines Primary Keys (nativer) festlegt wird den Objekten automatisch eine id als primary key gegben (künstlicher)

- Welche Beziehungstypen zwischen Tabellen gibt es?
-> 1:1 (1 zu 1)
-> 1:n (1 zu Viele)
-> n:n (Viele zu Viele)

- Welche Wildcards gibt es in MySQL und was bedeuten sie?
-> % = Ein oder mehr Charaktäre
-> _ = Ein Charaktär

- Was ist ein Join?
-> Operation, mit der man mehrere Tabellen abhängig von bestimmten Spalten oder Werten miteinander verbinden

- Was ist ein left- und was ein right-Join?
-> Left-Join: Zeigt alle Daten aus der linken Tabelle und ergänzt die aus der rechten Tabelle
-> Right-Join Zeigt alle Daten aus der rechten Tabelle und ergänzt die aus der linken Tabelle
-> Falls irgendwo ein Eintrag fehlt, dann wird dieser durch NULL ersetzt

- Was ist das kartesische Produkt zweier Tabellen?
-> Alle möglichen Kombinationen aus den einzelnen Rows dieser Tabellen

- Was ist Kaskadierung?
-> Kaskadisierung ist, wenn sich Änderungen auf einem übergeordneten Objekt sich auf ein untergeordnetes Objekt weitergeben
-> BSP. Ich lösche ein Buch Objekt, welches viele Seite Objekte hatte, daraufhin werden automatisch alle Seite Objekte, welche in dem Buch Objekt waren gelöscht

- Wann werden Gruppierungen benötigt?
-> Wenn man bestimmte Daten aus unterschiedlichen Rows auf Basis einer gemeinsamen Spalte (wie einer id) zusammenfassen will
-> z. B. Wenn man einen Kunde mit vielen Bestellungen hat und die insgesammte Bestellpreissumme haben will, dann gruppiert man die Bestellungen nach der Kundennummer und zieht dann die Summer des Bestellwerts

- Was ist ein DBMS?
-> System zum managen von Datenbanken (z. B. Mongo DB)

- Was versteht man unter Datenintegrität?
-> Daten müssen frei von Ungenauigkeiten und Wiedersprüchen sein 
-> Daten müssen korrekt gespeichert werden
-> Enitätsintegrirär (Keine Duplikate, durch Primärschlüssel)
-> Referentielle Integrität (Daten müssen Konsistenz sein (Durch Beziehungen))
-> Wertebereichsintegrität (Daten müssen Sinn ergeben, z. B. kein Geburtsdatum in der Zukunft)
-> Sematische Integrität (Zellen dürfen nur die angegebene Art von Daten zulassen)

- Was ist Normalisierung?
-> Redundante Speicherung wird durch das nur einmal aufschreiben von Daten entfernt, dadurch gibt es keine Inkonsistenten oder Anomalien

- Was sind Aggregationsfunktionen und welche gibt es? (3 Beispiele)
-> Aggregationen machen etwas mit den Werten einer Spalte mehrerer Rows
-> z. B. COUNT() Zählt die Anzahl der Werte 
-> z. B. SUM() berechnet die Summe der Werte
-> z. B. MAX() gibt den hochsten Wert der Werte wieder