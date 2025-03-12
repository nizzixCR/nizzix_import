import cloudscraper

class TempMail:
    def __init__(self, proxies=None):
        self.mailbox_url = "https://web2.temp-mail.org/mailbox"
        self.messages_url = "https://web2.temp-mail.org/messages"
        self.proxies = proxies if proxies else []
        self.token = None
        self.new_mailbox = None
        self.scraper = cloudscraper.create_scraper()

    def get_new_email(self):
        response = self.scraper.post(self.mailbox_url)
        response_data = response.json()
        self.token = response_data.get("token")
        self.new_mailbox = response_data.get("mailbox")

        if not self.token or not self.new_mailbox:
            for proxy in self.proxies:
                try:
                    self.scraper = cloudscraper.create_scraper()
                    response = self.scraper.post(self.mailbox_url, proxies={'http': proxy, 'https': proxy}, timeout=5)
                    response_data = response.json()
                    self.token = response_data.get("token")
                    self.new_mailbox = response_data.get("mailbox")
                    if self.token and self.new_mailbox:
                        break
                except Exception as e:
                    print(f"Proxy {proxy} failed: {e}")

        return self.new_mailbox

    def get_mails(self):
        if not self.token:
            print("No token available, please get a new email first.")
            return []

        headers = {"Authorization": f"Bearer {self.token}"}
        messages_response = self.scraper.get(self.messages_url, headers=headers)
        messages_data = messages_response.json()
        return messages_data

    def __str__(self):
        return f"Email: {self.new_mailbox}, Token: {self.token}"