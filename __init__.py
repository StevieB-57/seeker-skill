from mycroft import MycroftSkill, intent_file_handler


class Seeker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('seeker.intent')
    def handle_seeker(self, message):
        self.speak_dialog('seeker')


def create_skill():
    return Seeker()

