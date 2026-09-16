# Design: Skill `/4mat-me`

Stand: 2026-09-16. Freigegeben von Ruben Langwara.

## Zweck

Ein Interview-Skill für Claude Code, der eine Person dabei begleitet, eine Botschaft nach dem 4MAT (Bernice McCarthy, deutsche Fassung nach Sebastian Mauritz) zu sortieren. Vorbild ist `grill-me` von Matt Pocock: relentless interview in Runden, stateless, offen für jedes Thema. Unterschied: Der Entscheidungsbaum steht fest.

Typischer Fall: Eine Führungskraft kündigt dem Team eine Veränderung an und will vorher wissen, als wer sie spricht, für wen, was im Raum ist, und warum, was, wie, wozu.

## Nicht Ziel

- Keine Dateien schreiben (kein CONTEXT.md, keine ADRs, kein Team-Gedächtnis). Personendaten über Teammitglieder gehören nicht auf die Platte.
- Kein fertiger Redetext ohne Nachfrage. Der Text ist ein Angebot nach der Rahmung.
- Keine Typologie der Zuhörenden (Warum-Typ usw.) als Diagnose. Präferenzen dürfen als Hinweis dienen, alle vier Fragen werden immer beantwortet.

## Entscheidungen

| Frage | Entscheidung | Grund |
|---|---|---|
| Sprache | Deutsch | Die Unterscheidung Warum (weil) / Wozu (damit, um zu) trägt nur im Deutschen. Zielgruppe deutschsprachig. README mit englischem Abschnitt. |
| Aufruf | `/4mat-me`, `disable-model-invocation: true` | Wie grill-me: bewusst gestartet, Claude springt nicht ungefragt hinein. |
| Zustand | Stateless. Mitgegebene Dokumente werden gelesen. | Fakten finden ist Aufgabe des Skills, nicht des Nutzers. Dateien schreiben nur auf ausdrückliche Bitte. |
| Ergebnis | Sortierte Rahmung im Chat, danach Angebot Redetext | Nutzer behält die Formulierung in der Hand. |
| Sprachregeln | Kompakt eingebettet, Verweis auf Skill `vermenschlichen`, falls installiert | Der Skill muss ohne Rubens lokale Skills funktionieren. |
| Repo | `Rubwara93/4mat-skill`, öffentlich, MIT, Plugin-Manifest | Teilen per Marktplatz oder Kopieren. |

## Struktur des Interviews

Baum, in dieser Abhängigkeit:

```
Anlass
 ├─ Als wer?      Rolle, Position, Funktion. Welchen Hut habe ich auf?
 ├─ Für wen?      Rolle, Position, Informationsstand der Zuhörenden.
 └─ Im Raum       Was ist vermutlich schon da: Flurfunk, Vorgeschichte, Emotionen beider Seiten.
      └─ Warum    Vergangenheit, Anlass, Problem. Antwort mit „weil".
           └─ Was Zahlen, Daten, Fakten. Was ändert sich, was bleibt.
                └─ Wie   Schritte, Zeitplan, Ablauf des Gesprächs selbst, Ort für Zuhören und Abfrage.
                     └─ Wozu  Zukunft, Endbild, Nutzen. Antwort mit „damit" oder „um zu".
Offene Punkte     Was noch nicht gesagt werden kann: benennen, begründen, terminieren.
```

Runden über die Frontier wie in `grilling`: Alle Fragen, deren Voraussetzungen geklärt sind, kommen in einer Runde, nummeriert, mit Empfehlung. Runde 1 enthält immer Anlass, Als wer, Für wen, Im Raum. Die Reihenfolge der vier Fragen bleibt Warum, Was, Wie, Wozu. Fragt der Nutzer selbst zuerst nach dem Wozu, darf der Skill es vorziehen und danach die Lücken schließen.

Format je Frage (übernommen aus `grilling`):

```
❓ **F1** - **Titel**: Fragetext, ggf. mit Auswahl

➡️ Empfehlung
```

## Qualitätsprüfungen, die der Skill anwendet

- Warum und Wozu müssen sich unterscheiden. Test: Warum mit „weil" lesen, Wozu mit „damit" lesen. Ist das Warum ein verkleidetes Ziel, nachfragen.
- Das Was enthält, was sich konkret ändert und was gleich bleibt. Unscharfe Begriffe („Neuaufstellung", „Synergien", „agiler") werden geschärft: Was heißt das für die Person in der dritten Reihe?
- Das Wie enthält den Ablauf der Veränderung und den Ablauf des Gesprächs selbst (erst spreche ich als X, dann höre ich zu, am Ende frage ich ab).
- Offene Punkte werden nicht mit Pseudo-Antworten gefüllt („Veränderung ist die einzige Konstante"). Stattdessen: Was fehlt, warum noch, wann kommt es.
- Die Rahmung bleibt kurz. Eine Ansprache von fünf Sätzen reicht oft.

## Emotionen im Raum

Leitsatz: Erleichterung kommt vor Erheiterung. Störungen haben Vorrang. Erst die unangenehmen Emotionen abholen, dann Chancen sammeln.

Erwartbare Emotionen bei Veränderungen und ihr Bedürfnis:

| Im Raum | Braucht | Frage oder Baustein |
|---|---|---|
| Unsicherheit, Sorge, Angst | Sicherheit, Orientierung, Kontrolle | Was bleibt? Welche Sicherheiten brauchen Sie? Fehlende Infos begründen und terminieren. |
| Widerstand, Ablehnung, Nörgeln | Beständigkeit, Bekanntes | Was darf gleich bleiben? Das Alte im Neuen zeigen. Bei Dauerklage: Was möchten Sie stattdessen? |
| Ärger, Irritation | Werte | Was ist Ihnen daran wichtig? Erzählen lassen, Werte hören. |
| Enttäuschung, Trauer, Resignation | Raum, Zuhören, Würdigung, Blick zurück | Ich nehme Ihre Enttäuschung aus früheren Erfahrungen wahr. Plan nennen, durch Handeln beweisen. |
| Interesse, Freude | Fokus, Zukunft | Welche Chancen sehen Sie? Erst nach dem Abholen der Störungen. |

Regeln für die Benennung:

- Als Ich-Wahrnehmung („Ich kann mir vorstellen, dass …", „Ich habe gehört, dass …"), nie als Zuschreibung („Sie haben Angst").
- Intensität treffen: „Unsicherheit" statt „Angst", „Irritation" statt „Wut", „Vorbehalte" statt „Ekel". Ein Spektrum nennen holt mehr Menschen ab.
- Beide Seiten ansprechen: die, die sich sorgen, und die, die sich freuen.
- Die Emotion benennen, nicht die Ursache in den Mund legen.
- Nach der Benennung Pause, Resonanz lesen.
- Haltung vor Methode: Wer es nicht meint, lässt es weg.

Platz in der Struktur: vor oder im Warum (Benennung und Würdigung des Bisherigen), im Wie (Raum zum Zuhören ankündigen), am Ende (Abfrage, die am Anfang angekündigt wurde: Sorgen und Chancen, was gleich bleiben darf). Wenn Wünsche nicht erfüllbar sind: paraphrasieren, Dilemma transparent machen, Warum und Wozu nennen.

## Ergebnis einer Session

Wenn die Frontier leer ist, gibt der Skill die Rahmung aus:

```
## Rahmung

**Als wer** …
**Für wen** …
**Im Raum** … (Emotion → Bedürfnis → wie ich es aufgreife)
**Warum** … weil …
**Was** … (ändert sich / bleibt)
**Wie** … (Schritte, Zeitplan, Ablauf des Gesprächs, Abfrage)
**Wozu** … damit …
**Offen** … (was, warum noch nicht, wann)
```

Danach das Angebot: Redetext in den eigenen Worten des Nutzers, nach den Sprachregeln. Nur auf Wunsch. Dateien nur auf Wunsch.

## Sprachregeln für Rahmung und Redetext

Kompakt im Skill, entnommen aus dem Skill `vermenschlichen`:

- Schlichte Verben, keine gehobenen Synonyme.
- Kein Pathos, keine Werbesprache, keine Bedeutungsaufblähung.
- Keine Gedankenstrich-Häufung.
- Kein „nicht nur, sondern auch", kein Dreierschema, keine Wiederholungsfloskeln („gemeinsam" siebenmal).
- Kein Fazit-Absatz, keine Zusammenfassung am Ende, die den Text wiederholt.
- Nichts erfinden: keine Zahlen, Termine, Zusagen, die der Nutzer nicht genannt hat.
- Fettdruck sparsam.
- Ist der Skill `vermenschlichen` installiert, gilt er zusätzlich.

## Repo

```
4mat-skill/
├── README.md                 Deutsch, kurzer englischer Abschnitt
├── LICENSE                   MIT
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   └── 4mat-me/
│       └── SKILL.md          unter 900 Wörter
└── docs/superpowers/specs/   dieses Dokument
```

Installation: `/plugin marketplace add Rubwara93/4mat-skill` und `/plugin install 4mat-skill@...`, oder `skills/4mat-me` nach `~/.claude/skills/` kopieren.

## Test

Skill-Erstellung folgt RED-GREEN-REFACTOR (Skill `writing-skills`):

1. RED: Ein Agent ohne Skill bekommt das Szenario „Bereichsleitung stellt Teams neu auf, Flurfunk seit zwei Wochen, Meeting Donnerstag" und die Bitte, das nach 4MAT zu strukturieren. Verhalten dokumentieren.
2. GREEN: Derselbe Agent mit Skill, zwei bis drei Antwortrunden mit einem gespielten Nutzer. Prüfpunkte: Runden statt Einzelfragen; Empfehlung je Frage; Als wer und Für wen vor den vier Fragen; Emotionen mit Bedürfnis eingebaut; Warum und Wozu getrennt; Offene Punkte benannt; Rahmung am Ende; kein ungefragter Redetext; keine Dateien.
3. REFACTOR: Lücken aus dem Test in den Skill ziehen, erneut testen.

## Quellen

- Resilienz-Akademie, ABC der Resilienz: 4MAT. https://www.resilienz-akademie.com/abc-der-resilienz/4mat/
- Rethinking Resilience, Folge 65: Resilient Tools 4MAT. https://www.resilienz-akademie.com/resilienz-podcast/resilienz-podcast-rethinking-resilience-folge-65/
- Ausbildung Emotionale Resilienz (Ruben Langwara), Tag 4: Emotionale Change-Kommunikation. Interne Transkripte, nicht veröffentlicht.
- Matt Pocock, grill-me / grilling. https://github.com/mattpocock/skills
- McCarthy, B. (1980). The 4MAT System. Kolb, D. (1984). Experiential Learning. Antonovsky, A. (1987). Unraveling the Mystery of Health.
