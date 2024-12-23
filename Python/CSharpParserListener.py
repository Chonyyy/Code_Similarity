# Generated from CSharpParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSharpParser import CSharpParser
else:
    from CSharpParser import CSharpParser

# This class defines a complete listener for a parse tree produced by CSharpParser.
class CSharpParserListener(ParseTreeListener):

    # Enter a parse tree produced by CSharpParser#compilation_unit.
    def enterCompilation_unit(self, ctx:CSharpParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by CSharpParser#compilation_unit.
    def exitCompilation_unit(self, ctx:CSharpParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by CSharpParser#compilation_unit_element.
    def enterCompilation_unit_element(self, ctx:CSharpParser.Compilation_unit_elementContext):
        pass

    # Exit a parse tree produced by CSharpParser#compilation_unit_element.
    def exitCompilation_unit_element(self, ctx:CSharpParser.Compilation_unit_elementContext):
        pass


    # Enter a parse tree produced by CSharpParser#top_level_statements.
    def enterTop_level_statements(self, ctx:CSharpParser.Top_level_statementsContext):
        pass

    # Exit a parse tree produced by CSharpParser#top_level_statements.
    def exitTop_level_statements(self, ctx:CSharpParser.Top_level_statementsContext):
        pass


    # Enter a parse tree produced by CSharpParser#global_using_directives.
    def enterGlobal_using_directives(self, ctx:CSharpParser.Global_using_directivesContext):
        pass

    # Exit a parse tree produced by CSharpParser#global_using_directives.
    def exitGlobal_using_directives(self, ctx:CSharpParser.Global_using_directivesContext):
        pass


    # Enter a parse tree produced by CSharpParser#global_using_directive.
    def enterGlobal_using_directive(self, ctx:CSharpParser.Global_using_directiveContext):
        pass

    # Exit a parse tree produced by CSharpParser#global_using_directive.
    def exitGlobal_using_directive(self, ctx:CSharpParser.Global_using_directiveContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_or_type_name.
    def enterNamespace_or_type_name(self, ctx:CSharpParser.Namespace_or_type_nameContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_or_type_name.
    def exitNamespace_or_type_name(self, ctx:CSharpParser.Namespace_or_type_nameContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_.
    def enterType_(self, ctx:CSharpParser.Type_Context):
        pass

    # Exit a parse tree produced by CSharpParser#type_.
    def exitType_(self, ctx:CSharpParser.Type_Context):
        pass


    # Enter a parse tree produced by CSharpParser#function_pointer_type.
    def enterFunction_pointer_type(self, ctx:CSharpParser.Function_pointer_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#function_pointer_type.
    def exitFunction_pointer_type(self, ctx:CSharpParser.Function_pointer_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#function_pointer_parameter_list.
    def enterFunction_pointer_parameter_list(self, ctx:CSharpParser.Function_pointer_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#function_pointer_parameter_list.
    def exitFunction_pointer_parameter_list(self, ctx:CSharpParser.Function_pointer_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#base_type.
    def enterBase_type(self, ctx:CSharpParser.Base_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#base_type.
    def exitBase_type(self, ctx:CSharpParser.Base_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#tuple_type.
    def enterTuple_type(self, ctx:CSharpParser.Tuple_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#tuple_type.
    def exitTuple_type(self, ctx:CSharpParser.Tuple_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#deconstruction_expression.
    def enterDeconstruction_expression(self, ctx:CSharpParser.Deconstruction_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#deconstruction_expression.
    def exitDeconstruction_expression(self, ctx:CSharpParser.Deconstruction_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#deconstruction_tuple.
    def enterDeconstruction_tuple(self, ctx:CSharpParser.Deconstruction_tupleContext):
        pass

    # Exit a parse tree produced by CSharpParser#deconstruction_tuple.
    def exitDeconstruction_tuple(self, ctx:CSharpParser.Deconstruction_tupleContext):
        pass


    # Enter a parse tree produced by CSharpParser#deconstruction_element.
    def enterDeconstruction_element(self, ctx:CSharpParser.Deconstruction_elementContext):
        pass

    # Exit a parse tree produced by CSharpParser#deconstruction_element.
    def exitDeconstruction_element(self, ctx:CSharpParser.Deconstruction_elementContext):
        pass


    # Enter a parse tree produced by CSharpParser#tuple_element.
    def enterTuple_element(self, ctx:CSharpParser.Tuple_elementContext):
        pass

    # Exit a parse tree produced by CSharpParser#tuple_element.
    def exitTuple_element(self, ctx:CSharpParser.Tuple_elementContext):
        pass


    # Enter a parse tree produced by CSharpParser#simple_type.
    def enterSimple_type(self, ctx:CSharpParser.Simple_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#simple_type.
    def exitSimple_type(self, ctx:CSharpParser.Simple_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#numeric_type.
    def enterNumeric_type(self, ctx:CSharpParser.Numeric_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#numeric_type.
    def exitNumeric_type(self, ctx:CSharpParser.Numeric_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#integral_type.
    def enterIntegral_type(self, ctx:CSharpParser.Integral_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#integral_type.
    def exitIntegral_type(self, ctx:CSharpParser.Integral_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#floating_point_type.
    def enterFloating_point_type(self, ctx:CSharpParser.Floating_point_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#floating_point_type.
    def exitFloating_point_type(self, ctx:CSharpParser.Floating_point_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#default_value_expression.
    def enterDefault_value_expression(self, ctx:CSharpParser.Default_value_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#default_value_expression.
    def exitDefault_value_expression(self, ctx:CSharpParser.Default_value_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#explictly_typed_default.
    def enterExplictly_typed_default(self, ctx:CSharpParser.Explictly_typed_defaultContext):
        pass

    # Exit a parse tree produced by CSharpParser#explictly_typed_default.
    def exitExplictly_typed_default(self, ctx:CSharpParser.Explictly_typed_defaultContext):
        pass


    # Enter a parse tree produced by CSharpParser#default_literal.
    def enterDefault_literal(self, ctx:CSharpParser.Default_literalContext):
        pass

    # Exit a parse tree produced by CSharpParser#default_literal.
    def exitDefault_literal(self, ctx:CSharpParser.Default_literalContext):
        pass


    # Enter a parse tree produced by CSharpParser#variable_reference.
    def enterVariable_reference(self, ctx:CSharpParser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by CSharpParser#variable_reference.
    def exitVariable_reference(self, ctx:CSharpParser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_type.
    def enterClass_type(self, ctx:CSharpParser.Class_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_type.
    def exitClass_type(self, ctx:CSharpParser.Class_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_argument_list.
    def enterType_argument_list(self, ctx:CSharpParser.Type_argument_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_argument_list.
    def exitType_argument_list(self, ctx:CSharpParser.Type_argument_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#argument_list.
    def enterArgument_list(self, ctx:CSharpParser.Argument_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#argument_list.
    def exitArgument_list(self, ctx:CSharpParser.Argument_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#argument.
    def enterArgument(self, ctx:CSharpParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CSharpParser#argument.
    def exitArgument(self, ctx:CSharpParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CSharpParser#argument_name.
    def enterArgument_name(self, ctx:CSharpParser.Argument_nameContext):
        pass

    # Exit a parse tree produced by CSharpParser#argument_name.
    def exitArgument_name(self, ctx:CSharpParser.Argument_nameContext):
        pass


    # Enter a parse tree produced by CSharpParser#expression.
    def enterExpression(self, ctx:CSharpParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#expression.
    def exitExpression(self, ctx:CSharpParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#non_assignment_expression.
    def enterNon_assignment_expression(self, ctx:CSharpParser.Non_assignment_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#non_assignment_expression.
    def exitNon_assignment_expression(self, ctx:CSharpParser.Non_assignment_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#assignment.
    def enterAssignment(self, ctx:CSharpParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CSharpParser#assignment.
    def exitAssignment(self, ctx:CSharpParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CSharpParser#assignment_operator.
    def enterAssignment_operator(self, ctx:CSharpParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by CSharpParser#assignment_operator.
    def exitAssignment_operator(self, ctx:CSharpParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by CSharpParser#conditional_expression.
    def enterConditional_expression(self, ctx:CSharpParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#conditional_expression.
    def exitConditional_expression(self, ctx:CSharpParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#null_coalescing_expression.
    def enterNull_coalescing_expression(self, ctx:CSharpParser.Null_coalescing_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#null_coalescing_expression.
    def exitNull_coalescing_expression(self, ctx:CSharpParser.Null_coalescing_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#conditional_or_expression.
    def enterConditional_or_expression(self, ctx:CSharpParser.Conditional_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#conditional_or_expression.
    def exitConditional_or_expression(self, ctx:CSharpParser.Conditional_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#conditional_and_expression.
    def enterConditional_and_expression(self, ctx:CSharpParser.Conditional_and_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#conditional_and_expression.
    def exitConditional_and_expression(self, ctx:CSharpParser.Conditional_and_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#inclusive_or_expression.
    def enterInclusive_or_expression(self, ctx:CSharpParser.Inclusive_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#inclusive_or_expression.
    def exitInclusive_or_expression(self, ctx:CSharpParser.Inclusive_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#exclusive_or_expression.
    def enterExclusive_or_expression(self, ctx:CSharpParser.Exclusive_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#exclusive_or_expression.
    def exitExclusive_or_expression(self, ctx:CSharpParser.Exclusive_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#and_expression.
    def enterAnd_expression(self, ctx:CSharpParser.And_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#and_expression.
    def exitAnd_expression(self, ctx:CSharpParser.And_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#equality_expression.
    def enterEquality_expression(self, ctx:CSharpParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#equality_expression.
    def exitEquality_expression(self, ctx:CSharpParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#relational_expression.
    def enterRelational_expression(self, ctx:CSharpParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#relational_expression.
    def exitRelational_expression(self, ctx:CSharpParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#shift_expression.
    def enterShift_expression(self, ctx:CSharpParser.Shift_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#shift_expression.
    def exitShift_expression(self, ctx:CSharpParser.Shift_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#additive_expression.
    def enterAdditive_expression(self, ctx:CSharpParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#additive_expression.
    def exitAdditive_expression(self, ctx:CSharpParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:CSharpParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:CSharpParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#switch_expression.
    def enterSwitch_expression(self, ctx:CSharpParser.Switch_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#switch_expression.
    def exitSwitch_expression(self, ctx:CSharpParser.Switch_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#switch_expression_arms.
    def enterSwitch_expression_arms(self, ctx:CSharpParser.Switch_expression_armsContext):
        pass

    # Exit a parse tree produced by CSharpParser#switch_expression_arms.
    def exitSwitch_expression_arms(self, ctx:CSharpParser.Switch_expression_armsContext):
        pass


    # Enter a parse tree produced by CSharpParser#switch_expression_arm.
    def enterSwitch_expression_arm(self, ctx:CSharpParser.Switch_expression_armContext):
        pass

    # Exit a parse tree produced by CSharpParser#switch_expression_arm.
    def exitSwitch_expression_arm(self, ctx:CSharpParser.Switch_expression_armContext):
        pass


    # Enter a parse tree produced by CSharpParser#range_expression.
    def enterRange_expression(self, ctx:CSharpParser.Range_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#range_expression.
    def exitRange_expression(self, ctx:CSharpParser.Range_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#unary_expression.
    def enterUnary_expression(self, ctx:CSharpParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#unary_expression.
    def exitUnary_expression(self, ctx:CSharpParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#cast_expression.
    def enterCast_expression(self, ctx:CSharpParser.Cast_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#cast_expression.
    def exitCast_expression(self, ctx:CSharpParser.Cast_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#collection_expression.
    def enterCollection_expression(self, ctx:CSharpParser.Collection_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#collection_expression.
    def exitCollection_expression(self, ctx:CSharpParser.Collection_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#collection_element_list.
    def enterCollection_element_list(self, ctx:CSharpParser.Collection_element_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#collection_element_list.
    def exitCollection_element_list(self, ctx:CSharpParser.Collection_element_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#collection_element.
    def enterCollection_element(self, ctx:CSharpParser.Collection_elementContext):
        pass

    # Exit a parse tree produced by CSharpParser#collection_element.
    def exitCollection_element(self, ctx:CSharpParser.Collection_elementContext):
        pass


    # Enter a parse tree produced by CSharpParser#primary_expression.
    def enterPrimary_expression(self, ctx:CSharpParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#primary_expression.
    def exitPrimary_expression(self, ctx:CSharpParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#literalExpression.
    def enterLiteralExpression(self, ctx:CSharpParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#literalExpression.
    def exitLiteralExpression(self, ctx:CSharpParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#simpleNameExpression.
    def enterSimpleNameExpression(self, ctx:CSharpParser.SimpleNameExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#simpleNameExpression.
    def exitSimpleNameExpression(self, ctx:CSharpParser.SimpleNameExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#parenthesisExpressions.
    def enterParenthesisExpressions(self, ctx:CSharpParser.ParenthesisExpressionsContext):
        pass

    # Exit a parse tree produced by CSharpParser#parenthesisExpressions.
    def exitParenthesisExpressions(self, ctx:CSharpParser.ParenthesisExpressionsContext):
        pass


    # Enter a parse tree produced by CSharpParser#memberAccessExpression.
    def enterMemberAccessExpression(self, ctx:CSharpParser.MemberAccessExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#memberAccessExpression.
    def exitMemberAccessExpression(self, ctx:CSharpParser.MemberAccessExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#literalAccessExpression.
    def enterLiteralAccessExpression(self, ctx:CSharpParser.LiteralAccessExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#literalAccessExpression.
    def exitLiteralAccessExpression(self, ctx:CSharpParser.LiteralAccessExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#thisReferenceExpression.
    def enterThisReferenceExpression(self, ctx:CSharpParser.ThisReferenceExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#thisReferenceExpression.
    def exitThisReferenceExpression(self, ctx:CSharpParser.ThisReferenceExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#baseAccessExpression.
    def enterBaseAccessExpression(self, ctx:CSharpParser.BaseAccessExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#baseAccessExpression.
    def exitBaseAccessExpression(self, ctx:CSharpParser.BaseAccessExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#objectCreationExpression.
    def enterObjectCreationExpression(self, ctx:CSharpParser.ObjectCreationExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#objectCreationExpression.
    def exitObjectCreationExpression(self, ctx:CSharpParser.ObjectCreationExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#targetTypedNewExpression.
    def enterTargetTypedNewExpression(self, ctx:CSharpParser.TargetTypedNewExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#targetTypedNewExpression.
    def exitTargetTypedNewExpression(self, ctx:CSharpParser.TargetTypedNewExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#tupleExpression.
    def enterTupleExpression(self, ctx:CSharpParser.TupleExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#tupleExpression.
    def exitTupleExpression(self, ctx:CSharpParser.TupleExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#typeofExpression.
    def enterTypeofExpression(self, ctx:CSharpParser.TypeofExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#typeofExpression.
    def exitTypeofExpression(self, ctx:CSharpParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#checkedExpression.
    def enterCheckedExpression(self, ctx:CSharpParser.CheckedExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#checkedExpression.
    def exitCheckedExpression(self, ctx:CSharpParser.CheckedExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#uncheckedExpression.
    def enterUncheckedExpression(self, ctx:CSharpParser.UncheckedExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#uncheckedExpression.
    def exitUncheckedExpression(self, ctx:CSharpParser.UncheckedExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#defaultValueExpression.
    def enterDefaultValueExpression(self, ctx:CSharpParser.DefaultValueExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#defaultValueExpression.
    def exitDefaultValueExpression(self, ctx:CSharpParser.DefaultValueExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#anonymousMethodExpression.
    def enterAnonymousMethodExpression(self, ctx:CSharpParser.AnonymousMethodExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#anonymousMethodExpression.
    def exitAnonymousMethodExpression(self, ctx:CSharpParser.AnonymousMethodExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#sizeofExpression.
    def enterSizeofExpression(self, ctx:CSharpParser.SizeofExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#sizeofExpression.
    def exitSizeofExpression(self, ctx:CSharpParser.SizeofExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#nameofExpression.
    def enterNameofExpression(self, ctx:CSharpParser.NameofExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#nameofExpression.
    def exitNameofExpression(self, ctx:CSharpParser.NameofExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#throwable_expression.
    def enterThrowable_expression(self, ctx:CSharpParser.Throwable_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#throwable_expression.
    def exitThrowable_expression(self, ctx:CSharpParser.Throwable_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#throw_expression.
    def enterThrow_expression(self, ctx:CSharpParser.Throw_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#throw_expression.
    def exitThrow_expression(self, ctx:CSharpParser.Throw_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#member_access.
    def enterMember_access(self, ctx:CSharpParser.Member_accessContext):
        pass

    # Exit a parse tree produced by CSharpParser#member_access.
    def exitMember_access(self, ctx:CSharpParser.Member_accessContext):
        pass


    # Enter a parse tree produced by CSharpParser#bracket_expression.
    def enterBracket_expression(self, ctx:CSharpParser.Bracket_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#bracket_expression.
    def exitBracket_expression(self, ctx:CSharpParser.Bracket_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#indexer_argument.
    def enterIndexer_argument(self, ctx:CSharpParser.Indexer_argumentContext):
        pass

    # Exit a parse tree produced by CSharpParser#indexer_argument.
    def exitIndexer_argument(self, ctx:CSharpParser.Indexer_argumentContext):
        pass


    # Enter a parse tree produced by CSharpParser#predefined_type.
    def enterPredefined_type(self, ctx:CSharpParser.Predefined_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#predefined_type.
    def exitPredefined_type(self, ctx:CSharpParser.Predefined_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#expression_list.
    def enterExpression_list(self, ctx:CSharpParser.Expression_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#expression_list.
    def exitExpression_list(self, ctx:CSharpParser.Expression_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#object_or_collection_initializer.
    def enterObject_or_collection_initializer(self, ctx:CSharpParser.Object_or_collection_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#object_or_collection_initializer.
    def exitObject_or_collection_initializer(self, ctx:CSharpParser.Object_or_collection_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#object_initializer.
    def enterObject_initializer(self, ctx:CSharpParser.Object_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#object_initializer.
    def exitObject_initializer(self, ctx:CSharpParser.Object_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#member_initializer_list.
    def enterMember_initializer_list(self, ctx:CSharpParser.Member_initializer_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#member_initializer_list.
    def exitMember_initializer_list(self, ctx:CSharpParser.Member_initializer_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#member_initializer.
    def enterMember_initializer(self, ctx:CSharpParser.Member_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#member_initializer.
    def exitMember_initializer(self, ctx:CSharpParser.Member_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#initializer_value.
    def enterInitializer_value(self, ctx:CSharpParser.Initializer_valueContext):
        pass

    # Exit a parse tree produced by CSharpParser#initializer_value.
    def exitInitializer_value(self, ctx:CSharpParser.Initializer_valueContext):
        pass


    # Enter a parse tree produced by CSharpParser#collection_initializer.
    def enterCollection_initializer(self, ctx:CSharpParser.Collection_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#collection_initializer.
    def exitCollection_initializer(self, ctx:CSharpParser.Collection_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#element_initializer.
    def enterElement_initializer(self, ctx:CSharpParser.Element_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#element_initializer.
    def exitElement_initializer(self, ctx:CSharpParser.Element_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#anonymous_object_initializer.
    def enterAnonymous_object_initializer(self, ctx:CSharpParser.Anonymous_object_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#anonymous_object_initializer.
    def exitAnonymous_object_initializer(self, ctx:CSharpParser.Anonymous_object_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#member_declarator_list.
    def enterMember_declarator_list(self, ctx:CSharpParser.Member_declarator_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#member_declarator_list.
    def exitMember_declarator_list(self, ctx:CSharpParser.Member_declarator_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#member_declarator.
    def enterMember_declarator(self, ctx:CSharpParser.Member_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#member_declarator.
    def exitMember_declarator(self, ctx:CSharpParser.Member_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#unbound_type_name.
    def enterUnbound_type_name(self, ctx:CSharpParser.Unbound_type_nameContext):
        pass

    # Exit a parse tree produced by CSharpParser#unbound_type_name.
    def exitUnbound_type_name(self, ctx:CSharpParser.Unbound_type_nameContext):
        pass


    # Enter a parse tree produced by CSharpParser#generic_dimension_specifier.
    def enterGeneric_dimension_specifier(self, ctx:CSharpParser.Generic_dimension_specifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#generic_dimension_specifier.
    def exitGeneric_dimension_specifier(self, ctx:CSharpParser.Generic_dimension_specifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#isType.
    def enterIsType(self, ctx:CSharpParser.IsTypeContext):
        pass

    # Exit a parse tree produced by CSharpParser#isType.
    def exitIsType(self, ctx:CSharpParser.IsTypeContext):
        pass


    # Enter a parse tree produced by CSharpParser#isTypePatternArms.
    def enterIsTypePatternArms(self, ctx:CSharpParser.IsTypePatternArmsContext):
        pass

    # Exit a parse tree produced by CSharpParser#isTypePatternArms.
    def exitIsTypePatternArms(self, ctx:CSharpParser.IsTypePatternArmsContext):
        pass


    # Enter a parse tree produced by CSharpParser#isTypePatternArm.
    def enterIsTypePatternArm(self, ctx:CSharpParser.IsTypePatternArmContext):
        pass

    # Exit a parse tree produced by CSharpParser#isTypePatternArm.
    def exitIsTypePatternArm(self, ctx:CSharpParser.IsTypePatternArmContext):
        pass


    # Enter a parse tree produced by CSharpParser#lambda_expression.
    def enterLambda_expression(self, ctx:CSharpParser.Lambda_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#lambda_expression.
    def exitLambda_expression(self, ctx:CSharpParser.Lambda_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#anonymous_function_signature.
    def enterAnonymous_function_signature(self, ctx:CSharpParser.Anonymous_function_signatureContext):
        pass

    # Exit a parse tree produced by CSharpParser#anonymous_function_signature.
    def exitAnonymous_function_signature(self, ctx:CSharpParser.Anonymous_function_signatureContext):
        pass


    # Enter a parse tree produced by CSharpParser#explicit_anonymous_function_parameter_list.
    def enterExplicit_anonymous_function_parameter_list(self, ctx:CSharpParser.Explicit_anonymous_function_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#explicit_anonymous_function_parameter_list.
    def exitExplicit_anonymous_function_parameter_list(self, ctx:CSharpParser.Explicit_anonymous_function_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#explicit_anonymous_function_parameter.
    def enterExplicit_anonymous_function_parameter(self, ctx:CSharpParser.Explicit_anonymous_function_parameterContext):
        pass

    # Exit a parse tree produced by CSharpParser#explicit_anonymous_function_parameter.
    def exitExplicit_anonymous_function_parameter(self, ctx:CSharpParser.Explicit_anonymous_function_parameterContext):
        pass


    # Enter a parse tree produced by CSharpParser#implicit_anonymous_function_parameter_list.
    def enterImplicit_anonymous_function_parameter_list(self, ctx:CSharpParser.Implicit_anonymous_function_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#implicit_anonymous_function_parameter_list.
    def exitImplicit_anonymous_function_parameter_list(self, ctx:CSharpParser.Implicit_anonymous_function_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#anonymous_function_body.
    def enterAnonymous_function_body(self, ctx:CSharpParser.Anonymous_function_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#anonymous_function_body.
    def exitAnonymous_function_body(self, ctx:CSharpParser.Anonymous_function_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#query_expression.
    def enterQuery_expression(self, ctx:CSharpParser.Query_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#query_expression.
    def exitQuery_expression(self, ctx:CSharpParser.Query_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#from_clause.
    def enterFrom_clause(self, ctx:CSharpParser.From_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#from_clause.
    def exitFrom_clause(self, ctx:CSharpParser.From_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#query_body.
    def enterQuery_body(self, ctx:CSharpParser.Query_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#query_body.
    def exitQuery_body(self, ctx:CSharpParser.Query_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#query_body_clause.
    def enterQuery_body_clause(self, ctx:CSharpParser.Query_body_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#query_body_clause.
    def exitQuery_body_clause(self, ctx:CSharpParser.Query_body_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#let_clause.
    def enterLet_clause(self, ctx:CSharpParser.Let_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#let_clause.
    def exitLet_clause(self, ctx:CSharpParser.Let_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#where_clause.
    def enterWhere_clause(self, ctx:CSharpParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#where_clause.
    def exitWhere_clause(self, ctx:CSharpParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#combined_join_clause.
    def enterCombined_join_clause(self, ctx:CSharpParser.Combined_join_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#combined_join_clause.
    def exitCombined_join_clause(self, ctx:CSharpParser.Combined_join_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#orderby_clause.
    def enterOrderby_clause(self, ctx:CSharpParser.Orderby_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#orderby_clause.
    def exitOrderby_clause(self, ctx:CSharpParser.Orderby_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#ordering.
    def enterOrdering(self, ctx:CSharpParser.OrderingContext):
        pass

    # Exit a parse tree produced by CSharpParser#ordering.
    def exitOrdering(self, ctx:CSharpParser.OrderingContext):
        pass


    # Enter a parse tree produced by CSharpParser#select_or_group_clause.
    def enterSelect_or_group_clause(self, ctx:CSharpParser.Select_or_group_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#select_or_group_clause.
    def exitSelect_or_group_clause(self, ctx:CSharpParser.Select_or_group_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#query_continuation.
    def enterQuery_continuation(self, ctx:CSharpParser.Query_continuationContext):
        pass

    # Exit a parse tree produced by CSharpParser#query_continuation.
    def exitQuery_continuation(self, ctx:CSharpParser.Query_continuationContext):
        pass


    # Enter a parse tree produced by CSharpParser#statement.
    def enterStatement(self, ctx:CSharpParser.StatementContext):
        pass

    # Exit a parse tree produced by CSharpParser#statement.
    def exitStatement(self, ctx:CSharpParser.StatementContext):
        pass


    # Enter a parse tree produced by CSharpParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:CSharpParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by CSharpParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:CSharpParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_function_declaration.
    def enterLocal_function_declaration(self, ctx:CSharpParser.Local_function_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_function_declaration.
    def exitLocal_function_declaration(self, ctx:CSharpParser.Local_function_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_function_header.
    def enterLocal_function_header(self, ctx:CSharpParser.Local_function_headerContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_function_header.
    def exitLocal_function_header(self, ctx:CSharpParser.Local_function_headerContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_function_modifiers.
    def enterLocal_function_modifiers(self, ctx:CSharpParser.Local_function_modifiersContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_function_modifiers.
    def exitLocal_function_modifiers(self, ctx:CSharpParser.Local_function_modifiersContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_function_body.
    def enterLocal_function_body(self, ctx:CSharpParser.Local_function_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_function_body.
    def exitLocal_function_body(self, ctx:CSharpParser.Local_function_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#labeled_Statement.
    def enterLabeled_Statement(self, ctx:CSharpParser.Labeled_StatementContext):
        pass

    # Exit a parse tree produced by CSharpParser#labeled_Statement.
    def exitLabeled_Statement(self, ctx:CSharpParser.Labeled_StatementContext):
        pass


    # Enter a parse tree produced by CSharpParser#embedded_statement.
    def enterEmbedded_statement(self, ctx:CSharpParser.Embedded_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#embedded_statement.
    def exitEmbedded_statement(self, ctx:CSharpParser.Embedded_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#empty_statement.
    def enterEmpty_statement(self, ctx:CSharpParser.Empty_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#empty_statement.
    def exitEmpty_statement(self, ctx:CSharpParser.Empty_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#if_statement.
    def enterIf_statement(self, ctx:CSharpParser.If_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#if_statement.
    def exitIf_statement(self, ctx:CSharpParser.If_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#checked_statement.
    def enterChecked_statement(self, ctx:CSharpParser.Checked_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#checked_statement.
    def exitChecked_statement(self, ctx:CSharpParser.Checked_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#unchecked_statement.
    def enterUnchecked_statement(self, ctx:CSharpParser.Unchecked_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#unchecked_statement.
    def exitUnchecked_statement(self, ctx:CSharpParser.Unchecked_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#lock_statement.
    def enterLock_statement(self, ctx:CSharpParser.Lock_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#lock_statement.
    def exitLock_statement(self, ctx:CSharpParser.Lock_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#unmanaged_type.
    def enterUnmanaged_type(self, ctx:CSharpParser.Unmanaged_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#unmanaged_type.
    def exitUnmanaged_type(self, ctx:CSharpParser.Unmanaged_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#stackalloc_expression.
    def enterStackalloc_expression(self, ctx:CSharpParser.Stackalloc_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#stackalloc_expression.
    def exitStackalloc_expression(self, ctx:CSharpParser.Stackalloc_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#stackalloc_initializer.
    def enterStackalloc_initializer(self, ctx:CSharpParser.Stackalloc_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#stackalloc_initializer.
    def exitStackalloc_initializer(self, ctx:CSharpParser.Stackalloc_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#stackalloc_initializer_element_list.
    def enterStackalloc_initializer_element_list(self, ctx:CSharpParser.Stackalloc_initializer_element_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#stackalloc_initializer_element_list.
    def exitStackalloc_initializer_element_list(self, ctx:CSharpParser.Stackalloc_initializer_element_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#stackalloc_element_initializer.
    def enterStackalloc_element_initializer(self, ctx:CSharpParser.Stackalloc_element_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#stackalloc_element_initializer.
    def exitStackalloc_element_initializer(self, ctx:CSharpParser.Stackalloc_element_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#using_statement.
    def enterUsing_statement(self, ctx:CSharpParser.Using_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#using_statement.
    def exitUsing_statement(self, ctx:CSharpParser.Using_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#yield_statement.
    def enterYield_statement(self, ctx:CSharpParser.Yield_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#yield_statement.
    def exitYield_statement(self, ctx:CSharpParser.Yield_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_statement.
    def enterFixed_statement(self, ctx:CSharpParser.Fixed_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_statement.
    def exitFixed_statement(self, ctx:CSharpParser.Fixed_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#unsafe_statement.
    def enterUnsafe_statement(self, ctx:CSharpParser.Unsafe_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#unsafe_statement.
    def exitUnsafe_statement(self, ctx:CSharpParser.Unsafe_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#try_statement.
    def enterTry_statement(self, ctx:CSharpParser.Try_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#try_statement.
    def exitTry_statement(self, ctx:CSharpParser.Try_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#block.
    def enterBlock(self, ctx:CSharpParser.BlockContext):
        pass

    # Exit a parse tree produced by CSharpParser#block.
    def exitBlock(self, ctx:CSharpParser.BlockContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_variable_declaration.
    def enterLocal_variable_declaration(self, ctx:CSharpParser.Local_variable_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_variable_declaration.
    def exitLocal_variable_declaration(self, ctx:CSharpParser.Local_variable_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#unsafe_function_pointer.
    def enterUnsafe_function_pointer(self, ctx:CSharpParser.Unsafe_function_pointerContext):
        pass

    # Exit a parse tree produced by CSharpParser#unsafe_function_pointer.
    def exitUnsafe_function_pointer(self, ctx:CSharpParser.Unsafe_function_pointerContext):
        pass


    # Enter a parse tree produced by CSharpParser#delegate_function_pointer.
    def enterDelegate_function_pointer(self, ctx:CSharpParser.Delegate_function_pointerContext):
        pass

    # Exit a parse tree produced by CSharpParser#delegate_function_pointer.
    def exitDelegate_function_pointer(self, ctx:CSharpParser.Delegate_function_pointerContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_variable_type.
    def enterLocal_variable_type(self, ctx:CSharpParser.Local_variable_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_variable_type.
    def exitLocal_variable_type(self, ctx:CSharpParser.Local_variable_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_variable_declarator.
    def enterLocal_variable_declarator(self, ctx:CSharpParser.Local_variable_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_variable_declarator.
    def exitLocal_variable_declarator(self, ctx:CSharpParser.Local_variable_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_variable_initializer.
    def enterLocal_variable_initializer(self, ctx:CSharpParser.Local_variable_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_variable_initializer.
    def exitLocal_variable_initializer(self, ctx:CSharpParser.Local_variable_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_constant_declaration.
    def enterLocal_constant_declaration(self, ctx:CSharpParser.Local_constant_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_constant_declaration.
    def exitLocal_constant_declaration(self, ctx:CSharpParser.Local_constant_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#switch_section.
    def enterSwitch_section(self, ctx:CSharpParser.Switch_sectionContext):
        pass

    # Exit a parse tree produced by CSharpParser#switch_section.
    def exitSwitch_section(self, ctx:CSharpParser.Switch_sectionContext):
        pass


    # Enter a parse tree produced by CSharpParser#switch_label.
    def enterSwitch_label(self, ctx:CSharpParser.Switch_labelContext):
        pass

    # Exit a parse tree produced by CSharpParser#switch_label.
    def exitSwitch_label(self, ctx:CSharpParser.Switch_labelContext):
        pass


    # Enter a parse tree produced by CSharpParser#case_guard.
    def enterCase_guard(self, ctx:CSharpParser.Case_guardContext):
        pass

    # Exit a parse tree produced by CSharpParser#case_guard.
    def exitCase_guard(self, ctx:CSharpParser.Case_guardContext):
        pass


    # Enter a parse tree produced by CSharpParser#statement_list.
    def enterStatement_list(self, ctx:CSharpParser.Statement_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#statement_list.
    def exitStatement_list(self, ctx:CSharpParser.Statement_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#for_initializer.
    def enterFor_initializer(self, ctx:CSharpParser.For_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#for_initializer.
    def exitFor_initializer(self, ctx:CSharpParser.For_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#for_iterator.
    def enterFor_iterator(self, ctx:CSharpParser.For_iteratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#for_iterator.
    def exitFor_iterator(self, ctx:CSharpParser.For_iteratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#catch_clauses.
    def enterCatch_clauses(self, ctx:CSharpParser.Catch_clausesContext):
        pass

    # Exit a parse tree produced by CSharpParser#catch_clauses.
    def exitCatch_clauses(self, ctx:CSharpParser.Catch_clausesContext):
        pass


    # Enter a parse tree produced by CSharpParser#specific_catch_clause.
    def enterSpecific_catch_clause(self, ctx:CSharpParser.Specific_catch_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#specific_catch_clause.
    def exitSpecific_catch_clause(self, ctx:CSharpParser.Specific_catch_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#general_catch_clause.
    def enterGeneral_catch_clause(self, ctx:CSharpParser.General_catch_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#general_catch_clause.
    def exitGeneral_catch_clause(self, ctx:CSharpParser.General_catch_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#exception_filter.
    def enterException_filter(self, ctx:CSharpParser.Exception_filterContext):
        pass

    # Exit a parse tree produced by CSharpParser#exception_filter.
    def exitException_filter(self, ctx:CSharpParser.Exception_filterContext):
        pass


    # Enter a parse tree produced by CSharpParser#finally_clause.
    def enterFinally_clause(self, ctx:CSharpParser.Finally_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#finally_clause.
    def exitFinally_clause(self, ctx:CSharpParser.Finally_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#resource_acquisition.
    def enterResource_acquisition(self, ctx:CSharpParser.Resource_acquisitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#resource_acquisition.
    def exitResource_acquisition(self, ctx:CSharpParser.Resource_acquisitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_declaration.
    def enterNamespace_declaration(self, ctx:CSharpParser.Namespace_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_declaration.
    def exitNamespace_declaration(self, ctx:CSharpParser.Namespace_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#qualified_identifier.
    def enterQualified_identifier(self, ctx:CSharpParser.Qualified_identifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#qualified_identifier.
    def exitQualified_identifier(self, ctx:CSharpParser.Qualified_identifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_body.
    def enterNamespace_body(self, ctx:CSharpParser.Namespace_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_body.
    def exitNamespace_body(self, ctx:CSharpParser.Namespace_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#extern_alias_directives.
    def enterExtern_alias_directives(self, ctx:CSharpParser.Extern_alias_directivesContext):
        pass

    # Exit a parse tree produced by CSharpParser#extern_alias_directives.
    def exitExtern_alias_directives(self, ctx:CSharpParser.Extern_alias_directivesContext):
        pass


    # Enter a parse tree produced by CSharpParser#extern_alias_directive.
    def enterExtern_alias_directive(self, ctx:CSharpParser.Extern_alias_directiveContext):
        pass

    # Exit a parse tree produced by CSharpParser#extern_alias_directive.
    def exitExtern_alias_directive(self, ctx:CSharpParser.Extern_alias_directiveContext):
        pass


    # Enter a parse tree produced by CSharpParser#using_directives.
    def enterUsing_directives(self, ctx:CSharpParser.Using_directivesContext):
        pass

    # Exit a parse tree produced by CSharpParser#using_directives.
    def exitUsing_directives(self, ctx:CSharpParser.Using_directivesContext):
        pass


    # Enter a parse tree produced by CSharpParser#usingAliasDirective.
    def enterUsingAliasDirective(self, ctx:CSharpParser.UsingAliasDirectiveContext):
        pass

    # Exit a parse tree produced by CSharpParser#usingAliasDirective.
    def exitUsingAliasDirective(self, ctx:CSharpParser.UsingAliasDirectiveContext):
        pass


    # Enter a parse tree produced by CSharpParser#usingNamespaceDirective.
    def enterUsingNamespaceDirective(self, ctx:CSharpParser.UsingNamespaceDirectiveContext):
        pass

    # Exit a parse tree produced by CSharpParser#usingNamespaceDirective.
    def exitUsingNamespaceDirective(self, ctx:CSharpParser.UsingNamespaceDirectiveContext):
        pass


    # Enter a parse tree produced by CSharpParser#usingStaticDirective.
    def enterUsingStaticDirective(self, ctx:CSharpParser.UsingStaticDirectiveContext):
        pass

    # Exit a parse tree produced by CSharpParser#usingStaticDirective.
    def exitUsingStaticDirective(self, ctx:CSharpParser.UsingStaticDirectiveContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_member_declarations.
    def enterNamespace_member_declarations(self, ctx:CSharpParser.Namespace_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_member_declarations.
    def exitNamespace_member_declarations(self, ctx:CSharpParser.Namespace_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_member_declaration.
    def enterNamespace_member_declaration(self, ctx:CSharpParser.Namespace_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_member_declaration.
    def exitNamespace_member_declaration(self, ctx:CSharpParser.Namespace_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_declaration.
    def enterType_declaration(self, ctx:CSharpParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_declaration.
    def exitType_declaration(self, ctx:CSharpParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#record_definition.
    def enterRecord_definition(self, ctx:CSharpParser.Record_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#record_definition.
    def exitRecord_definition(self, ctx:CSharpParser.Record_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#record_base.
    def enterRecord_base(self, ctx:CSharpParser.Record_baseContext):
        pass

    # Exit a parse tree produced by CSharpParser#record_base.
    def exitRecord_base(self, ctx:CSharpParser.Record_baseContext):
        pass


    # Enter a parse tree produced by CSharpParser#record_body.
    def enterRecord_body(self, ctx:CSharpParser.Record_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#record_body.
    def exitRecord_body(self, ctx:CSharpParser.Record_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#record_parameters.
    def enterRecord_parameters(self, ctx:CSharpParser.Record_parametersContext):
        pass

    # Exit a parse tree produced by CSharpParser#record_parameters.
    def exitRecord_parameters(self, ctx:CSharpParser.Record_parametersContext):
        pass


    # Enter a parse tree produced by CSharpParser#record_parameter.
    def enterRecord_parameter(self, ctx:CSharpParser.Record_parameterContext):
        pass

    # Exit a parse tree produced by CSharpParser#record_parameter.
    def exitRecord_parameter(self, ctx:CSharpParser.Record_parameterContext):
        pass


    # Enter a parse tree produced by CSharpParser#qualified_alias_member.
    def enterQualified_alias_member(self, ctx:CSharpParser.Qualified_alias_memberContext):
        pass

    # Exit a parse tree produced by CSharpParser#qualified_alias_member.
    def exitQualified_alias_member(self, ctx:CSharpParser.Qualified_alias_memberContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_parameter_list.
    def enterType_parameter_list(self, ctx:CSharpParser.Type_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_parameter_list.
    def exitType_parameter_list(self, ctx:CSharpParser.Type_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_parameter.
    def enterType_parameter(self, ctx:CSharpParser.Type_parameterContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_parameter.
    def exitType_parameter(self, ctx:CSharpParser.Type_parameterContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_base.
    def enterClass_base(self, ctx:CSharpParser.Class_baseContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_base.
    def exitClass_base(self, ctx:CSharpParser.Class_baseContext):
        pass


    # Enter a parse tree produced by CSharpParser#interface_type_list.
    def enterInterface_type_list(self, ctx:CSharpParser.Interface_type_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#interface_type_list.
    def exitInterface_type_list(self, ctx:CSharpParser.Interface_type_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_parameter_constraints_clauses.
    def enterType_parameter_constraints_clauses(self, ctx:CSharpParser.Type_parameter_constraints_clausesContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_parameter_constraints_clauses.
    def exitType_parameter_constraints_clauses(self, ctx:CSharpParser.Type_parameter_constraints_clausesContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_parameter_constraints_clause.
    def enterType_parameter_constraints_clause(self, ctx:CSharpParser.Type_parameter_constraints_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_parameter_constraints_clause.
    def exitType_parameter_constraints_clause(self, ctx:CSharpParser.Type_parameter_constraints_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_parameter_constraints.
    def enterType_parameter_constraints(self, ctx:CSharpParser.Type_parameter_constraintsContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_parameter_constraints.
    def exitType_parameter_constraints(self, ctx:CSharpParser.Type_parameter_constraintsContext):
        pass


    # Enter a parse tree produced by CSharpParser#primary_constraint.
    def enterPrimary_constraint(self, ctx:CSharpParser.Primary_constraintContext):
        pass

    # Exit a parse tree produced by CSharpParser#primary_constraint.
    def exitPrimary_constraint(self, ctx:CSharpParser.Primary_constraintContext):
        pass


    # Enter a parse tree produced by CSharpParser#pattern.
    def enterPattern(self, ctx:CSharpParser.PatternContext):
        pass

    # Exit a parse tree produced by CSharpParser#pattern.
    def exitPattern(self, ctx:CSharpParser.PatternContext):
        pass


    # Enter a parse tree produced by CSharpParser#rest_pattern.
    def enterRest_pattern(self, ctx:CSharpParser.Rest_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#rest_pattern.
    def exitRest_pattern(self, ctx:CSharpParser.Rest_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#list_pattern.
    def enterList_pattern(self, ctx:CSharpParser.List_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#list_pattern.
    def exitList_pattern(self, ctx:CSharpParser.List_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#pattern_items.
    def enterPattern_items(self, ctx:CSharpParser.Pattern_itemsContext):
        pass

    # Exit a parse tree produced by CSharpParser#pattern_items.
    def exitPattern_items(self, ctx:CSharpParser.Pattern_itemsContext):
        pass


    # Enter a parse tree produced by CSharpParser#is_pattern.
    def enterIs_pattern(self, ctx:CSharpParser.Is_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#is_pattern.
    def exitIs_pattern(self, ctx:CSharpParser.Is_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#property_pattern.
    def enterProperty_pattern(self, ctx:CSharpParser.Property_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#property_pattern.
    def exitProperty_pattern(self, ctx:CSharpParser.Property_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#property_pattern_clause.
    def enterProperty_pattern_clause(self, ctx:CSharpParser.Property_pattern_clauseContext):
        pass

    # Exit a parse tree produced by CSharpParser#property_pattern_clause.
    def exitProperty_pattern_clause(self, ctx:CSharpParser.Property_pattern_clauseContext):
        pass


    # Enter a parse tree produced by CSharpParser#relational_pattern.
    def enterRelational_pattern(self, ctx:CSharpParser.Relational_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#relational_pattern.
    def exitRelational_pattern(self, ctx:CSharpParser.Relational_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#and_pattern.
    def enterAnd_pattern(self, ctx:CSharpParser.And_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#and_pattern.
    def exitAnd_pattern(self, ctx:CSharpParser.And_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#or_pattern.
    def enterOr_pattern(self, ctx:CSharpParser.Or_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#or_pattern.
    def exitOr_pattern(self, ctx:CSharpParser.Or_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#not_pattern.
    def enterNot_pattern(self, ctx:CSharpParser.Not_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#not_pattern.
    def exitNot_pattern(self, ctx:CSharpParser.Not_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#declaration_pattern.
    def enterDeclaration_pattern(self, ctx:CSharpParser.Declaration_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#declaration_pattern.
    def exitDeclaration_pattern(self, ctx:CSharpParser.Declaration_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#simple_designation.
    def enterSimple_designation(self, ctx:CSharpParser.Simple_designationContext):
        pass

    # Exit a parse tree produced by CSharpParser#simple_designation.
    def exitSimple_designation(self, ctx:CSharpParser.Simple_designationContext):
        pass


    # Enter a parse tree produced by CSharpParser#single_variable_designation.
    def enterSingle_variable_designation(self, ctx:CSharpParser.Single_variable_designationContext):
        pass

    # Exit a parse tree produced by CSharpParser#single_variable_designation.
    def exitSingle_variable_designation(self, ctx:CSharpParser.Single_variable_designationContext):
        pass


    # Enter a parse tree produced by CSharpParser#constant_pattern.
    def enterConstant_pattern(self, ctx:CSharpParser.Constant_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#constant_pattern.
    def exitConstant_pattern(self, ctx:CSharpParser.Constant_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#var_pattern.
    def enterVar_pattern(self, ctx:CSharpParser.Var_patternContext):
        pass

    # Exit a parse tree produced by CSharpParser#var_pattern.
    def exitVar_pattern(self, ctx:CSharpParser.Var_patternContext):
        pass


    # Enter a parse tree produced by CSharpParser#designation.
    def enterDesignation(self, ctx:CSharpParser.DesignationContext):
        pass

    # Exit a parse tree produced by CSharpParser#designation.
    def exitDesignation(self, ctx:CSharpParser.DesignationContext):
        pass


    # Enter a parse tree produced by CSharpParser#module_initializer_declaration.
    def enterModule_initializer_declaration(self, ctx:CSharpParser.Module_initializer_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#module_initializer_declaration.
    def exitModule_initializer_declaration(self, ctx:CSharpParser.Module_initializer_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#secondary_constraints.
    def enterSecondary_constraints(self, ctx:CSharpParser.Secondary_constraintsContext):
        pass

    # Exit a parse tree produced by CSharpParser#secondary_constraints.
    def exitSecondary_constraints(self, ctx:CSharpParser.Secondary_constraintsContext):
        pass


    # Enter a parse tree produced by CSharpParser#constructor_constraint.
    def enterConstructor_constraint(self, ctx:CSharpParser.Constructor_constraintContext):
        pass

    # Exit a parse tree produced by CSharpParser#constructor_constraint.
    def exitConstructor_constraint(self, ctx:CSharpParser.Constructor_constraintContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_body.
    def enterClass_body(self, ctx:CSharpParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_body.
    def exitClass_body(self, ctx:CSharpParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_member_declarations.
    def enterClass_member_declarations(self, ctx:CSharpParser.Class_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_member_declarations.
    def exitClass_member_declarations(self, ctx:CSharpParser.Class_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_member_declaration.
    def enterClass_member_declaration(self, ctx:CSharpParser.Class_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_member_declaration.
    def exitClass_member_declaration(self, ctx:CSharpParser.Class_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#all_member_modifiers.
    def enterAll_member_modifiers(self, ctx:CSharpParser.All_member_modifiersContext):
        pass

    # Exit a parse tree produced by CSharpParser#all_member_modifiers.
    def exitAll_member_modifiers(self, ctx:CSharpParser.All_member_modifiersContext):
        pass


    # Enter a parse tree produced by CSharpParser#all_member_modifier.
    def enterAll_member_modifier(self, ctx:CSharpParser.All_member_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#all_member_modifier.
    def exitAll_member_modifier(self, ctx:CSharpParser.All_member_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#common_member_declaration.
    def enterCommon_member_declaration(self, ctx:CSharpParser.Common_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#common_member_declaration.
    def exitCommon_member_declaration(self, ctx:CSharpParser.Common_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#typed_member_declaration.
    def enterTyped_member_declaration(self, ctx:CSharpParser.Typed_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#typed_member_declaration.
    def exitTyped_member_declaration(self, ctx:CSharpParser.Typed_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#constant_declarators.
    def enterConstant_declarators(self, ctx:CSharpParser.Constant_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharpParser#constant_declarators.
    def exitConstant_declarators(self, ctx:CSharpParser.Constant_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharpParser#constant_declarator.
    def enterConstant_declarator(self, ctx:CSharpParser.Constant_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#constant_declarator.
    def exitConstant_declarator(self, ctx:CSharpParser.Constant_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#variable_declarators.
    def enterVariable_declarators(self, ctx:CSharpParser.Variable_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharpParser#variable_declarators.
    def exitVariable_declarators(self, ctx:CSharpParser.Variable_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharpParser#variable_declarator.
    def enterVariable_declarator(self, ctx:CSharpParser.Variable_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#variable_declarator.
    def exitVariable_declarator(self, ctx:CSharpParser.Variable_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#variable_initializer.
    def enterVariable_initializer(self, ctx:CSharpParser.Variable_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#variable_initializer.
    def exitVariable_initializer(self, ctx:CSharpParser.Variable_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#return_type.
    def enterReturn_type(self, ctx:CSharpParser.Return_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#return_type.
    def exitReturn_type(self, ctx:CSharpParser.Return_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#member_name.
    def enterMember_name(self, ctx:CSharpParser.Member_nameContext):
        pass

    # Exit a parse tree produced by CSharpParser#member_name.
    def exitMember_name(self, ctx:CSharpParser.Member_nameContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_body.
    def enterMethod_body(self, ctx:CSharpParser.Method_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_body.
    def exitMethod_body(self, ctx:CSharpParser.Method_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#formal_parameter_list.
    def enterFormal_parameter_list(self, ctx:CSharpParser.Formal_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#formal_parameter_list.
    def exitFormal_parameter_list(self, ctx:CSharpParser.Formal_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_parameters.
    def enterFixed_parameters(self, ctx:CSharpParser.Fixed_parametersContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_parameters.
    def exitFixed_parameters(self, ctx:CSharpParser.Fixed_parametersContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_parameter.
    def enterFixed_parameter(self, ctx:CSharpParser.Fixed_parameterContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_parameter.
    def exitFixed_parameter(self, ctx:CSharpParser.Fixed_parameterContext):
        pass


    # Enter a parse tree produced by CSharpParser#parameter_modifier.
    def enterParameter_modifier(self, ctx:CSharpParser.Parameter_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#parameter_modifier.
    def exitParameter_modifier(self, ctx:CSharpParser.Parameter_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#parameter_array.
    def enterParameter_array(self, ctx:CSharpParser.Parameter_arrayContext):
        pass

    # Exit a parse tree produced by CSharpParser#parameter_array.
    def exitParameter_array(self, ctx:CSharpParser.Parameter_arrayContext):
        pass


    # Enter a parse tree produced by CSharpParser#accessor_declarations.
    def enterAccessor_declarations(self, ctx:CSharpParser.Accessor_declarationsContext):
        pass

    # Exit a parse tree produced by CSharpParser#accessor_declarations.
    def exitAccessor_declarations(self, ctx:CSharpParser.Accessor_declarationsContext):
        pass


    # Enter a parse tree produced by CSharpParser#init_accessor_declaration.
    def enterInit_accessor_declaration(self, ctx:CSharpParser.Init_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#init_accessor_declaration.
    def exitInit_accessor_declaration(self, ctx:CSharpParser.Init_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#get_accessor_declaration.
    def enterGet_accessor_declaration(self, ctx:CSharpParser.Get_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#get_accessor_declaration.
    def exitGet_accessor_declaration(self, ctx:CSharpParser.Get_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#set_accessor_declaration.
    def enterSet_accessor_declaration(self, ctx:CSharpParser.Set_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#set_accessor_declaration.
    def exitSet_accessor_declaration(self, ctx:CSharpParser.Set_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#accessor_modifier.
    def enterAccessor_modifier(self, ctx:CSharpParser.Accessor_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#accessor_modifier.
    def exitAccessor_modifier(self, ctx:CSharpParser.Accessor_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#accessor_body.
    def enterAccessor_body(self, ctx:CSharpParser.Accessor_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#accessor_body.
    def exitAccessor_body(self, ctx:CSharpParser.Accessor_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#event_accessor_declarations.
    def enterEvent_accessor_declarations(self, ctx:CSharpParser.Event_accessor_declarationsContext):
        pass

    # Exit a parse tree produced by CSharpParser#event_accessor_declarations.
    def exitEvent_accessor_declarations(self, ctx:CSharpParser.Event_accessor_declarationsContext):
        pass


    # Enter a parse tree produced by CSharpParser#add_accessor_declaration.
    def enterAdd_accessor_declaration(self, ctx:CSharpParser.Add_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#add_accessor_declaration.
    def exitAdd_accessor_declaration(self, ctx:CSharpParser.Add_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#remove_accessor_declaration.
    def enterRemove_accessor_declaration(self, ctx:CSharpParser.Remove_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#remove_accessor_declaration.
    def exitRemove_accessor_declaration(self, ctx:CSharpParser.Remove_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#overloadable_operator.
    def enterOverloadable_operator(self, ctx:CSharpParser.Overloadable_operatorContext):
        pass

    # Exit a parse tree produced by CSharpParser#overloadable_operator.
    def exitOverloadable_operator(self, ctx:CSharpParser.Overloadable_operatorContext):
        pass


    # Enter a parse tree produced by CSharpParser#conversion_operator_declarator.
    def enterConversion_operator_declarator(self, ctx:CSharpParser.Conversion_operator_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#conversion_operator_declarator.
    def exitConversion_operator_declarator(self, ctx:CSharpParser.Conversion_operator_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#constructor_initializer.
    def enterConstructor_initializer(self, ctx:CSharpParser.Constructor_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#constructor_initializer.
    def exitConstructor_initializer(self, ctx:CSharpParser.Constructor_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#body.
    def enterBody(self, ctx:CSharpParser.BodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#body.
    def exitBody(self, ctx:CSharpParser.BodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#struct_interfaces.
    def enterStruct_interfaces(self, ctx:CSharpParser.Struct_interfacesContext):
        pass

    # Exit a parse tree produced by CSharpParser#struct_interfaces.
    def exitStruct_interfaces(self, ctx:CSharpParser.Struct_interfacesContext):
        pass


    # Enter a parse tree produced by CSharpParser#struct_body.
    def enterStruct_body(self, ctx:CSharpParser.Struct_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#struct_body.
    def exitStruct_body(self, ctx:CSharpParser.Struct_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#struct_member_declaration.
    def enterStruct_member_declaration(self, ctx:CSharpParser.Struct_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#struct_member_declaration.
    def exitStruct_member_declaration(self, ctx:CSharpParser.Struct_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#array_type.
    def enterArray_type(self, ctx:CSharpParser.Array_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#array_type.
    def exitArray_type(self, ctx:CSharpParser.Array_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#rank_specifier.
    def enterRank_specifier(self, ctx:CSharpParser.Rank_specifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#rank_specifier.
    def exitRank_specifier(self, ctx:CSharpParser.Rank_specifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#array_initializer.
    def enterArray_initializer(self, ctx:CSharpParser.Array_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#array_initializer.
    def exitArray_initializer(self, ctx:CSharpParser.Array_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#variant_type_parameter_list.
    def enterVariant_type_parameter_list(self, ctx:CSharpParser.Variant_type_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#variant_type_parameter_list.
    def exitVariant_type_parameter_list(self, ctx:CSharpParser.Variant_type_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#variant_type_parameter.
    def enterVariant_type_parameter(self, ctx:CSharpParser.Variant_type_parameterContext):
        pass

    # Exit a parse tree produced by CSharpParser#variant_type_parameter.
    def exitVariant_type_parameter(self, ctx:CSharpParser.Variant_type_parameterContext):
        pass


    # Enter a parse tree produced by CSharpParser#variance_annotation.
    def enterVariance_annotation(self, ctx:CSharpParser.Variance_annotationContext):
        pass

    # Exit a parse tree produced by CSharpParser#variance_annotation.
    def exitVariance_annotation(self, ctx:CSharpParser.Variance_annotationContext):
        pass


    # Enter a parse tree produced by CSharpParser#interface_base.
    def enterInterface_base(self, ctx:CSharpParser.Interface_baseContext):
        pass

    # Exit a parse tree produced by CSharpParser#interface_base.
    def exitInterface_base(self, ctx:CSharpParser.Interface_baseContext):
        pass


    # Enter a parse tree produced by CSharpParser#interface_body.
    def enterInterface_body(self, ctx:CSharpParser.Interface_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#interface_body.
    def exitInterface_body(self, ctx:CSharpParser.Interface_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#interface_member_declaration.
    def enterInterface_member_declaration(self, ctx:CSharpParser.Interface_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#interface_member_declaration.
    def exitInterface_member_declaration(self, ctx:CSharpParser.Interface_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#interface_accessors.
    def enterInterface_accessors(self, ctx:CSharpParser.Interface_accessorsContext):
        pass

    # Exit a parse tree produced by CSharpParser#interface_accessors.
    def exitInterface_accessors(self, ctx:CSharpParser.Interface_accessorsContext):
        pass


    # Enter a parse tree produced by CSharpParser#enum_base.
    def enterEnum_base(self, ctx:CSharpParser.Enum_baseContext):
        pass

    # Exit a parse tree produced by CSharpParser#enum_base.
    def exitEnum_base(self, ctx:CSharpParser.Enum_baseContext):
        pass


    # Enter a parse tree produced by CSharpParser#enum_body.
    def enterEnum_body(self, ctx:CSharpParser.Enum_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#enum_body.
    def exitEnum_body(self, ctx:CSharpParser.Enum_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#enum_member_declaration.
    def enterEnum_member_declaration(self, ctx:CSharpParser.Enum_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#enum_member_declaration.
    def exitEnum_member_declaration(self, ctx:CSharpParser.Enum_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#global_attribute_section.
    def enterGlobal_attribute_section(self, ctx:CSharpParser.Global_attribute_sectionContext):
        pass

    # Exit a parse tree produced by CSharpParser#global_attribute_section.
    def exitGlobal_attribute_section(self, ctx:CSharpParser.Global_attribute_sectionContext):
        pass


    # Enter a parse tree produced by CSharpParser#global_attribute_target.
    def enterGlobal_attribute_target(self, ctx:CSharpParser.Global_attribute_targetContext):
        pass

    # Exit a parse tree produced by CSharpParser#global_attribute_target.
    def exitGlobal_attribute_target(self, ctx:CSharpParser.Global_attribute_targetContext):
        pass


    # Enter a parse tree produced by CSharpParser#attributes.
    def enterAttributes(self, ctx:CSharpParser.AttributesContext):
        pass

    # Exit a parse tree produced by CSharpParser#attributes.
    def exitAttributes(self, ctx:CSharpParser.AttributesContext):
        pass


    # Enter a parse tree produced by CSharpParser#attribute_section.
    def enterAttribute_section(self, ctx:CSharpParser.Attribute_sectionContext):
        pass

    # Exit a parse tree produced by CSharpParser#attribute_section.
    def exitAttribute_section(self, ctx:CSharpParser.Attribute_sectionContext):
        pass


    # Enter a parse tree produced by CSharpParser#attribute_target.
    def enterAttribute_target(self, ctx:CSharpParser.Attribute_targetContext):
        pass

    # Exit a parse tree produced by CSharpParser#attribute_target.
    def exitAttribute_target(self, ctx:CSharpParser.Attribute_targetContext):
        pass


    # Enter a parse tree produced by CSharpParser#attribute_list.
    def enterAttribute_list(self, ctx:CSharpParser.Attribute_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#attribute_list.
    def exitAttribute_list(self, ctx:CSharpParser.Attribute_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#attribute.
    def enterAttribute(self, ctx:CSharpParser.AttributeContext):
        pass

    # Exit a parse tree produced by CSharpParser#attribute.
    def exitAttribute(self, ctx:CSharpParser.AttributeContext):
        pass


    # Enter a parse tree produced by CSharpParser#attribute_argument.
    def enterAttribute_argument(self, ctx:CSharpParser.Attribute_argumentContext):
        pass

    # Exit a parse tree produced by CSharpParser#attribute_argument.
    def exitAttribute_argument(self, ctx:CSharpParser.Attribute_argumentContext):
        pass


    # Enter a parse tree produced by CSharpParser#pointer_type.
    def enterPointer_type(self, ctx:CSharpParser.Pointer_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#pointer_type.
    def exitPointer_type(self, ctx:CSharpParser.Pointer_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_pointer_declarators.
    def enterFixed_pointer_declarators(self, ctx:CSharpParser.Fixed_pointer_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_pointer_declarators.
    def exitFixed_pointer_declarators(self, ctx:CSharpParser.Fixed_pointer_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_pointer_declarator.
    def enterFixed_pointer_declarator(self, ctx:CSharpParser.Fixed_pointer_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_pointer_declarator.
    def exitFixed_pointer_declarator(self, ctx:CSharpParser.Fixed_pointer_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_pointer_initializer.
    def enterFixed_pointer_initializer(self, ctx:CSharpParser.Fixed_pointer_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_pointer_initializer.
    def exitFixed_pointer_initializer(self, ctx:CSharpParser.Fixed_pointer_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#fixed_size_buffer_declarator.
    def enterFixed_size_buffer_declarator(self, ctx:CSharpParser.Fixed_size_buffer_declaratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#fixed_size_buffer_declarator.
    def exitFixed_size_buffer_declarator(self, ctx:CSharpParser.Fixed_size_buffer_declaratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#right_arrow.
    def enterRight_arrow(self, ctx:CSharpParser.Right_arrowContext):
        pass

    # Exit a parse tree produced by CSharpParser#right_arrow.
    def exitRight_arrow(self, ctx:CSharpParser.Right_arrowContext):
        pass


    # Enter a parse tree produced by CSharpParser#right_shift.
    def enterRight_shift(self, ctx:CSharpParser.Right_shiftContext):
        pass

    # Exit a parse tree produced by CSharpParser#right_shift.
    def exitRight_shift(self, ctx:CSharpParser.Right_shiftContext):
        pass


    # Enter a parse tree produced by CSharpParser#right_shift_assignment.
    def enterRight_shift_assignment(self, ctx:CSharpParser.Right_shift_assignmentContext):
        pass

    # Exit a parse tree produced by CSharpParser#right_shift_assignment.
    def exitRight_shift_assignment(self, ctx:CSharpParser.Right_shift_assignmentContext):
        pass


    # Enter a parse tree produced by CSharpParser#literal.
    def enterLiteral(self, ctx:CSharpParser.LiteralContext):
        pass

    # Exit a parse tree produced by CSharpParser#literal.
    def exitLiteral(self, ctx:CSharpParser.LiteralContext):
        pass


    # Enter a parse tree produced by CSharpParser#utf8_string_literal.
    def enterUtf8_string_literal(self, ctx:CSharpParser.Utf8_string_literalContext):
        pass

    # Exit a parse tree produced by CSharpParser#utf8_string_literal.
    def exitUtf8_string_literal(self, ctx:CSharpParser.Utf8_string_literalContext):
        pass


    # Enter a parse tree produced by CSharpParser#boolean_literal.
    def enterBoolean_literal(self, ctx:CSharpParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by CSharpParser#boolean_literal.
    def exitBoolean_literal(self, ctx:CSharpParser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by CSharpParser#string_literal.
    def enterString_literal(self, ctx:CSharpParser.String_literalContext):
        pass

    # Exit a parse tree produced by CSharpParser#string_literal.
    def exitString_literal(self, ctx:CSharpParser.String_literalContext):
        pass


    # Enter a parse tree produced by CSharpParser#interpolated_regular_string.
    def enterInterpolated_regular_string(self, ctx:CSharpParser.Interpolated_regular_stringContext):
        pass

    # Exit a parse tree produced by CSharpParser#interpolated_regular_string.
    def exitInterpolated_regular_string(self, ctx:CSharpParser.Interpolated_regular_stringContext):
        pass


    # Enter a parse tree produced by CSharpParser#interpolated_verbatium_string.
    def enterInterpolated_verbatium_string(self, ctx:CSharpParser.Interpolated_verbatium_stringContext):
        pass

    # Exit a parse tree produced by CSharpParser#interpolated_verbatium_string.
    def exitInterpolated_verbatium_string(self, ctx:CSharpParser.Interpolated_verbatium_stringContext):
        pass


    # Enter a parse tree produced by CSharpParser#interpolated_regular_string_part.
    def enterInterpolated_regular_string_part(self, ctx:CSharpParser.Interpolated_regular_string_partContext):
        pass

    # Exit a parse tree produced by CSharpParser#interpolated_regular_string_part.
    def exitInterpolated_regular_string_part(self, ctx:CSharpParser.Interpolated_regular_string_partContext):
        pass


    # Enter a parse tree produced by CSharpParser#interpolated_verbatium_string_part.
    def enterInterpolated_verbatium_string_part(self, ctx:CSharpParser.Interpolated_verbatium_string_partContext):
        pass

    # Exit a parse tree produced by CSharpParser#interpolated_verbatium_string_part.
    def exitInterpolated_verbatium_string_part(self, ctx:CSharpParser.Interpolated_verbatium_string_partContext):
        pass


    # Enter a parse tree produced by CSharpParser#interpolated_string_expression.
    def enterInterpolated_string_expression(self, ctx:CSharpParser.Interpolated_string_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#interpolated_string_expression.
    def exitInterpolated_string_expression(self, ctx:CSharpParser.Interpolated_string_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#interpolation_minimum_width.
    def enterInterpolation_minimum_width(self, ctx:CSharpParser.Interpolation_minimum_widthContext):
        pass

    # Exit a parse tree produced by CSharpParser#interpolation_minimum_width.
    def exitInterpolation_minimum_width(self, ctx:CSharpParser.Interpolation_minimum_widthContext):
        pass


    # Enter a parse tree produced by CSharpParser#format_string.
    def enterFormat_string(self, ctx:CSharpParser.Format_stringContext):
        pass

    # Exit a parse tree produced by CSharpParser#format_string.
    def exitFormat_string(self, ctx:CSharpParser.Format_stringContext):
        pass


    # Enter a parse tree produced by CSharpParser#constant_expression.
    def enterConstant_expression(self, ctx:CSharpParser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#constant_expression.
    def exitConstant_expression(self, ctx:CSharpParser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#keyword.
    def enterKeyword(self, ctx:CSharpParser.KeywordContext):
        pass

    # Exit a parse tree produced by CSharpParser#keyword.
    def exitKeyword(self, ctx:CSharpParser.KeywordContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_definition.
    def enterClass_definition(self, ctx:CSharpParser.Class_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_definition.
    def exitClass_definition(self, ctx:CSharpParser.Class_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#primary_constructor_parameters.
    def enterPrimary_constructor_parameters(self, ctx:CSharpParser.Primary_constructor_parametersContext):
        pass

    # Exit a parse tree produced by CSharpParser#primary_constructor_parameters.
    def exitPrimary_constructor_parameters(self, ctx:CSharpParser.Primary_constructor_parametersContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_modifier.
    def enterClass_modifier(self, ctx:CSharpParser.Class_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_modifier.
    def exitClass_modifier(self, ctx:CSharpParser.Class_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#struct_definition.
    def enterStruct_definition(self, ctx:CSharpParser.Struct_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#struct_definition.
    def exitStruct_definition(self, ctx:CSharpParser.Struct_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#struct_modifier.
    def enterStruct_modifier(self, ctx:CSharpParser.Struct_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#struct_modifier.
    def exitStruct_modifier(self, ctx:CSharpParser.Struct_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#interface_definition.
    def enterInterface_definition(self, ctx:CSharpParser.Interface_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#interface_definition.
    def exitInterface_definition(self, ctx:CSharpParser.Interface_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#enum_definition.
    def enterEnum_definition(self, ctx:CSharpParser.Enum_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#enum_definition.
    def exitEnum_definition(self, ctx:CSharpParser.Enum_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#delegate_definition.
    def enterDelegate_definition(self, ctx:CSharpParser.Delegate_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#delegate_definition.
    def exitDelegate_definition(self, ctx:CSharpParser.Delegate_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#event_declaration.
    def enterEvent_declaration(self, ctx:CSharpParser.Event_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#event_declaration.
    def exitEvent_declaration(self, ctx:CSharpParser.Event_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#field_declaration.
    def enterField_declaration(self, ctx:CSharpParser.Field_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#field_declaration.
    def exitField_declaration(self, ctx:CSharpParser.Field_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#property_declaration.
    def enterProperty_declaration(self, ctx:CSharpParser.Property_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#property_declaration.
    def exitProperty_declaration(self, ctx:CSharpParser.Property_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#constant_declaration.
    def enterConstant_declaration(self, ctx:CSharpParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#constant_declaration.
    def exitConstant_declaration(self, ctx:CSharpParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#indexer_declaration.
    def enterIndexer_declaration(self, ctx:CSharpParser.Indexer_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#indexer_declaration.
    def exitIndexer_declaration(self, ctx:CSharpParser.Indexer_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#destructor_definition.
    def enterDestructor_definition(self, ctx:CSharpParser.Destructor_definitionContext):
        pass

    # Exit a parse tree produced by CSharpParser#destructor_definition.
    def exitDestructor_definition(self, ctx:CSharpParser.Destructor_definitionContext):
        pass


    # Enter a parse tree produced by CSharpParser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:CSharpParser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:CSharpParser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_declaration.
    def enterMethod_declaration(self, ctx:CSharpParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_declaration.
    def exitMethod_declaration(self, ctx:CSharpParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_header.
    def enterMethod_header(self, ctx:CSharpParser.Method_headerContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_header.
    def exitMethod_header(self, ctx:CSharpParser.Method_headerContext):
        pass


    # Enter a parse tree produced by CSharpParser#ref_kind.
    def enterRef_kind(self, ctx:CSharpParser.Ref_kindContext):
        pass

    # Exit a parse tree produced by CSharpParser#ref_kind.
    def exitRef_kind(self, ctx:CSharpParser.Ref_kindContext):
        pass


    # Enter a parse tree produced by CSharpParser#ref_method_modifiers.
    def enterRef_method_modifiers(self, ctx:CSharpParser.Ref_method_modifiersContext):
        pass

    # Exit a parse tree produced by CSharpParser#ref_method_modifiers.
    def exitRef_method_modifiers(self, ctx:CSharpParser.Ref_method_modifiersContext):
        pass


    # Enter a parse tree produced by CSharpParser#ref_return_type.
    def enterRef_return_type(self, ctx:CSharpParser.Ref_return_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#ref_return_type.
    def exitRef_return_type(self, ctx:CSharpParser.Ref_return_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_modifiers.
    def enterMethod_modifiers(self, ctx:CSharpParser.Method_modifiersContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_modifiers.
    def exitMethod_modifiers(self, ctx:CSharpParser.Method_modifiersContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_modifier.
    def enterMethod_modifier(self, ctx:CSharpParser.Method_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_modifier.
    def exitMethod_modifier(self, ctx:CSharpParser.Method_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#ref_method_body.
    def enterRef_method_body(self, ctx:CSharpParser.Ref_method_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#ref_method_body.
    def exitRef_method_body(self, ctx:CSharpParser.Ref_method_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#ref_method_modifier.
    def enterRef_method_modifier(self, ctx:CSharpParser.Ref_method_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#ref_method_modifier.
    def exitRef_method_modifier(self, ctx:CSharpParser.Ref_method_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_member_name.
    def enterMethod_member_name(self, ctx:CSharpParser.Method_member_nameContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_member_name.
    def exitMethod_member_name(self, ctx:CSharpParser.Method_member_nameContext):
        pass


    # Enter a parse tree produced by CSharpParser#operator_declaration.
    def enterOperator_declaration(self, ctx:CSharpParser.Operator_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#operator_declaration.
    def exitOperator_declaration(self, ctx:CSharpParser.Operator_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#arg_declaration.
    def enterArg_declaration(self, ctx:CSharpParser.Arg_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#arg_declaration.
    def exitArg_declaration(self, ctx:CSharpParser.Arg_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_invocation.
    def enterMethod_invocation(self, ctx:CSharpParser.Method_invocationContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_invocation.
    def exitMethod_invocation(self, ctx:CSharpParser.Method_invocationContext):
        pass


    # Enter a parse tree produced by CSharpParser#object_creation_expression.
    def enterObject_creation_expression(self, ctx:CSharpParser.Object_creation_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#object_creation_expression.
    def exitObject_creation_expression(self, ctx:CSharpParser.Object_creation_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#target_typed_new.
    def enterTarget_typed_new(self, ctx:CSharpParser.Target_typed_newContext):
        pass

    # Exit a parse tree produced by CSharpParser#target_typed_new.
    def exitTarget_typed_new(self, ctx:CSharpParser.Target_typed_newContext):
        pass


    # Enter a parse tree produced by CSharpParser#identifier.
    def enterIdentifier(self, ctx:CSharpParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#identifier.
    def exitIdentifier(self, ctx:CSharpParser.IdentifierContext):
        pass



del CSharpParser