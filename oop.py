import datetime


class user:
    def __init__(self, name):
        self.__name = name
        self.__is_logged_in = False
        self.__last_logged_in = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def is_logged_in(self):
        return self.__is_logged_in

    @property
    def last_logged_in_at(self):
        return self.__last_logged_in

    def log_in(self):
        self.__is_logged_in = True
        self.__last_logged_in = datetime.datetime.now()

    def log_out(self):
        self.__is_logged_in = False

    def can_edit(self, comment):
        if comment.author.name == self.name:
            return True
        else:
            return False

    def can_delete(self, comment):
        return False

    def to_string(self):
        return self.__name


class moderator(user):
    def __init__(self, name):
        user.__init__(self, name)

    def can_delete(self, comment):
        return True


class admin(moderator):
    def __init__(self, name):
        moderator.__init__(self, name)

    def can_edit(self, comment):
        return True

    def can_delete(self, comment):
        return True


class comment:
    def __init__(self, author, message, replied_to=None):
        self.__author = author
        self.__message = message
        self.__replied_to = replied_to
        self.__created_at = datetime.datetime.now()

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def created_at(self):
        return self.__created_at

    @property
    def replied_to(self):
        return self.__replied_to

    @replied_to.setter
    def replied_to(self, value):
        self.__replied_to = value

    def to_string(self):
        comment_string = "{} by {}".format(
            self.__message,
            self.author.to_string()
        )
        if self.__replied_to:
            comment_string = "{} (replied to {})".format(
            comment_string,
            self.__replied_to.author.to_string()
        )

        return comment_string