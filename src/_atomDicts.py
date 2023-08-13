from typing import Union, Iterator
import json
import os

class Atom: # Atom class, one exists for all atom like objects (including R sub 'Atom')
    def __init__(self, atomVals: dict[str, Union[int, str, float, list[int]]]) -> None:
        self.name = atomVals['name']
        self.symbol = atomVals['symbol']
        self.pos = atomVals['pos']
        self.num = atomVals['anum']
        self.mass = atomVals['ram']
    
    def setColour(self, colour: str) -> None:
        self.colour=colour
    

class PeriodicTableClass: # Main periodic table class, self explanatory
    def __init__(self) -> None:
        self._dir = os.path.dirname(os.path.realpath(__file__))
        self._table = {}
        with open(self._dir+'/table.json', 'r') as f: # loads data config
            tbl = json.loads(f.read())
            for i in tbl:
                self._table[i] = Atom(tbl[str(i)])

        with open(self._dir+'/colourcfg.json', 'r') as f: # Loads colour config
            colours = json.loads(f.read())
            for i in colours:
                if i != 'equation':
                    self._table[i].setColour(colours[str(i)])
                else:
                    self.equationCol = colours[str(i)]
    
    def writeTable(self) -> None: # writes updated data config
        with open(self._dir+'/table.json', 'w') as f:
            f.write(json.dumps(self._table))

    def writeColours(self) -> None: # writes updated colour config
        cols = {"equation": self.equationCol}
        for i in self._table:
            cols[i] = self._table[i].colour

        with open(self._dir+'/colourcfg.json', 'w') as f:
            f.write(json.dumps(cols))

    def atomNo(self, anum: Union[int, str]) -> Atom: # returns Atom instance for a given element number
        return self._table[str(anum)]
    
    def __iter__(self) -> Iterator[str]: # extends __iter__ methods such as list() to Periodic Table
        for i in self._table.values():
            yield i