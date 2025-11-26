class Mobile:
    def __init__(self):
        pass

    def callings(self):
        print('invoking calling function')

    def sms(self):
        print('invoking sms method')

    def game(self):
        print('invoking game ')


class MI_note_8_pro(Mobile):

    def cam(self):
        print('invoking cam method')

    def music(self):
        print('invoking music method')

    def video_call(self):
        print('invoking video call method')

minote_8_pro = MI_note_8_pro()
minote_8_pro.music()