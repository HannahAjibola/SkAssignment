class Tv:
    def __init__(self):
        self._tvIsOn = False
        self.max_volume = 100
        self.min_volume = 0

    def is_on(self):
        self._tvIsOn = True

    def is_off(self):
        self._tvIsOn = False

    def increase_volume(self, volume):
        if volume != 0:
            

