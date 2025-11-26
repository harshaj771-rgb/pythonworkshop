class Notification:

    def get_notification(self):
        pass

class Instagram(Notification):

    def get_notification(self):
        print("Notification from Instagram")


class facebook(Notification):

    def get_notification(self):
        print("Notification from Facebook")


Instagram = Instagram()
Instagram.get_notification()
facebook = facebook()
facebook.get_notification()
