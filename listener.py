from Python.CSharpParserListener import CSharpParserListener

class FeatureExtractorListener(CSharpParserListener):

    def __init__(self):
        self.node_count = {}
        self.max_depth = 0
        self.current_depth = 0
        self.total_nodes = 0
        self.total_children = 0
        self.variables = 0
        self.methods = 0
        self.classes = 0
        self.variable_names = set()
        self.method_names = set()
        self.class_names = set()
        self.distinct_tokens = {}
        self.control_structures = 0

    def enterEveryRule(self, ctx):
        node_type = type(ctx).__name__
        self.node_count[node_type] = self.node_count.get(node_type, 0) + 1
        self.current_depth += 1
        self.total_nodes += 1
        self.total_children += ctx.getChildCount()

        if self.current_depth > self.max_depth:
            self.max_depth = self.current_depth

        # identificar diferentes tipos de nodos:
        if node_type == "Local_variable_declaratorContext":
            self.variables += 1
            # if hasattr(ctx.children, 'IdentifierContext'):
            self.variable_names.add(ctx.start.text)
        
        elif node_type == "Method_declarationContext":  
            self.methods += 1
            # if hasattr(ctx, 'IdentifierContext'):
            self.method_names.add(ctx.start.text)
                
        elif node_type == "Class_definitionContext":  # Ajusta según tu gramática
            self.classes += 1
            node = ctx.children[1]
            if type(ctx.children[1]).__name__ == 'IdentifierContext':
                self.class_names.add(node.start.text)
                
        elif node_type in ["IfStatementContext", "SwitchStatementContext", 
                           "ForStatementContext", "WhileStatementContext", 
                           "DoWhileStatementContext"]:  # Ajusta según tu gramática
            self.control_structures += 1

        # Captura de tokens distintos y su conteo
        if hasattr(ctx, 'start'):
            token_text = ctx.start.text
            self.distinct_tokens[token_text] = self.distinct_tokens.get(token_text, 0) + 1

    def exitEveryRule(self, ctx):
        self.current_depth -= 1

    def get_features(self):
        average_children = self.total_children / self.total_nodes if self.total_nodes > 0 else 0
        return {
            "node_count": self.node_count,
            "max_depth": self.max_depth,
            "number_of_variables": self.variables,
            "number_of_methods": self.methods,
            "number_of_classes": self.classes,
            "variable_names": list(self.variable_names),
            "method_names": list(self.method_names),
            "class_names": list(self.class_names),
            "average_children_per_node": average_children,
            "distinct_tokens_count": self.distinct_tokens,
            "control_structures_count": self.control_structures
        }

def walk_tree(listener, node):
    if not node:
        return

    # Llamar al método de entrada del listener
    listener.enterEveryRule(node)

    # Recorrer todos los hijos del nodo actual
    for i in range(node.getChildCount()):
        child = node.getChild(i)
        # if isinstance(child, ParserRuleContext):
        walk_tree(listener, child)

    # Llamar al método de salida del listener
    listener.exitEveryRule(node)
