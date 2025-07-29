# Projektname: Datenpräsentation mit interaktiver Tabelle

## Beschreibung
In diesem Projekt soll eine Webanwendung erstellt werden, um Daten in einer Tabelle darzustellen. Die Tabelle soll über eine JavaScript-Suche verfügen, die es dem Benutzer ermöglicht, nach bestimmten Datensätzen zu suchen. Darüber hinaus soll es möglich sein, beim Klicken auf einen Datensatz ein Popup zu öffnen, das weitere Details zu diesem Datensatz anzeigt.

## Inhaltsverzeichnis
1. [Einrichten der Webanwendung](#einrichten-der-webanwendung)
2. [Erstellen der interaktiven Tabelle](#erstellen-der-interaktiven-tabelle)
3. [Implementieren der JavaScript-Suche](#implementieren-der-javascript-suche)
4. [Öffnen eines Popups bei Klick](#öffnen-eines-popups-bei-klick)
5. [Fragen und Antworten](#fragen-und-antworten)

## Einrichten der Webanwendung
- Richte eine neue Webanwendung ein, die die Daten anzeigen wird.
- Verwende geeignete Technologien wie HTML, CSS, JavaScript und eine geeignete Webframework wie Flask oder Django.

## Erstellen der interaktiven Tabelle
- Erstelle eine Tabelle in der Webanwendung, um die Daten anzuzeigen.
- Gestalte die Tabelle so, dass sie benutzerfreundlich ist und gut lesbar ist.

## Implementieren der JavaScript-Suche
- Implementiere eine JavaScript-Suchfunktion, die es dem Benutzer ermöglicht, nach bestimmten Datensätzen in der Tabelle zu suchen.
- Die Suchfunktion sollte dynamisch sein und die Tabelle entsprechend filtern, während der Benutzer tippt.

## Öffnen eines Popups bei Klick
- Implementiere eine Funktion, die es dem Benutzer ermöglicht, beim Klicken auf einen Datensatz ein Popup zu öffnen.
- Das Popup sollte weitere Details zu dem ausgewählten Datensatz anzeigen, möglicherweise in Form eines Modalfensters oder einer Lightbox.

## Fragen und Antworten
- Was sind die verschiedenen Technologien, die in der Webentwicklung verwendet werden? Nenne Beispiele und ihre Verwendungszwecke.
-> Flask: Webseiteaufsatz
-> HTMl: Anordung eines Inhalts einer Webseite, sowie definierung des Inhalts
-> CSS: Styling des Inhalts einer Webseite
-> JS: Dynamisierung des Inhalts einer Webseite

- Was versteht man unter serverseitig und clientseitig? Erläutere die Unterschiede und ihre Bedeutung in der Webentwicklung.
-> Serverseitig ist alles, was auf dem Server auf dem die Webseite läuft passiert, alles was das Gerät eines Clients selber macht ist clientseitig

- Erkläre die Begriffe Frontend und Backend und ihre Rollen in der Webentwicklung.
-> Frontend: 
    --> Alles, mit dem der Benutzer einer Webseite in Kontakt kommt (die GUI).
    --> HTML, CSS, JS 
-> Backend:
    --> Serverlogik, ist für die Bereitstellung für die Daten, welche das Frontend darstellt verantwortlich
    --> Datenkbanken, APIs, Authentifizierung
    --> Python, PHP, etc.

- Erkläre HTML, CSS und JS und wie diese zusammenarbeiten, um Webseiten zu erstellen.
-> Ref. erste Antwort

- Aus welchen beiden Hauptteilen besteht ein HTML-Dokument? Beschreibe die Struktur eines typischen HTML-Dokuments.
-> Ein HTMl-Dokument besteht in der Regel aus einem head und einem body
-> Im head stehen die generellen Infos über das HTML-Dokument wie der Name der Seite und die Stylesheets
-> Im body steht der anzuzeigende Inhalt der Webseite

- Wie schreibt man Kommentare in HTML, CSS und JS? Zeige Beispiele für Kommentare in jeder dieser Sprachen.
-> HTML: <!-- ... -->
CSS: /* ... */
JS:
    --> Einzeilig: // ...
    --> Mehrzeilig: /* ... */ 

- Was ist ein HTML-Tag? Erläutere die Bedeutung und Verwendung von HTML-Tags.
-> HTML-Tags dienen der Strukturierung von Inhalt auf einer Webseite, durch sie kann man definieren wie etwas aufgebaut sein soll, und wie es aussehen soll (tags haben style)

- Was ist ein div-Tag und wofür wird es verwendet? Beschreibe die Verwendung von div-Tags in HTML.
-> Der div-Tag dient der Unterteilung verschiedener Webseitbereiche, es ist eine Art Container mit dem man Elemente gliedern kann

- Was ist XPath? Erkläre, wofür XPath verwendet wird und wie es in der Webentwicklung eingesetzt werden kann.
-> XPath ist eine Query Sprache für XML Dokumente, man kann den Wert bestimmter Elemente in einem XML Dokument aufrufen, des Weiteren bietet es auch einige Filteroptionen
-> Man kann es beispielsweise Verwenden um nur eine bestimmte Art von Element welches einen Wert von über 100 hat aufzurufen und ggf. anzuzeigen

- Was ist ein Z-Index? Erläutere die Bedeutung des Z-Index in CSS.
-> Die Höhe eines Objekts auf einer Seite, Objekte mit einem höheren Z-Index werden über Objekten mit einem niedrigeren Z-Index angezeigt

- Was ist jQuery? Beschreibe die Funktionen und Verwendungszwecke von jQuery.
-> JQuery ist eine JS-Bibiliothek, sie stellt JS Funktionen für eine einfachere Manipulation von Webseitinhalt und viele visuelle Effekte bereit
-> Man kann mit der JQuery DOM Manipulation den CSS eines Elements dynamisch verändern
-> Bsp: Button soll nach 30 Sekunden rot werden

- Wie lässt sich JavaScript in eine Website einfügen? Nenne zwei Möglichkeiten, um JavaScript-Code in HTML-Dokumente einzubinden.
-> Include: <script src="URL">
-> Inline: <script> ... </script>