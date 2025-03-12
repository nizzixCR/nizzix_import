from tempmail import EMail

class temp_1secmail:
    def __init__(self):
        """
        Initialise une adresse e-mail temporaire et prépare l'objet.
        """
        self._email = EMail()
        self.address = self._email.address

    def __str__(self):
        """
        Représentation textuelle de l'objet temp_1secmail.
        """
        return f"Temporary Email: {self.address}"

    def check_inbox(self):
        """
        Récupère tous les e-mails présents dans la boîte de réception.
        
        :return: Liste des e-mails sous forme de tuples (sujet, contenu).
        """
        inbox = self._email.get_inbox()
        return [(msg.subject, msg.message) for msg in inbox]

    def get_inbox_summary(self):
        """
        Récupère un résumé des e-mails avec sujet, expéditeur et date.
        
        :return: Liste des tuples (sujet, expéditeur, date).
        """
        inbox = self._email.get_inbox()
        return [(msg.subject, msg.from_addr, msg.date) for msg in inbox]

    def delete_all_emails(self):
        """
        Supprime tous les e-mails de la boîte de réception.
        
        :return: Nombre d'e-mails supprimés.
        """
        inbox = self._email.get_inbox()
        count = 0
        for msg in inbox:
            self._email.delete_message(msg.id)
            count += 1
        return count

    def wait_for_email_with_subject(self, subject, timeout=300):
        """
        Attend un e-mail avec un sujet spécifique.
        
        :param subject: Sujet recherché.
        :param timeout: Temps maximal d'attente en secondes.
        :return: L'e-mail correspondant ou None si timeout.
        """
        def subject_filter(msg):
            return msg.subject == subject

        return self._email.wait_for_message(filter=subject_filter, timeout=timeout)

    def get_emails_from_domain(self, domain):
        """
        Filtre et retourne les e-mails provenant d'un domaine spécifique.
        
        :param domain: Nom de domaine recherché (ex: "example.com").
        :return: Liste des e-mails sous forme de tuples (sujet, contenu).
        """
        inbox = self._email.get_inbox()
        return [(msg.subject, msg.message) for msg in inbox if domain in msg.from_addr]

    def wait_for_specific_email(self, filter_func=None, timeout=300):
        """
        Attend un e-mail correspondant à un filtre personnalisé.
        
        :param filter_func: Fonction de filtre prenant un message en paramètre. (Optionnel)
        :param timeout: Temps maximal d'attente en secondes.
        :return: Le message correspondant ou None si timeout.
        """
        return self._email.wait_for_message(filter=filter_func, timeout=timeout)

    def get_email_by_id(self, email_id):
        """
        Récupère un e-mail spécifique en fonction de son ID.
        
        :param email_id: ID unique de l'e-mail.
        :return: Contenu de l'e-mail sous forme de tuple (sujet, contenu).
        """
        msg = self._email.get_message(email_id)
        return (msg.subject, msg.message) if msg else None

    def count_emails(self):
        """
        Compte le nombre d'e-mails actuellement dans la boîte de réception.
        
        :return: Nombre total d'e-mails.
        """
        return len(self._email.get_inbox())

    def search_email_by_keyword(self, keyword):
        """
        Recherche les e-mails contenant un mot-clé dans le sujet ou le contenu.
        
        :param keyword: Mot-clé à rechercher.
        :return: Liste des e-mails correspondants sous forme de tuples (sujet, contenu).
        """
        inbox = self._email.get_inbox()
        return [
            (msg.subject, msg.message)
            for msg in inbox
            if keyword.lower() in msg.subject.lower() or keyword.lower() in msg.message.lower()
        ]

    def get_latest_email(self):
        """
        Récupère le dernier e-mail reçu dans la boîte de réception.
        
        :return: Tuple (sujet, contenu) du dernier e-mail ou None si la boîte est vide.
        """
        inbox = self._email.get_inbox()
        if inbox:
            latest_msg = inbox[0]
            return (latest_msg.subject, latest_msg.message)
        return None

    def get_sender_emails(self):
        """
        Récupère une liste des expéditeurs uniques des e-mails reçus.
        
        :return: Liste des adresses e-mail des expéditeurs.
        """
        inbox = self._email.get_inbox()
        return list(set(msg.from_addr for msg in inbox))

    def delete_email_by_subject(self, subject):
        """
        Supprime tous les e-mails avec un sujet donné.
        
        :param subject: Sujet des e-mails à supprimer.
        :return: Nombre d'e-mails supprimés.
        """
        inbox = self._email.get_inbox()
        count = 0
        for msg in inbox:
            if msg.subject == subject:
                self._email.delete_message(msg.id)
                count += 1
        return count