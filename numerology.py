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
        1: ("Individualiste, ambitieux(se), et un(e) leader naturel(le). Vous possédez une volonté intrinsèque "
            "de réussir et avez le potentiel de laisser une empreinte durable sur votre chemin choisi. Votre "
            "indépendance et votre détermination vous permettent de surmonter les défis et d'inspirer les autres "
            "à suivre votre exemple.",
            "Travailler en Équipe : En tant que leader naturel, vous avez la capacité de guider et de motiver "
            "les membres de votre équipe. Vous préférez diriger plutôt qu'être dirigé, et votre confiance en "
            "vous peut inspirer les autres à vous suivre.",
            "Traits de Personnalité : Vous êtes ambitieux(se), déterminé(e) et confiant(e). Votre indépendance "
            "peut parfois vous rendre têtu(e), mais cela reflète également votre forte détermination.",
            "Points de Vigilance : Assurez-vous de tenir compte des idées des autres et de ne pas négliger les "
            "avis de votre équipe. Veillez également à équilibrer votre ambition avec des moments de repos et de "
            "réflexion.",
            "Chemin de Vie Professionnel : Votre leadership naturel vous permet d'exceller dans des rôles de "
            "direction. Vous êtes attiré(e) par des postes de leadership où vous pouvez faire valoir vos talents "
            "d'innovation et de prise de décision.",
            "Chemin de Vie Personnel : Votre indépendance vous pousse à chercher des expériences qui vous "
            "permettent de vous démarquer. Vous valorisez votre autonomie et recherchez des opportunités qui vous "
            "permettent de faire une différence significative.",
            "Chemin de Vie Financier : Votre ambition peut se traduire par des gains financiers substantiels. "
            "Cependant, veillez à ne pas vous concentrer uniquement sur l'argent. Investissez dans des opportunités "
            "qui reflètent vos valeurs et vos aspirations personnelles."),
        2: ("Harmonieux(se), coopératif(ve), et diplomate. Votre capacité à comprendre et à ressentir de l'empathie "
            "pour les autres fait de vous un excellent médiateur et collaborateur. Vous excellez dans les "
            "partenariats et cherchez l'équilibre dans tous les aspects de la vie, favorisant ainsi l'unité et la "
            "compréhension.",
            "Travailler en Équipe : Votre nature coopérative en fait un membre précieux de toute équipe. Vous "
            "facilitez la communication entre les membres et trouvez des solutions qui conviennent à tous. Votre "
            "capacité à mettre les gens à l'aise favorise un environnement de travail positif.",
            "Traits de Personnalité : Vous êtes empathique, adaptable et aimable. Votre nature diplomate vous aide "
            "à résoudre les conflits. Cependant, il est important de vous assurer que vos propres besoins sont "
            "également pris en compte.",
            "Points de Vigilance : Méfiez-vous de la tendance à éviter les conflits à tout prix, car cela peut "
            "éventuellement nuire à vos propres intérêts. Assurez-vous également de ne pas vous surcharger en "
            "cherchant constamment l'équilibre.",
            "Chemin de Vie Professionnel : Vous excellez dans des rôles qui nécessitent une collaboration et une "
            "communication efficaces. Vous prospérez dans des environnements où vous pouvez aider à résoudre les "
            "conflits et faciliter les relations harmonieuses.",
            "Chemin de Vie Personnel : Vous recherchez des relations et des expériences qui sont équilibrées et "
            "harmonieuses. Vous êtes attiré(e) par des environnements où vous pouvez contribuer à créer une ambiance "
            "positive.",
            "Chemin de Vie Financier : Vous valorisez la stabilité financière et recherchez des opportunités qui "
            "vous permettent de maintenir l'équilibre dans vos finances. Les investissements axés sur la coopération "
            "et la collaboration peuvent vous convenir."),
        3: ("Créatif(ve), expressif(ve), et sociable. Vos talents artistiques et votre personnalité vibrante attirent "
            "les gens vers vous. Vous possédez le don de la communication efficace et êtes capable d'apporter de la "
            "joie et de l'inspiration à votre entourage.",
            "Travailler en Équipe : Votre nature sociable et communicative en fait un atout précieux pour le travail "
            "d'équipe. Votre capacité à exprimer vos idées de manière créative peut stimuler l'innovation au sein "
            "de l'équipe. Vous aimez également encourager et motiver les autres.",
            "Traits de Personnalité : Vous êtes expressif(ve), charismatique et optimiste. Votre énergie est "
            "contagieuse, mais veillez à ne pas vous laisser emporter par des projets multiples, ce qui pourrait "
            "diviser votre attention.",
            "Points de Vigilance : Évitez de vous disperser dans trop de projets à la fois. Assurez-vous de prendre "
            "du temps pour vous reposer et recharger vos batteries.",
            "Chemin de Vie Professionnel : Vous excellez dans des domaines qui vous permettent de vous exprimer "
            "créativement. Les carrières artistiques, la communication et les médias pourraient vous offrir des "
            "opportunités d'épanouissement.",
            "Chemin de Vie Personnel : Vous cherchez constamment des moyens de vous exprimer et de créer. Vous êtes "
            "attiré(e) par des expériences qui stimulent votre créativité et vous permettent de partager votre "
            "perspective unique.",
            "Chemin de Vie Financier : Vous pouvez tirer parti de vos talents créatifs pour générer des opportunités "
            "financières. Les projets qui vous permettent de mettre en valeur votre expression artistique peuvent "
            "aussi apporter des bénéfices financiers."),
        4: ("Pratique, discipliné(e), et travailleur(e). Votre éthique de travail solide et votre souci du détail "
            "font de vous une personne fiable. Vous excellez dans des environnements structurés et contribuez à la "
            "construction de bases solides et durables.",
            "Travailler en Équipe : Votre approche méthodique est précieuse dans les équipes où la précision et la "
            "rigueur sont essentielles. Vous vous investissez dans les projets à long terme et pouvez être compté(e) "
            "pour respecter les délais et les attentes.",
            "Traits de Personnalité : Vous êtes fiable, organisé(e) et pragmatique. Votre attention aux détails vous "
            "permet d'exceller dans des domaines nécessitant une précision minutieuse.",
            "Points de Vigilance : Évitez de devenir trop rigide ou de vous perdre dans les détails au détriment de "
            "l'innovation. Trouvez un équilibre entre la structure et la flexibilité.",
            "Chemin de Vie Professionnel : Vous êtes attiré(e) par des rôles qui nécessitent une planification "
            "méticuleuse et une exécution précise. Les domaines tels que la gestion de projet, la comptabilité et "
            "la logistique peuvent convenir à vos compétences.",
            "Chemin de Vie Personnel : Vous appréciez l'organisation et la stabilité dans votre vie personnelle. "
            "Vous valorisez les routines qui vous aident à maintenir un équilibre entre le travail et le repos.",
            "Chemin de Vie Financier : Vous avez une approche méthodique pour gérer vos finances. Les stratégies "
            "d'épargne et d'investissement à long terme sont susceptibles de vous convenir."),
        5: ("Aventureux(se), adaptable, et amoureux(se) de la liberté. Votre soif d'expériences vous pousse à explorer "
            "l'inconnu. Votre polyvalence et votre capacité d'adaptation vous permettent de prospérer dans des "
            "situations que d'autres pourraient trouver difficiles.",
            "Travailler en Équipe : Votre nature aventureuse peut apporter un souffle d'air frais à toute équipe. Vous "
            "êtes ouvert(e) aux idées nouvelles et audacieuses, ce qui peut stimuler la créativité de l'équipe. Votre "
            "capacité à vous adapter rapidement est précieuse.",
            "Traits de Personnalité : Vous êtes curieux(se), flexible et indépendant(e). Votre adaptabilité vous permet "
            "de relever efficacement de nouveaux défis et de naviguer dans des environnements en constante évolution.",
            "Points de Vigilance : Assurez-vous de maintenir un niveau d'engagement suffisant dans les projets à long "
            "terme et de ne pas être trop distrait(e) par les opportunités changeantes.",
            "Chemin de Vie Professionnel : Vous êtes attiré(e) par des rôles qui vous permettent de rester "
            "constamment en mouvement. Les carrières liées aux voyages, à la vente ou à l'entrepreneuriat peuvent "
            "répondre à votre désir d'exploration.",
            "Chemin de Vie Personnel : Vous recherchez des expériences qui vous permettent de sortir de votre zone "
            "de confort et d'explorer de nouveaux horizons. Les aventures et les activités stimulantes enrichissent "
            "votre vie personnelle.",
            "Chemin de Vie Financier : Vous êtes disposé(e) à prendre des risques calculés pour générer des gains "
            "financiers. Cependant, assurez-vous d'élaborer des stratégies financières flexibles pour faire face "
            "aux changements."),
        6: ("Nourrissant(e), responsable, et orienté(e) vers la famille. Votre nature compatissante et votre sens du devoir "
            "font de vous un pilier de soutien pour vos proches. Vous trouvez de la satisfaction à créer des "
            "environnements harmonieux et à offrir des conseils à ceux qui en ont besoin.",
            "Travailler en Équipe : Vous êtes le ciment qui maintient l'équipe unie. Votre capacité à écouter et à "
            "nourrir les besoins des membres de l'équipe est inestimable. Vous êtes souvent le médiateur qui résout les "
            "conflits.",
            "Traits de Personnalité : Vous êtes attentionné(e), fiable et dévoué(e). Votre engagement envers le bien-être "
            "des autres est évident dans vos actions. Votre nature maternelle/paternelle se reflète dans vos interactions.",
            "Points de Vigilance : Évitez de devenir surprotecteur(trice) au point d'oublier de prendre soin de vous. "
            "Trouvez un équilibre entre le soutien aux autres et la préservation de votre propre bien-être.",
            "Chemin de Vie Professionnel : Vous prospérez dans des environnements de travail qui vous permettent de "
            "nourrir et de soutenir les autres. Les carrières liées à l'éducation, aux soins de santé et à la conseil "
            "sont susceptibles de répondre à vos aspirations professionnelles.",
            "Chemin de Vie Personnel : Vous accordez une grande importance aux relations familiales et aux amitiés. "
            "Créer des liens solides avec les autres et offrir un soutien émotionnel sont des aspects essentiels de "
            "votre vie personnelle.",
            "Chemin de Vie Financier : Vous êtes prêt(e) à investir dans le bien-être financier de votre famille et "
            "de vos proches. La stabilité financière et la sécurité sont des priorités importantes pour vous."),
        7: ("Intellectuel(le), introspectif(ve), et spirituel(le). Vous possédez une curiosité profonde sur le monde qui "
            "vous entoure et cherchez constamment une compréhension plus profonde. Votre esprit analytique et votre "
            "connexion à la spiritualité vous guident vers la découverte de vérités profondes.",
            "Travailler en Équipe : Votre approche analytique peut apporter une perspective unique à l'équipe. Vous "
            "posez des questions pertinentes et encouragez la réflexion approfondie. Votre désir de comprendre les "
            "aspects cachés des situations est précieux.",
            "Traits de Personnalité : Vous êtes réfléchi(e), intuitif(ve) et philosophique. Votre soif de connaissances "
            "vous pousse à explorer des sujets profonds et complexes.",
            "Points de Vigilance : Veillez à ne pas trop vous perdre dans vos pensées au point de manquer des occasions "
            "pratiques. Équilibrez votre recherche de vérité avec des actions concrètes.",
            "Chemin de Vie Professionnel : Vous êtes attiré(e) par des carrières qui vous permettent de creuser en "
            "profondeur et d'analyser des informations complexes. Les domaines de la recherche, de la philosophie et "
            "du développement personnel vous attirent.",
            "Chemin de Vie Personnel : Votre quête de compréhension et de sens guide vos relations personnelles. Vous "
            "recherchez des connexions profondes et des conversations significatives avec les autres.",
            "Chemin de Vie Financier : Vous préférez investir dans des opportunités qui ont un impact durable et qui "
            "alignent vos valeurs spirituelles. La croissance financière peut être un moyen de soutenir vos objectifs "
            "de recherche de vérité."),
        8: ("Orienté(e) vers la réussite, autoritaire, et matérialiste. Vos compétences en leadership et votre détermination "
            "vous permettent d'atteindre vos objectifs. Vous avez le potentiel d'accumuler des richesses matérielles et "
            "d'exercer de l'influence, bien que le maintien de l'équilibre soit crucial.",
            "Travailler en Équipe : Votre nature directive peut être précieuse pour prendre des décisions éclairées. Vous "
            "avez la capacité de guider l'équipe vers les résultats souhaités, mais assurez-vous d'écouter également les "
            "idées des autres.",
            "Traits de Personnalité : Vous êtes ambitieux(se), déterminé(e) et pragmatique. Votre esprit de décision "
            "peut être inspirant pour les autres, mais veillez à ne pas devenir trop dominateur(trice).",
            "Points de Vigilance : Assurez-vous que votre quête de succès ne vous amène pas à négliger les relations "
            "personnelles et le bien-être émotionnel. Trouvez un équilibre entre le travail et la vie personnelle.",
            "Chemin de Vie Professionnel : Vous êtes attiré(e) par des rôles de leadership qui vous permettent de "
            "gérer des projets ambitieux et de réaliser des gains financiers. Les carrières liées à la gestion "
            "d'entreprise et aux investissements peuvent correspondre à vos aspirations.",
            "Chemin de Vie Personnel : Vous recherchez un mode de vie confortable et avez tendance à valoriser les "
            "possessions matérielles. Vous accordez de l'importance à la sécurité financière pour vous et vos proches.",
            "Chemin de Vie Financier : Vous êtes motivé(e) par la croissance financière et l'accumulation de richesses. "
            "Cependant, veillez à gérer vos finances avec sagesse et à ne pas négliger d'autres domaines de votre vie."),
        9: ("Compatissant(e), idéaliste, et concentré(e) sur l'aide aux autres. Votre nature empathique et votre fort sens de "
            "la justice vous poussent à créer un changement positif dans le monde. Vous avez le potentiel d'inspirer les "
            "autres à œuvrer en vue d'un avenir meilleur.",
            "Travailler en Équipe : Votre engagement envers le bien-être des autres est un atout majeur pour l'équipe. Vous "
            "apportez une perspective humanitaire et inspirez les autres à participer à des initiatives qui ont un impact "
            "positif.",
            "Traits de Personnalité : Vous êtes compatissant(e), idéaliste et altruiste. Votre nature attentionnée vous "
            "pousse à agir pour le bien-être collectif.",
            "Points de Vigilance : Veillez à ne pas vous laisser submerger par les besoins des autres au détriment de "
            "vos propres besoins. Trouvez un équilibre entre l'aide aux autres et la préservation de votre énergie.",
            "Chemin de Vie Professionnel : Vous êtes attiré(e) par des carrières qui vous permettent de faire une "
            "différence significative dans la société. Les domaines liés à l'activisme, aux soins de santé et à "
            "l'éducation sociale peuvent aligner vos aspirations.",
            "Chemin de Vie Personnel : Vous recherchez des relations profondes et significatives qui vous permettent de "
            "contribuer positivement à la vie des autres. Votre vie personnelle est souvent centrée sur des causes "
            "humanitaires.",
            "Chemin de Vie Financier : Vous préférez investir dans des projets qui ont un impact positif sur la société. "
            "La philanthropie et les investissements socialement responsables reflètent vos valeurs financières.")
    
    }
    
    return interpretations.get(number, ("Interprétation inconnue.",
                                       "Travailler en Équipe : N/A",
                                       "Traits de Personnalité : N/A",
                                       "Points de Vigilance : N/A",
                                       "Chemin de Vie Professionnel : N/A",
                                       "Chemin de Vie Personnel : N/A",
                                       "Chemin de Vie Financier : N/A"))

def main():
    st.title("Calculateur de Chemin de Vie et Numéro du Nom")
    st.write("Choisissez les options de calcul :")

    calculate_life_path = st.checkbox("Calculer le Chemin de Vie")
    calculate_name = st.checkbox("Calculer le Numéro du Nom")
    
    use_combination = st.checkbox("Utiliser la combinaison de Chemin de Vie et Numéro du Nom")
    
    if calculate_life_path:
        birthdate = st.text_input("Entrez votre date de naissance (JJ-MM-AAAA) :")
    
    if calculate_name:
        name = st.text_input("Entrez votre nom complet :")
    
    if st.button("Calculer"):
        if calculate_life_path:
            life_path_number = calculate_life_path_number(birthdate)
            interpretation, team_work, personality, vigilance, prof_life, pers_life, fin_life = interpret_life_path_number(life_path_number)
            st.write(f"Votre Chemin de Vie est : {life_path_number}")
            st.write(f"Interprétation détaillée (Chemin de Vie) : {interpretation}")
            st.write(f"Travailler en Équipe : {team_work}")
            st.write(f"Traits de Personnalité : {personality}")
            st.write(f"Points de Vigilance : {vigilance}")
            st.write(f"Chemin de Vie Professionnel : {prof_life}")
            st.write(f"Chemin de Vie Personnel : {pers_life}")
            st.write(f"Chemin de Vie Financier : {fin_life}")
        
        if calculate_name:
            name_number = calculate_name_number(name)
            interpretation, team_work, personality, vigilance, prof_life, pers_life, fin_life = interpret_life_path_number(name_number)
            st.write(f"Votre Numéro du Nom est : {name_number}")
            st.write(f"Interprétation détaillée (Numéro du Nom) : {interpretation}")
            st.write(f"Travailler en Équipe : {team_work}")
            st.write(f"Traits de Personnalité : {personality}")
            st.write(f"Points de Vigilance : {vigilance}")
            st.write(f"Chemin de Vie Professionnel : {prof_life}")
            st.write(f"Chemin de Vie Personnel : {pers_life}")
            st.write(f"Chemin de Vie Financier : {fin_life}")
        
        if use_combination:
            combined_number = life_path_number + name_number
            while combined_number > 9:
                combined_number = sum(int(digit) for digit in str(combined_number))
            interpretation, team_work, personality, vigilance, prof_life, pers_life, fin_life = interpret_life_path_number(combined_number)
            st.write(f"Interprétation détaillée (Chemin de Vie + Numéro du Nom) : {interpretation}")
            st.write(f"Travailler en Équipe : {team_work}")
            st.write(f"Traits de Personnalité : {personality}")
            st.write(f"Points de Vigilance : {vigilance}")
            st.write(f"Chemin de Vie Professionnel : {prof_life}")
            st.write(f"Chemin de Vie Personnel : {pers_life}")
            st.write(f"Chemin de Vie Financier : {fin_life}")

if __name__ == "__main__":
    main()