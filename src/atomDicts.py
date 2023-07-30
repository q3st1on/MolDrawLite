import json
import os

class Atom:
    def __init__(self, atomVals):
        self.name = atomVals['name']
        self.symbol = atomVals['symbol']
        self.pos = atomVals['pos']
        self.num = atomVals['anum']
        self.mass = atomVals['ram']
    
    def setColour(self, colour):
        self.colour=colour
    

class PeriodicTableClass:
    def __init__(self):
        self._dir = os.path.dirname(os.path.realpath(__file__))
        self._table = {}
        with open(self._dir+'/table.json', 'r') as f:
            tbl = json.loads(f.read())
            for i in tbl:
                self._table[i] = Atom(tbl[str(i)])

        with open(self._dir+'/colourcfg.json', 'r') as f:
            colours = json.loads(f.read())
            for i in colours:
                if i != 'equation':
                    self._table[i].setColour(colours[str(i)])
                else:
                    self.equationCol = colours[str(i)]
    
    def writeTable(self):
        with open(self._dir+'/table.json', 'w') as f:
            f.write(json.dumps(self._table))

    def writeColours(self):
        cols = {"equation": self.equationCol}
        for i in self._table:
            cols[i] = self._table[i].colour

        with open(self._dir+'/colourcfg.json', 'w') as f:
            f.write(json.dumps(cols))

    def atomNo(self, anum):
        return self._table[str(anum)]
    
    def __iter__(self):
        for i in self._table.values():
            yield i


PeriodicTable = PeriodicTableClass()