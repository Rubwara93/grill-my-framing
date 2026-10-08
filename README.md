# grill-my-framing

Ein Skill für Claude Code, der eine Botschaft nach dem 4MAT®-Modell von Bernice McCarthy sortiert, bevor sie gesprochen oder geschrieben wird. Er interviewt in Runden, wie `grill-me` von Matt Pocock, daher der Name, und hört auf, wenn sieben Felder gefüllt sind:

```
Als wer? → Für wen? → Was ist im Raum? → Warum → Was → Wie → Wozu
```

Typischer Fall: Eine Führungskraft kündigt dem Team eine Veränderung an. Der Skill fragt, aus welcher Rolle sie spricht, wer zuhört, welche Emotionen vermutlich schon im Raum sind, und sortiert dann Warum, Was, Wie und Wozu. Am Ende steht eine kompakte Rahmung im Chat. Einen Redetext gibt es nur auf Wunsch.

Der Skill schreibt keine Dateien. Mitgegebene Unterlagen (Präsentation, Organigramm, Protokoll) liest er selbst und fragt nichts ab, was dort steht.

## Installation

**Claude Code**, als Plugin:

```
/plugin marketplace add Rubwara93/grill-my-framing
/plugin install grill-my-framing@rubenlangwara
```

**Codex CLI**: den Ordner `skills/grill-my-framing` nach `~/.codex/skills/` kopieren (oder in `.codex/skills/` im Projekt). Codex liest dieselbe `SKILL.md`; die Datei `agents/openai.yaml` liefert Anzeigename und sperrt den automatischen Aufruf.

```bash
git clone https://github.com/Rubwara93/grill-my-framing.git && cp -r grill-my-framing/skills/grill-my-framing ~/.codex/skills/
```

**Jeder Agent, der das Agent-Skills-Format kennt** (Claude Code, Codex, Cursor, Gemini CLI und andere), über den skills.sh-Installer:

```bash
npx skills@latest add Rubwara93/grill-my-framing
```

Oder von Hand nach `~/.claude/skills/` kopieren:

```bash
git clone https://github.com/Rubwara93/grill-my-framing.git && cp -r grill-my-framing/skills/grill-my-framing ~/.claude/skills/
```

Der Skill startet nur auf Zuruf mit `/grill-my-framing` (in Codex: `$grill-my-framing` oder „nutze den Skill grill-my-framing“). Der Agent greift nicht von selbst danach.

**Ohne Claude Code oder Codex, einfach im Chat** (claude.ai, ChatGPT, Gemini, Copilot): Die Datei [`chat/grill-my-framing-prompt.md`](chat/grill-my-framing-prompt.md) enthält denselben Ablauf als Prompt. In claude.ai als Projektanweisung eines Projekts „grill-my-framing“ einfügen, in ChatGPT als Projekt- oder Custom-GPT-Anweisung, oder als erste Nachricht einer Unterhaltung schicken und die eigene Situation darunter schreiben. Unterlagen als Anhang mitgeben. Die Chat-Fassung wird aus der SKILL.md erzeugt (`python3 scripts/build-chat-prompt.py`), Änderungen bitte dort.

## Benutzung

In einer frischen Sitzung:

```
/grill-my-framing Ich muss meinem Team am Donnerstag die neue Teamstruktur ankündigen. Die Präsentation liegt unter ./neuaufstellung.pdf
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

Der Skill ist auf Deutsch geschrieben, weil die Unterscheidung von Warum und Wozu im Englischen keine direkte Entsprechung hat. Für Rahmung und Redetext gelten kompakte Regeln gegen typische Muster maschineller Texte. Hat die Nutzerin oder der Nutzer einen eigenen Schreibstil hinterlegt (Stil-Skill, Stilanweisung in CLAUDE.md oder AGENTS.md, Textprobe), formuliert der Skill danach. Wer zusätzlich einen Stil-Skill namens `vermenschlichen` installiert hat (Regeln nach den Wikipedia-Seiten [Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte)), bekommt ihn obendrauf angewendet.

## English summary

`grill-my-framing` is a Claude Code skill that interviews you, round by round, until a message is sorted along the 4MAT® model (Bernice McCarthy): Why, What, How and, in Sebastian Mauritz's German adaptation, Wozu (what for). Two questions come first: as whom am I speaking, and to whom. A third block covers the emotions likely present in the room and what each one needs before people can listen. The skill is written in German because the Warum/Wozu distinction ("weil" versus "damit") has no clean English equivalent. It writes no files and produces a speech draft only on request. It follows the Agent Skills format, so it runs in Claude Code, Codex CLI and other agents that read `SKILL.md`. For plain chat (claude.ai, ChatGPT), `chat/grill-my-framing-prompt.md` holds the same flow as a prompt you paste into a project or a custom GPT. If you keep a writing style of your own (a style skill, a note in CLAUDE.md or AGENTS.md, a text sample), the speech draft follows it. Install with `/plugin marketplace add Rubwara93/grill-my-framing`, `npx skills@latest add Rubwara93/grill-my-framing`, or copy `skills/grill-my-framing` into `~/.claude/skills/` or `~/.codex/skills/`.

## Markenhinweis

4MAT® ist eine Marke von About Learning, Inc. Dieses Projekt nennt das Modell nur als Quelle. Es steht in keiner Verbindung zu About Learning und ist weder von dort autorisiert noch geprüft. Bis Oktober 2026 hieß der Skill `4mat-me`, das Repo `4mat-skill`.

4MAT® is a trademark of About Learning, Inc. This project is not affiliated with, endorsed or reviewed by About Learning.

## Lizenz

MIT. Ruben Langwara, 2026.
