import torch
from torch.nn import functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv
from torch.optim import Adam
from antlr4 import *
from antlr4 import CommonTokenStream
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser
import os
from collections import deque, defaultdict
import gensim.downloader as api

# Cargar el modelo preentrenado de GloVe
glove_model = api.load("glove-wiki-gigaword-50")

# Guardar el modelo en el disco
glove_model.save("glove-wiki-gigaword-50.model")

# Step 2: Define the GCN model
class GCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x

def create_graph_from_antlr(ctx):
    # Initialize lists for node features and edges
    node_features = []
    edges = []
    node_type_to_index = {}

    # Function to recursively traverse the AST
    def traverse(ctx, parent_idx=None):
        nonlocal node_features, edges

        # Add current node feature
        node_features.append(type(ctx).__name__)

        # Add edges from parent to children
        if parent_idx is not None:
            edges.append((parent_idx, len(node_features) - 1))

        # Recursively traverse children
        current_idx = len(node_features) - 1
        
        if type(ctx).__name__ == 'TerminalNodeImpl':
            return
        
        for child in ctx.children:
            traverse(child, parent_idx=current_idx)

    # Start traversal from the root context
    traverse(ctx)

    # Convert node features to tensor
    x = torch.tensor([[f] for f in node_features], dtype=torch.float32)

    # Convert edges to torch LongTensor (edge_index)
    edge_index = torch.tensor(list(zip(*edges)), dtype=torch.long)

    # Create a PyTorch Geometric Data object
    data = Data(x=x, edge_index=edge_index)

    return data

def main(input_code):
    input_stream = InputStream(input_code)
    lexer = CSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)
    tree = parser.compilation_unit()  # Cambia 'startRule' por la regla inicial de tu gramática
    
    return create_graph_from_antlr(tree)

if __name__ == "__main__":
    json_file_path = f'{os.getcwd()}/Projects/All/Ab3lucho_Moogle/Moogle-main/MoogleEngine/Query.cs'

    with open(json_file_path, 'r') as file:
        code = file.read()
        
    out = main(code)
    print(out)