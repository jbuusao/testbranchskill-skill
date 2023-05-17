from mycroft import MycroftSkill, intent_file_handler


class Testbranchskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testbranchskill.intent')
    def handle_testbranchskill(self, message):
        self.speak_dialog('testbranchskill')


def create_skill():
    return Testbranchskill()

