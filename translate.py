#!/usr/bin/env python3
"""
Translation script for CAN YOU BREXIT gamebook.
Reads _sections.json (English), applies translations, writes translated index.html.
"""
import json
import re
import sys

def load_sections():
    with open('_sections.json', 'r') as f:
        return json.load(f)

def load_translations(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def translate_mechanical_line(line, button_text_map):
    """Translate the quoted button text in a mechanical line (OPTION/GOTO/TOSS/COUNT_GOTO).
    Preserves [OPTION], [IF...], [EFFECT...], ►destination etc."""
    # Find the quoted text
    match = re.search(r'"([^"]*)"', line)
    if match:
        original = match.group(1)
        if original in button_text_map:
            translated = button_text_map[original]
            line = line[:match.start(1)] + translated + line[match.end(1):]
    return line

def apply_translations(sections, translations):
    """Apply translations to sections."""
    for sec_num, trans in translations.items():
        if sec_num not in sections:
            print(f"Warning: section {sec_num} not found in original", file=sys.stderr)
            continue

        section = sections[sec_num]

        # Replace PROSE
        if 'PROSE' in trans:
            section['PROSE'] = trans['PROSE']

        # Replace REPORT
        if 'REPORT' in trans:
            section['REPORT'] = trans['REPORT']

        # Translate OPTIONS button text
        if 'OPTIONS' in trans:
            if isinstance(trans['OPTIONS'], list):
                # Full replacement
                section['OPTIONS'] = trans['OPTIONS']
            elif isinstance(trans['OPTIONS'], dict):
                # Button text mapping
                if 'OPTIONS' in section:
                    section['OPTIONS'] = [
                        translate_mechanical_line(line, trans['OPTIONS'])
                        for line in section['OPTIONS']
                    ]

        # Translate GOTO button text
        if 'GOTO' in trans:
            if isinstance(trans['GOTO'], list):
                section['GOTO'] = trans['GOTO']
            elif isinstance(trans['GOTO'], dict):
                if 'GOTO' in section:
                    section['GOTO'] = [
                        translate_mechanical_line(line, trans['GOTO'])
                        for line in section['GOTO']
                    ]

        # Translate TOSS_ONE button text
        if 'TOSS_ONE' in trans:
            if isinstance(trans['TOSS_ONE'], list):
                section['TOSS_ONE'] = trans['TOSS_ONE']
            elif isinstance(trans['TOSS_ONE'], dict):
                if 'TOSS_ONE' in section:
                    section['TOSS_ONE'] = [
                        translate_mechanical_line(line, trans['TOSS_ONE'])
                        for line in section['TOSS_ONE']
                    ]

        # Translate TOSS_TWO button text
        if 'TOSS_TWO' in trans:
            if isinstance(trans['TOSS_TWO'], list):
                section['TOSS_TWO'] = trans['TOSS_TWO']
            elif isinstance(trans['TOSS_TWO'], dict):
                if 'TOSS_TWO' in section:
                    section['TOSS_TWO'] = [
                        translate_mechanical_line(line, trans['TOSS_TWO'])
                        for line in section['TOSS_TWO']
                    ]

        # Translate COUNT_GOTO
        if 'COUNT_GOTO' in trans:
            if isinstance(trans['COUNT_GOTO'], list):
                section['COUNT_GOTO'] = trans['COUNT_GOTO']
            elif isinstance(trans['COUNT_GOTO'], dict):
                if 'COUNT_GOTO' in section:
                    section['COUNT_GOTO'] = [
                        translate_mechanical_line(line, trans['COUNT_GOTO'])
                        for line in section['COUNT_GOTO']
                    ]

    return sections

def write_output(sections):
    """Write the translated sections back into index.html."""
    with open('_header.html', 'r') as f:
        header = f.read()
    with open('_footer.html', 'r') as f:
        footer = f.read()

    # Format sections as JavaScript object
    sections_js = json.dumps(sections, ensure_ascii=False, indent=2)

    with open('index.html', 'w') as f:
        f.write(header)
        f.write(sections_js)
        f.write(';\n')
        f.write(footer)

    print(f"Written translated index.html with {len(sections)} sections")

def main():
    sections = load_sections()

    # Load and apply all translation files
    import glob
    trans_files = sorted(glob.glob('translations_*.json'))

    if not trans_files:
        print("No translation files found (translations_*.json)")
        sys.exit(1)

    for tf in trans_files:
        print(f"Loading {tf}...")
        translations = load_translations(tf)
        sections = apply_translations(sections, translations)

    # Count translated vs untranslated
    # (A simple heuristic: check if any PROSE line starts with common French patterns)
    translated = 0
    untranslated = 0
    for key, section in sections.items():
        if 'PROSE' in section and section['PROSE']:
            first_line = section['PROSE'][0]
            # Check for French characters/patterns
            if any(c in first_line for c in 'àâéèêëïîôùûüçÀÉÈÊ«»'):
                translated += 1
            else:
                untranslated += 1

    print(f"Sections with French text: {translated}")
    print(f"Sections potentially untranslated: {untranslated}")

    write_output(sections)

if __name__ == '__main__':
    main()
