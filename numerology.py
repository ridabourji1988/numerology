import streamlit as st

def calculate_life_path_number(birthdate):
    day, month, year = map(int, birthdate.split('-'))
    
    def sum_digits(n):
        return sum(int(digit) for digit in str(n))
    
    day_sum = sum_digits(day)
    month_sum = sum_digits(month)
    year_sum = sum_digits(year)
    
    life_path_number = day_sum + month_sum + year_sum
    
    while life_path_number > 9:
        life_path_number = sum_digits(life_path_number)
    
    return life_path_number

def calculate_name_number(name):
    name = name.upper()
    name_number = 0
    
    for char in name:
        if char.isalpha():
            name_number += ord(char) - ord('A') + 1
    
    while name_number > 9:
        name_number = sum(int(digit) for digit in str(name_number))
    
    return name_number

def interpret_life_path_number(number):
    interpretations = {
        1: ("🔮 Numéro de Chemin de Vie 1 🔮\n"
        "Individualiste, ambitieux(se), et un(e) leader naturel(le). Vous possédez une volonté intrinsèque "
        "de réussir et avez le potentiel de laisser une empreinte durable sur votre chemin choisi. Votre "
        "indépendance et votre détermination vous permettent de surmonter les défis et d'inspirer les autres "
        "à suivre votre exemple.",
        "🌟 Travailler en Équipe :\nEn tant que leader naturel, vous avez la capacité de guider et de motiver "
        "les membres de votre équipe. Vous préférez diriger plutôt qu'être dirigé, et votre confiance en "
        "vous peut inspirer les autres à vous suivre.",
        "🧩 Traits de Personnalité :\nVous êtes ambitieux(se), déterminé(e) et confiant(e). Votre indépendance "
        "peut parfois vous rendre têtu(e), mais cela reflète également votre forte détermination.",
        "🚧 Points de Vigilance :\nAssurez-vous de tenir compte des idées des autres et de ne pas négliger les "
        "avis de votre équipe. Veillez également à équilibrer votre ambition avec des moments de repos et de "
        "réflexion.",
        "👔 Chemin de Vie Professionnel :\nVotre leadership naturel vous permet d'exceller dans des rôles de "
        "direction. Vous êtes attiré(e) par des postes de leadership où vous pouvez faire valoir vos talents "
        "d'innovation et de prise de décision.",
        "🏡 Chemin de Vie Personnel :\nVotre indépendance vous pousse à chercher des expériences qui vous "
        "permettent de vous démarquer. Vous valorisez votre autonomie et recherchez des opportunités qui vous "
        "permettent de faire une différence significative.",
        "💰 Chemin de Vie Financier :\nVotre ambition peut se traduire par des gains financiers substantiels. "
        "Cependant, veillez à ne pas vous concentrer uniquement sur l'argent. Investissez dans des opportunités "
        "qui reflètent vos valeurs et vos aspirations personnelles.",
        "🔢 Insights en Numérologie :\nLe numéro 1 est souvent associé au commencement et à l'individualité. Il "
        "symbolise le leadership et la détermination. Dans les enseignements spirituels, il représente l'unité "
        "et le potentiel créateur.",
        "👤 Personnalités Célèbres :\nDes personnalités telles que [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont connues pour leur leadership et leur détermination, reflétant les traits du numéro de Chemin de Vie 1."),
    2: ("🔮 Numéro de Chemin de Vie 2 🔮\n"
        "Harmonieux(se), coopératif(ve), et diplomate. Votre capacité à comprendre et à ressentir de l'empathie "
        "pour les autres fait de vous un excellent médiateur et collaborateur. Vous excellez dans les "
        "partenariats et cherchez l'équilibre dans tous les aspects de la vie, favorisant ainsi l'unité et la "
        "compréhension.",
        "🌟 Travailler en Équipe :\nVotre nature coopérative en fait un membre précieux de toute équipe. Vous "
        "facilitez la communication entre les membres et trouvez des solutions qui conviennent à tous. Votre "
        "capacité à mettre les gens à l'aise favorise un environnement de travail positif.",
        "🧩 Traits de Personnalité :\nVous êtes empathique, adaptable et aimable. Votre nature diplomate vous aide "
        "à résoudre les conflits. Cependant, il est important de vous assurer que vos propres besoins sont "
        "également pris en compte.",
        "🚧 Points de Vigilance :\nMéfiez-vous de la tendance à éviter les conflits à tout prix, car cela peut "
        "éventuellement nuire à vos propres intérêts. Assurez-vous également de ne pas vous surcharger en "
        "cherchant constamment l'équilibre.",
        "👔 Chemin de Vie Professionnel :\nVous excellez dans des rôles qui nécessitent une collaboration et une "
        "communication efficaces. Vous prospérez dans des environnements où vous pouvez aider à résoudre les "
        "conflits et faciliter les relations harmonieuses.",
        "🏡 Chemin de Vie Personnel :\nVous recherchez des relations et des expériences qui sont équilibrées et "
        "harmonieuses. Vous êtes attiré(e) par des environnements où vous pouvez contribuer à créer une ambiance "
        "positive.",
        "💰 Chemin de Vie Financier :\nVous valorisez la stabilité financière et recherchez des opportunités qui "
        "vous permettent de maintenir l'équilibre dans vos finances. Les investissements axés sur la coopération "
        "et la collaboration peuvent vous convenir.",
        "🔢 Insights en Numérologie :\nLe numéro 2 symbolise la dualité et l'équilibre. Il reflète la coopération, la "
        "diplomatie et les relations. Spirituellement, il représente l'harmonie et la compréhension.",
        "👤 Personnalités Célèbres :\nDes personnalités telles que [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur capacité à créer des liens harmonieux et à favoriser la collaboration, reflétant "
        "les traits du numéro de Chemin de Vie 2."),
    3: ("🔮 Numéro de Chemin de Vie 3 🔮\n"
        "Créatif(ve), expressif(ve), et sociable. Vos talents artistiques et votre personnalité vibrante attirent "
        "les gens vers vous. Vous possédez le don de la communication efficace et êtes capable d'apporter de la "
        "joie et de l'inspiration à votre entourage.",
        "🌟 Travailler en Équipe :\nVotre nature sociable et communicative en fait un atout précieux pour le travail "
        "d'équipe. Votre capacité à exprimer vos idées de manière créative peut stimuler l'innovation au sein "
        "de l'équipe. Vous aimez également encourager et motiver les autres.",
        "🧩 Traits de Personnalité :\nVous êtes expressif(ve), charismatique et optimiste. Votre énergie est "
        "contagieuse, mais veillez à ne pas vous laisser emporter par des projets multiples, ce qui pourrait "
        "diviser votre attention.",
        "🚧 Points de Vigilance :\nÉvitez de vous disperser dans trop de projets à la fois. Assurez-vous de prendre "
        "du temps pour vous reposer et recharger vos batteries.",
        "👔 Chemin de Vie Professionnel :\nVous excellez dans des domaines qui vous permettent de vous exprimer "
        "créativement. Les carrières artistiques, la communication et les médias pourraient vous offrir des "
        "opportunités d'épanouissement.",
        "🏡 Chemin de Vie Personnel :\nVous cherchez constamment des moyens de vous exprimer et de créer. Vous êtes "
        "attiré(e) par des expériences qui stimulent votre créativité et vous permettent de partager votre "
        "perspective unique.",
        "💰 Chemin de Vie Financier :\nVous pouvez tirer parti de vos talents créatifs pour générer des opportunités "
        "financières. Les projets qui vous permettent de mettre en valeur votre expression artistique peuvent "
        "aussi apporter des bénéfices financiers.",
        "🔢 Insights en Numérologie :\nLe numéro 3 évoque la créativité, l'expression personnelle et la communication. C'est "
        "un nombre lié à l'optimisme et à la joie. Spirituellement, il symbolise la croissance et l'expansion.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leurs talents créatifs et leur capacité à inspirer les autres, reflétant les traits "
        "du numéro de Chemin de Vie 3."),
        4: ("🔮 Numéro de Chemin de Vie 4 🔮\n"
        "Pratique, discipliné(e), et travailleur(e). Votre éthique de travail solide et votre souci du détail "
        "font de vous une personne fiable. Vous excellez dans des environnements structurés et contribuez à la "
        "construction de bases solides et durables.",
        "🌟 Travailler en Équipe :\nVotre approche méthodique est précieuse dans les équipes où la précision et la "
        "rigueur sont essentielles. Vous vous investissez dans les projets à long terme et pouvez être compté(e) "
        "pour respecter les délais et les attentes.",
        "🧩 Traits de Personnalité :\nVous êtes fiable, organisé(e) et pragmatique. Votre attention aux détails vous "
        "permet d'exceller dans des domaines nécessitant une précision minutieuse.",
        "🚧 Points de Vigilance :\nÉvitez de devenir trop rigide ou de vous perdre dans les détails au détriment de "
        "l'innovation. Trouvez un équilibre entre la structure et la flexibilité.",
        "👔 Chemin de Vie Professionnel :\nVous êtes attiré(e) par des rôles qui nécessitent une planification "
        "méticuleuse et une exécution précise. Les domaines tels que la gestion de projet, la comptabilité et "
        "la logistique peuvent convenir à vos compétences.",
        "🏡 Chemin de Vie Personnel :\nVous appréciez l'organisation et la stabilité dans votre vie personnelle. "
        "Vous valorisez les routines qui vous aident à maintenir un équilibre entre le travail et le repos.",
        "💰 Chemin de Vie Financier :\nVous avez une approche méthodique pour gérer vos finances. Les stratégies "
        "d'épargne et d'investissement à long terme sont susceptibles de vous convenir.",
        "🔢 Insights en Numérologie :\nLe numéro 4 symbolise la stabilité, la structure et la persévérance. Il reflète "
        "le sens des responsabilités et l'importance du travail acharné. Spirituellement, il représente la solidité "
        "et la fondation.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur dévouement et leur approche méthodique, reflétant les traits du numéro de Chemin "
        "de Vie 4."),
    5: ("🔮 Numéro de Chemin de Vie 5 🔮\n"
        "Aventureux(se), adaptable, et amoureux(se) de la liberté. Votre soif d'expériences vous pousse à explorer "
        "l'inconnu. Votre polyvalence et votre capacité d'adaptation vous permettent de prospérer dans des "
        "situations que d'autres pourraient trouver difficiles.",
        "🌟 Travailler en Équipe :\nVotre nature aventureuse peut apporter un souffle d'air frais à toute équipe. Vous "
        "êtes ouvert(e) aux idées nouvelles et audacieuses, ce qui peut stimuler la créativité de l'équipe. Votre "
        "capacité à vous adapter rapidement est précieuse.",
        "🧩 Traits de Personnalité :\nVous êtes curieux(se), flexible et indépendant(e). Votre adaptabilité vous permet "
        "de relever efficacement de nouveaux défis et de naviguer dans des environnements en constante évolution.",
        "🚧 Points de Vigilance :\nAssurez-vous de maintenir un niveau d'engagement suffisant dans les projets à long "
        "terme et de ne pas être trop distrait(e) par les opportunités changeantes.",
        "👔 Chemin de Vie Professionnel :\nVous êtes attiré(e) par des rôles qui vous permettent de rester "
        "constamment en mouvement. Les carrières liées aux voyages, à la vente ou à l'entrepreneuriat peuvent "
        "répondre à votre désir d'exploration.",
        "🏡 Chemin de Vie Personnel :\nVous recherchez des expériences qui vous permettent de sortir de votre zone "
        "de confort et d'explorer de nouveaux horizons. Les aventures et les activités stimulantes enrichissent "
        "votre vie personnelle.",
        "💰 Chemin de Vie Financier :\nVous êtes disposé(e) à prendre des risques calculés pour générer des gains "
        "financiers. Cependant, assurez-vous d'élaborer des stratégies financières flexibles pour faire face "
        "aux changements.",
        "🔢 Insights en Numérologie :\nLe numéro 5 évoque la liberté, l'adaptabilité et l'exploration. Il symbolise "
        "le changement et la curiosité. Spirituellement, il représente la transformation et la découverte de soi.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur nature aventureuse et leur capacité à naviguer dans des situations complexes, "
        "reflétant les traits du numéro de Chemin de Vie 5."),
    6: ("🔮 Numéro de Chemin de Vie 6 🔮\n"
        "Nourrissant(e), responsable, et orienté(e) vers la famille. Votre nature compatissante et votre sens du devoir "
        "font de vous un pilier de soutien pour vos proches. Vous trouvez de la satisfaction à créer des "
        "environnements harmonieux et à offrir des conseils à ceux qui en ont besoin.",
        "🌟 Travailler en Équipe :\nVous êtes le ciment qui maintient l'équipe unie. Votre capacité à écouter et à "
        "nourrir les besoins des membres de l'équipe est inestimable. Vous êtes souvent le médiateur qui résout les "
        "conflits.",
        "🧩 Traits de Personnalité :\nVous êtes attentionné(e), fiable et dévoué(e). Votre engagement envers le bien-être "
        "des autres est évident dans vos actions. Votre nature maternelle/paternelle se reflète dans vos interactions.",
        "🚧 Points de Vigilance :\nÉvitez de devenir surprotecteur(trice) au point d'oublier de prendre soin de vous. "
        "Trouvez un équilibre entre le soutien aux autres et la préservation de votre propre bien-être.",
        "👔 Chemin de Vie Professionnel :\nVous prospérez dans des environnements de travail qui vous permettent de "
        "nourrir et de soutenir les autres. Les carrières liées à l'éducation, aux soins de santé et à la conseil "
        "sont susceptibles de répondre à vos aspirations professionnelles.",
        "🏡 Chemin de Vie Personnel :\nVous accordez une grande importance aux relations familiales et aux amitiés. "
        "Créer des liens solides avec les autres et offrir un soutien émotionnel sont des aspects essentiels de "
        "votre vie personnelle.",
        "💰 Chemin de Vie Financier :\nVous êtes prêt(e) à investir dans le bien-être financier de votre famille et "
        "de vos proches. La stabilité financière et la sécurité sont des priorités importantes pour vous.",
        "🔢 Insights en Numérologie :\nLe numéro 6 symbolise l'harmonie, la famille et le service. Il reflète la "
        "responsabilité et la protection. Spirituellement, il représente l'amour inconditionnel et le soutien.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur engagement envers la famille et leur dévouement envers le bien-être des autres, "
        "reflétant les traits du numéro de Chemin de Vie 6."),
    7: ("🔮 Numéro de Chemin de Vie 7 🔮\n"
        "Intellectuel(le), introspectif(ve), et spirituel(le). Vous possédez une curiosité profonde sur le monde qui "
        "vous entoure et cherchez constamment une compréhension plus profonde. Votre esprit analytique et votre "
        "connexion à la spiritualité vous guident vers la découverte de vérités profondes.",
        "🌟 Travailler en Équipe :\nVotre approche analytique peut apporter une perspective unique à l'équipe. Vous "
        "posez des questions pertinentes et encouragez la réflexion approfondie. Votre désir de comprendre les "
        "aspects cachés des situations est précieux.",
        "🧩 Traits de Personnalité :\nVous êtes réfléchi(e), intuitif(ve) et philosophique. Votre soif de connaissances "
        "vous pousse à explorer des sujets profonds et complexes.",
        "🚧 Points de Vigilance :\nVeillez à ne pas trop vous perdre dans vos pensées au point de manquer des occasions "
        "pratiques. Équilibrez votre recherche de vérité avec des actions concrètes.",
        "👔 Chemin de Vie Professionnel :\nVous êtes attiré(e) par des carrières qui vous permettent de creuser en "
        "profondeur et d'analyser des informations complexes. Les domaines de la recherche, de la philosophie et "
        "du développement personnel vous attirent.",
        "🏡 Chemin de Vie Personnel :\nVotre quête de compréhension et de sens guide vos relations personnelles. Vous "
        "recherchez des connexions profondes et des conversations significatives avec les autres.",
        "💰 Chemin de Vie Financier :\nVous préférez investir dans des opportunités qui ont un impact durable et qui "
        "alignent vos valeurs spirituelles. La croissance financière peut être un moyen de soutenir vos objectifs "
        "de recherche de vérité.",
        "🔢 Insights en Numérologie :\nLe numéro 7 évoque la spiritualité, la sagesse et la recherche intérieure. Il "
        "symbolise la connaissance cachée et la découverte de la vérité profonde. Spirituellement, il représente "
        "l'illumination et la connexion à l'univers.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur esprit analytique et leur quête de vérité, reflétant les traits du numéro de Chemin "
        "de Vie 7."),
    8: ("🔮 Numéro de Chemin de Vie 8 🔮\n"
        "Ambitieux(se), autoritaire, et axé(e) sur le succès. Vous êtes doté(e) d'un grand potentiel de leadership et "
        "d'une détermination inébranlable pour atteindre vos objectifs. Votre capacité à gérer les affaires "
        "et à créer des résultats tangibles est impressionnante.",
        "🌟 Travailler en Équipe :\nVotre sens aigu des affaires et votre capacité à prendre des décisions difficiles "
        "font de vous un leader naturel au sein de l'équipe. Vous inspirez les autres à se concentrer sur les "
        "résultats et à réaliser des gains concrets.",
        "🧩 Traits de Personnalité :\nVous êtes ambitieux(se), confiant(e) et persévérant(e). Votre détermination "
        "vous pousse à surmonter les obstacles et à poursuivre vos objectifs avec passion.",
        "🚧 Points de Vigilance :\nÉvitez de devenir trop autoritaire au point de négliger les besoins et les "
        "contributions des autres. Trouvez un équilibre entre le succès personnel et la collaboration.",
        "👔 Chemin de Vie Professionnel :\nLes rôles de direction, la gestion d'entreprise et les opportunités "
        "entrepreneuriales sont en harmonie avec vos compétences en leadership et votre désir de réussite.",
        "🏡 Chemin de Vie Personnel :\nVous cherchez à créer une vie de succès et de prospérité. Les expériences de "
        "croissance personnelle et financière sont essentielles pour votre épanouissement.",
        "💰 Chemin de Vie Financier :\nVous êtes déterminé(e) à atteindre l'indépendance financière et la sécurité. "
        "Les investissements et les stratégies commerciales peuvent vous aider à réaliser vos ambitions financières.",
        "🔢 Insights en Numérologie :\nLe numéro 8 symbolise le pouvoir, la réussite et l'abondance. Il reflète la "
        "capacité de manifester des résultats concrets dans le monde matériel. Spirituellement, il représente "
        "l'équilibre entre le matériel et le spirituel.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur leadership puissant et leur succès financier, reflétant les traits du numéro de "
        "Chemin de Vie 8."),
    9: ("🔮 Numéro de Chemin de Vie 9 🔮\n"
        "Altruiste, compatissant(e), et visionnaire. Vous êtes animé(e) par le désir de faire une différence positive "
        "dans le monde. Votre capacité à voir le panorama d'ensemble vous pousse à œuvrer pour le bien-être de "
        "l'humanité.",
        "🌟 Travailler en Équipe :\nVotre approche humanitaire inspire les autres membres de l'équipe. Vous êtes "
        "sensible aux besoins des autres et apportez une perspective globale aux projets. Votre volonté de créer "
        "un impact positif est contagieuse.",
        "🧩 Traits de Personnalité :\nVous êtes compatissant(e), idéaliste et attentionné(e). Votre désir de faire "
        "le bien guide vos choix et vos actions. Votre compréhension des émotions humaines vous permet de "
        "créer des connexions profondes.",
        "🚧 Points de Vigilance :\nVeillez à ne pas vous épuiser en donnant trop aux autres au détriment de vos "
        "propres besoins. Trouvez un équilibre entre l'altruisme et la préservation de votre bien-être.",
        "👔 Chemin de Vie Professionnel :\nVous êtes attiré(e) par des carrières qui vous permettent de contribuer "
        "au bien-être collectif. Les domaines liés à la philanthropie, à la psychologie et à l'enseignement peuvent "
        "résonner avec vos aspirations professionnelles.",
        "🏡 Chemin de Vie Personnel :\nVotre vie personnelle est guidée par le désir de créer un impact positif. Vous "
        "travaillez à construire des relations significatives et à encourager le bien-être de vos proches.",
        "💰 Chemin de Vie Financier :\nVous envisagez l'argent comme un moyen de réaliser des projets humanitaires et "
        "de créer un changement positif. Vous cherchez des moyens d'utiliser vos ressources financières pour le bien "
        "commun.",
        "🔢 Insights en Numérologie :\nLe numéro 9 symbolise la compassion, la finition et la spiritualité universelle. "
        "Il reflète la réalisation des idéaux et le service désintéressé envers l'humanité. Spirituellement, il "
        "représente l'illumination et l'amour universel.",
        "👤 Personnalités Célèbres :\nDes personnalités comme [Famous Celebrity 1] et [Famous Celebrity 2] "
        "sont reconnues pour leur engagement envers le bien commun et leur désir de faire une différence, reflétant "
        "les traits du numéro de Chemin de Vie 9.")
    
    }
    
    return interpretations.get(number, ("Interprétation inconnue.",
                                       "Travailler en Équipe : N/A",
                                       "Traits de Personnalité : N/A",
                                       "Points de Vigilance : N/A",
                                       "Chemin de Vie Professionnel : N/A",
                                       "Chemin de Vie Personnel : N/A",
                                       "Chemin de Vie Financier : N/A"))

import streamlit as st


def main():
    st.title("🔮 Calculateur de Chemin de Vie et Numéro du Nom")
    st.write("Choisissez les options de calcul :")

    calculate_life_path = st.checkbox("Calculer le Chemin de Vie", key="calculate_life_path")
    calculate_name = st.checkbox("Calculer le Numéro du Nom", key="calculate_name")
    use_combination = st.checkbox("Utiliser la combinaison de Chemin de Vie et Numéro du Nom", key="use_combination")
    
    if use_combination:
        calculate_life_path = True
        calculate_name = True

    life_path_number = None
    name_number = None
    
    if calculate_life_path:
        birthdate = st.text_input("Entrez votre date de naissance (JJ-MM-AAAA) :")
        if birthdate:
            life_path_number = calculate_life_path_number(birthdate)

    if calculate_name:
        name = st.text_input("Entrez votre nom complet :")
        if name:
            name_number = calculate_name_number(name)

    if st.button("Calculer"):
        if use_combination and life_path_number is not None and name_number is not None:
            combined_number = life_path_number + name_number
            while combined_number > 9:
                combined_number = sum(int(digit) for digit in str(combined_number))
            resulting_number = combined_number
        elif calculate_life_path and life_path_number is not None:
            resulting_number = life_path_number
        elif calculate_name and name_number is not None:
            resulting_number = name_number
        else:
            resulting_number = None
        
        if resulting_number is not None:
            st.write(f"Résultat : {resulting_number}")

        if resulting_number is not None:
            interpretation, team_work, personality, vigilance, prof_life, pers_life, fin_life, numerology_insights, famous_personalities = interpret_life_path_number(resulting_number)

            st.write("Interprétation du Résultat :")
            st.write(f" {team_work}")
            st.write(f" {personality}")
            st.write(f" {vigilance}")
            st.write(f" {prof_life}")
            st.write(f" {pers_life}")
            st.write(f" {fin_life}")
            st.write(f" {numerology_insights}")
            st.write(f" {famous_personalities}")

if __name__ == "__main__":
    main()
