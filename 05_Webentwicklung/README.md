# Projektname: Webanwendung mit Flask und ansprechendem Styling

## Beschreibung
Dieses Projekt zielt darauf ab, eine Webanwendung mit Flask aufzusetzen und sie mit einem ansprechenden Styling zu versehen. Zusätzlich sollen weitere Seiten erstellt werden, auf denen Daten aus einer Datenbank ausgelesen werden können. Die Benutzer sollen die Möglichkeit haben, Daten direkt über die Website zu bearbeiten oder zu löschen.

## Inhaltsverzeichnis
1. [Webanwendung mit Flask aufsetzen](#webanwendung-mit-flask-aufsetzen)
2. [Daten aus der Datenbank auslesen](#daten-aus-der-datenbank-auslesen)
3. [Daten bearbeiten und löschen](#daten-bearbeiten-und-löschen)
4. [Fragen und Antworten](#fragen-und-antworten)

## Webanwendung mit Flask aufsetzen
- Setze eine Webanwendung mit Flask auf.
- Verleihe der Webanwendung ein ansprechendes Styling, um eine positive Benutzererfahrung sicherzustellen.
- Erstelle weitere Seiten, auf denen die Daten aus einer Datenbank angezeigt werden.

## Daten aus der Datenbank auslesen
- Implementiere Funktionen, um Daten aus der Datenbank abzurufen und auf den Webseiten darzustellen.

## Daten bearbeiten und löschen
- Biete den Benutzern die Möglichkeit, Daten direkt über die Website zu bearbeiten oder zu löschen.

# Aufgaben -> ./Webentwicklung_Flask/

## Fragen und Antworten
- Was ist Webentwicklung? Erkläre den Prozess des "Bauens" von Webseiten oder Anwendungen für das Internet.
-> Webentwicklung ist das Erstellen von Webseiten (& Webanwendungen wie Crunchyroll), es umfasst quasi alles was man braucht, damit eine Webseite funktioniert
-> 

- Was ist ein Framework und was ein SDK? Unterscheide zwischen den beiden und erkläre ihre Rolle in der Entwicklung.
-> SDK: Sammlung von Libraries, APIs, Dokus, Tools, etc. welches dir quasi Bausteine, welche du selber verwenden kannst gibt
-> Framework: Art Grundgerüst für eine bestimme Art von Applikation, es bestimmt die Grundstruktur und den Grundablauf eines Programms fest und lässt dich deinen eigenen Code an bestimmten stellen einhängen
-> Unterschiede:
Kontrolle:
    -> SDK: Man kann selber kontrollieren, wie man das gegebene verwendet
    -> Framework: Man ist von der Struktur des Frameworks abhängig
Aufwand:
    -> SDK: Man muss alles selber aufbauen
    -> Framework: Der Grundaufbaus ist bereits vorhanden

- Welche Sprachen und Frameworks spielen eine Rolle in der Webentwicklung? Nenne Beispiele und ihre Verwendungszwecke.
-> HTML -> Inhalt und Struktur von Webseiten definieren (bsp. Absätze, Bilder)
-> CSS -> Gestaltung und Layout von Webseiten definieren (bsp. Farbe, Schriftart)
-> JS -> Seiten interaktiv/dynamisch machen (bsp. dynamischer Table mit Pagination)
-> TS -> Typsicherheit für JS
-> SQL/NoSQL -> Verbindung mit Datenbank durch bsp. MySQL
-> Python, Java, C++, etc. -> Sprachen für die Backend Logik

- Was ist Jinja2 und wofür kann ich es verwenden? Erläutere die Verwendung von Jinja2 in Flask.
-> Jinja2 ist eine HTML-Erweiterung, welche dich html Seiten mit vom Backend kommenden Daten eine Seite definieren lässt, es erlaubt auch Vererbung von Webseiteigenschaften und Layouts

- Was sind die Flask HTTP-Methoden, welche gibt es und wann brauche ich welche? Beschreibe die verschiedenen HTTP-Methoden in Flask und ihre Verwendung.
-> Flask HTTP-Methoden sind Arten wie man auf eine Webseitroute zugreifen kann
-> GET: Wenn man Daten abrufen will                                                     -> Meistens nur Header (Body kann theoretisch existieren)
-> POST: Wenn man eine Ressource auf dem Server erstellen oder verändern will           -> Header + Body
-> PUT: Wenn man eine bestimme Ressource auf dem Server erstellen oder ersetzen will    -> Header + Body
-> DELETE: Damit kann man eine bestimmte Ressource wie eine SQL Row löschen             -> Meistens nur Header (Body eher selten)
-> PATCH: Wenn man eine Ressource teileweise aktualisieren (verändern) will             -> Header + Body
-> HEAD: GET aber man bekommt nur Header-Informationen                                  -> Nur Header
-> OPTIONS: Wenn man wissen will was für HTTP-Methoden man auf eine Route anwenden kann -> Meistens nur Header

- Was sind Strukturelemente? Erläutere die Bedeutung von Strukturelementen in der Webentwicklung.
-> Strukturelemente sind html tags, welche die Webseite in unterschiedliche Teile aufteilen, man packt z. B. die Navigation in einen Nav tag

-> Strukturelemente sind HTML-Tags, welche verwendet werden, um den Aufbau und Einteilung einer Webseite zu definieren. 
-> Strukturelemente teilen den den HTML-Code in Unterbereiche auf. 
-> Beispiel: <header>, <nav>, <section>, <article>.
-> Anwendungsbeispiel: Die Navigationsleiste kommt in den Nav tag und der header in den header tag

- Was sind Flask Blueprints und welchen Vorteil bieten sie? Erkläre die Verwendung von Flask Blueprints in großen Webanwendungen.
-> Flask Blueprints sind Bestandteile der Webseite, welche nicht direkt in der innit definiert sind, sie erlauben es Webseitecode auszulagern und strukturierter zu schreiben, man kann beispielsweise für die Authentifikation einen eigenen Blueprint mit eigenen Routen erstellen

- Was ist Bootstrap und wie kann ich es verwenden? Beschreibe Bootstrap und seine Rolle beim Erstellen responsiver Websites.
-> Bootstrap ist eine CSS + JS Library, welche beispielsweise css Classen für die Farbe von Objekten hat, man braucht also nicht selber seine Klassen fürs Stylen von Objekten erstellen
-> Bootstrap Klassen und Funktionen sind im Grunde für Handys entwickelt und werden daraufhin hochskaliert, somit kann jeder die Webseite gut nutzen
-> Bootstrap Klassen und Funktionen sind so entwickelt, dass sie auf kleinen Bildschirmen funktionieren und für große Bildschirme werden sie erweitert

- Was sind SVGs? Erläutere SVGs und ihre Verwendung in der Webentwicklung.
-> SVGs sind Dateien, welche anstatt mit Pixeln durch mathematische Formeln definiert sind. Dadurch gibt es beim Skalieren keinen Qualitätsverlust.
-> Durch sie ist es egal, welche Auflösung ein Bildschirms hat, die Bilder sehen immer scharf aus.

- Was versteht man unter responsive Design? Erkläre die Bedeutung von responsivem Design und warum es wichtig ist.
-> Webseiten sollen egal mit welchen Eigenschaften eines Geräts funktionieren und gut aussehen
-> Bsp. Wenn ein Gerät eine andere Bildschirmauflösung hat, dann sollen die Elemente der Webseite dynamisch angepasst werden
-> Ohne responsives Design wären Webseiten auf bsp. Handys schwer lesbar oder nur bedingt nutzbar.