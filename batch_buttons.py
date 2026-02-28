#!/usr/bin/env python3
"""
Step 1: Replace common button texts across all sections.
This handles the most frequent option/goto/toss button texts.
"""
import json
import re

with open('_sections.json', 'r') as f:
    sections = json.load(f)

# Common button text translations (English -> French)
BUTTON_TRANSLATIONS = {
    "Continue": "Continuer",
    "Carry on": "Poursuivre",
    "Onwards": "En avant",
    "Let's find out": "Voyons voir",
    "Press on": "Continuons",
    "What's next?": "Et ensuite ?",
    "Forward": "En avant",
    "Find another question": "Chercher une autre question",
    "Time will tell": "L'avenir le dira",
    "Give up and get a good night's sleep": "Abandonner et aller dormir",
    "We'll see": "On verra bien",
    "Skip to another question": "Passer à une autre question",
    "So far so good": "Jusqu'ici tout va bien",
    "You've had enough, and it's time for bed": "Vous en avez assez, il est l'heure de dormir",
    "Keep up the good work": "Continuez sur cette lancée",
    "You'll show them": "Vous allez leur montrer",
    "On with the job": "Au travail",
    "Spin the wheel": "Tourner la roue",
    "Ponder your next move": "Réfléchir à la suite",
    "Drink up": "Buvez",
    "Plug on regardless": "On continue coûte que coûte",
    "Let's see": "Voyons voir",
    "Next": "Suivant",
    "Watch a little more": "Regarder encore un peu",
    "Talk about something else": "Parler d'autre chose",
    "Enough talk. Actions speak louder than words": "Assez parlé. Les actes valent mieux que les mots",
    "Now then…": "Alors…",
    "That's a headache for another day": "Ce sera un casse-tête pour un autre jour",
    "Flavour of the month": "En pleine grâce",
    "Out of favour": "En disgrâce",
    "Let's find out what the voters want": "Voyons ce que veulent les électeurs",
    "Get your score": "Obtenir votre score",
    "Face the inevitable": "Affronter l'inévitable",
}

def translate_button_in_line(line, translations):
    """Replace quoted button text in a mechanical line."""
    m = re.search(r'"([^"]*)"', line)
    if m:
        original = m.group(1)
        if original in translations:
            return line[:m.start(1)] + translations[original] + line[m.end(1):]
    return line

count = 0
for key, sec in sections.items():
    for field in ['OPTIONS', 'GOTO', 'TOSS_ONE', 'TOSS_TWO', 'COUNT_GOTO']:
        if field in sec:
            new_lines = []
            for line in sec[field]:
                new_line = translate_button_in_line(line, BUTTON_TRANSLATIONS)
                if new_line != line:
                    count += 1
                new_lines.append(new_line)
            sec[field] = new_lines

with open('_sections.json', 'w') as f:
    json.dump(sections, f, ensure_ascii=False, indent=2)

print(f"Replaced {count} common button texts")
