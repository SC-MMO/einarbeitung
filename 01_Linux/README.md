# Einrichten einer Virtual Machine (VM) unter Rocky Linux

## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.


### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer für das tägliche arbeiten. Du kannst ihn benennen wie du möchtest 


### Installierte Programme
a) nvim  
b) Git  
c) check-mk 
b) Erstelle ein Basis Monitoring für ein Server, Switches, Firewall ä

## Fragen und Antworten
- Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
-> Linux ist Open Source, es wird nicht von einer konkreten Firma sondern von vielen einzelnen Gruppen entwickelt, deshalbt gibt es viele unterschiedliche Versionen (Distributionen)

- Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
-> Man hat mehr Kontrolle über sein System, Linux ist meist performanter, Linx ist konfigurierbarer

- Warum sollt man nicht dauerhaft mit dem root User arbeiten?
-> Der root user hat alle Rechte, wenn man also auf irgendeinen verdächtigen Link oder so clickt, dann hat der Virus viel mehr Schadenspotenzial, außerdem beschütz eine Einschränkung von Rechten auch vor menschlicher Dummheit (Du kannst bsp. nicht dein eigenes System nuken)

- Was ist Virtualisierung und welche Vorteile bieten VMs?
-> Virtualisierung erlaubt es einem, mehrere OS auf einem Hardwareset laufen zu lassen, es ist gut für die Abtrennung wichtiger Systeme, wenn z. B. ein System komprimiert wird, dann wirkt das sich nicht auf die restlichen System aus.

- Was sind yum und dnf?
-> Packet Manager (Zum installieren, Updaten & Deinstallieren von Applikationen, Abhängikeiten (automatisch), Konfigurationsdateien, Metadaten Kernel Versionen, etc.)

- Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
-> IDE = Entwicklungsumgebung (fürs Coden)
-> IDE's haben im Gegensatz zu Texteditoren oft Debuggingmöglichkeiten und lassen dich den Code direkt ausführen/kompilieren
-> IDE's lassen einen leicht mehrere Dateien vergleichen bzw. etlauben es zwischen mehreren Dateien leicht zu wechseln
-> IDE's können oft direkt mit Git oder anderen Versionskontrollprogrammen grafisch interagieren
-> IDE's lassen einen oft ziemlich leicht Extensions für bsp. einen Live Share oder Live Server installieren

- Was ist der Unterschied zwischen einem LSP und einem Texteditor?
-> LSP erlaubt Autovervollständig

- Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
-> program &
-> 'jobs' zum anzeigen, 'bg' um jobs in den Hintegrund zu schieben, 'fg' um jobs in den Vordergrund zu schieben

- Wie kann man Skripte unter Linux erstellen und ausführen?
-> Leere  Shelldatei erstellen (touch meinscript.sh)
-> Datei bearbeiten (vim meinscrip.sh)
(Die ersten beiden Schritte können auch gleichzeitig gemacht werden)
-> Datein Ausführungsrechte (x) hinzufügen (chmod +x meinscript.sh)
-> Script ausführen (./meinscript.sh)

- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
-> Der Linux Kernel ist die Grundlage von Linux, es standardisiert den Hardwarezugriff für die Software
-> dnf up

- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
-> Symbolische Links zeigen auf den Dateinamen, Hardlinks zeigen auf den Dateicontent

- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
-> Weniger potenziell riskante changes & features
-> Längere Supportdauer -> Weniger Gefahr bei Hackerangriffen

- Wie schreibt man Kommentare in Bash?
-> # 

- Was ist vim?
-> Ein Texteditor, welcher sehr leicht über die command line aufgerufen werden kann (bsp. vim <datei>)
-> Eine erweiterte Version von Vi

### Linux-Befehle
Was bewirken folgende Befehle:
- `history`
-> Zeigt Command history an

- `chmod`
-> Lässt dich die Berechtigungen von bestimmten Gruppen/Nutzern für eine Datei konfigurieren/ändern

- `chown`
-> Lässt dich den Dateibesitzer / die Dateibesitzergruppe ändern

- `mv test.txt abc`
-> Lässt dich Dateien rumbewegen oder umbenennen

- `ll | grep test`
-> Zeigt alle Dateien welche im derzeitigen Verzeichnis welche 'test' in ihrem Namen enthalten an (ll = ls - l, grep test filtert nach test)

- `find . -name cisco`
-> Sucht nach Dateien oder Ordnern names cisco vom derzeitigen Verzeichnis ausgehend -> d. h. er geht in jeden Order rekursiv rein und schaut ob er einen Ordner names test findet 

- `find / -name cisco`
-> Sucht nach Dateien oder Ordnern names cisco vom root Verzeichnis ausgehend -> d. h. er geht in jeden Order rekursiv rein und schaut ob er einen Ordner names test findet 

- `tar -xvf archive.tar.gz`
-> Unkompressiert eine Datei names archive.tar.gz

- `df -h`
-> Zeigt wie viel Speicherplatz in den gemounteten Dateisystemen noch frei ist bzw. wie viel belegt ist

- `du -sh directory`
-> Zeigt Größe von Verzeichnis (Wie viele KB)

- `ps aux`
-> Zeigt alle derzeitigen Prozesse mit detallierten Infos wie CPU- und Arbeitsspeicher-Nutzung 

- `grep pattern file`
-> Zeigt alle Vorkomnisse des angegebenen Patterns in der angegebenen Datei (Patterns unterstützten Regex)

- `top`
-> Zeigt Linux Prozesse an

- `netstat -tuln`
-> Zeigt Protokollstatus

- `ifconfig`
-> Lässt dich IP-Netzwerkinterfaces konfigurieren 

- `ping host`
-> Schickt dem gegeben Host (Bsp. einen Computer) Nachrichten um zu überprüfen ob dieser erreichbar ist