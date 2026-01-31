"""
User Personalization Memory
---------------------------
This program demonstrates how
AI systems store user preferences
and personalize responses.

Author: AI Course
"""

class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {}

    def update_preference(self, key, value):
        self.preferences[key] = value

    def get_preference(self, key, default=None):
        return self.preferences.get(key, default)


class PersonalizedAssistant:
    def __init__(self):
        self.user_profiles = {}

    def get_profile(self, user_id):
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = UserProfile(user_id)
        return self.user_profiles[user_id]

    def respond(self, user_id, message):
        profile = self.get_profile(user_id)

        # Learn preferences
        if "python" in message.lower():
            profile.update_preference("language", "Python")
        if "short" in message.lower():
            profile.update_preference("response_style", "concise")

        # Personalize response
        language = profile.get_preference("language", "general programming")
        style = profile.get_preference("response_style", "detailed")

        response = (
            f"I'll tailor responses for {language}. "
            f"My style will be {style}."
        )
        return response


def main():
    print("USER PERSONALIZATION MEMORY")
    print("----------------------------")

    assistant = PersonalizedAssistant()

    user_id = "user_123"

    messages = [
        "I like Python examples",
        "Keep responses short",
        "Explain AI"
    ]

    for msg in messages:
        print("\nUser:", msg)
        reply = assistant.respond(user_id, msg)
        print("Assistant:", reply)


if __name__ == "__main__":
    main()
