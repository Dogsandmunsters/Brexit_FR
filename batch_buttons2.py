#!/usr/bin/env python3
"""Step 2: Replace more button texts across all sections."""
import json
import re

with open('_sections.json', 'r') as f:
    sections = json.load(f)

BUTTON_TRANSLATIONS = {
    "'Let me ask you something else.'": "« Laissez-moi vous poser une autre question. »",
    "Get a briefing on the issues you're facing": "Se faire briefer sur les dossiers en cours",
    "The so-called Norway model: a very close relationship within the European Economic Area, giving comprehensive access to trade in goods and services": "Le modèle dit norvégien : une relation très étroite au sein de l'Espace économique européen, offrant un large accès au commerce des biens et services",
    "The Swiss model: an arrangement outside the EEA with only partial access to trade in goods and services, but with more opt-outs and no contributions to the EU budget": "Le modèle suisse : un arrangement hors de l'EEE avec un accès seulement partiel au commerce des biens et services, mais avec plus de dérogations et sans contribution au budget de l'UE",
    "'Of course, I shall be leading the fight to Remain.'": "« Bien sûr, je mènerai le combat pour le Remain. »",
    "'Good lord, no. I'm sitting this one out.'": "« Grand Dieu, non. Je reste en dehors de cette affaire. »",
    "'I intend to give my support to the Leave campaign.'": "« J'ai l'intention de soutenir la campagne du Leave. »",
    "'You mentioned non-tariff barriers.'": "« Vous avez mentionné les barrières non tarifaires. »",
    "'Those are details we can look at another time.'": "« Ce sont des détails que nous pourrons examiner une autre fois. »",
    "'What are the pros and cons?'": "« Quels sont les avantages et les inconvénients ? »",
    "'We can be a team player. But not all members of a team are identical. The EU needs to recognize that Britain has unique skills to bring onto the field. Our military expertise, our financial sector skills, our international diplomatic reach. So this last two years will hopefully have taught both sides something.'": "« Nous pouvons jouer collectif. Mais tous les membres d'une équipe ne sont pas identiques. L'UE doit reconnaître que la Grande-Bretagne a des compétences uniques à apporter. Notre expertise militaire, nos compétences financières, notre rayonnement diplomatique international. Alors ces deux dernières années auront, espérons-le, appris quelque chose aux deux camps. »",
    "'If your child makes a noise in class and pulls another child's pigtails, is that any reason to give up on them? I think the country has learned its lesson from the sharp shock of Brexit. We'll be better behaved in future.'": "« Si votre enfant fait du bruit en classe et tire les couettes d'un camarade, est-ce une raison pour l'abandonner ? Je pense que le pays a retenu la leçon après le choc du Brexit. Nous serons plus sages à l'avenir. »",
    "Geriatric unit": "Service de gériatrie",
    "Miracle cure facility": "Service des remèdes miracles",
    "The Innovative Medicines Initiative": "L'Initiative pour les Médicaments Innovants",
    "Casualty": "Urgences",
    "'No comment.'": "« Pas de commentaire. »",
    "'Let's pick this up later.'": "« Reprenons cela plus tard. »",
    "EFTA": "L'AELE",
    "To consider the status of EU citizens already living here": "Examiner le statut des citoyens européens déjà installés ici",
    "'What can we learn from similar agreements the EU has done in the past?'": "« Que pouvons-nous apprendre d'accords similaires conclus par l'UE par le passé ? »",
    "'All right. Anything else?'": "« D'accord. Autre chose ? »",
    "Ask him what kinds of mission EU forces undertake": "Lui demander quels types de missions les forces de l'UE mènent",
    "Deal with EU Trade Talks": "Gérer les négociations commerciales avec l'UE",
    "'Tell me about funding for ongoing projects.'": "« Parlez-moi du financement des projets en cours. »",
    "'Pensions sound like a problem that won't go away soon.'": "« Les retraites semblent être un problème qui ne disparaîtra pas de sitôt. »",
    "Play on": "Continuons",
    "'Can an EU national apply for UK residency?'": "« Un citoyen européen peut-il demander la résidence au Royaume-Uni ? »",
    "Reopen those discussions": "Rouvrir ces discussions",
    "See what happens": "Voir ce qui se passe",
    "Free movement": "Libre circulation",
    "Point out that some sort of customs union hasn't been ruled out": "Faire remarquer qu'une forme d'union douanière n'a pas été écartée",
    "Tell her that privately you're hoping to reverse Brexit and stay part of the EU": "Lui confier qu'en privé, vous espérez renverser le Brexit et rester dans l'UE",
    "You're on a roll": "Vous êtes lancé",
    "'What's wrong with referendums anyway?'": "« Quel est le problème avec les référendums, au juste ? »",
    "Plug on": "On continue",
    "'What will happen to EU citizens in Britain if we leave without a deal regarding their status?'": "« Qu'adviendra-t-il des citoyens européens en Grande-Bretagne si nous partons sans accord sur leur statut ? »",
    "'What do you suggest is the best way to grant residency rights to EU citizens, should we want to?'": "« Quelle est selon vous la meilleure façon d'accorder les droits de résidence aux citoyens européens, si nous le souhaitons ? »",
    "'That's all for now, thanks.'": "« Ce sera tout pour le moment, merci. »",
    "'Do immigrants steal jobs?'": "« Les immigrés volent-ils les emplois ? »",
    "'Does immigration lower wages?'": "« L'immigration fait-elle baisser les salaires ? »",
    "'What are the actual EU rules on immigration?'": "« Quelles sont les véritables règles de l'UE en matière d'immigration ? »",
    "'Why do they have to come here?'": "« Pourquoi doivent-ils venir ici ? »",
    "'Isn't it time we had a points system?'": "« N'est-il pas temps d'adopter un système à points ? »",
    "'Why is immigration out of control?'": "« Pourquoi l'immigration est-elle hors de contrôle ? »",
    "Agree": "Accepter",
    "Refuse": "Refuser",
    "'Every market has to have laws. When a trader wheels his barrow into the town square, who says what he can sell, how much for, and whether his weights and measures are true? Who says his onions are safe to eat?'": "« Tout marché doit avoir des lois. Quand un commerçant pousse sa charrette sur la place du village, qui décide de ce qu'il peut vendre, à quel prix, et si ses poids et mesures sont justes ? Qui garantit que ses oignons sont bons à manger ? »",
    "'What about financial services?'": "« Et les services financiers ? »",
    "The moment of truth": "Le moment de vérité",
    "'We'd better go over the threats.'": "« Nous ferions mieux de passer en revue les menaces. »",
    "Chin up": "Haut les cœurs",
    "Easy-peasy": "Les doigts dans le nez",
    "Keep going": "On continue",
    "Keep your nerve": "Gardez votre sang-froid",
    "What now?": "Et maintenant ?",
    "'We won't drill down into details just now.'": "« N'entrons pas dans les détails pour l'instant. »",
    "Unilaterally guarantee EU citizens' right to remain in Britain": "Garantir unilatéralement le droit des citoyens européens de rester en Grande-Bretagne",
    "Announce that EU citizens in the UK will be told to leave after Brexit": "Annoncer que les citoyens européens au Royaume-Uni devront partir après le Brexit",
    "Ignore it and see what the EU Commission decides to do": "Ignorer la question et voir ce que la Commission européenne décide",
    "No looking back": "Plus de retour en arrière",
    "Make a wish": "Faites un vœu",
    "Slog on": "On s'accroche",
    "Ask the Chancellor to stay behind for a chat": "Demander au chancelier de l'Échiquier de rester pour discuter",
    "Wake up before it's too late!": "Réveillez-vous avant qu'il ne soit trop tard !",
    # Additional common ones
    "Crack the whip": "Serrer la vis",
    "A customs union, like Turkey has with the EU": "Une union douanière, comme celle de la Turquie avec l'UE",
    "Try for a slightly more distant Swiss-style model": "Tenter un modèle un peu plus distant, à la suisse",
    "Suggest a EEA-like relationship such as Norway has": "Proposer une relation de type EEE, comme celle de la Norvège",
    "Briefings are a distraction. It's time to do something!": "Les briefings sont une distraction. Il est temps d'agir !",
    "Agree to his suggestion": "Accepter sa suggestion",
    "Pursue a customs union like Turkey's arrangement": "Poursuivre une union douanière à la turque",
    "Aim for a bespoke free trade agreement": "Viser un accord de libre-échange sur mesure",
    "Go for it": "Foncez",
    "Turn him down": "Refuser sa proposition",
    "See where this goes": "Voir où cela mène",
    "Turn it off and get some  sleep": "Éteindre et aller dormir",
    "Let's find out what the nation thinks": "Voyons ce que pense la nation",
    "Grab a brolly": "Prenez votre parapluie",
    "Seeing as you're here anyway, why not?": "Tant que vous êtes là, pourquoi pas ?",
}

def translate_button_in_line(line, translations):
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

print(f"Replaced {count} more button texts")
