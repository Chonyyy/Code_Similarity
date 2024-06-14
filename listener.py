from Python.CSharpParserListener import CSharpParserListener

class FeatureExtractorListener(CSharpParserListener):

    def __init__(self):
        self.total_nodes = 0
        self.node_count = {}
        self.max_depth = 0
        self.current_depth = 0
        
        self.variables = 0
        self.constants = 0
        self.out_variables = 0
        
        self.methods = 0
        self.classes = 0
        self.interfaces = 0
        self.abstract_classes = 0
        self.sealed_classes = 0
        self.import_statements = 0
        self.function_calls = 0
        self.try_catch_blocks = 0
        self.lists = 0
        self.dicts = 0
        self.enums = 0
        self.delegates = 0

        self.variable_names = set()
        self.method_names = set()
        self.method_lengths = []
        self.class_names = set()
        self.interface_names = set()
        self.enum_names = set()
        self.delegate_names = set()
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
        self.library_calls = {
            "Console": 0,
            "Math": 0
            # "List": 0,
            # "Dictionary": 0
        }
        self.linq_queries = {
            "Select": 0,
            "Where": 0,
            "OrderBy": 0,
            "GroupBy": 0,
            "Join": 0,
            "Sum": 0,
            "Count": 0
        }
        
        self.method_return_types = {}
        self.method_parameters = {}
        
        self.number_of_lambdas = 0
        self.number_of_getters_setters = {'get': 0, 'set': 0}
        self.number_of_tuples = 0
        self.number_of_namespaces = 0

    def enterEveryRule(self, ctx):
        node_type = type(ctx).__name__
        self.node_count[node_type] = self.node_count.get(node_type, 0) + 1
        self.current_depth += 1
        self.total_nodes += 1
        
        try:
            if ctx.start.text == "namespace":
                pass
            if ctx.start.text == "lambda":
                pass
        except:
            pass
         
        if self.current_depth > self.max_depth:
            self.max_depth = self.current_depth

        # identificar diferentes tipos de nodos:
        if node_type == "Local_variable_declarationContext":
            var_type = ctx.children[0].start.text
            var_name = ctx.children[1].start.text
            self.variables += 1
            self.variable_names.add((var_type, var_name))
            
            if var_type == "Tuple":
                self.number_of_tuples += 1
            if var_type == "List":
                self.lists += 1
            if var_type == "Dictionary":
                self.dicts += 1
         
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

                if ctx.children[2].parameter_array():
                    param = ctx.children[2].parameter_array()
                    param_type = param.children[1].start.text
                    param_name = param.children[2].start.text
                    param_info.append((param_type, param_name))
                    param_count += 1
                    
                if ctx.children[2] .fixed_parameter():
                    for param in ctx.children[2].children[0].fixed_parameter() :
                        if param.children[0].children[0].getText() == "out":
                            self.out_variables += 1
                            param_type = param.children[1].children[0].getText()
                            param_name = param.children[1].children[1].getText()
                        else:
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
            self.try_catch_blocks += 1
        
        elif node_type == "ObjectCreationExpressionContext":
            self.function_calls += 1 #Revisar esto
            
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
            modif = ctx.start.text
            if modif in self.other_modifiers:
                self.other_modifiers[modif] += 1
            
        elif node_type == "Constant_declarationContext":
            self.constants += 1
        
        elif node_type == "Enum_definitionContext":
            self.enums += 1
            self.enum_names.add(ctx.children[1].start.text)
            
        elif node_type == "Delegate_definitionContext":
            self.delegates += 1
            name = ctx.start.text
            return_type = ctx.children[1].start.text
            self.delegate_names.add((name, return_type))
        
        elif node_type == "All_member_modifierContext":
            modifier = ctx.start.text
            if modifier in self.other_modifiers:
                self.other_modifiers[modifier] += 1
            if modifier in self.access_modifiers_methods:
                self.access_modifiers_methods[modifier] += 1
        
        elif node_type == "Method_invocationContext":
            method_name = ctx.parentCtx.start.text
            if method_name in self.library_calls:
                self.library_calls[method_name] += 1 
        
        if node_type == "Lambda_expressionContext":
            self.number_of_lambdas += 1

        if node_type == "Accessor_declarationsContext":
            accessor_type = ctx.children[0].getText()
            if accessor_type == "get":
                self.number_of_getters_setters['get'] += 1
            elif accessor_type == "set":
                self.number_of_getters_setters['set'] += 1
        
        if node_type == "Set_accessor_declarationContext":
            self.number_of_getters_setters['set'] += 1

        if node_type == "Namespace_declarationContext":
            self.number_of_namespaces += 1
        
        elif node_type == "IdentifierContext":
            name = ctx.start.text
            if name in self.linq_queries:
                self.linq_queries[name] += 1
             
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
            "out_variables": self.out_variables,
            "number_of_methods": self.methods,
            "number_of_classes": self.classes,
            "number_of_interfaces": self.interfaces,
            "number_of_abstract_classes": self.abstract_classes,
            "number_of_sealed_classes": self.sealed_classes,
            "import_statements": self.import_statements,
            "number_of_try_blocks": self.try_catch_blocks,
            "number_of_lists": self.lists,
            "number_of_dictionaries": self.dicts,
            "number_of_enums": self.enums,
            "number_of_delegates": self.delegates,
            "function_calls": self.function_calls,
            "variable_names": list(self.variable_names),
            "method_names": list(self.method_names),
            "method_lengths": self.method_lengths,
            "class_names": list(self.class_names),
            "interface_names": list(self.interface_names),
            "delegate_names": list(self.delegate_names),
            "enums_names":list(self.enum_names),
            "distinct_tokens_count": self.distinct_tokens,
            "control_structures_count": self.control_structures,
            "access_modifiers_methods_count": self.access_modifiers_methods,
            "other_modifiers_count": self.other_modifiers,
            "method_return_types": self.method_return_types,
            "method_parameters": self.method_parameters,
            "out_variables": self.out_variables,
            "linq_queries": self.linq_queries,
            "library_calls": self.library_calls,
            "number_of_lambdas": self.number_of_lambdas,
            "number_of_getters_setters": self.number_of_getters_setters,
            "number_of_tuples": self.number_of_tuples,
            "number_of_namespaces": self.number_of_namespaces
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
