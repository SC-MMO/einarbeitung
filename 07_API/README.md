# Projektname: Erstellung einer API zur Datenabfrage

## Beschreibung
In diesem Projekt wird eine API erstellt, über die Daten abgefragt werden können. Es sollen zwei Endpunkte implementiert werden: Einer, der alle Datensätze zurückgibt, und ein anderer, der einen bestimmten Datensatz anhand einer speziellen ID liefert.

## Inhaltsverzeichnis
1. [Einrichten der API](#einrichten-der-api)
2. [Implementierung der Datenabfrage](#implementierung-der-datenabfrage)
3. [Fragen und Antworten](#fragen-und-antworten)

## Einrichten der API
- Richte eine API ein, die auf einem Webframework wie Flask oder Django basiert.
- Konfiguriere die Routen und Endpunkte für die Datenabfrage.

## Implementierung der Datenabfrage
- Implementiere zwei Endpunkte: Einen für die Abfrage aller Datensätze und einen für die Abfrage eines bestimmten Datensatzes anhand einer ID.
- Stelle sicher, dass die Daten korrekt formatiert und über die API zurückgegeben werden.

## Fragen und Antworten
- Was ist eine API? Erläutere den Begriff und ihre Bedeutung in der Softwareentwicklung.
-> API (Application Programming Interface) bedeutet auf deutsch soviel wie Anwendungsprogrammierschnittstelle
-> APIs ermöglichen die Kommunikation zwischen mehreren Applikationen für den Datenaustausch

- Woraus besteht eine API? Beschreibe die Komponenten und Funktionen einer API.

- Wann wird eine API verwendet? Erkläre die Einsatzgebiete und Situationen, in denen APIs eingesetzt werden.
-> Eine API wird immer dann verwendet, wenn unterschiedliche Systeme miteinander für z. B. einen Datenaustausch kommunizieren müssen
-> Bsp. Applikation 1 will Daten von Applikation 2 abfragen -> API
-> Bsp. Ich will ChatGPT in meinem Python Programm verwenden -> API

- Warum sind APIs wichtig? Diskutiere die Bedeutung von APIs für die Interoperabilität und Integration von Systemen.
-> Ohne APIs könnten Systeme nicht miteinander kommunizieren, dementsrächend müsste jedes System alles selbst machen und unterschiedliche Systeme könnten nicht miteinander Synchronisiert sein

- Was ist ein API-Token und was ein API-Key? Unterscheide zwischen den beiden und erkläre ihre Verwendungszwecke.
API-Key:
    -> Definition: Dauerhaft gültiger Wert, welcher eienn Benutzer in einem System idenitfiziert 
    -> Verwendung: Authentifizierung
    -> Eigenschaften:
        --> Grundlegend permanent gültig
API-Token:
    -> Definition: Temporärer Wert, welcher den Zugriff auf bestimmte Ressourcen oder das ausführen von bestimmten Aktionen ermöglicht, meist als Sitzung.
    -> Verwendung: Autorisierung
    -> Eigenschaften:
        --> Nur temporär gültig (bsp. für 60 Minuten)
        --> Erneuerbar

- Warum nicht die Daten direkt auf der DB abfragen? Diskutiere die Vorteile der Verwendung einer API zur Datenabfrage im Vergleich zur direkten Abfrage der Datenbank.
-> Es ist sicherer, da man ein Muster für das, was man Abfragen können soll vorgeben kann und sagen kann, we was abfragen darf (Zugriffskontrolle)
-> Es ist einfacher, da man einfach nur ne Url aufrufen muss, man muss nicht immer eine SQL-Query abgeben
-> Es ist abstraktiert, also ist kann man den Zugriff auf die Datenbank über eine API leicht abschalten

- Nenne verschiedene Bereiche, in denen APIs verwendet werden. Beschreibe die Anwendungsbereiche und Beispiele für die Verwendung von APIs.
-> Wetterapps:
    --> Fragen alle paar Minuten von einem Server die derzeitigen Wetterwerte ab
-> Google Maps:
    --> Karte wird von Server abgefragt und dann auf meinem Gerät dargestellt
-> Beispielwebseite, welche Infos über Unternehmen anzeigt:
    --> Echkdaten der Firma von bsp. Zefix abfragen 
    --> Temperatur am Standort der Firma von Wetterserver abfragen

- Was ist REST? Erläutere den Begriff und die Prinzipien von RESTful APIs.
-> REST (Representational State Transfer) definiert, wie Computer über das Internet miteinander kommunizieren.
-> Client-Server-Modell: Der Client und Server sind getrennt voneinander.
-> Zustandslosigkeit: REST-API Aufrufe können unabhängig voneinander erfolgen.
-> Cache-Fähigkeit: Unterstützt die Speicherung Cache-fähiger Daten.
-> Einheitliche Schnittstelle: Der Client und Server sind so verbunden, dass solange die Schnittstelle gleich bleibt man nichts ändern muss.
-> Skalierbarkeit & Modularität
-> Code on Demand: Ermöglicht die Übertragung von Code oder Applets über die API zur Nutzung in der Anwendung.


- Was ist GraphQL und wie unterscheidet es sich von REST? Beschreibe die Unterschiede zwischen GraphQL und RESTful APIs.
-> GraphQL ist sowohl eine Abfragesprache für APIs als auch eine Applikation auf dem Server zur Ausführung von den Abfragen.
-> GraphQL: Der Client kann exakt bestimmen, welche Daten er haben will. Die Anfrage wird an die GraphQL Applikation auf dem Server gesendet, diese ruft dann die benötigten Daten ab.
-> REST: Der Client ruft Daten über vordefinierte Endpunkte mit festgelegten Strukturen ab. Man kann nicht genauer definieren, welche Informationen man haben will

- Welche Sicherheitsaspekte sind bei der Entwicklung einer API zu beachten? Diskutiere mögliche Sicherheitsrisiken und Best Practices für die API-Sicherheit.
-> Risiken:
    --> Vertraulichkeit von Daten
    --> Integrität von Daten (Injektionsangriffe)
    --> Spamschutz
    --> Man in the Middle Angriffe
-> Best Practices:
    --> Authentifizierung/Autorisierung
    --> Verschlüsselung von Daten
    --> Anfrageanzahlbegrenzung pro IP
    --> Eingabevalidierung (Injektionsangriffe verhindern)
    --> Verfolgung des Ablaufes der API-Requests
    --> Wiederholte Sicherheitstest