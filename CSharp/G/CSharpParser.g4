// Eclipse Public License - v 1.0, http://www.eclipse.org/legal/epl-v10.html
// Copyright (c) 2013, Christian Wulf (chwchw@gmx.de)
// Copyright (c) 2016-2017, Ivan Kochurkin (kvanttt@gmail.com), Positive Technologies.

// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar CSharpParser;

options {
    tokenVocab = CSharpLexer;
    superClass = CSharpParserBase;
}

// entry point
compilation_unit
    : BYTE_ORDER_MARK? compilation_unit_element* EOF
    ;

compilation_unit_element
    : extern_alias_directives
    | using_directives
    | global_attribute_section
    | top_level_statements
    | namespace_member_declarations
    | global_using_directives
    ;


top_level_statements
    : (statement | type_declaration)+
    ;

global_using_directives
    : global_using_directive+
    ;

global_using_directive
    : GLOBAL USING identifier '=' namespace_or_type_name ';'
    | GLOBAL USING namespace_or_type_name ';'
    | GLOBAL USING STATIC namespace_or_type_name ';'
    ;

//B.2 Syntactic grammar

//B.2.1 Basic concepts

namespace_or_type_name
    : (identifier type_argument_list? | qualified_alias_member) (
        '.' identifier type_argument_list?
    )*
    ;

//B.2.2 Types
type_
    : base_type ('?' | rank_specifier | '*')*
    | function_pointer_type
    | REF? READONLY? base_type ('<' type_argument_list '>')?
    | REF? READONLY? base_type '[' INTEGER_LITERAL ']'  
    ;

function_pointer_type
    : 'delegate' '*' '<' function_pointer_parameter_list '>'
    ;

function_pointer_parameter_list
    : type_ (',' type_)*
    ;


base_type
    : simple_type
    | class_type // represents types: enum, class, interface, delegate, type_parameter
    | VOID '*'
    | tuple_type
    ;

tuple_type
    : '(' tuple_element (',' tuple_element)+ ')'
    | deconstruction_expression
    ;

deconstruction_expression
    : 'var'? deconstruction_tuple
    ;

deconstruction_tuple
    : '(' deconstruction_element (',' deconstruction_element)+ ')'
    ;

deconstruction_element
    : deconstruction_tuple
    | identifier?
    ;

tuple_element
    : type_? identifier
    ;

simple_type
    : numeric_type
    | BOOL
    ;

numeric_type
    : integral_type
    | floating_point_type
    | DECIMAL
    ;

integral_type
    : SBYTE
    | BYTE
    | SHORT
    | USHORT
    | INT
    | UINT
    | LONG
    | ULONG
    | CHAR
    ;

floating_point_type
    : FLOAT
    | DOUBLE
    ;


// Source: §12.8.21 Default value expressions
default_value_expression
    : explictly_typed_default
    | default_literal
    ;

explictly_typed_default
    : 'default' '(' type_ ')'
    ;

default_literal
    : 'default'
    ;


// Source: §9.5 Variable references
variable_reference
    : expression
    ;


/** namespace_or_type_name, OBJECT, STRING */
class_type
    : namespace_or_type_name
    | OBJECT
    | DYNAMIC
    | STRING
    ;

type_argument_list
    : '<' type_ (',' type_)* '>'
    ;

//B.2.4 Expressions
argument_list
    : argument (',' argument)*
    ;

argument
    : argument_name? refout = (REF | OUT | IN)? (expression | (VAR | type_) expression)
    ;

argument_name
    : identifier ':'
    ;

expression
    : assignment
    | non_assignment_expression
    | REF non_assignment_expression
    | lambda_expression
    | collection_expression 
    | method_invocation

    ;

non_assignment_expression
    : lambda_expression
    | query_expression
    | conditional_expression
    ;

assignment
    : unary_expression assignment_operator expression
    | unary_expression '??=' throwable_expression
    ;

assignment_operator
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    | '%='
    | '&='
    | '|='
    | '^='
    | '<<='
    | right_shift_assignment
    ;

// Source: §12.18 Conditional operator
conditional_expression
    : null_coalescing_expression
    | null_coalescing_expression '?' expression ':' expression
    | null_coalescing_expression '?' 'ref' variable_reference ':'
      'ref' variable_reference
    ;

null_coalescing_expression
    : conditional_or_expression ('??' (null_coalescing_expression | throw_expression))?
    ;

conditional_or_expression
    : conditional_and_expression (OP_OR conditional_and_expression)*
    ;

conditional_and_expression
    : inclusive_or_expression (OP_AND inclusive_or_expression)*
    ;

inclusive_or_expression
    : exclusive_or_expression ('|' exclusive_or_expression)*
    ;

exclusive_or_expression
    : and_expression ('^' and_expression)*
    ;

and_expression
    : equality_expression ('&' equality_expression)*
    ;

equality_expression
    : relational_expression ((OP_EQ | OP_NE) relational_expression)*
    ;

relational_expression
    : shift_expression (('<' | '>' | '<=' | '>=') shift_expression | IS isType | AS isType | IS pattern)*
    ;

shift_expression
    : additive_expression (('<<' | right_shift) additive_expression)*
    ;

additive_expression
    : multiplicative_expression (('+' | '-') multiplicative_expression)*
    ;

multiplicative_expression
    : switch_expression (('*' | '/' | '%') switch_expression)*
    ;

switch_expression
    : range_expression ('switch' OPEN_BRACE (switch_expression_arms ','?)? CLOSE_BRACE)?
    ;

switch_expression_arms
    : switch_expression_arm (',' switch_expression_arm)*
    ;

switch_expression_arm
    : pattern case_guard? right_arrow throwable_expression
    ;

range_expression
    : unary_expression
    | unary_expression? OP_RANGE unary_expression?
    ;

// https://msdn.microsoft.com/library/6a71f45d(v=vs.110).aspx
unary_expression
    : cast_expression
    | primary_expression
    | '+' unary_expression
    | '-' unary_expression
    | BANG unary_expression
    | '~' unary_expression
    | '++' unary_expression
    | '--' unary_expression
    | AWAIT unary_expression // C# 5
    | '&' unary_expression
    | '*' unary_expression
    | '^' unary_expression // C# 8 ranges
    ;

cast_expression
    : OPEN_PARENS type_ CLOSE_PARENS unary_expression
    ;

collection_expression
    : '[' collection_element_list? ']'
    ;

collection_element_list
    : collection_element (',' collection_element)*
    ;

collection_element
    : expression
    | '..' expression
    ;


primary_expression // Null-conditional operators C# 6: https://msdn.microsoft.com/en-us/library/dn986595.aspx
    : pe = primary_expression_start '!'? bracket_expression* '!'? (
        (member_access | method_invocation | '++' | '--' | '->' identifier) '!'? bracket_expression* '!'?
    )*
    | tuple_type
    | default_value_expression
    | stackalloc_expression
    | collection_expression
    ;

primary_expression_start
    : literal                                                             # literalExpression
    | identifier type_argument_list?                                      # simpleNameExpression
    | OPEN_PARENS expression CLOSE_PARENS                                 # parenthesisExpressions
    | predefined_type                                                     # memberAccessExpression
    | qualified_alias_member                                              # memberAccessExpression
    | LITERAL_ACCESS                                                      # literalAccessExpression
    | THIS                                                                # thisReferenceExpression
    | BASE ('.' identifier type_argument_list? | '[' expression_list ']') # baseAccessExpression
    | NEW (
        type_ (
            object_creation_expression
            | object_or_collection_initializer
            | '[' expression_list ']' rank_specifier* array_initializer?
            | rank_specifier+ array_initializer
        )
        | anonymous_object_initializer
        | rank_specifier array_initializer
    )?                                                                                               # objectCreationExpression
    | NEW target_typed_new                                # targetTypedNewExpression
    | OPEN_PARENS argument ( ',' argument)+ CLOSE_PARENS                                            # tupleExpression
    | TYPEOF OPEN_PARENS (unbound_type_name | type_ | VOID) CLOSE_PARENS                            # typeofExpression
    | CHECKED OPEN_PARENS expression CLOSE_PARENS                                                   # checkedExpression
    | UNCHECKED OPEN_PARENS expression CLOSE_PARENS                                                 # uncheckedExpression
    | DEFAULT (OPEN_PARENS type_ CLOSE_PARENS)?                                                     # defaultValueExpression
    | ASYNC? DELEGATE (OPEN_PARENS explicit_anonymous_function_parameter_list? CLOSE_PARENS)? block # anonymousMethodExpression
    | SIZEOF OPEN_PARENS type_ CLOSE_PARENS                                                         # sizeofExpression
    // C# 6: https://msdn.microsoft.com/en-us/library/dn986596.aspx
    | NAMEOF OPEN_PARENS (identifier '.')* identifier CLOSE_PARENS # nameofExpression
    ;

throwable_expression
    : expression
    | throw_expression
    ;

throw_expression
    : THROW expression
    ;

member_access
    : '?'? '.' identifier type_argument_list?
    ;

bracket_expression
    : '?'? '[' indexer_argument (',' indexer_argument)* ']'
    ;

indexer_argument
    : (identifier ':')? expression
    ;

predefined_type
    : BOOL
    | BYTE
    | CHAR
    | DECIMAL
    | DOUBLE
    | FLOAT
    | INT
    | LONG
    | OBJECT
    | SBYTE
    | SHORT
    | STRING
    | UINT
    | ULONG
    | USHORT
    ;

expression_list
    : expression (',' expression)*
    ;

object_or_collection_initializer
    : object_initializer
    | collection_initializer
    ;

object_initializer
    : OPEN_BRACE (member_initializer_list ','?)? CLOSE_BRACE
    ;

member_initializer_list
    : member_initializer (',' member_initializer)*
    ;

member_initializer
    : (identifier | '[' expression ']') '=' initializer_value // C# 6
    ;

initializer_value
    : expression
    | object_or_collection_initializer
    | tuple_type
    ;

collection_initializer
    : OPEN_BRACE element_initializer (',' element_initializer)* ','? CLOSE_BRACE
    ;

element_initializer
    : non_assignment_expression
    | OPEN_BRACE expression_list CLOSE_BRACE
    | expression
    ;

anonymous_object_initializer
    : OPEN_BRACE (member_declarator_list ','?)? CLOSE_BRACE
    ;

member_declarator_list
    : member_declarator (',' member_declarator)*
    ;

member_declarator
    : primary_expression
    | identifier ('=' expression)?
    | identifier '[' INTEGER_LITERAL ']' 
    ;

unbound_type_name
    : identifier (generic_dimension_specifier? | '::' identifier generic_dimension_specifier?) (
        '.' identifier generic_dimension_specifier?
    )*
    ;

generic_dimension_specifier
    : '<' ','* '>'
    ;

isType
    : base_type (rank_specifier | '*')* '?'? isTypePatternArms? identifier?
    ;

isTypePatternArms
    : OPEN_BRACE isTypePatternArm (',' isTypePatternArm)* CLOSE_BRACE
    ;

isTypePatternArm
    : identifier ':' expression
    ;

lambda_expression
    : attributes? ASYNC? STATIC? anonymous_function_signature right_arrow anonymous_function_body
    ;

anonymous_function_signature
    : OPEN_PARENS CLOSE_PARENS
    | OPEN_PARENS explicit_anonymous_function_parameter_list CLOSE_PARENS
    | OPEN_PARENS implicit_anonymous_function_parameter_list CLOSE_PARENS
    | identifier
    ;

explicit_anonymous_function_parameter_list
    : explicit_anonymous_function_parameter (',' explicit_anonymous_function_parameter)*
    ;

explicit_anonymous_function_parameter
    : attributes? (REF | OUT | IN | REF READONLY)? type_? identifier ('=' expression)?
    ;

implicit_anonymous_function_parameter_list
    : identifier (',' identifier)*
    ;

anonymous_function_body
    : throwable_expression
    | block
    ;

query_expression
    : from_clause query_body
    ;

from_clause
    : FROM type_? identifier IN expression
    ;

query_body
    : query_body_clause* select_or_group_clause query_continuation?
    ;

query_body_clause
    : from_clause
    | let_clause
    | where_clause
    | combined_join_clause
    | orderby_clause
    ;

let_clause
    : LET identifier '=' expression
    ;

where_clause
    : WHERE expression
    ;

combined_join_clause
    : JOIN type_? identifier IN expression ON expression EQUALS expression (INTO identifier)?
    ;

orderby_clause
    : ORDERBY ordering (',' ordering)*
    ;

ordering
    : expression dir = (ASCENDING | DESCENDING)?
    ;

select_or_group_clause
    : SELECT expression
    | GROUP expression BY expression
    ;

query_continuation
    : INTO identifier query_body
    ;

//B.2.5 Statements
statement
    : labeled_Statement
    | declarationStatement
    | embedded_statement
    ;

declarationStatement
    : local_variable_declaration ';'
    | local_constant_declaration ';'
    | local_function_declaration
    ;

local_function_declaration
    : local_function_header local_function_body
    ;

local_function_header
    : local_function_modifiers? return_type identifier type_parameter_list? OPEN_PARENS formal_parameter_list? CLOSE_PARENS
        type_parameter_constraints_clauses?
    ;

local_function_modifiers
    : (ASYNC | UNSAFE) STATIC?
    | STATIC (ASYNC | UNSAFE)?
    | UNSAFE STRUCT
    ;

local_function_body
    : block
    | right_arrow throwable_expression ';'
    ;

labeled_Statement
    : identifier ':' statement
    ;

embedded_statement
    : block
    | empty_statement
    | expression ';' 

    // selection statements
    | if_statement
    | SWITCH OPEN_PARENS expression CLOSE_PARENS OPEN_BRACE switch_section* CLOSE_BRACE 

    // iteration statements
    | WHILE OPEN_PARENS expression CLOSE_PARENS embedded_statement                                            // whileStatement
    | DO embedded_statement WHILE OPEN_PARENS expression CLOSE_PARENS ';'                                     // doStatement
    | FOR OPEN_PARENS for_initializer? ';' expression? ';' for_iterator? CLOSE_PARENS embedded_statement      // forStatement
    | AWAIT? FOREACH OPEN_PARENS local_variable_type (identifier | deconstruction_element) IN expression CLOSE_PARENS embedded_statement // foreachStatement

    // jump statements
    | BREAK ';'                                                              
    | CONTINUE ';'                                                           
    | GOTO (identifier | CASE expression | DEFAULT) ';'                      
    | RETURN expression? ';'                                                 
    | THROW expression? ';'                                                  

    | try_statement
    | checked_statement
    | unchecked_statement
    | lock_statement
    | using_statement
    | yield_statement
    | unsafe_statement   // unsafe code support
    | fixed_statement    // unsafe code support
    ;

empty_statement
    : ';'
    ;

// Source: §13.8.2 The if statement
if_statement
    : 'if' '(' expression ')' embedded_statement
    | 'if' '(' expression ')' embedded_statement
      'else' embedded_statement
    ;

// Source: §13.12 The checked and unchecked statements
checked_statement
    : CHECKED block
    ;

unchecked_statement
    : UNCHECKED block
    ;

// Source: §13.13 The lock statement
lock_statement
    : 'lock' OPEN_PARENS expression CLOSE_PARENS embedded_statement
    ;

// Source: §8.8 Unmanaged types
unmanaged_type
    : type_
    | pointer_type     // unsafe code support
    ;

// Source: §12.8.22 Stack allocation
stackalloc_expression
    : STACKALLOC type_ '[' expression ']'
    | STACKALLOC type_? '[' expression? ']' stackalloc_initializer
    ;


stackalloc_initializer
     : OPEN_BRACE stackalloc_initializer_element_list CLOSE_BRACE
     ;

stackalloc_initializer_element_list
     : stackalloc_element_initializer (',' stackalloc_element_initializer)* ','?
     ;
    
stackalloc_element_initializer
    : expression
    ;


// Source: §13.14 The using statement
using_statement
    : 'using' '(' resource_acquisition ')' embedded_statement
    ;

// Source: §13.15 The yield statement
yield_statement
    : 'yield' 'return' expression ';'
    | 'yield' 'break' ';'
    ;

fixed_statement
    : FIXED '(' pointer_type fixed_pointer_declarators ')' embedded_statement
    ;

unsafe_statement
    : UNSAFE block
    ;


// Source: §13.11 The try statement
try_statement
    : TRY block catch_clauses
    | TRY block catch_clauses? finally_clause
    ;


block
    : OPEN_BRACE statement_list? CLOSE_BRACE
    ;

local_variable_declaration
    : (USING | REF | REF READONLY)? local_variable_type local_variable_declarator
      (',' local_variable_declarator)* 
    | FIXED pointer_type fixed_pointer_declarators
    | 'var' deconstruction_expression '=' expression
    | unsafe_function_pointer
    | attributes? type_ identifier '=' lambda_expression
    ;

unsafe_function_pointer
    : UNSAFE OPEN_BRACE delegate_function_pointer CLOSE_BRACE
    ;

delegate_function_pointer
    : DELEGATE '*' '<' function_pointer_parameter_list '>' identifier '=' '&' identifier ';'
    ;


local_variable_type
    : VAR
    | type_
    ;

local_variable_declarator
    : identifier ('=' REF? local_variable_initializer)?
    ;

local_variable_initializer
    : expression
    | array_initializer
    | stackalloc_initializer
    | deconstruction_element
    | lambda_expression
    ;

local_constant_declaration
    : CONST type_ constant_declarators
    ;


switch_section
    : switch_label+ statement_list
    ;

switch_label
    : CASE expression case_guard? ':'
    | CASE pattern case_guard?  ':'
    | DEFAULT ':'
    ;

case_guard
    : WHEN expression
    ;

statement_list
    : statement+
    ;

for_initializer
    : local_variable_declaration
    | expression (',' expression)*
    ;

for_iterator
    : expression (',' expression)*
    ;

catch_clauses
    : specific_catch_clause specific_catch_clause* general_catch_clause?
    | general_catch_clause
    ;

specific_catch_clause
    : CATCH OPEN_PARENS class_type identifier? CLOSE_PARENS exception_filter? block
    ;

general_catch_clause
    : CATCH exception_filter? block
    ;

exception_filter // C# 6
    : WHEN OPEN_PARENS expression CLOSE_PARENS
    ;

finally_clause
    : FINALLY block
    ;

resource_acquisition
    : local_variable_declaration
    | expression
    ;

//B.2.6 Namespaces;
namespace_declaration
    : NAMESPACE qi = qualified_identifier namespace_body ';'?
    ;

qualified_identifier
    : identifier ('.' identifier)*
    ;

namespace_body
    : OPEN_BRACE extern_alias_directives? using_directives? namespace_member_declarations? CLOSE_BRACE
    | ';'
    ;

extern_alias_directives
    : extern_alias_directive+
    ;

extern_alias_directive
    : EXTERN ALIAS identifier ';'
    ;

using_directives
    : using_directive+
    ;

using_directive
    : GLOBAL? USING identifier '=' (namespace_or_type_name | tuple_type) ';' # usingAliasDirective
    | GLOBAL? USING namespace_or_type_name ';'                # usingNamespaceDirective
    // C# 6: https://msdn.microsoft.com/en-us/library/ms228593.aspx
    | GLOBAL? USING STATIC namespace_or_type_name ';' # usingStaticDirective
    ;

namespace_member_declarations
    : namespace_member_declaration+
    ;

namespace_member_declaration
    : namespace_declaration
    | type_declaration
    | module_initializer_declaration
    | common_member_declaration
    ;

type_declaration
    : attributes? all_member_modifiers? (
        class_definition
        | struct_definition
        | interface_definition
        | enum_definition
        | delegate_definition
        | record_definition  // Nueva alternativa para records
    )
    ;

// Nueva regla para la definición de records
record_definition
    : RECORD STRUCT? identifier type_parameter_list? record_base? type_parameter_constraints_clauses? 
      '(' record_parameters? ')' record_body
    ;

record_base
    : ':' class_type (',' namespace_or_type_name)*
    ;

record_body
    : OPEN_BRACE class_member_declarations? CLOSE_BRACE
    | ';'
    ;

record_parameters
    : record_parameter (',' record_parameter)*
    ;

record_parameter
    : attributes? type_ identifier
    ;

qualified_alias_member
    : identifier '::' identifier type_argument_list?
    ;

//B.2.7 Classes;
type_parameter_list
    : '<' type_parameter (',' type_parameter)* '>'
    ;

type_parameter
    : attributes? identifier
    ;

class_base
    : ':' class_type (',' namespace_or_type_name)*
    ;

interface_type_list
    : namespace_or_type_name (',' namespace_or_type_name)*
    ;

type_parameter_constraints_clauses
    : type_parameter_constraints_clause+
    ;

type_parameter_constraints_clause
    : WHERE identifier ':' type_parameter_constraints
    ;

type_parameter_constraints
    : constructor_constraint
    | primary_constraint (',' secondary_constraints)? (',' constructor_constraint)?
    ;

primary_constraint
    : class_type
    | CLASS '?'?
    | STRUCT
    | UNMANAGED
    ;

// Source: §11.2.1 General
pattern
    : declaration_pattern
    | constant_pattern
    | var_pattern
    | relational_pattern
    | and_pattern
    | or_pattern
    | not_pattern
    | expression
    | is_pattern
    | list_pattern
    | rest_pattern
    ;

rest_pattern
    : '..' type_? expression?
    ;

list_pattern
    : '[' pattern_items ']'
    ;

pattern_items
    : pattern (',' pattern)* ','?
    ;


    
is_pattern
    : type_? simple_designation? property_pattern?
    ;

property_pattern
    : OPEN_BRACE property_pattern_clause (',' property_pattern_clause)* CLOSE_BRACE
    ;

property_pattern_clause
    : identifier ':' pattern
    ;


relational_pattern
    : '<' expression
    | '<=' expression
    | '>' expression
    | '>=' expression
    ;

and_pattern
    : relational_pattern 'and' pattern
    ;

or_pattern
    : relational_pattern 'or' pattern
    ;

not_pattern
    : NOT pattern
    ;

// Source: §11.2.2 Declaration pattern
declaration_pattern
    : type_ simple_designation
    ;
simple_designation
    : single_variable_designation
    ;
single_variable_designation
    : identifier
    ;

// Source: §11.2.3 Constant pattern
constant_pattern
    : constant_expression
    ;

// Source: §11.2.4 Var pattern
var_pattern
    : 'var' designation
    ;
designation
    : simple_designation
    ;

module_initializer_declaration
    : attributes INTERNAL? PUBLIC? STATIC VOID identifier '(' ')' method_body
    ;


// namespace_or_type_name includes identifier
secondary_constraints
    : namespace_or_type_name (',' namespace_or_type_name)*
    ;

constructor_constraint
    : NEW OPEN_PARENS CLOSE_PARENS
    ;

class_body
    : OPEN_BRACE class_member_declarations? CLOSE_BRACE
    ;

class_member_declarations
    : class_member_declaration+
    ;

class_member_declaration
    : attributes? all_member_modifiers? (common_member_declaration | destructor_definition)
    ;

all_member_modifiers
    : all_member_modifier+
    ;

all_member_modifier
    : NEW
    | PUBLIC
    | PROTECTED
    | INTERNAL
    | PRIVATE
    | READONLY
    | VOLATILE
    | VIRTUAL
    | SEALED
    | OVERRIDE
    | ABSTRACT
    | STATIC
    | UNSAFE
    | EXTERN
    | PARTIAL
    | ASYNC 
    | FILE
    ;

// represents the intersection of struct_member_declaration and class_member_declaration
common_member_declaration
    : constant_declaration
    | typed_member_declaration
    | event_declaration
    | conversion_operator_declarator (body | right_arrow throwable_expression ';') // C# 6
    | constructor_declaration
    | method_declaration
    | class_definition
    | struct_definition
    | interface_definition
    | enum_definition
    | delegate_definition
    | record_definition
    ;

typed_member_declaration
    : (REF | READONLY REF | REF READONLY)? REQUIRED? type_ (
        namespace_or_type_name '.' indexer_declaration
        | method_declaration
        | property_declaration
        | indexer_declaration
        | operator_declaration
        | field_declaration
    )
    ;

constant_declarators
    : constant_declarator (',' constant_declarator)*
    ;

constant_declarator
    : identifier '=' expression
    ;

variable_declarators
    : variable_declarator (',' variable_declarator)*
    ;

variable_declarator
    : identifier ('=' variable_initializer)?
    ;

variable_initializer
    : expression
    | array_initializer
    ;

return_type
    : type_
    | VOID
    ;

member_name
    : namespace_or_type_name
    ;

method_body
    : block
    | ';'
    | right_arrow expression ';'  // Soporte para métodos de expresión
    ;

formal_parameter_list
    : parameter_array
    | fixed_parameters (',' parameter_array)?
    ;

fixed_parameters
    : fixed_parameter (',' fixed_parameter)*
    ;

fixed_parameter
    : attributes? parameter_modifier? arg_declaration
    | ARGLIST
    ;

parameter_modifier
    : REF
    | OUT
    | IN
    | REF READONLY
    | REF THIS
    | IN THIS
    | THIS
    ;

parameter_array
    : attributes? PARAMS array_type identifier
    ;

accessor_declarations
    : attrs = attributes? mods = accessor_modifier? (
        GET accessor_body set_accessor_declaration?
        | SET accessor_body get_accessor_declaration?
        | GET accessor_body init_accessor_declaration?
        | INIT accessor_body get_accessor_declaration?
    )
    
    ;

init_accessor_declaration
    : attributes? INIT accessor_body
    ;

get_accessor_declaration
    : attributes? accessor_modifier? GET accessor_body
    ;

set_accessor_declaration
    : attributes? accessor_modifier? SET accessor_body
    ;

accessor_modifier
    : PROTECTED
    | INTERNAL
    | PRIVATE
    | PROTECTED INTERNAL
    | INTERNAL PROTECTED
    | PROTECTED PRIVATE
    | PRIVATE PROTECTED
    | READONLY
    | REQUIRED
    ;

accessor_body
    : block
    | right_arrow expression ';'
    | ';'
    ;

event_accessor_declarations
    : attributes? (ADD block remove_accessor_declaration | REMOVE block add_accessor_declaration)
    ;

add_accessor_declaration
    : attributes? ADD block
    ;

remove_accessor_declaration
    : attributes? REMOVE block
    ;

overloadable_operator
    : '+'
    | '-'
    | BANG
    | '~'
    | '++'
    | '--'
    | TRUE
    | FALSE
    | '*'
    | '/'
    | '%'
    | '&'
    | '|'
    | '^'
    | '<<'
    | right_shift
    | OP_EQ
    | OP_NE
    | '>'
    | '<'
    | '>='
    | '<='
    ;

conversion_operator_declarator
    : (IMPLICIT | EXPLICIT) OPERATOR type_ OPEN_PARENS arg_declaration CLOSE_PARENS
    ;

constructor_initializer
    : ':' (BASE | THIS) OPEN_PARENS argument_list? CLOSE_PARENS
    ;

body
    : block
    | ';'
    | right_arrow expression ';'
    ;

//B.2.8 Structs
struct_interfaces
    : ':' interface_type_list
    ;

struct_body
    : OPEN_BRACE struct_member_declaration* CLOSE_BRACE
    | ';'
    ;

struct_member_declaration
    : attributes? all_member_modifiers? (
        common_member_declaration
        | FIXED type_ fixed_size_buffer_declarator+ ';'
        | type_ member_declarator ';'
    )
    ;

//B.2.9 Arrays
array_type
    : base_type (('*' | '?')* rank_specifier)+
    ;

rank_specifier
    : '[' ','* ']'
    ;

array_initializer
    : OPEN_BRACE (variable_initializer (',' variable_initializer)* ','?)? CLOSE_BRACE
    ;

//B.2.10 Interfaces
variant_type_parameter_list
    : '<' variant_type_parameter (',' variant_type_parameter)* '>'
    ;

variant_type_parameter
    : attributes? variance_annotation? identifier
    ;

variance_annotation
    : IN
    | OUT
    ;

interface_base
    : ':' interface_type_list
    ;

interface_body // ignored in csharp 8
    : OPEN_BRACE interface_member_declaration* CLOSE_BRACE
    ;

interface_member_declaration
    : attributes? NEW? (
        UNSAFE? (REF | REF READONLY | READONLY REF)? type_ (
            identifier type_parameter_list? OPEN_PARENS formal_parameter_list? CLOSE_PARENS type_parameter_constraints_clauses? ';'
            | identifier OPEN_BRACE interface_accessors CLOSE_BRACE
            | THIS '[' formal_parameter_list ']' OPEN_BRACE interface_accessors CLOSE_BRACE
        )
        | UNSAFE? VOID identifier type_parameter_list? OPEN_PARENS formal_parameter_list? CLOSE_PARENS type_parameter_constraints_clauses? ';'
        | EVENT type_ identifier ';'
    )
    ;

interface_accessors
    : attributes? (GET ';' (attributes? SET ';')? | SET ';' (attributes? GET ';')?)
    ;

//B.2.11 Enums
enum_base
    : ':' type_
    ;

enum_body
    : OPEN_BRACE (enum_member_declaration (',' enum_member_declaration)* ','?)? CLOSE_BRACE
    ;

enum_member_declaration
    : attributes? identifier ('=' expression)?
    ;

//B.2.12 Delegates

//B.2.13 Attributes
global_attribute_section
    : '[' global_attribute_target ':' attribute_list ','? ']'
    ;

global_attribute_target
    : keyword
    | identifier
    ;

attributes
    : attribute_section+
    ;

attribute_section
    : '[' (attribute_target ':')? attribute_list ','? ']'
    | '[' attribute_list ']' (',' '[' attribute_list ']')*
    ;

attribute_target
    : keyword
    | identifier
    ;

attribute_list
    : attribute (',' attribute)*
    ;

attribute
    : namespace_or_type_name (
        OPEN_PARENS (attribute_argument (',' attribute_argument)*)? CLOSE_PARENS
    )?
    ;

attribute_argument
    : (identifier ':')? expression
    ;

//B.3 Grammar extensions for unsafe code
pointer_type
    : (simple_type | class_type) (rank_specifier | '?')* '*'
    | VOID '*'
    ;

fixed_pointer_declarators
    : fixed_pointer_declarator (',' fixed_pointer_declarator)*
    ;

fixed_pointer_declarator
    : identifier '=' fixed_pointer_initializer
    ;

fixed_pointer_initializer
    : '&'? expression
    | stackalloc_initializer
    ;

fixed_size_buffer_declarator
    : identifier '[' expression ']'
    ;


right_arrow
    : first = '=' second = '>' {$first.index + 1 == $second.index}? // Nothing between the tokens?
    ;

right_shift
    : first = '>' second = '>' {$first.index + 1 == $second.index}? // Nothing between the tokens?
    ;

right_shift_assignment
    : first = '>' second = '>=' {$first.index + 1 == $second.index}? // Nothing between the tokens?
    ;

literal
    : boolean_literal
    | string_literal
    | RAW_STRING_LITERAL
    | utf8_string_literal
    | INTEGER_LITERAL
    | HEX_INTEGER_LITERAL
    | BIN_INTEGER_LITERAL
    | REAL_LITERAL
    | CHARACTER_LITERAL
    | NULL_
    ;

utf8_string_literal
    : REGULAR_STRING UTF8_SUFFIX
    | VERBATIUM_STRING UTF8_SUFFIX
    ;


boolean_literal
    : TRUE
    | FALSE
    ;

string_literal
    : interpolated_regular_string
    | interpolated_verbatium_string
    | REGULAR_STRING
    | VERBATIUM_STRING
    ;


interpolated_regular_string
    : INTERPOLATED_REGULAR_STRING_START interpolated_regular_string_part* DOUBLE_QUOTE_INSIDE
    ;

interpolated_verbatium_string
    : INTERPOLATED_VERBATIUM_STRING_START interpolated_verbatium_string_part* DOUBLE_QUOTE_INSIDE
    ;

interpolated_regular_string_part
    : interpolated_string_expression
    | DOUBLE_CURLY_INSIDE
    | REGULAR_CHAR_INSIDE
    | REGULAR_STRING_INSIDE
    | OPEN_BRACE_INSIDE
    | CLOSE_BRACE_INSIDE
    | DOUBLE_QUOTE_INSIDE
    | VERBATIUM_INSIDE_STRING
    | OPEN_BRACE
    | CLOSE_BRACE
    ;

interpolated_verbatium_string_part
    : interpolated_string_expression
    | DOUBLE_CURLY_INSIDE
    | VERBATIUM_DOUBLE_QUOTE_INSIDE
    | VERBATIUM_INSIDE_STRING
    ;

interpolated_string_expression
    : OPEN_BRACE_INSIDE expression (',' interpolation_minimum_width)? format_string? CLOSE_BRACE_INSIDE
    ;

interpolation_minimum_width
    : constant_expression
    ;

format_string
    : ':' FORMAT_STRING+
    ;

constant_expression
    : expression
    ;


//B.1.7 Keywords
keyword
    : ABSTRACT
    | AS
    | BASE
    | BOOL
    | BREAK
    | BYTE
    | CASE
    | CATCH
    | CHAR
    | CHECKED
    | CLASS
    | CONST
    | CONTINUE
    | DECIMAL
    | DEFAULT
    | DELEGATE
    | DO
    | DOUBLE
    | ELSE
    | ENUM
    | EVENT
    | EXPLICIT
    | EXTERN
    | FALSE
    | FINALLY
    | FIXED
    | FLOAT
    | FOR
    | FOREACH
    | GOTO
    | IF
    | IMPLICIT
    | IN
    | INT
    | INTERFACE
    | INTERNAL
    | IS
    | LOCK
    | LONG
    | NAMESPACE
    | NEW
    | NULL_
    | OBJECT
    | OPERATOR
    | OUT
    | OVERRIDE
    | PARAMS
    | PRIVATE
    | PROTECTED
    | PUBLIC
    | READONLY
    | REF
    | RETURN
    | SBYTE
    | SEALED
    | SHORT
    | SIZEOF
    | STACKALLOC
    | STATIC
    | STRING
    | STRUCT
    | SWITCH
    | THIS
    | THROW
    | TRUE
    | TRY
    | TYPEOF
    | UINT
    | ULONG
    | UNCHECKED
    | UNMANAGED
    | UNSAFE
    | USHORT
    | USING
    | VIRTUAL
    | VOID
    | VOLATILE
    | WHILE
    ;

// -------------------- extra rules for modularization --------------------------------

class_definition
    : class_modifier* PARTIAL? CLASS identifier type_parameter_list? primary_constructor_parameters? class_base? type_parameter_constraints_clauses? class_body ';'?
    ;

primary_constructor_parameters
    : OPEN_PARENS formal_parameter_list? CLOSE_PARENS
    ;

// Source: §15.2.2.1 General
class_modifier
    : NEW
    | PUBLIC
    | PROTECTED
    | INTERNAL
    | PRIVATE
    | ABSTRACT
    | SEALED
    | STATIC
    | UNSAFE
    | FILE
    ;

struct_definition
    : struct_modifier* REF? PARTIAL? (RECORD | READONLY RECORD)? STRUCT identifier type_parameter_list? struct_interfaces? type_parameter_constraints_clauses? struct_body
    ;

// Source: §16.2.2 Struct modifiers
struct_modifier
    : NEW
    | PUBLIC
    | PROTECTED
    | INTERNAL
    | PRIVATE
    | READONLY
    | UNSAFE   
    | FILE
    ;


interface_definition
    : INTERFACE identifier variant_type_parameter_list? interface_base? type_parameter_constraints_clauses? class_body ';'?
    ;

enum_definition
    : ENUM identifier enum_base? enum_body ';'?
    ;

delegate_definition
    : DELEGATE return_type identifier variant_type_parameter_list? OPEN_PARENS formal_parameter_list? CLOSE_PARENS type_parameter_constraints_clauses?
        ';'
    ;

event_declaration
    : EVENT type_ (
        variable_declarators ';'
        | member_name OPEN_BRACE event_accessor_declarations CLOSE_BRACE
    )
    ;

field_declaration
    : variable_declarators ';'
    ;

property_declaration
    : member_name (
        OPEN_BRACE accessor_declarations CLOSE_BRACE ('=' variable_initializer ';')?
        | right_arrow throwable_expression ';'
    )
    ;

constant_declaration
    : CONST type_ constant_declarators ';'
    ;

indexer_declaration // lamdas from C# 6
    : THIS '[' formal_parameter_list ']' (
        OPEN_BRACE accessor_declarations CLOSE_BRACE
        | right_arrow throwable_expression ';'
    )
    ;

destructor_definition
    : '~' identifier OPEN_PARENS CLOSE_PARENS body
    ;

constructor_declaration
    : identifier OPEN_PARENS formal_parameter_list? CLOSE_PARENS constructor_initializer? body
    ;

method_declaration
    : attributes? method_modifiers PUBLIC? return_type method_header method_body
    | attributes? ref_method_modifiers ref_kind ref_return_type method_header
      ref_method_body
    ;

method_header
    : method_member_name '(' formal_parameter_list? ')'
    | method_member_name type_parameter_list '(' formal_parameter_list? ')'
      type_parameter_constraints_clause*
    ;

ref_kind
    : 'ref'
    | 'ref' 'readonly'
    ;

ref_method_modifiers
    : ref_method_modifier*
    ;

ref_return_type
    : type_
    ;

method_modifiers
    : method_modifier* 'partial'?
    ;

method_modifier
    : ref_method_modifier
    | 'async'
    ;

ref_method_body
    : block
    | right_arrow REF variable_reference ';'
    | ';'
    ;

ref_method_modifier
    : 'new'
    | 'public'
    | 'protected'
    | 'internal'
    | 'private'
    | 'static'
    | 'virtual'
    | 'sealed'
    | 'override'
    | 'abstract'
    | 'extern'
    | UNSAFE
    ;

method_member_name
    : (identifier | identifier '::' identifier) (type_argument_list? '.' identifier)*
    ;

operator_declaration // lamdas form C# 6
    : OPERATOR overloadable_operator OPEN_PARENS IN? arg_declaration (',' IN? arg_declaration)? CLOSE_PARENS (
        body
        | right_arrow throwable_expression ';'
    )
    ;

arg_declaration
    : type_ identifier ('=' expression)?
    ;

method_invocation
    : primary_expression? OPEN_PARENS argument_list? CLOSE_PARENS
    ;

object_creation_expression
    : OPEN_PARENS argument_list? CLOSE_PARENS object_or_collection_initializer?
    | object_or_collection_initializer
    | target_typed_new
    | '[' expression_list ']' rank_specifier* array_initializer?
    ;

target_typed_new
    : '(' argument_list? ')' object_or_collection_initializer?
    ;

identifier
    : IDENTIFIER
    | ADD
    | ALIAS
    | ARGLIST
    | ASCENDING
    | ASYNC
    | AWAIT
    | BY
    | DESCENDING
    | DYNAMIC
    | EQUALS
    | FROM
    | GET
    | GROUP
    | INTO
    | JOIN
    | LET
    | NAMEOF
    | ON
    | ORDERBY
    | PARTIAL
    | REMOVE
    | SELECT
    | SET
    | UNMANAGED
    | VAR
    | WHEN
    | WHERE
    | YIELD
    ;