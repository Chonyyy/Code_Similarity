from Python.CSharpParserListener import CSharpParserListener
import numpy as np
import pandas as pd

class FeatureExtractorListener(CSharpParserListener):

    def __init__(self):
        self.total_nodes = 0
        self.max_depth = 0
        self.current_depth = 0
        
        self.variables = 0
        self.constants = 0
        self.out_variables = 0
        self.ref_params = 0
        
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

        
        self.control_structures_if = 0
        self.control_structures_switch = 0
        self.control_structures_for = 0
        self.control_structures_while = 0
        self.control_structures_dowhile = 0
        
        self.access_modifiers_public = 0
        self.access_modifiers_private = 0
        self.access_modifiers_protected = 0
        self.access_modifiers_internal = 0
        self.access_modifiers_static = 0
        self.access_modifiers_protected_internal = 0 
        self.access_modifiers_private_protected = 0
        
        self.modifier_readonly = 0
        self.modifier_volatile = 0
        self.modifier_virtual = 0
        self.modifier_override = 0
        self.modifier_new = 0
        self.modifier_partial = 0
        self.modifier_extern = 0
        self.modifier_unsafe = 0
        self.modifier_async = 0
        
        self.library_call_console = 0
        self.library_call_math = 0
        
        self.linq_queries_select = 0
        self.linq_queries_where = 0
        self.linq_queries_orderBy = 0
        self.linq_queries_groupBy = 0
        self.linq_queries_join = 0
        self.linq_queries_sum = 0
        self.linq_queries_count = 0
                
        self.number_of_lambdas = 0
        self.number_of_getters = 0
        self.number_of_setters = 0
        self.number_of_tuples = 0
        self.number_of_namespaces = 0

        # self.method_parameters = {}
        self.method_parameters = []
        self.variable_names = set()
        self.method_return_types = set()
        self.method_names = set()
        # self.method_lengths = []
        self.class_names = set()
        self.interface_names = set()
        self.enum_names = set()
        self.delegate_names = set()
        # self.distinct_tokens = {}
        self.node_count = {}

    def enterEveryRule(self, ctx):
        node_type = type(ctx).__name__
        self.node_count[node_type] = self.node_count.get(node_type, 0) + 1
        self.current_depth += 1
        self.total_nodes += 1
        
        # try:
        #     if ctx.start.text == "void":
        #         pass
        #     if ctx.start.text == "lambda":
        #         pass
        # except:
        #     pass
         
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
            
            return_type = ctx.parentCtx.start.text
            self.method_return_types.add((ctx.start.text,return_type))            
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
                
                if ctx.children[2].fixed_parameters():
                    for param in ctx.children[2].children[0].fixed_parameter() :
                        if param.children[0].children[0].getText() == "out":
                            self.out_variables += 1
                            param_type = param.children[1].children[0].getText()
                            param_name = param.children[1].children[1].getText()
                            
                        elif param.children[0].children[0].getText() == "ref":
                            self.ref_params += 1
                            param_type = param.children[1].children[0].getText()
                            param_name = param.children[1].children[1].getText()
                            
                        else:
                            param_type = param.children[0].children[0].getText()
                            param_name = param.children[0].children[1].getText()
                        
                        param_info.append((param_type, param_name))
                
                # self.method_parameters[ctx.start.text] = param_info
                self.method_parameters.append([ctx.start.text, param_info])
                pass
            
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
            self.control_structures_if += 1

        elif node_type == "SwitchStatementContext":
            self.control_structures_switch += 1
            
        elif node_type == "ForStatementContext":
            self.control_structures_for += 1
        
        elif node_type == "WhileStatementContext":
            self.control_structures_while += 1
        
        elif node_type == "DoWhileStatementContext":
            self.control_structures_dowhile += 1
            
        elif node_type == "Local_variable_initializerContext":
            modifier = ctx.start.text
            self._count_modifiers(modifier)
            
        elif node_type == "Constant_declarationContext":
            self.constants += 1
        
        elif node_type == "Enum_definitionContext":
            self.enums += 1
            self.enum_names.add(ctx.children[1].start.text)
            
        elif node_type == "Delegate_definitionContext":
            self.delegates += 1
            name = ctx.children[2].start.text
            return_type = ctx.children[1].start.text
            self.delegate_names.add((name, return_type))
        
        elif node_type == "All_member_modifierContext":
            modifier = ctx.start.text
            self._count_modifiers(modifier)
                    
        elif node_type == "Method_invocationContext":
            method_name = ctx.parentCtx.start.text
            if method_name == 'Console':
                self.library_call_console += 1
            if method_name == 'Math':
                self.library_call_math += 1 
        
        if node_type == "Lambda_expressionContext":
            self.number_of_lambdas += 1

        if node_type == "Accessor_declarationsContext":
            accessor_type = ctx.children[0].getText()
            if accessor_type == "get":
                self.number_of_getters += 1
            elif accessor_type == "set":
                self.number_of_setters += 1
        
        if node_type == "Set_accessor_declarationContext":
            self.number_of_setters += 1

        if node_type == "Namespace_declarationContext":
            self.number_of_namespaces += 1
        
        elif node_type == "IdentifierContext":
            name = ctx.start.text
            if name == 'Select':
                self.linq_queries_select += 1
            if name == 'Where':
                self.linq_queries_where += 1
            if name == 'OrderBy':
                self.linq_queries_orderBy += 1
            if name == 'GroupBy':
                self.linq_queries_groupBy += 1
            if name == 'Join':
                self.linq_queries_join += 1
            if name == 'Sum':
                self.linq_queries_sum += 1
            if name == 'Count':
                self.linq_queries_sum += 1
             
    def _count_modifiers(self, modifier):
        if modifier == 'new':
            self.modifier_new += 1
        elif modifier == 'readonly':
            self.modifier_readonly += 1
        elif modifier == 'volatile':
            self.modifier_volatile += 1
        elif modifier == 'virtual':
            self.modifier_virtual += 1
        elif modifier == 'override':
            self.modifier_override += 1
        elif modifier == 'partial':
            self.modifier_partial += 1
        elif modifier == 'extern':
            self.modifier_extern += 1
        elif modifier == 'unsafe':
            self.modifier_unsafe += 1
        elif modifier == 'async':
            self.modifier_async += 1
            
        if modifier == 'public':
            self.access_modifiers_public += 1
        elif modifier == 'private':
            self.access_modifiers_private += 1
        elif modifier == 'static':
            self.access_modifiers_static += 1
        elif modifier == 'protected':
            self.access_modifiers_protected += 1
        elif modifier == 'internal':
            self.access_modifiers_internal += 1
        elif modifier == 'protected internal':
            self.access_modifiers_protected_internal += 1
        elif modifier == 'private protected':
            self.access_modifiers_private_protected += 1

    def exitEveryRule(self, ctx):
        self.current_depth -= 1
    
    def get_features(self):
        return {
            "total_nodes": self.total_nodes,
            "max_depth": self.max_depth,
            "number_of_variables": self.variables,
            "number_of_constants": self.constants,
            "out_variables": self.out_variables,
            "ref_params": self.ref_params,
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
            "enums_names":list(self.enum_names),
            "control_structures_if": self.control_structures_if,
            "control_structures_switch": self.control_structures_switch,
            "control_structures_for": self.control_structures_for,
            "control_structures_while": self.control_structures_while,
            "control_structures_dowhile": self.control_structures_dowhile,
            "access_modifiers_public": self.access_modifiers_public,
            "access_modifiers_private": self.access_modifiers_private,
            "access_modifiers_protected": self.access_modifiers_protected,
            "access_modifiers_internal": self.access_modifiers_internal,
            "access_modifiers_static": self.access_modifiers_static,
            "access_modifiers_protected_internal": self.access_modifiers_protected_internal,
            "access_modifiers_private_protected": self.access_modifiers_private_protected,
            "modifier_readonly": self.modifier_readonly,
            "modifier_volatile": self.modifier_volatile,
            "modifier_virtual": self.modifier_virtual,
            "modifier_override": self.modifier_override,
            "modifier_new": self.modifier_new,
            "modifier_partial": self.modifier_partial,
            "modifier_readonly": self.modifier_readonly,
            "modifier_extern": self.modifier_extern,
            "modifier_unsafe": self.modifier_unsafe,
            "modifier_async": self.modifier_async,
            "out_variables": self.out_variables,
            "linq_querie_select": self.linq_queries_select,
            "linq_queries_where": self.linq_queries_where,
            "linq_queries_orderBy": self.linq_queries_orderBy,
            "linq_queries_groupBy": self.linq_queries_groupBy,
            "linq_queries_join": self.linq_queries_join,
            "linq_queries_sum": self.linq_queries_sum,
            "linq_queries_count": self.linq_queries_count,
            "library_call_console": self.library_call_console,
            "library_call_math": self.library_call_math,
            "number_of_lambdas": self.number_of_lambdas,
            "number_of_getters": self.number_of_getters,
            "number_of_setters": self.number_of_setters,
            "number_of_tuples": self.number_of_tuples,
            "number_of_namespaces": self.number_of_namespaces,
            # "method_lengths": self.method_lengths,
            "method_parameters": self.method_parameters,
            "variable_names": list(self.variable_names),
            "method_names": list(self.method_names),
            "method_return_types": self.method_return_types,
            "class_names": list(self.class_names),
            "interface_names": list(self.interface_names),
            "delegate_names": list(self.delegate_names),
            # "distinct_tokens_count": self.distinct_tokens,
            "node_count": self.node_count
        }

class FeatureDifferenceDF:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.differences = self.calculate_differences()

    def calculate_differences(self):
        attributes = [
            'total_nodes', 'max_depth', 'current_depth', 'variables', 'constants', 
            'out_variables', 'ref_params', 'methods', 'classes', 'interfaces', 
            'abstract_classes', 'sealed_classes', 'import_statements', 'function_calls', 
            'try_catch_blocks', 'lists', 'dicts', 'enums', 'delegates', 
            'control_structures_if', 'control_structures_switch', 'control_structures_for', 
            'control_structures_while', 'control_structures_dowhile', 'access_modifiers_public', 
            'access_modifiers_private', 'access_modifiers_protected', 'access_modifiers_internal', 
            'access_modifiers_static', 'access_modifiers_protected_internal', 
            'access_modifiers_private_protected', 'modifier_readonly', 'modifier_volatile', 
            'modifier_virtual', 'modifier_override', 'modifier_new', 'modifier_partial', 
            'modifier_extern', 'modifier_unsafe', 'modifier_async', 'library_call_console', 
            'library_call_math', 'linq_queries_select', 'linq_queries_where', 'linq_queries_orderBy', 
            'linq_queries_groupBy', 'linq_queries_join', 'linq_queries_sum', 'linq_queries_count', 
            'number_of_lambdas', 'number_of_getters', 'number_of_setters', 'number_of_tuples', 
            'number_of_namespaces'
        ]

        fe1_values = self.df.loc[0, attributes].values
        fe2_values = self.df.loc[1, attributes].values
        
        differences = np.array(fe1_values, dtype=int) - np.array(fe2_values, dtype=int)
        return differences

    def get_differences(self):
        return self.differences


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
    
def calculate_differences(self):
    attributes = [
        'total_nodes', 'max_depth', 'current_depth', 'variables', 'constants', 
        'out_variables', 'ref_params', 'methods', 'classes', 'interfaces', 
        'abstract_classes', 'sealed_classes', 'import_statements', 'function_calls', 
        'try_catch_blocks', 'lists', 'dicts', 'enums', 'delegates', 
        'control_structures_if', 'control_structures_switch', 'control_structures_for', 
        'control_structures_while', 'control_structures_dowhile', 'access_modifiers_public', 
        'access_modifiers_private', 'access_modifiers_protected', 'access_modifiers_internal', 
        'access_modifiers_static', 'access_modifiers_protected_internal', 
        'access_modifiers_private_protected', 'modifier_readonly', 'modifier_volatile', 
        'modifier_virtual', 'modifier_override', 'modifier_new', 'modifier_partial', 
        'modifier_extern', 'modifier_unsafe', 'modifier_async', 'library_call_console', 
        'library_call_math', 'linq_queries_select', 'linq_queries_where', 'linq_queries_orderBy', 
        'linq_queries_groupBy', 'linq_queries_join', 'linq_queries_sum', 'linq_queries_count', 
        'number_of_lambdas', 'number_of_getters', 'number_of_setters', 'number_of_tuples', 
        'number_of_namespaces'
    ]

    fe1_values = np.array([getattr(self.fe1, attr) for attr in attributes])
    fe2_values = np.array([getattr(self.fe2, attr) for attr in attributes])
    
    differences = fe1_values - fe2_values
    return differences