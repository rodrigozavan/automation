class Proppertys:
    def __init__(self):
        self._url = None
        self._user = None
        self._password = None
        self._type_bot = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, new_url):
        self._url = new_url

    @property
    def type_bot(self):
        return self._type_bot

    @type_bot.setter
    def type_bot(self, new_type_bot):
        self._type_bot = new_type_bot

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, new_user):
        self._user = new_user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password
