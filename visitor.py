from CSharpParserVisitor import CSharpParserVisitor

class FeatureExtractorVisitor(CSharpParserVisitor):

    def __init__(self):
        self.node_count = {}
        self.max_depth = 0
        self.current_depth = 0

    def visit(self, ctx):
        node_type = type(ctx).__name__
        self.node_count[node_type] = self.node_count.get(node_type, 0) + 1
        self.current_depth += 1
        if self.current_depth > self.max_depth:
            self.max_depth = self.current_depth
        result = super().visit(ctx)
        self.current_depth -= 1
        return result

    def get_features(self):
        return {
            "node_count": self.node_count,
            "max_depth": self.max_depth
        }

