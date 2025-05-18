class gfg:
    def __init__(self,topic):
        self._topic = topic

    def topic(self):
        print('Topic',self._topic)

ins = gfg('Python')

ins.topic()