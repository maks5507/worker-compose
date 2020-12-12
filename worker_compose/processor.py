#
# Created by maks5507 (me@maksimeremeev.com)
#


class Processor:
    def __init__(self, instance):
        self.instance = instance

    def run(self, chunk, **kwargs):
        for path in chunk:
            self.instance.run(path, **kwargs)
