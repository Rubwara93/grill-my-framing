#!/usr/bin/env python3
"""Erzeugt chat/4mat-me-prompt.md aus skills/4mat-me/SKILL.md.

Die Chat-Fassung ist für claude.ai, ChatGPT und andere Chat-Oberflächen gedacht:
kein Dateizugriff, keine Slash-Befehle, keine installierten Skills.
Aufruf: python3 scripts/build-chat-prompt.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / "skills" / "4mat-me" / "SKILL.md"
dst = root / "chat" / "4mat-me-prompt.md"

text = src.read_text(encoding="utf-8")
# Frontmatter entfernen
body = text.split("---", 2)[2].lstrip()

replacements = [
    (
        "# 4MAT-me\n\nInterviewe die Person so lange",
        "Du bist mein Sparringspartner für eine Botschaft, die ich vorbereiten muss. "
        "Interviewe mich so lange",
    ),
    (
        "Fakten finden ist deine Aufgabe. Was in mitgegebenen Unterlagen steht (Präsentation, Organigramm, Protokoll, Mail-Entwurf), liest du und fragst es nicht ab.",
        "Fakten finden ist deine Aufgabe. Was in Unterlagen steht, die ich anhänge oder einfüge (Präsentation, Organigramm, Protokoll, Mail-Entwurf), liest du und fragst es nicht ab.",
    ),
    (
        "Bevor du den Redetext anbietest, prüfe, ob die Person einen eigenen Schreibstil hinterlegt hat: ein Stil-Skill, eine Stilanweisung in CLAUDE.md oder AGENTS.md, eine Textprobe. Findest du etwas, nenne es im Angebot und formuliere danach. Findest du nichts, frag einmal. Der eigene Stil hat Vorrang. Ist der Skill `vermenschlichen` installiert, gilt er zusätzlich.",
        "Bevor du den Redetext anbietest, prüfe, ob ich dir eine Stilanweisung oder eine Textprobe gegeben habe: in den Projektanweisungen, in dieser Unterhaltung oder als Anhang. Findest du etwas, nenne es im Angebot und formuliere danach. Findest du nichts, frag einmal. Mein eigener Stil hat Vorrang.",
    ),
    (
        "Danach ein Satz: Ob du daraus einen Redetext in ihren eigenen Worten machen sollst. Nur auf Wunsch. Dateien schreibst du nur, wenn jemand darum bittet.",
        "Danach ein Satz: Ob du daraus einen Redetext in meinen eigenen Worten machen sollst. Nur auf Wunsch.",
    ),
]
for old, new in replacements:
    assert old in body, f"Nicht gefunden: {old[:60]}"
    body = body.replace(old, new)

# Anrede im Chat: „die Person" ist der Nutzer selbst
body = body.replace("bis ihre Botschaft sortiert ist. Der Inhalt kommt aus ihren Antworten", "bis meine Botschaft sortiert ist. Der Inhalt kommt aus meinen Antworten")
body = body.replace("Fragt die Person selbst zuerst nach dem Wozu", "Frage ich selbst zuerst nach dem Wozu")
body = body.replace("Entscheidungen sind Sache der Person.", "Entscheidungen sind meine Sache.")
body = body.replace("die die Person nicht genannt hat", "die ich nicht genannt habe")
body = body.replace("Frag in Runde 1, was die Person aus Flurfunk", "Frag in Runde 1, was ich aus Flurfunk")

header = """# 4MAT-me als Chat-Prompt

Diese Fassung ist für Chat-Oberflächen ohne Skill-System: claude.ai, ChatGPT, Gemini, Copilot. Sie wird aus `skills/4mat-me/SKILL.md` erzeugt, bitte dort ändern und `python3 scripts/build-chat-prompt.py` ausführen.

**So verwendest du sie**

- claude.ai: Ein Projekt „4MAT-me" anlegen und den Text unten als Projektanweisung einfügen. Jede neue Unterhaltung im Projekt startet damit. Alternativ den Text als erste Nachricht einer Unterhaltung schicken und die eigene Situation direkt darunter schreiben.
- ChatGPT: Als Anweisung in einem Projekt oder als Custom GPT anlegen, oder als erste Nachricht einfügen.
- Unterlagen (Präsentation, Organigramm, Mail-Entwurf) als Anhang mitgeben oder einfügen. Eine Textprobe des eigenen Stils dazu, wenn der Redetext danach klingen soll.

Alles unterhalb der Linie ist der Prompt.

---

"""
dst.write_text(header + body, encoding="utf-8")
print(f"geschrieben: {dst.relative_to(root)} ({len(body.split())} Wörter Prompt)")
