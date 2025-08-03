# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata


from datetime import datetime

class URLStore:
    def __init__(self):
        self.urls = {}  # short_code -> data

    def add_url(self, code, original_url):
        self.urls[code] = {
            "original_url": original_url,
            "clicks": 0,
            "created_at": datetime.utcnow()
        }

    def get_url(self, code):
        return self.urls.get(code, {}).get("original_url")

    def increment_click(self, code):
        if code in self.urls:
            self.urls[code]["clicks"] += 1

    def get_metadata(self, code):
        return self.urls.get(code)

url_store = URLStore()
