"""
This script converts master CNFs into a bipartite graph, in NetworkX format,
for further graph induction algorithms.
Note that the two are already equivalent, i.e., have a bijection between them.
It writes the resulting NetworkX into [db_file_name].gpickle, which can be
read with graph = pickle.load(open('filename.pickle', 'rb')).

Run `python CNF2networkx.py [db_file.yaml]` in cmd line.
The following packages are needed: `pyyaml`, `networkx`, `boolean.py`.
"""

import sys
import os
import pickle

import yaml
import networkx as nx
from networkx.algorithms.bipartite import is_bipartite
from boolean import BooleanAlgebra, AND, OR, NOT


assert len(sys.argv) == 2, "Usage: python CNF2networkx.py [db_file.yaml]"
filepath = sys.argv[-1]
src_name, src_ext = os.path.splitext(filepath)
assert os.path.exists(filepath) and src_ext == '.yaml', "Invalid db file provided"


# load from db file
try:
    with open(filepath, 'r') as stream:
        loaded = yaml.safe_load(stream)
        CNF = loaded['CNF']
        var2vocab = loaded['VocabMap']
except KeyError as e:
    print("Missing 'CNF' or 'VocabMap' fields in the provided db file.", file=sys.stderr)
    raise e

# add complement to VocabMap
for key, value in list(var2vocab.items()):
    assert type(key) is str and type(value) is str
    var2vocab[f'~{key}'] = value


bool_algebra = BooleanAlgebra()
CNF = bool_algebra.parse(CNF.replace('¬', '~'))
assert type(CNF) is AND

print('Creating Networkx bipartite graph '
      f'with {len(CNF.symbols)} symbols and {len(CNF.args)} clauses')
graph = nx.Graph()
for idx, clause in enumerate(CNF.args):
    assert type(clause) is OR
    clause_name = f'C{idx}'
    graph.add_nodes_from([clause_name], bipartite=0)
    for literal in clause.args:
        vocab = var2vocab[str(literal)]     # str(literal) 
        graph.add_nodes_from([vocab], bipartite=1)
        graph.add_edges_from([(clause_name, vocab)])
assert is_bipartite(graph)

# save graph object to file
pickle.dump(graph, open(f'{src_name}.pickle', 'wb'))
print(f'{len(graph.edges)} edges added. Done and saved.')
