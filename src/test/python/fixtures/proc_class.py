class Processor:
    def __init__(self):
        pass


    def initialize(self):
        return 'initialize'

    def computeTile(self, x, y, array):
        self.spend_some_time()
        return 'computeTile-' + str(x) + ',' + str(y)

    def dispose(self):
        return 'dispose'


    def spend_some_time(self):
        l = list(range(10000))
        for i in range(10000):
            l.reverse()



