import ast


class FeatureExtractor(ast.NodeVisitor):
    def __init__(self):
        self.features = {
            "total_nodes": 0,
            "max_depth": 0,
            "number_of_variables": 0,
            "number_of_constants": 0,
            "out_variables": 0,
            "ref_params": 0,
            "number_of_methods": 0,
            "number_of_classes": 0,
            "number_of_interfaces": 0,
            "number_of_abstract_classes": 0,
            "number_of_sealed_classes": 0,
            "import_statements": 0,
            "number_of_try_blocks": 0,
            "number_of_lists": 0,
            "number_of_dictionaries": 0,
            "number_of_enums": 0,
            "number_of_delegates": 0,
            "function_calls": 0,
            "enums_names": [],
            "control_structures_if": 0,
            "control_structures_switch": 0,
            "control_structures_for": 0,
            "control_structures_while": 0,
            "control_structures_dowhile": 0,
            "access_modifiers_public": 0,
            "access_modifiers_private": 0,
            "access_modifiers_protected": 0,
            "access_modifiers_internal": 0,
            "access_modifiers_static": 0,
            "access_modifiers_protected_internal": 0,
            "access_modifiers_private_protected": 0,
            "modifier_readonly": 0,
            "modifier_volatile": 0,
            "modifier_virtual": 0,
            "modifier_override": 0,
            "modifier_new": 0,
            "modifier_partial": 0,
            "modifier_extern": 0,
            "modifier_unsafe": 0,
            "modifier_async": 0,
            "linq_querie_select": 0,
            "linq_queries_where": 0,
            "linq_queries_orderBy": 0,
            "linq_queries_groupBy": 0,
            "linq_queries_join": 0,
            "linq_queries_sum": 0,
            "linq_queries_count": 0,
            "library_call_console": 0,
            "library_call_math": 0,
            "number_of_lambdas": 0,
            "number_of_getters": 0,
            "number_of_setters": 0,
            "number_of_tuples": 0,
            "number_of_namespaces": 0,
            "method_parameters": [],
            "variable_names": [],
            "method_names": [],
            "method_return_types": [],
            "class_names": [],
            "interface_names": [],
            "delegate_names": [],
            "node_count": {},
            "project_name": "",
            "label": "original"
        }

    def visit(self, node, depth=0):
        self.features["total_nodes"] += 1
        self.features["max_depth"] = max(self.features["max_depth"], depth)

        node_type = type(node).__name__
        self.features["node_count"].setdefault(node_type, 0)
        self.features["node_count"][node_type] += 1

        super().visit(node)

        for child in ast.iter_child_nodes(node):
            self.visit(child, depth + 1)

    def visit_Import(self, node):
        self.features["import_statements"] += 1

    def visit_ClassDef(self, node):
        self.features["number_of_classes"] += 1
        self.features["class_names"].append(node.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.features["number_of_methods"] += 1
        self.features["method_names"].append(node.name)

        # Agregar parámetros de métodos
        method_params = [(arg.arg, arg.annotation.id if arg.annotation else None) for arg in node.args.args]
        self.features["method_parameters"].append((node.name, method_params))

        self.generic_visit(node)

    def visit_Assign(self, node):
        self.features["number_of_variables"] += len(node.targets)

        # Extraer nombres de variables
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.features["variable_names"].append(target.id)

        self.generic_visit(node)

    def visit_Constant(self, node):
        self.features["number_of_constants"] += 1
        self.generic_visit(node)

    def visit_List(self, node):
        self.features["number_of_lists"] += 1
        self.generic_visit(node)

    def visit_Dict(self, node):
        self.features["number_of_dictionaries"] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        self.features["function_calls"] += 1

        # Detectar llamadas específicas a librerías (ej. math, print)
        if isinstance(node.func, ast.Attribute):
            if node.func.value.id == "math":
                self.features["library_call_math"] += 1
            elif node.func.value.id == "console":
                self.features["library_call_console"] += 1
        elif isinstance(node.func, ast.Name) and node.func.id == "print":
            self.features["library_call_console"] += 1

        self.generic_visit(node)

    def visit_If(self, node):
        self.features["control_structures_if"] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.features["control_structures_for"] += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.features["control_structures_while"] += 1
        self.generic_visit(node)


# Ejemplo de código para analizar
codigo = """
import math

class Moogle:
    def __init__(self, query):
        self.query = query

    def Items(self):
        return []

    def Query(self, query):
        return "SearchResult"

if __name__ == "__main__":
    print("Hello, world!")
"""

# Parsear el código y generar el AST
arbol = ast.parse(codigo)

# Extraer características
extractor = FeatureExtractor()
extractor.visit(arbol)

# Mostrar resultados
import pprint
pprint.pprint(extractor.features)
