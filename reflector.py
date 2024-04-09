class Reflector:
    def __init__(self, swaps) -> None:
        self.swaps = swaps
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, signal):
        letter = self.swaps[signal]
        signal = self.alpha.find(letter)
        return signal

    def returnReflector(self):
        return self.swaps
