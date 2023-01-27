from matplotlib import pyplot


class GraphCreator:
    def __init__(self):
        self.creator = pyplot

    def create_graph(self, data_x: list, data_y: list):
        self.creator.figure(figsize=(12, 6))
        self.creator.plot([x.replace(' ', '\n') for x in data_x], data_y)
        self.creator.savefig('temp.png')
