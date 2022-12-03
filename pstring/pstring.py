class PString:
    def __init__(self, first_arg, *args):
        self.string = str(first_arg)
        for arg in args:
            self.string += " " + str(arg)

        self.string += "\033[0m"

    def __repr__(self):
        return self.string

    def __add__(self, other):
        return PString(self.string + other.string)

    def print(self, **kwargs):
        """Print string"""
        print(self.string, **kwargs)

    def r(self):
        """Make string red"""
        self.string = "\033[31m" + self.string
        return self

    def g(self):
        """Make string green"""
        self.string = "\033[32m" + self.string
        return self

    def y(self):
        """Make string yellow"""
        self.string = "\033[33m" + self.string
        return self

    def b(self):
        """Make string blue"""
        self.string = "\033[34m" + self.string
        return self

    def w(self):
        """Make string white"""
        self.string = "\033[37m" + self.string
        return self

    def bg_r(self):
        """Make string background red"""
        self.string = "\033[41m" + self.string
        return self

    def bg_g(self):
        """Make string background green"""
        self.string = "\033[42m" + self.string
        return self

    def bg_y(self):
        """Make string background yellow"""
        self.string = "\033[43m" + self.string
        return self

    def bg_b(self):
        """Make string background blue"""
        self.string = "\033[44m" + self.string
        return self

    def bg_w(self):
        """Make string background white"""
        self.string = "\033[47m" + self.string
        return self

    def bold(self):
        """Make string bold"""
        self.string = "\033[1m" + self.string
        return self

    def italic(self):
        """Make string italic"""
        self.string = "\033[3m" + self.string
        return self

    def underline(self):
        """Make string underlined"""
        self.string = "\033[4m" + self.string
        return self




