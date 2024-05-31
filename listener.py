from Python.CSharpParserListener import CSharpParserListener

class FeatureExtractorListener(CSharpParserListener):

    def __init__(self):
        self.max_depth = 0
        self.current_depth = 0
        self.total_nodes = 0
        self.node_count = {}
        
        self.variables = 0
        self.constants = 0
        self.out_variables = 0
        
        self.methods = 0
        self.classes = 0
        self.interfaces = 0
        self.abstract_classes = 0
        self.sealed_classes = 0
        self.import_statements = 0
        self.nested_classes = 0
        self.exceptions_handled = 0
        self.method_lengths = []
        self.function_calls = 0

        self.variable_names = set()
        self.method_names = set()
        self.class_names = set()
        self.interface_names = set()
        self.distinct_tokens = {}
        self.control_structures = {
            'if': 0,
            'switch': 0,
            'for': 0,
            'while': 0,
            'dowhile': 0
        }
        self.access_modifiers_methods = {
            'public': 0,
            'private': 0,
            'protected': 0,
            'internal': 0,
            'protected internal': 0,
            'private protected': 0,
            'static': 0
        }
        self.other_modifiers = {
            'readonly': 0,
            'volatile': 0,
            'virtual': 0,
            'override': 0,
            'new': 0, 
            'partial': 0,
            'extern': 0,
            'unsafe': 0,
            'async': 0
        }
        
        self.method_return_types = {}
        self.method_parameters = {}

    def enterEveryRule(self, ctx):
        node_type = type(ctx).__name__
        self.node_count[node_type] = self.node_count.get(node_type, 0) + 1
        self.current_depth += 1
        self.total_nodes += 1
        
        try:
            if ctx.start.text == "partial":
                pass
        except:
            pass
        
        if self.current_depth > self.max_depth:
            self.max_depth = self.current_depth

        # identificar diferentes tipos de nodos:
        if node_type == "Local_variable_declaratorContext":
            self.variables += 1
            self.variable_names.add(ctx.start.text)
        
        elif node_type == "Method_declarationContext": 
            self.methods += 1
            self.method_names.add(ctx.start.text)
            start_line = ctx.start.line
            stop_line = ctx.stop.line
            self.method_lengths.append(stop_line - start_line + 1)
            
            return_type = ctx.parentCtx.start.text
            self.method_return_types[ctx.start.text] = return_type
            
            # Obtener parámetros del método
            param_count = 0
            param_info = []
            
            if(type(ctx.children[2]).__name__ == "Formal_parameter_listContext"):
                for param in ctx.children[2].children[0].fixed_parameter() :
                    param_type = param.children[0].children[0].getText()
                    param_name = param.children[0].children[1].getText()
                    param_info.append((param_type, param_name))
                    param_count += 1
                self.method_parameters[ctx.start.text] = {"count": param_count, "params": param_info}
            
        elif node_type == "Interface_definitionContext":
            self.interfaces += 1
            self.interface_names.add(ctx.children[1].start.text)
                
        elif node_type == "Class_definitionContext": 
            self.classes += 1
            node = ctx.children[1]
            if type(ctx.children[1]).__name__ == 'IdentifierContext':
                self.class_names.add(node.start.text)
            if ctx.parentCtx.start.text == 'abstract':
                self.abstract_classes += 1
            if ctx.parentCtx.start.text == 'sealed':
                self.sealed_classes += 1
            
        elif node_type == "TryStatementContext":
            self.exceptions_handled += 1
        
        elif node_type == "ObjectCreationExpressionContext":
            self.function_calls += 1
            
        elif node_type == "Using_directivesContext":
            self.import_statements += 1
        
        elif node_type == "IfStatementContext":
            self.control_structures['if'] += 1

        elif node_type == "SwitchStatementContext":
            self.control_structures['switch'] += 1
            
        elif node_type == "ForStatementContext":
            self.control_structures['for'] += 1
        
        elif node_type == "WhileStatementContext":
            self.control_structures['while'] += 1
        
        elif node_type == "DoWhileStatementContext":
            self.control_structures['dowhile'] += 1
            
        elif node_type == "Local_variable_initializerContext":
            self.other_modifiers[ctx.start.text] += 1
            
        elif node_type == "Constant_declarationContext":
            self.constants += 1
        
        elif node_type == "All_member_modifierContext":
            modifier = ctx.start.text
            if modifier in self.other_modifiers:
                self.other_modifiers[modifier] += 1
            if modifier in self.access_modifiers_methods:
                self.access_modifiers_methods[modifier] += 1
            
        # Captura de tokens distintos y su conteo
        if hasattr(ctx, 'symbol'):
            token_text = ctx.symbol.text
            self.distinct_tokens[token_text] = self.distinct_tokens.get(token_text, 0) + 1

    def exitEveryRule(self, ctx):
        self.current_depth -= 1
    
    def get_features(self):
        return {
            "total_nodes": self.total_nodes,
            "node_count": self.node_count,
            "max_depth": self.max_depth,
            "number_of_variables": self.variables,
            "number_of_constants": self.constants,
            "number_of_methods": self.methods,
            "number_of_classes": self.classes,
            "number_of_abstract_classes": self.abstract_classes,
            "number_of_sealed_classes": self.sealed_classes,
            "number_of_interfaces": self.interfaces,
            "import_statements": self.import_statements,
            "exceptions_handled": self.exceptions_handled,
            "function_calls": self.function_calls,
            "variable_names": list(self.variable_names),
            "method_names": list(self.method_names),
            "class_names": list(self.class_names),
            "interface_names": list(self.interface_names),
            "distinct_tokens_count": self.distinct_tokens,
            "control_structures_count": self.control_structures,
            "method_return_types": self.method_return_types,
            "method_parameters": self.method_parameters,
            "access_modifiers_methods_count": self.access_modifiers_methods,
            "other_modifiers_count": self.other_modifiers,
            "out_variables": self.out_variables,
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
