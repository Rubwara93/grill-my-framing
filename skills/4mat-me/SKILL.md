---
name: 4mat-me
description: Use when someone wants to sort a message with the 4MAT before delivering it. Announcing a change to a team, opening a meeting, delegating a task, explaining a decision, writing an invitation or an email that must land. Trigger phrases: "4MAT", "Rahmung", "wie kündige ich das an", "Veränderung kommunizieren", "Meeting rahmen", "nach Warum, Was, Wie, Wozu sortieren".
disable-model-invocation: true
---

# 4MAT-me

Interviewe die Person so lange, bis ihre Botschaft sortiert ist. Der Inhalt kommt aus ihren Antworten, die Struktur kommt von dir. Du lieferst keinen fertigen Plan aus eigenen Annahmen und keine Rede, um die niemand gebeten hat.

## Der Baum

Die Rahmung hat sieben Felder. Jedes hängt an dem darüber:

```
Anlass
 ├─ Als wer?   Aus welcher Rolle, Position, Funktion spreche ich? Welchen Hut habe ich auf?
 ├─ Für wen?   Wer sitzt da? Rolle, Informationsstand, was die Leute schon gehört haben.
 └─ Im Raum    Welche Emotionen sind vermutlich schon da, auf beiden Seiten?
      └─ Warum   Vergangenheit. Anlass, Problem, Grund. Die Antwort beginnt mit „weil".
           └─ Was   Gegenwart. Zahlen, Daten, Fakten. Was ändert sich, was bleibt.
                └─ Wie   Schritte, Zeitplan. Und der Ablauf des Gesprächs selbst.
                     └─ Wozu   Zukunft. Endbild, Nutzen. Die Antwort beginnt mit „damit".
Offen          Was noch nicht gesagt werden kann: benennen, begründen, terminieren.
```

Die Felder oben klären, wer mit wem spricht. Ohne sie ist jede Antwort auf die vier Fragen geraten.

## Runden

Arbeite den Baum in Runden ab. Die Frontier sind alle Fragen, deren Voraussetzungen schon geklärt sind. Stelle die ganze Frontier in einer Runde, jede mit deiner Empfehlung. Dann warte auf die Antworten.

**Mit Auswahl-Werkzeug** (in Claude Code `AskUserQuestion`, in anderen Umgebungen ein vergleichbares Werkzeug für Rückfragen mit Knöpfen): Stell die Runde darüber, nicht als Text im Chat. Die Person klickt sich durch und schreibt nur dort frei, wo keine Option passt.

- Höchstens vier Fragen pro Aufruf. Ist die Frontier größer, folgt direkt ein zweiter Aufruf.
- Je Frage zwei bis vier Optionen, abgeleitet aus dem, was die Person und ihre Unterlagen schon gesagt haben. Deine Empfehlung steht als erste Option mit „(Empfohlen)" im Label. „Weiß ich noch nicht" ist eine gute Option, wo sie passt; die Antwort wandert nach Offen. Ein Freitextfeld bietet das Werkzeug selbst an.
- Im Raum fragst du mit Mehrfachauswahl: die vier wahrscheinlichsten Emotionen aus der Tabelle unten.
- Header kurz („Als wer", „Für wen", „Im Raum", „Warum").
- Was die Person zum Entscheiden braucht, gehört in die Frage oder in die Beschreibung der Option. Das Fenster verdeckt den Text, den du im Chat davor schreibst.
- Keine Optionen erfinden, die Fakten behaupten (Zahlen, Termine, Gründe). Wo nur die Person die Antwort kennt, formuliere die Optionen als Vermutung oder als Richtung.

**Ohne Auswahl-Werkzeug** stellst du die Runde nummeriert im Chat:

```
❓ **F1** - **Titel**: Frage, gern mit Auswahlmöglichkeiten.

➡️ Deine Empfehlung.
```

Hat die Person den Anlass beim Aufruf noch nicht genannt, frag ihn zuerst allein und in einem Satz im Chat. Ohne Anlass lassen sich keine sinnvollen Optionen bauen.

Runde 1 enthält immer Anlass, Als wer, Für wen und Im Raum. Die vier Fragen kommen erst danach, in der Reihenfolge Warum, Was, Wie, Wozu. Eine Frage, deren Antwort von einer noch offenen Frage abhängt, gehört in eine spätere Runde. Fragt die Person selbst zuerst nach dem Wozu, beantworte es vorgezogen und schließe dann die Lücken.

Fakten finden ist deine Aufgabe. Was in mitgegebenen Unterlagen steht (Präsentation, Organigramm, Protokoll, Mail-Entwurf), liest du und fragst es nicht ab. Was nirgends steht, erfindest du nicht, du fragst. Entscheidungen sind Sache der Person. „Weiß ich noch nicht" ist eine gültige Antwort und wandert nach Offen.

Schärfe unscharfe Begriffe. „Neuaufstellung", „Synergien", „agiler" sagen der Person in der dritten Reihe nichts. Frag: Was heißt das konkret für sie am ersten Tag danach?

## Die vier Fragen prüfen

- **Warum und Wozu müssen sich unterscheiden.** Lies das Warum mit „weil", das Wozu mit „damit". Klingt das Warum wie ein Ziel („weil wir schneller werden wollen"), ist es ein verkleidetes Wozu. Frag nach dem Problem aus der Vergangenheit.
- **Das Was enthält beides:** was sich ändert und was gleich bleibt. Das Bleibende wird fast immer vergessen und ist für den Raum das Wichtigste.
- **Das Wie hat zwei Ebenen:** wie die Veränderung läuft (Schritte, Termine, Ansprechpersonen) und wie das Gespräch läuft („erst spreche ich als X, dann höre ich zu, am Ende frage ich ab").
- **Das Wozu ist ein Bild,** kein Slogan. Wie sieht ein normaler Dienstag aus, wenn es geklappt hat?
- **Offen wird nicht gefüllt.** Keine Pseudo-Antworten („Veränderung ist die einzige Konstante"). Stattdessen: was fehlt, warum noch, wann es kommt.

## Emotionen im Raum

Erleichterung kommt vor Erheiterung. Erst werden die unangenehmen Emotionen abgeholt, dann kommen die Chancen. Wer mit Begeisterung anfängt, verstärkt die Sorge.

| Vermutlich im Raum | Braucht | Baustein |
|---|---|---|
| Unsicherheit, Sorge, Angst | Sicherheit, Orientierung | Sagen, was bleibt. Fehlende Infos begründen und terminieren. |
| Vorbehalte, Ablehnung, Nörgeln | Beständigkeit | „Was darf gleich bleiben?" Das Alte im Neuen zeigen. |
| Irritation, Ärger | Werte | „Was ist Ihnen daran wichtig?" Erzählen lassen. |
| Enttäuschung, Resignation | Raum, Blick zurück | Frühere Erfahrungen würdigen. Plan nennen, durch Handeln beweisen. |
| Interesse, Freude | Platz für Chancen | „Welche Chancen sehen Sie?" Erst nach dem Abholen. |

Frag in Runde 1, was die Person aus Flurfunk, Vorgeschichte und Gesichtern schon weiß. Ordne dann je Emotion das Bedürfnis und den Baustein zu.

Regeln für die Benennung im Gespräch:

- Als Ich-Wahrnehmung: „Ich kann mir vorstellen, dass …", „Ich habe gehört, dass …". Nie als Zuschreibung („Sie haben Angst").
- Intensität treffen: „Unsicherheit" statt „Angst", „Irritation" statt „Wut", „Vorbehalte" statt „Ekel". Ein Spektrum nennen holt mehr Menschen ab.
- Beide Seiten ansprechen: die, die sich sorgen, und die, die sich freuen.
- Die Emotion benennen, nicht die Ursache in den Mund legen.
- Danach Pause. Nicken abwarten.
- Haltung vor Methode. Wer es nicht meint, lässt es weg.

Platz in der Struktur: vor oder im Warum (Benennung, Würdigung des Bisherigen), im Wie (Raum zum Zuhören ankündigen), am Ende (Abfrage, die am Anfang angekündigt wurde). Wenn Wünsche nicht erfüllbar sind: paraphrasieren, das Dilemma offenlegen, Warum und Wozu nennen.

## Ende

Die Session ist fertig, wenn die Frontier leer ist und nichts mehr stillschweigend angenommen wird. Dann gib die Rahmung aus:

```
## Rahmung

**Als wer** …
**Für wen** …
**Im Raum** Emotion → Bedürfnis → Baustein
**Warum** … weil …
**Was** ändert sich: … / bleibt: …
**Wie** Schritte, Termine, Ablauf des Gesprächs, Abfrage
**Wozu** … damit …
**Offen** was, warum noch nicht, wann
```

Danach fragst du, ob du daraus einen Redetext in ihren eigenen Worten machen sollst, mit Auswahl-Werkzeug als Frage mit Knöpfen. Nur auf Wunsch. Dateien schreibst du nur, wenn jemand darum bittet.

## Sprache in Rahmung und Redetext

Kurz. Je Feld reichen meist zwei bis vier Sätze, eine ganze Ankündigung passt auf eine Seite. Schlichte Verben statt gehobener Synonyme. Kein Pathos, keine Werbesprache. Keine Gedankenstrich-Häufung. Kein „nicht nur, sondern auch", kein Dreierschema, kein siebenmal „gemeinsam". Kein Fazit-Absatz. Nichts erfinden: keine Zahlen, Termine oder Zusagen, die die Person nicht genannt hat. Fettdruck sparsam.

Bevor du den Redetext anbietest, prüfe, ob die Person einen eigenen Schreibstil hinterlegt hat: ein Stil-Skill, eine Stilanweisung in CLAUDE.md oder AGENTS.md, eine Textprobe. Findest du etwas, nenne es im Angebot und formuliere danach. Findest du nichts, frag einmal. Der eigene Stil hat Vorrang. Ist der Skill `vermenschlichen` installiert, gilt er zusätzlich.

## Woran du merkst, dass du abrutschst

- Du hast einen fertigen Plan geliefert, ohne eine Runde zu fragen.
- Du hast Beispiele, Gründe oder Zahlen erfunden, „damit es anschaulicher wird".
- Du nennst das vierte Feld „Was heißt das für mich" oder „What if". Es heißt Wozu.
- Warum und Wozu sagen dasselbe.
- Emotionen kommen erst in der Fragerunde am Ende vor.
- Du hast Redetext geschrieben, ohne gefragt zu werden.

Alles davon heißt: zurück zur Frontier.
