#!/usr/bin/env python3
"""Translate batch 8 sections from English to French."""
import json

with open('/home/user/Brexit_FR/_sections.json', 'r') as f:
    data = json.load(f)

translations = {}

# Section 760 - already translated, skip

# Section 762
translations["762"] = {
    "PROSE": [
        "Celle qui pose la question est une femme d'âge moyen dont la peau a la couleur d'un poulet de supermarché. « J'ai vu l'affiche, dit-elle. Toutes ces hordes de réfugiés. C'est pour ça que j'ai voté pour qu'on quitte le Brexit. »",
        "Lucy Tooth éclate littéralement de rire, stupéfaite. Voilà qui va lui coûter des voix. Les gens bêtes sont susceptibles face à la moquerie, et leur rancune est spectaculaire.",
        "« Cette affiche était retouchée sur Photoshop, lâche Bob Owlbear en lançant un regard noir à Colin Fungale. Franchement, je suis surpris que les nazis n'aient pas intenté un procès pour violation de droits d'auteur. »",
        "Inutile. La plupart des électeurs du Brexit vivent encore au siècle dernier ; ils pensent que Photoshop est l'endroit où l'on va faire développer ses photos de vacances. Pas étonnant que le sourire de Fungale ne fasse que s'élargir.",
        "« Aviez-vous une question ? » demande Martin Mugglemore à la femme dans le public.",
        "Elle a l'air perdue, mais cherche quelque chose à demander. « Ce que je veux savoir, c'est si on peut arrêter les clandestins maintenant ? C'est pas juste ceux de l'UE. Y'a des Pakis qui se sont installés dans ma rue – »",
        "« Une question ! » glapit Mugglemore.",
        "« D'accord. Est-ce que vous allez arrêter de distribuer des allocations aux étrangers et faire en sorte que l'argent aille aux Britanniques désormais ? C'est pour le conservateur, M. Tode. »",
        "Vous voyez le dilemme de Tode. Il aimerait bien marquer des points démagogiques auprès de la foule, mais un simple principe de décence prend le dessus.",
        "« Je ne suis pas sûr que vous parliez vraiment de l'UE… Vous voulez dire les réfugiés de pays comme la Syrie et la Libye ? »",
        "Vous aviez bien raison de reléguer Tode dans le désert politique. Peter Strewel aurait saisi la balle au bond et couru avec aussi vite que ses grosses jambes le lui auraient permis. Et aucun murmure de conscience ne l'aurait fait hésiter."
    ],
    "OPTIONS": [
        '[OPTION] "Voir s\'il peut rattraper le coup" ►41',
        '[OPTION] "Passer à une autre question" ►405'
    ]
}

# Section 763
translations["763"] = {
    "PROSE": [
        "L'endurance, plus que tout le reste, est ce qu'il vous faut pour ce poste. Et vous en avez à revendre."
    ],
    "OPTIONS": [
        '[OPTION] "Qui a besoin de dormir, de toute façon ?" ►450'
    ]
}

# Section 764
translations["764"] = {
    "PROSE": [
        "Le négociateur en chef de l'UE et son équipe prennent contact avec vous. Il a discuté de vos propositions avec les autres États membres de l'UE et peut désormais vous communiquer leur réponse."
    ],
    "GOTO": [
        '[IF Goodwill>=50] "Vous êtes tout ouïe" ►749',
        '[ELSE] "Très bien, alors" ►427'
    ]
}

# Section 765
translations["765"] = {
    "PROSE": [
        "Vous n'avez pas eu le temps de vous occuper de cela, parmi toutes les autres questions exigeant votre attention personnelle. Vous ne pouvez qu'espérer que vos ministres n'en ont pas fait un gâchis.",
        "Ils reviennent avec la nouvelle que la Grande-Bretagne conservera un rôle d'associé aux côtés des forces armées européennes, et qu'en matière policière elle continuera de coopérer avec Europol tout en se désengageant des accords de partage de données et d'extradition."
    ],
    "REPORT": [
        "<strong>-5 % Bienveillance</strong> : l'UE est contrariée par l'augmentation du niveau de menace causée par le désengagement de la Grande-Bretagne de la pleine participation aux initiatives de lutte contre le terrorisme et de maintien de la paix militaire.",
        "<strong>-5 % Popularité</strong> : les électeurs prennent conscience de la façon dont le Brexit affaiblit la sécurité du pays, et ils vous en tiennent responsable.",
        "Les dispositions en matière de Sécurité et Défense sont désormais fixées."
    ],
    "OPTIONS": [
        '[OPTION] "Si peu de temps…" ►332'
    ]
}

# Section 766
translations["766"] = {
    "PROSE": [
        "Les premiers sondages donnent le Leave en tête de justesse. Mais les sondages sont un baromètre notoirement peu fiable de l'opinion publique ces temps-ci. Un facteur plus révélateur est de savoir si les jeunes prendront la peine de voter. Le dernier référendum ayant, à leurs yeux, posé une bombe sous leur avenir, cette fois-ci ils pourraient se déplacer en plus grand nombre.",
        "« Cela renvoie à la question plus profonde de l'apathie du public, dit votre attachée de presse Terri Trough. Les gens font l'effort de voter quand ils sont remontés. Et ça arrive quand ils voient leurs salaires se faire rogner. C'est pour ça que le vote des jeunes ne compte pas. Ils n'ont ni maison ni frais de scolarité à payer. »",
        "« Je sais. \"C'est l'économie, imbécile.\" »",
        "Elle vous regarde avec sérieux. « Je ne me permettrais jamais de vous traiter d'imbécile, Premier ministre. »"
    ]
}

# Section 767
translations["767"] = {
    "PROSE": [
        "« Nous paierions moins qu'eux, assurément. »",
        "« Hmm. Cela pourrait provoquer du ressentiment parmi les autres membres de l'EEE. »",
        "Stollard secoue la tête. « Plutôt de la pitié. La Grande-Bretagne est plus pauvre que la Norvège en termes de PIB par habitant, nous pouvons donc démontrer de bonnes raisons pour une contribution réduite. De plus, nous récupérerions encore une bonne partie du rabais, car il y a davantage d'opportunités d'investissement rentable par l'UE dans la recherche scientifique britannique et ainsi de suite. »",
        "« En résumé ? »",
        "« Notre contribution de plein membre s'élève à un peu moins de 100 livres par personne et par an. C'est en tenant compte du rabais, de l'argent qui revient sous forme d'investissements au Royaume-Uni, et des engagements d'aide étrangère que nous payons actuellement via l'UE. Si nous atterrissons dans l'Espace économique européen après le Brexit, cela pourrait être plutôt de l'ordre de 75 livres par tête. »",
        "« Comment ça va passer auprès des électeurs ? ricane Barkwell. On vous a fait économiser le prix d'un plat à emporter ! »",
        "« En réalité, ce serait un gain net, fait remarquer Stollard. 75 livres par an contre environ 750 livres par ménage que nous perdrions en dehors de l'EEE. »",
        "« Même si c'était vrai, Alan, dit Dent, vous ne comprenez pas. C'est de la politique, pas des tableurs. Les gens ont voté pour ne plus envoyer le moindre sou à Bruxelles. »"
    ]
}

# Section 770
translations["770"] = {
    "PROSE": [
        "« Vous n'êtes pas vraiment engagé, tout de même, n'est-ce pas ? Pas en faveur d'un Brexit ultra-dur qui trancherait tous les anciens liens et nous sortirait du marché unique, de l'union douanière et de tout le reste. »",
        "Que répondez-vous à cela ?"
    ],
    "OPTIONS": [
        "[OPTION] \"« Je n'ai peut-être pas votre degré de conviction, mais c'est mon devoir de mener à bien un Brexit dur et j'ai bien l'intention de le faire. »\" ►859",
        "[OPTION] \"« Un Brexit plus souple est ce que veut la majorité des gens. Nous pouvons quitter l'UE sans créer une nation divisée. »\" ►308"
    ]
}

# Section 772
translations["772"] = {
    "PROSE": [
        "« Le commerce est bénéfique pour les raisons évidentes. »",
        "« Ça rapporte de l'argent. »",
        "« Exactement. Mais il y a des effets secondaires. Basculer vers de nouveaux circuits entraîne une baisse de productivité. La réduction du commerce diminue la concurrence, ce qui a un impact sur l'efficacité des entreprises. »",
        "« Mais nous aurons davantage de concurrence. »",
        "« Peut-être. Nous nous démènerons pour conclure des accords, ce qui ne revient pas forcément au même. Il est certain que nous aurons moins accès aux produits intermédiaires de qualité supérieure en provenance de l'UE, les produits chimiques utilisés dans l'industrie pharmaceutique par exemple, et par conséquent l'innovation pourrait en pâtir. »"
    ],
    "OPTIONS": [
        "[OPTION] \"« Les gens devront se montrer à la hauteur du défi. »\" ►142",
        "[OPTION] \"« Vous avez commencé, alors autant terminer. »\" ►188",
        "[OPTION] \"« Assez de catastrophisme pour aujourd'hui. »\" ►666"
    ]
}

# Section 774
translations["774"] = {
    "PROSE": [
        "Vous vous surprenez à réfléchir aux contours d'un accord commercial avec l'UE tandis que vous vous asseyez pour un énième petit-déjeuner de travail. Vous semblez enchaîner les matinées très matinales ces derniers temps, et les veillées tardives aussi. Si seulement vous pouviez ajouter une heure à la journée. Cette pensée vous arrache un gloussement quasi hystérique, aussitôt réprimé. Une heure de plus ? De la folie, évidemment. Impossible. Mais après tout, négocier un Brexit satisfaisant en moins de deux ans l'est tout autant.",
        "Wilkins se glisse dans la pièce et pose un menu devant vous. « Que prendrez-vous, Premier ministre ? »"
    ],
    "OPTIONS": [
        "[OPTION] \"Peut-être le saumon fumé écossais et les œufs brouillés\" ►430",
        "[OPTION] \"Ou le traditionnel petit-déjeuner anglais\" ►355",
        "[OPTION] \"D'un autre côté, le continental a l'air bien plus sain\" ►785",
        "[OPTION] \"Du sirop d'érable sur des pancakes – miam !\" ►282"
    ]
}

# Section 776
translations["776"] = {
    "PROSE": [
        "« Je suppose, dit Strewel en essayant de paraître optimiste. Remarquez, c'est de la Suisse qu'on parle ici, pas de la Ruritanie. Leur économie fait un quart de la nôtre. Elle serait bien plus grande aussi s'ils avaient pleinement accès aux industries de services de l'UE. »",
        "« Fadaises, dit Barkwell. On accorde beaucoup trop d'importance aux services, si vous voulez mon avis. Qu'est-ce que c'est, au fond ? Resservir du café à quelqu'un ? Lui couper les cheveux ? L'avenir de la Grande-Bretagne est dans l'industrie manufacturière. »",
        "C'est assez alarmant d'entendre cela de la bouche de votre ministre du Commerce international, mais vous apaisez vos inquiétudes en vous disant qu'il fait peut-être de l'ironie."
    ]
}

# Section 779
translations["779"] = {
    "PROSE": [
        "« Je suis sûr que les ministres auront besoin d'avoir une idée du nombre de ces permis qui seraient délivrés chaque année, dit le président Terlamen. »",
        "« De manière réaliste, peut-être cinquante mille par an pendant les cinq premières années. Après quoi nous réviserons les chiffres. »",
        "« Mais actuellement vous admettez un quart de million de citoyens européens par an, fait remarquer le Premier ministre suédois. »",
        "« Et c'est bien le problème. C'est trop. Les communautés ne peuvent pas absorber autant d'étrangers qui affluent. »",
        "« Mais réduire à un cinquième… » La chancelière Käsen secoue la tête, ce qui lui donne plus que jamais l'air d'un carlin lugubre. « C'est trop drastique. »",
        "« Les citoyens de l'UE veulent s'installer en Grande-Bretagne parce que vous êtes un pays riche, intervient le Premier ministre espagnol. Et ils vous enrichissent davantage. Si vous tenez tant que ça à fermer le robinet, quittez tout simplement le marché unique. Quand vous serez aussi pauvres que nous, vous verrez combien de gens font la queue pour immigrer. »"
    ],
    "OPTIONS": [
        "[OPTION] \"Vous ne vous laisserez pas dicter votre conduite. Leur dire que votre décision est de refuser la libre circulation et d'instaurer un système à points à la place\" ►216",
        "[OPTION] \"Vous gagnerez davantage en cédant du terrain. Accepter de vous en tenir strictement aux restrictions actuelles de libre circulation, le dernier mot revenant aux tribunaux britanniques\" ►183",
        "[OPTION] \"Être ferme mais juste. Vous appliquerez un quota de cinquante mille immigrants européens par an. À prendre ou à laisser\" ►369"
    ]
}

# Section 780
translations["780"] = {
    "PROSE": [
        "« Ce ne sera pas rapide, dit Dent. Les négociations suisses ont pris cinq ou six ans rien que pour obtenir les trois quarts de l'accès au marché unique. »",
        "« L'UE accélérerait les choses pour nous, estime Barkwell. Ils seraient comme un chien affamé devant un os juteux. »",
        "« Bien que je convienne qu'il n'est dans l'intérêt de personne de faire attendre la Grande-Bretagne pour un accord, dit Stollard, nous devons nous rappeler que le type d'accord sur mesure que nous proposerions doit être bien plus étendu que celui de la Suisse. Et nous manquons toujours de personnel qualifié pour les négociations complexes de ce type. Si je devais deviner, je dirais qu'il faudra un minimum de cinq ans. »",
        "« Si nous empruntons cette voie, rétorque Dent. Peut-être serions-nous mieux lotis sous les règles de l'Organisation mondiale du commerce plutôt que dans l'AELE. »"
    ]
}

# Section 781
translations["781"] = {
    "PROSE": [
        "« Les barrières non tarifaires au commerce, dit le chancelier de l'Échiquier. Réfléchissez-y. Le tarif douanier international moyen sur les marchandises est d'un peu plus de 2 %. La moyenne sur les marchandises entrant dans l'UE est moitié moindre, grâce aux accords commerciaux de l'UE. Mais les facteurs qui influencent le plus le commerce de nos jours sont les normes, les qualifications, les quotas – l'inévitable paperasserie qui garantit au consommateur un traitement équitable, considérablement simplifiée quand un article expédié ou un service proposé à travers l'Europe n'a pas à être contrôlé à une douzaine de frontières. Faire cavalier seul va franchement être aussi pénible que de devoir présenter un passeport pour aller à Pimlico. »"
    ]
}

# Section 782
translations["782"] = {
    "PROSE": [
        "Quand le moment de votre défaite arrive, vous ne l'accueillez avec aucune des émotions violentes auxquelles vous vous attendiez. Colère, chagrin, regret, déni. Tout ce que vous ressentez est un vaste engourdissement. Peut-être Dieu a-t-il éprouvé cela lorsqu'Il a contemplé ce qu'Il avait créé.",
        "« Que direz-vous à votre successeur, Wilkins ? » demandez-vous tandis qu'il supervise les déménageurs qui emportent vos affaires.",
        "« Je dirai ce que j'ai toujours dit. \"Bienvenue, Premier ministre.\" Mais d'abord… »",
        "Vous attendez. « Oui ? »",
        "« Au revoir, Premier ministre. »",
        "<p class=\"centered\">FIN</p>"
    ]
}

# Section 784
translations["784"] = {
    "PROSE": [
        "Dieu vous accorde un moment de contemplation silencieuse, vous permettant de constater que vous n'avez rien à craindre des Lib Dems. Même au sommet de leur popularité, avec près d'un quart des voix, ils ont remporté moins de soixante sièges. Bien sûr, à l'époque il avait été douloureux de devoir former une coalition avec eux, de les laisser freiner le programme d'austérité conservateur et ainsi de suite.",
        "Mais cela s'est bien terminé au final. Les gens reprochent encore davantage aux Lib Dems qu'à votre propre parti, et ils ont été contraints de se séparer de leur ancien dirigeant, très capable et éloquent, au profit de l'évangéliste maladroit Bob Fobber.",
        "Cette pensée vous donne un instant de pause. Et si Fobber avait ses propres conversations avec le Tout-Puissant ? Mais non – vous êtes convaincu qu'on le mettrait en attente, se contentant d'écouter vingt minutes d'harmonies célestes avant de recevoir finalement un message enregistré d'un ange.",
        "Alors qu'en est-il des Lib Dems sous la direction d'amateur de Fobber ? Selon les sondages actuels, ils pourraient récupérer une douzaine de sièges, mais pas assez pour constituer une menace sérieuse. Sur ce point, vous pouvez dormir tranquille."
    ],
    "OPTIONS": [
        "[OPTION] \"« Et les travaillistes ? »\" ►626",
        "[OPTION] \"« Comment m'y prendrais-je pour convoquer des élections ? »\" ►35",
        "[OPTION] \"« Nous serions balayés en Écosse. »\" ►3",
        "[OPTION] \"« Amen et bonne nuit, Lord. »\" ►666"
    ]
}

# Section 785
translations["785"] = {
    "PROSE": [
        "Un petit-déjeuner continental, voilà exactement ce que le médecin a prescrit. Croissants, café, jambon belge et fruits. Attendez, pourtant, d'après le menu c'est en réalité du jambon du Wiltshire, et des croissants cuits au coin de la rue. Évidemment, de quoi aurait-il l'air si le Premier ministre se régalait d'un petit-déjeuner d'origine étrangère ? L'<em>Outrage</em> et le <em>Heil</em> ont des reporters qui fouillent les poubelles derrière le 10 Downing Street pour vous prendre en flagrant délit de ce genre de chose.",
        "Vous retroussez la lèvre de frustration. En dehors de l'UE, il y aura bien moins de choix sur les menus de la Grande-Bretagne. Et, soyons honnête, la meilleure issue pour l'économie serait presque certainement de rester dans l'Espace économique européen, comme la Norvège. Si nous devons quitter l'UE, faisons-le de manière à ne prendre aucun risque avec l'économie. Et ce serait le paquet de sortie le plus facile à négocier avec l'UE. En réalité, pas grand-chose ne changerait, si ce n'est que nous aurions moins d'influence. Et Dieu sait que le reste de l'UE en serait ravi. Nous pourrions tout boucler dans les deux ans également.",
        "Mais comment vendre cela à la presse anti-européenne, sans parler de votre propre parti ?"
    ],
    "OPTIONS": [
        "[OPTION] \"Vous ne pouvez que faire de votre mieux\" ►747"
    ]
}

# Section 786
translations["786"] = {
    "PROSE": [
        "Elle n'est pas impressionnée. « Après quarante ans au sein de l'UE, nous manquons franchement d'expertise pour conclure des accords commerciaux internationaux. Et même si nous l'avions, il faudrait des décennies pour mettre en place des accords suffisamment avantageux pour remplacer ce que nous perdons. Les gens n'ont certainement pas voté pour s'appauvrir, ce qui est pourtant ce qui arrivera si nous ne faisons pas attention. »",
        "« Oh, allons, je pense que vous êtes un peu négative. La Grande-Bretagne reste une grande nation, vous savez. De nombreux pays se précipiteront pour venir conclure un accord avec nous. »",
        "« Cela prendra quand même des années et en attendant les entreprises trinquent. Allez-vous garantir les subventions au développement régional ? Les investissements dans les entreprises ? Les fonds de recherche ? L'accès à nos universités pour l'élite des étudiants européens ? La Grande-Bretagne bénéficie de tout cela grâce à son appartenance à l'UE et nous ne pouvons tout simplement pas nous permettre de couper les vivres. »",
        "Wilkins vous fait signe que le chancelier de l'Échiquier et les autres sont prêts à vous recevoir."
    ],
    "OPTIONS": [
        "[OPTION] \"Mettre fin à cette réunion\" ►240",
        "[OPTION] \"La rassurer que vous annulerez le Brexit si vous le pouvez\" ►37"
    ]
}

# Section 787
translations["787"] = {
    "PROSE": [
        "Vos lettres de créance en matière de Brexit sont solides. N'avez-vous pas limogé un secrétaire d'État subalterne pour avoir exprimé des sympathies hérétiques envers le Remain ? Que Noysom-Reek remette en question la sincérité de votre détermination à sortir la Grande-Bretagne de l'UE, c'est comme si César Borgia accusait Savonarole d'être insuffisamment dévot."
    ]
}

# Section 789
translations["789"] = {
    "PROSE": [
        "Vous rappelez au public les affiches de style nazi qui avaient été placardées pendant la campagne du référendum. « La conduite de M. Fungale est bien en deçà des standards que nous exigeons d'un homme politique conservateur, déclarez-vous dans une interview organisée à la hâte. Étant donné sa marque de politique incendiaire, nous estimons qu'il ferait mieux de sauter dans un avion et d'aller offrir ses talents douteux au président Windrip. »",
        "Cela laisse l'aile droite du parti fulminante. Beaucoup d'entre eux ne voyaient rien de mal dans ces affiches et les tactiques de peur xénophobes que Fungale avait employées pour attiser le vote Leave. Eh bien, qu'ils aillent rejoindre l'UKIP. Mais il n'entrera pas au parti conservateur tant que vous serez aux commandes."
    ]
}

# Section 790
translations["790"] = {
    "PROSE": [
        "« Franchement, nous aurions besoin d'au moins dix ans d'adhésion continue à l'UE, ou au moins d'adhésion associée, dit Stollard, pendant que nous peaufinons les détails du nouvel accord commercial. »",
        "« C'est de la conspiration pure et simple ! tonne Barkwell. »",
        "« On n'appelle pas ça une conspiration quand ce sont des ministres qui le font, Leslie, dit Stollard avec douceur. »",
        "Vous savez pourquoi Barkwell est inquiet. Dix ans, c'est largement suffisant pour organiser un second référendum – et bon nombre des plus fervents partisans du Brexit auront rendu l'âme d'ici là.",
        "« Pour commencer, n'appelons pas cela une phase de transition, décidez-vous. Ça fait timoré. Nous parlerons de phase de mise en œuvre. Nous mettons en œuvre le Brexit. »",
        "« Juste pas aussi vite, ajoute Stollard. La transition – pardon, la phase de mise en œuvre est notre parachute tandis que nous dérivons vers un atterrissage que l'on espère en douceur sur les rives d'un nouvel accord de libre-échange. »",
        "« Et ça ne peut pas prendre dix ans. Cela doit se produire durant la législature du prochain Parlement. Ainsi nous pourrons aborder les élections générales en disant : voilà, nous réalisons le Brexit. Nous remportons celles-ci et nous tâchons de mettre les points sur les i et les barres sur les t d'ici 2025 au plus tard. »",
        "« Pourvu que l'UE nous accorde ce répit, dit Dent. Certains d'entre eux espéreront probablement que nous changerons d'avis, donc ils ne s'opposeront pas à une période de transition, mais les envieux pourraient vouloir nous mettre dehors plus tôt. »"
    ]
}

# Section 791
translations["791"] = {
    "PROSE": [
        "Rufus vire vers une ligne plus dure sur le Brexit, invoquant son expérience de ministre de l'Intérieur comme ayant cimenté sa conviction que la souveraineté et les frontières britanniques doivent être sécurisées.",
        "Vous répondez en surenchérissant dans votre propre rhétorique sur le Brexit, déterminé à ce que, s'il faut choisir, vous soyez perçu comme le candidat le plus ferme sur le Brexit.",
        "« Espérons qu'il n'y a pas de cadavres dans le placard », dit Wilkins en disposant vos vêtements le matin du prochain vote."
    ]
}

# Section 792
translations["792"] = {
    "PROSE": [
        "Sans surprise pour personne hormis elle-même, Amelia Dimple est éliminée au premier tour de scrutin. Lors de son discours de concession, elle arbore son expression habituelle, celle d'une fumeuse invétérée essayant de comprendre l'électrodynamique quantique. « J'offrirai mes services partout où le pays aura besoin de moi », déclare-t-elle.",
        "Vous éclatez de rire et éteignez la télévision d'un geste tranchant de la télécommande. Cette femme ridicule. Vous ne lui confieriez même pas l'arrangement d'un bouquet de fleurs, encore moins la direction du pays.",
        "Il est bon de se débarrasser de cette distraction. Dimple était le goût de viande dont vous aviez besoin pour vous mettre en appétit pour le combat. Et maintenant il vous faut un plan pour faire face à l'opposition sérieuse."
    ],
    "GOTO": [
        '[IF keyword:NYLON] "Réflexion en cours" ►27',
        '[ELSE] "Élaborer un plan" ►73'
    ]
}

# Section 793
translations["793"] = {
    "PROSE": [
        "« La Norvège en a en abondance, fait remarquer le chancelier de l'Échiquier. Et si la Grande-Bretagne rejoignait l'Association européenne de libre-échange, ce serait 65 millions de personnes ajoutant notre voix aux 5 millions actuels de l'AELE. Notre présence triplerait le PIB de l'ensemble du bloc du jour au lendemain. »",
        "« Attendez un instant, dites-vous. Nous sommes tellement plus grands mais nous ne faisons qu'augmenter le PIB global par trois ? »",
        "« N'oubliez pas que l'AELE comprend déjà la Norvège et la Suisse, Premier ministre, deux pays très riches en termes de PIB par habitant comparé au Royaume-Uni. »",
        "Dent rougit à ces mots, détestant entendre des faits et des chiffres qui ne dépeignent pas la Grande-Bretagne comme la plus grande nation de l'hémisphère nord.",
        "« L'important, c'est que nous serions le poisson-chat face à leurs vairons, intervient Strewel. Remarquez, l'UE est un sacré gros brochet. L'économie européenne serait encore cinq fois plus grande que l'AELE plus le Royaume-Uni combinés. »"
    ],
    "OPTIONS": [
        "[OPTION] \"« Alors l'UE nous imposerait sa volonté. »\" ►131",
        "[OPTION] \"« Y a-t-il un moyen d'utiliser notre stature internationale pour obtenir un levier commercial ? »\" ►684"
    ]
}

# Section 794
translations["794"] = {
    "PROSE": [
        "Vos bonnes relations avec les autres États de l'UE, combinées à votre volonté manifeste de rester un allié proche et un partenaire commercial après le Brexit, les rassurent quant à la possibilité de maintenir le Royaume-Uni au sein du mandat d'arrêt européen.",
        "« Qui sait ? dit Willy Franjeboom, le négociateur en chef de l'UE. Nous pouvons espérer que le départ de la Grande-Bretagne ne soit que temporaire. »"
    ],
    "REPORT": [
        "<strong>+2 % Autorité</strong> : les médias le présentent comme un triomphe de vos talents de négociateur.",
        "<strong>+2 % Bienveillance</strong> : les Vingt-Sept commencent à se sentir plus confiants quant à l'engagement continu de la Grande-Bretagne.",
        "<strong>+3 % Popularité</strong> : les électeurs se sentent en sécurité."
    ],
    "OPTIONS": [
        "[OPTION] \"Prochain ordre du jour\" ►286"
    ]
}

# Section 795
translations["795"] = {
    "PROSE": [
        "« Jamais, dit Ron d'un ton pince-sans-rire. Enfin, pas avant que tous les fonctionnaires européens actuellement en poste soient décédés, donc en pratique nous pouvons dire qu'il n'y a pas de limite de temps sur celui-là. »",
        "« Nous ne pourrions pas simplement accepter de couvrir les retraites des citoyens britanniques travaillant pour l'UE ? Quel est le pourcentage dans ce cas ? »",
        "« Huit pour cent. Mais – »",
        "« Ce n'est pas si mal. Je peux vendre ça à la presse plus facilement que de payer la note pour une bande d'eurocrates gâteux. Pourquoi cette tête d'enterrement, Ron ? »",
        "« Ce ne sont pas que les Britanniques, Premier ministre. La position de l'UE sur ce point est que la nationalité d'un fonctionnaire est sans importance. Ils s'attendront à ce que nous couvrions notre part des pensions pour tous les fonctionnaires européens qui ont commencé à travailler alors que nous étions encore membres. »",
        "« C'est davantage ? »",
        "« Au moins moitié plus. Mais c'est sans doute un engagement juridique. Une entreprise doit faire de même pour ses employés quand elle vend une activité. »",
        "« Oui, voyez-vous, ça ne va pas aider à vendre la chose aux eurosceptiques. Imaginez les gros titres. \\\"PARASITES.\\\" \\\"EXTORSION.\\\" \\\"ILS NOUS SAIGNENT À BLANC.\\\" »",
        "Sous la lourde veste de tweed, ses épaules se soulèvent dans un haussement. « C'est pour ça qu'on appelle ça la politique, Premier ministre. »"
    ]
}

# Section 796
translations["796"] = {
    "PROSE": [
        "Même le plus fervent des brexiteurs sur les bancs d'arrière-ban conservateurs est convaincu que vous menez une négociation serrée avec l'UE. La seule question est de savoir si les travaillistes voteront la motion."
    ]
}

# Section 797
translations["797"] = {
    "PROSE": [
        "Vos fonctionnaires rapportent que le ministre chargé de négocier l'indemnité de sortie s'est emporté lorsque l'équipe de l'UE l'a contredit. Il est parti en claquant la porte, déclarant qu'il ne tolérerait pas ce qu'il a qualifié de passage à tabac punitif. Il y a même une rumeur selon laquelle il aurait comparé la délégation allemande à des gardiens de camp de concentration.",
        "« Ça aurait pu être pire, estime votre directeur de cabinet. J'ai veillé à faire remplir sa flasque avec de l'eau tonique. »",
        "« Mais que se passe-t-il maintenant ? Les Vingt-Sept vont porter l'affaire devant la Cour internationale. Nous pourrions finir par devoir payer davantage. »",
        "Il hoche la tête. « Mais pas avant les prochaines élections, au moins. »"
    ],
    "REPORT": [
        "<strong>-5 % Autorité</strong> : personne ne sait si vous avez le moindre contrôle sur votre cabinet.",
        "<strong>-15 % Bienveillance</strong> : l'attitude belliqueuse du ministre des Affaires étrangères vous a fait perdre des amis parmi les autres États de l'UE.",
        "<strong>+5 % Popularité</strong> : les électeurs perçoivent cela comme un coup de force."
    ],
    "OPTIONS": [
        "[OPTION] \"Cap maintenu\" ►580"
    ]
}

# Section 798
translations["798"] = {
    "PROSE": [
        "Alors que tout semblait réglé, vous êtes assailli par une avalanche d'amendements de la part de multiples pays de l'UE."
    ],
    "REPORT": [
        "<strong>-3 % Économie</strong> : encore plus de tracasseries administratives entravent les exportations britanniques.",
        "<strong>-2 % Popularité</strong> : les électeurs doutent de votre capacité à tenir vos promesses."
    ],
    "OPTIONS": [
        "[OPTION] \"Encore une nuit blanche\" ►865"
    ]
}

# Section 799
translations["799"] = {
    "PROSE": [
        "« Nous ne pourrions pas mener nos propres accords commerciaux, dit Barkwell. J'appelle ça un inconvénient de taille. Et ne vous y trompez pas, les gens verront cela aussi comme un aveu d'échec. »",
        "Ce n'est pas la première fois que Barkwell laisse entendre qu'il pourrait porter ses griefs hors de la salle du Conseil des ministres. Vous laissez votre regard glacial le refroidir de quelques degrés, puis vous vous tournez vers les autres.",
        "« Nous devrions nous conformer aux décisions de la Cour européenne, risque Dent. Techniquement, les tribunaux britanniques seraient indépendants, mais il y aurait une forêt de problèmes de conformité. Combien de céréales dans un biscuit au chocolat, ce genre de choses. Et l'UE étant plus grande, ses décisions domineraient. »",
        "« Peut-être pourrions-nous vendre le grésillement de la souveraineté à la presse sans mordre dans le substitut de viande à protéines texturées. » Votre regard passe sur Strewel, toujours en train d'engloutir son petit-déjeuner complet avec la gourmandise d'un écolier surdimensionné. « Alan, quelque chose à ajouter ? »",
        "Stollard acquiesce. « Une union douanière ne procure un avantage commercial que pour les biens. C'est très bien pour la Turquie, mais 80 % de notre économie relève du secteur des services. Donc nous devrions de toute façon négocier un accord spécial sur ce point. »"
    ],
    "OPTIONS": [
        "[OPTION] \"« Passons en revue les avantages du modèle turc. »\" ►681",
        "[OPTION] \"« Hormis une union douanière, quelles options avons-nous ? »\" ►703"
    ]
}

# Section 801
translations["801"] = {
    "PROSE": [
        "« C'est trop serré pour se prononcer, dit Ron Beardsley en vous tendant un sondage de sortie des commentaires formulés par les membres du parti conservateur. »",
        "« Je ne sais pas ce que nos membres font à l'ennemi, Ron, mais nom de Dieu, ils me terrifient. »",
        "Tandis que vous attendez l'annonce des résultats, à quoi pensez-vous ?"
    ],
    "OPTIONS": [
        "[OPTION] \"Les dés sont jetés\" ►782",
        "[OPTION] \"Advienne que pourra\" ►486"
    ]
}

# Section 802
translations["802"] = {
    "PROSE": [
        "Tiffany Rufus vous téléphone pour proposer un accord. « Faisons équipe pour éliminer Peter Strewel de la course. »",
        "« Et ensuite ? »",
        "« Ensuite ce ne sera plus que vous et moi, et les adhérents décideront. Mais aucun de nous ne souhaite affronter Peter quand ce ne sera plus le groupe parlementaire qui votera, n'est-ce pas ? »"
    ],
    "OPTIONS": [
        "[OPTION] \"« D'accord, concentrons-nous tous les deux sur le déstabiliser. »\" ►307",
        "[OPTION] \"« Je n'aime pas les arrangements en coulisses. Laissons les choses suivre leur cours. »\" ►94"
    ]
}

# Section 803
translations["803"] = {
    "PROSE": [
        "« Il n'y a pas d'argent, voilà le problème. »",
        "« Vous êtes le chancelier de l'Échiquier, Alan. Si vous ne trouvez pas le moyen de me faire financer le NHS, à quoi servez-vous ? »",
        "Vous êtes en visioconférence, alors qu'il est juste à côté. Ces jours-ci, vous tenez tous les deux à donner l'impression d'être débordés, alors il tape sur son clavier et prend de temps en temps des appels rapides pendant que vous gérez une succession d'assistants qui ne cessent de passer la tête dans votre bureau.",
        "« Oh, je peux vous trafiquer les comptes. Vous voulez plus d'hôpitaux, je peux couper dans la défense, ça vous va ? Ou l'aide étrangère. »",
        "« Voilà qui fait gagner des voix. »",
        "« Pas sur la scène diplomatique, ni même dans notre propre intérêt à long terme. »",
        "« Cinq ans d'horizon, c'est tout ce dont vous avez besoin, Alan. »"
    ]
}

# Section 804
translations["804"] = {
    "PROSE": [
        "L'amour. Qu'est-ce que cela signifie ? Vous aviez un chiot autrefois qui vous suivait partout jusqu'à ce que le laitier l'écrase avec sa camionnette. Mais était-ce de l'amour ? Ou la simple anxiété d'une créature impuissante à l'idée d'être laissée seule ?",
        "Et votre nounours. Il vous aimait, pensez-vous, mais votre relation avec lui a toujours été conflictuelle et portait en elle les germes de la trahison. Boucle d'Or devait toujours rester sur ses gardes, de peur qu'un matin le porridge ne suffise plus.",
        "Maintenant, enfin, vous connaissez quelque chose de mieux que l'amour. La peur abjecte et obséquieuse. Vous la voyez dans les sourires crispés et les yeux trop brillants autour de la table du Conseil des ministres, dans les réponses empressées et les postures serviles des députés à qui vous adressez la parole. Ils savent que votre pouvoir est absolu. D'un geste de la main, vous pourriez les élever au cercle intime ou les bannir vers une nouvelle investiture.",
        "Ce n'est que dans les petites heures du matin, quand vous vous réveillez et voyez la lueur du réverbère sur le mur de la chambre, que vous sentez un infime tiraillement de malaise. Car inquiète repose la tête qui porte la couronne."
    ],
    "OPTIONS": [
        "[OPTION] \"Garder son calme et continuer\" ►386"
    ]
}

# Section 805
translations["805"] = {
    "PROSE": [
        "Pouvez-vous rester en poste après un tel revers ? Il vous faudra une volonté de fer.",
        "Et maintenant ?"
    ],
    "REPORT": [
        "<strong>-10 % Popularité</strong> : vous payez le prix d'avoir choisi le camp perdant."
    ],
    "OPTIONS": [
        "[OPTION] \"Il est temps de jeter l'éponge\" ►395",
        "[OPTION] \"Vous ne partez nulle part. Il y a un travail à accomplir\" ►206"
    ]
}

# Section 807
translations["807"] = {
    "PROSE": [
        "« Pas vraiment, dit Stollard. Les services financiers et les professions connexes représentent un emploi britannique sur quinze. Et les deux tiers de ceux-ci se trouvent en dehors de Londres. »"
    ]
}

# Section 808
translations["808"] = {
    "PROSE": [
        "Les yeux de Barkwell manquent de lui sortir de la tête, tandis que Dent laisse échapper une toux courroucée.",
        "« Vous n'êtes pas d'accord, messieurs ? »",
        "« Rappelons-nous que le peuple nous a donné un mandat écrasant pour sortir du marché unique, siffle Barkwell. Il a parlé. Qui sommes-nous pour trahir ses vœux ? »",
        "« Nous sommes le gouvernement élu du Royaume-Uni, pas les grands prêtres de Baal. Nous ferons ce qui est dans l'intérêt du peuple. »",
        "« Et après tout, deux cinquièmes de ceux qui ont voté Leave voulaient en réalité que nous adoptions le modèle norvégien, dit Stollard. C'est donc la solution préférée de 69 % de l'électorat. »",
        "« Mensonge ! grogne Barkwell en quittant la pièce d'un pas rageur. »"
    ],
    "REPORT": [
        "<strong>-1 % Autorité</strong> : il n'est pas prudent de révéler vos plans à vos ennemis."
    ],
    "OPTIONS": [
        "[OPTION] \"Vous êtes entouré d'imbéciles\" ►666"
    ]
}

# Section 811
translations["811"] = {
    "PROSE": [
        "Le Remain dispose d'une avance écrasante dans les sondages. Le jour venu, une forte participation des jeunes électeurs en fait une certitude. À la télévision, vous voyez Peter Strewel quitter son domicile. Il affiche un sourire béat comme Winnie l'Ourson dans une fabrique de miel. Nul doute qu'il est soulagé, après le proverbial plat de pâtes, d'avoir eu la sagesse de ne pas faire campagne pour le Leave cette fois-ci."
    ]
}

# Section 812
translations["812"] = {
    "PROSE": [
        "Willy Franjeboom, le négociateur en chef de l'UE, vous appelle pour vous dire qu'ils sont parvenus à une décision concernant le sort des ressortissants britanniques vivant en Europe. « Vous serez soulagé d'apprendre que nous n'allons pas expulser tous ces retraités des plages espagnoles », dit-il en riant.",
        "« Ni les financiers, avocats, scientifiques et médecins britanniques. Vous ne voudriez pas renoncer à percevoir leurs impôts, n'est-ce pas ? »",
        "« Oh, ce n'est pas tant cela. Nous ne pouvions tout simplement pas laisser ces familles devenir des pions dans un jeu politique. »",
        "C'est à votre tour de rire. « Cela aurait mérité le plus petit violon du monde si vous l'aviez annoncé il y a un an. Vous avez simplement laissé traîner les choses en espérant que la Grande-Bretagne prendrait une décision en premier. »",
        "« Et quelle est votre décision ? »",
        "Voilà qui est délicat. Si vous ne répondez pas au geste de l'UE par un geste équivalent, vous allez passer pour mesquin. Mais il y a trois millions de ressortissants européens en Grande-Bretagne, et moins d'un million et demi de ressortissants britanniques répartis dans toute l'Europe, la situation est donc loin d'être équitable. Que lui direz-vous ?"
    ],
    "OPTIONS": [
        "[OPTION] \"« Les ressortissants de l'UE vivant déjà ici peuvent rester. »\" ►182",
        "[OPTION] \"« Je notifie que les ressortissants de l'UE doivent faire leurs valises et partir une fois que la Grande-Bretagne aura quitté l'UE. »\" ►357"
    ]
}

# Apply translations
for section_id, translation in translations.items():
    if "PROSE" in translation:
        data[section_id]["PROSE"] = translation["PROSE"]
    if "OPTIONS" in translation:
        data[section_id]["OPTIONS"] = translation["OPTIONS"]
    if "GOTO" in translation:
        data[section_id]["GOTO"] = translation["GOTO"]
    if "REPORT" in translation:
        data[section_id]["REPORT"] = translation["REPORT"]

with open('/home/user/Brexit_FR/_sections.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {len(translations)} sections successfully (batch 1)")
