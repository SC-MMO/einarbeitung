## Aufgabenbeschreibung

1. Erstelle aus den Daten eine YAML-Datei.
2. Erstelle ein XML-File aus der JSON.
3. Validiere das XML-File mittels XSD.

# Aufgaben -> ./03_Aufgaben.py

### Fragen:

1. Was sind die Unterschiede der Datentypen?
-> Darsetellung: JSON basiert auf JS, XML auf HTML, YAML benutzt Einrückungen
-> unterschiedliche Performance
-> XML ist eine Markup Sprache

2. Was sind Vor- und Nachteile der jeweiligen Dateiformate?
JSON:
- Vorteile:
    -> Sehr schnell
    -> Syntax wie in Python und JS
- Nachteile:
    -> Wenig Datentypen
    -> Keine Kommentare

XML:
- Vorteile:
    -> Möglicher Schemacheck durch XSD
- Nachteile:
    -> Komplexerer Syntax und schlechtere Performance als JSON

YAML:
- Vorteile:
    -> Meschliche Lesbarkeit
    -> Viele unterstützte Dateitypen
- Nachteile:
    -> Viel fehlerpotenzial bei kleinen Einrückungsfehlern

3. Wofür wird XML verwendet?
-> Datenserialisierung
-> Datenaustausch
-> Speicherung von Konfigurationsdateien

4. Unterstützt XML benutzerdefinierte Tags?
-> Ja

5. Wann ist welcher Datentyp von Vorteil?
-> XML, wenn man sichergehen will, dass Daten so interpretiert werden, wie man es will
-> JSON, wenn man die Datenübertragung simpler und performanter will
-> YAML, wenn man seine Daten am Lesbarsten haben will

6. Was ist eine XSD-Datei?
-> In einer XML Schema Definition (XSD) Datei kann man ein Schema für eine XML Datei anlegen und danach prüfen ob die XML Datei das Schema matched

7. Was versteht man unter Validierung?
-> Generell bedeutet Validierung die Richtigkeit von etwas zu prüfen aber im Kontext von diesen Dateiformaten bedeutet es zu überprüfen, ob die Dateien den Aufbau, den man haben will matchen

8. An was erinnert eine XML-Datei bzgl. ihres Aufbaus?
-> html

9. Was bedeutet Parsen?
-> Die Daten von einer Datei so umzustrukturieren, dass sie für einen Anwendungsfall passen (z. B. durchs Umwandeln in einen anderen Dateityp oder durch eine Änderung der Struktur)