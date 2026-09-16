# 4mat-me

Ein Skill für Claude Code, der eine Botschaft mit dem 4MAT sortiert, bevor sie gesprochen oder geschrieben wird. Er interviewt in Runden, wie `grill-me` von Matt Pocock, und hört auf, wenn sieben Felder gefüllt sind:

```
Als wer? → Für wen? → Was ist im Raum? → Warum → Was → Wie → Wozu
```

Typischer Fall: Eine Führungskraft kündigt dem Team eine Veränderung an. Der Skill fragt, aus welcher Rolle sie spricht, wer zuhört, welche Emotionen vermutlich schon im Raum sind, und sortiert dann Warum, Was, Wie und Wozu. Am Ende steht eine kompakte Rahmung im Chat. Einen Redetext gibt es nur auf Wunsch.

Der Skill schreibt keine Dateien. Mitgegebene Unterlagen (Präsentation, Organigramm, Protokoll) liest er selbst und fragt nichts ab, was dort steht.

## Installation

Als Plugin in Claude Code:

```
/plugin marketplace add Rubwara93/4mat-skill
/plugin install 4mat-skill@rubenlangwara
```

Oder von Hand: den Ordner `skills/4mat-me` nach `~/.claude/skills/` kopieren.

```bash
git clone https://github.com/Rubwara93/4mat-skill.git && cp -r 4mat-skill/skills/4mat-me ~/.claude/skills/
```

Der Skill startet nur auf Zuruf mit `/4mat-me`. Claude greift nicht von selbst danach.

## Benutzung

In einer frischen Sitzung:

```
/4mat-me Ich muss meinem Team am Donnerstag die neue Teamstruktur ankündigen. Die Präsentation liegt unter ./neuaufstellung.pdf
```

Dann kommen Fragen in Runden, jede mit Empfehlung. „Weiß ich noch nicht“ ist eine gültige Antwort, sie landet im Feld Offen. Die Sitzung ist fertig, wenn nichts mehr stillschweigend angenommen wird.

## Das Modell

Das 4MAT stammt von Bernice McCarthy (1980) und baut auf dem Lernzyklus von David Kolb auf. Im Original heißen die vier Fragen Why, What, How und What if. Sebastian Mauritz hat das What if für den deutschen Sprachraum als Wozu gefasst und die Fragen „Als wer?“ und „Für wen?“ vorangestellt: Wer spricht aus welcher Rolle mit wem?

Die Unterscheidung von Warum und Wozu trägt das Modell. Auf Warum antwortet man mit „weil“, auf Wozu mit „damit“ oder „um zu“. Das Warum blickt zurück auf Anlass und Problem, das Wozu nach vorn auf Ziel und Nutzen. Aaron Antonovskys Kohärenzgefühl lässt sich darauf abbilden: Warum schafft Verstehbarkeit, Was und Wie schaffen Handhabbarkeit, Wozu schafft Sinnhaftigkeit.

Der Teil zu den Emotionen im Raum kommt aus der Ausbildung Emotionale Resilienz von Ruben Langwara. Leitsatz: Erleichterung kommt vor Erheiterung. Unsicherheit braucht Sicherheit, Vorbehalte brauchen die Antwort auf „Was bleibt?“, Ärger braucht Werte, Enttäuschung braucht Raum. Emotionen werden als Ich-Wahrnehmung benannt, in der Intensität, die im Raum ist, und beide Seiten kommen vor.

Mehr dazu:

- [4MAT im ABC der Resilienz](https://www.resilienz-akademie.com/abc-der-resilienz/4mat/)
- [Rethinking Resilience, Folge 65: Resilient Tools 4MAT](https://www.resilienz-akademie.com/resilienz-podcast/resilienz-podcast-rethinking-resilience-folge-65/) (Sebastian Mauritz und Ruben Langwara)
- [grill-me und grilling](https://github.com/mattpocock/skills) von Matt Pocock, deren Interview-Prinzip hier übernommen ist

## Sprache

Der Skill ist auf Deutsch geschrieben, weil die Unterscheidung von Warum und Wozu im Englischen keine direkte Entsprechung hat. Für Rahmung und Redetext gelten kompakte Regeln gegen typische Muster maschineller Texte. Wer zusätzlich einen Stil-Skill namens `vermenschlichen` installiert hat (Regeln nach den Wikipedia-Seiten [Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte)), bekommt ihn obendrauf angewendet.

## English summary

`4mat-me` is a Claude Code skill that interviews you, round by round, until a message is sorted along the 4MAT (Bernice McCarthy): Why, What, How and, in Sebastian Mauritz's German adaptation, Wozu (what for). Two questions come first: as whom am I speaking, and to whom. A third block covers the emotions likely present in the room and what each one needs before people can listen. The skill is written in German because the Warum/Wozu distinction ("weil" versus "damit") has no clean English equivalent. It writes no files and produces a speech draft only on request. Install with `/plugin marketplace add Rubwara93/4mat-skill` or copy `skills/4mat-me` into `~/.claude/skills/`.

## Lizenz

MIT. Ruben Langwara, 2026.
