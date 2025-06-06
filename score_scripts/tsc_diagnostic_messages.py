# Copyright (c) Microsoft. All rights reserved.
""" Store and retrieve relevant information to tsc diagnostic messages """


# pylint: disable=too-many-lines
def get_tsc_diagnostic_messages():
    """Return information about each tsc diagnostic message."""
    return {
        "Unterminated string literal.": {"category": "Error", "code": 1002},
        "Identifier expected.": {"category": "Error", "code": 1003},
        "'{0}' expected.": {"category": "Error", "code": 1005},
        "A file cannot have a reference to itself.": {
            "category": "Error",
            "code": 1006,
        },
        "Trailing comma not allowed.": {"category": "Error", "code": 1009},
        "'*/' expected.": {"category": "Error", "code": 1010},
        "Unexpected token.": {"category": "Error", "code": 1012},
        "A rest parameter must be last in a parameter list.": {
            "category": "Error",
            "code": 1014,
        },
        "Parameter cannot have question mark and initializer.": {
            "category": "Error",
            "code": 1015,
        },
        "A required parameter cannot follow an optional parameter.": {
            "category": "Error",
            "code": 1016,
        },
        "An index signature cannot have a rest parameter.": {
            "category": "Error",
            "code": 1017,
        },
        "An index signature parameter cannot have an accessibility modifier.": {
            "category": "Error",
            "code": 1018,
        },
        "An index signature parameter cannot have a question mark.": {
            "category": "Error",
            "code": 1019,
        },
        "An index signature parameter cannot have an initializer.": {
            "category": "Error",
            "code": 1020,
        },
        "An index signature must have a type annotation.": {
            "category": "Error",
            "code": 1021,
        },
        "An index signature parameter must have a type annotation.": {
            "category": "Error",
            "code": 1022,
        },
        "An index signature parameter type must be 'string' or 'number'.": {
            "category": "Error",
            "code": 1023,
        },
        "Accessibility modifier already seen.": {"category": "Error", "code": 1028},
        "'{0}' modifier must precede '{1}' modifier.": {
            "category": "Error",
            "code": 1029,
        },
        "'{0}' modifier already seen.": {"category": "Error", "code": 1030},
        "'{0}' modifier cannot appear on a class element.": {
            "category": "Error",
            "code": 1031,
        },
        "'super' must be followed by an argument list or member access.": {
            "category": "Error",
            "code": 1034,
        },
        "Only ambient modules can use quoted names.": {
            "category": "Error",
            "code": 1035,
        },
        "Statements are not allowed in ambient contexts.": {
            "category": "Error",
            "code": 1036,
        },
        "A 'declare' modifier cannot be used in an already ambient context.": {
            "category": "Error",
            "code": 1038,
        },
        "Initializers are not allowed in ambient contexts.": {
            "category": "Error",
            "code": 1039,
        },
        "'{0}' modifier cannot be used in an ambient context.": {
            "category": "Error",
            "code": 1040,
        },
        "'{0}' modifier cannot be used with a class declaration.": {
            "category": "Error",
            "code": 1041,
        },
        "'{0}' modifier cannot be used here.": {"category": "Error", "code": 1042},
        "'{0}' modifier cannot appear on a data property.": {
            "category": "Error",
            "code": 1043,
        },
        "'{0}' modifier cannot appear on a module element.": {
            "category": "Error",
            "code": 1044,
        },
        "A '{0}' modifier cannot be used with an interface declaration.": {
            "category": "Error",
            "code": 1045,
        },
        "A 'declare' modifier is required for a top level declaration in a .d.ts file.": {
            "category": "Error",
            "code": 1046,
        },
        "A rest parameter cannot be optional.": {"category": "Error", "code": 1047},
        "A rest parameter cannot have an initializer.": {
            "category": "Error",
            "code": 1048,
        },
        "A 'set' accessor must have exactly one parameter.": {
            "category": "Error",
            "code": 1049,
        },
        "A 'set' accessor cannot have an optional parameter.": {
            "category": "Error",
            "code": 1051,
        },
        "A 'set' accessor parameter cannot have an initializer.": {
            "category": "Error",
            "code": 1052,
        },
        "A 'set' accessor cannot have rest parameter.": {
            "category": "Error",
            "code": 1053,
        },
        "A 'get' accessor cannot have parameters.": {"category": "Error", "code": 1054},
        "Type '{0}' is not a valid async function return type.": {
            "category": "Error",
            "code": 1055,
        },
        "Accessors are only available when targeting ECMAScript 5 and higher.": {
            "category": "Error",
            "code": 1056,
        },
        "An async function or method must have a valid awaitable return type.": {
            "category": "Error",
            "code": 1057,
        },
        "Operand for 'await' does not have a valid callable 'then' member.": {
            "category": "Error",
            "code": 1058,
        },
        "Return expression in async function does not have a valid callable 'then' member.": {
            "category": "Error",
            "code": 1059,
        },
        "Expression body for async arrow function does not have a valid callable 'then' member.": {
            "category": "Error",
            "code": 1060,
        },
        "Enum member must have initializer.": {"category": "Error", "code": 1061},
        "{0} is referenced directly or indirectly in the fulfillment callback of its own 'then' method.": {
            "category": "Error",
            "code": 1062,
        },
        "An export assignment cannot be used in a namespace.": {
            "category": "Error",
            "code": 1063,
        },
        "The return type of an async function or method must be the global Promise<T> type.": {
            "category": "Error",
            "code": 1064,
        },
        "In ambient enum declarations member initializer must be constant expression.": {
            "category": "Error",
            "code": 1066,
        },
        "Unexpected token. A constructor, method, accessor, or property was expected.": {
            "category": "Error",
            "code": 1068,
        },
        "A '{0}' modifier cannot be used with an import declaration.": {
            "category": "Error",
            "code": 1079,
        },
        "Invalid 'reference' directive syntax.": {"category": "Error", "code": 1084},
        "Octal literals are not available when targeting ECMAScript 5 and higher.": {
            "category": "Error",
            "code": 1085,
        },
        "An accessor cannot be declared in an ambient context.": {
            "category": "Error",
            "code": 1086,
        },
        "'{0}' modifier cannot appear on a constructor declaration.": {
            "category": "Error",
            "code": 1089,
        },
        "'{0}' modifier cannot appear on a parameter.": {
            "category": "Error",
            "code": 1090,
        },
        "Only a single variable declaration is allowed in a 'for...in' statement.": {
            "category": "Error",
            "code": 1091,
        },
        "Type parameters cannot appear on a constructor declaration.": {
            "category": "Error",
            "code": 1092,
        },
        "Type annotation cannot appear on a constructor declaration.": {
            "category": "Error",
            "code": 1093,
        },
        "An accessor cannot have type parameters.": {"category": "Error", "code": 1094},
        "A 'set' accessor cannot have a return type annotation.": {
            "category": "Error",
            "code": 1095,
        },
        "An index signature must have exactly one parameter.": {
            "category": "Error",
            "code": 1096,
        },
        "'{0}' list cannot be empty.": {"category": "Error", "code": 1097},
        "Type parameter list cannot be empty.": {"category": "Error", "code": 1098},
        "Type argument list cannot be empty.": {"category": "Error", "code": 1099},
        "Invalid use of '{0}' in strict mode.": {"category": "Error", "code": 1100},
        "'with' statements are not allowed in strict mode.": {
            "category": "Error",
            "code": 1101,
        },
        "'delete' cannot be called on an identifier in strict mode.": {
            "category": "Error",
            "code": 1102,
        },
        "A 'continue' statement can only be used within an enclosing iteration statement.": {
            "category": "Error",
            "code": 1104,
        },
        "A 'break' statement can only be used within an enclosing iteration or switch statement.": {
            "category": "Error",
            "code": 1105,
        },
        "Jump target cannot cross function boundary.": {
            "category": "Error",
            "code": 1107,
        },
        "A 'return' statement can only be used within a function body.": {
            "category": "Error",
            "code": 1108,
        },
        "Expression expected.": {"category": "Error", "code": 1109},
        "Type expected.": {"category": "Error", "code": 1110},
        "A class member cannot be declared optional.": {
            "category": "Error",
            "code": 1112,
        },
        "A 'default' clause cannot appear more than once in a 'switch' statement.": {
            "category": "Error",
            "code": 1113,
        },
        "Duplicate label '{0}'": {"category": "Error", "code": 1114},
        "A 'continue' statement can only jump to a label of an enclosing iteration statement.": {
            "category": "Error",
            "code": 1115,
        },
        "A 'break' statement can only jump to a label of an enclosing statement.": {
            "category": "Error",
            "code": 1116,
        },
        "An object literal cannot have multiple properties with the same name in strict mode.": {
            "category": "Error",
            "code": 1117,
        },
        "An object literal cannot have multiple get/set accessors with the same name.": {
            "category": "Error",
            "code": 1118,
        },
        "An object literal cannot have property and accessor with the same name.": {
            "category": "Error",
            "code": 1119,
        },
        "An export assignment cannot have modifiers.": {
            "category": "Error",
            "code": 1120,
        },
        "Octal literals are not allowed in strict mode.": {
            "category": "Error",
            "code": 1121,
        },
        "A tuple type element list cannot be empty.": {
            "category": "Error",
            "code": 1122,
        },
        "Variable declaration list cannot be empty.": {
            "category": "Error",
            "code": 1123,
        },
        "Digit expected.": {"category": "Error", "code": 1124},
        "Hexadecimal digit expected.": {"category": "Error", "code": 1125},
        "Unexpected end of text.": {"category": "Error", "code": 1126},
        "Invalid character.": {"category": "Error", "code": 1127},
        "Declaration or statement expected.": {"category": "Error", "code": 1128},
        "Statement expected.": {"category": "Error", "code": 1129},
        "'case' or 'default' expected.": {"category": "Error", "code": 1130},
        "Property or signature expected.": {"category": "Error", "code": 1131},
        "Enum member expected.": {"category": "Error", "code": 1132},
        "Variable declaration expected.": {"category": "Error", "code": 1134},
        "Argument expression expected.": {"category": "Error", "code": 1135},
        "Property assignment expected.": {"category": "Error", "code": 1136},
        "Expression or comma expected.": {"category": "Error", "code": 1137},
        "Parameter declaration expected.": {"category": "Error", "code": 1138},
        "Type parameter declaration expected.": {"category": "Error", "code": 1139},
        "Type argument expected.": {"category": "Error", "code": 1140},
        "String literal expected.": {"category": "Error", "code": 1141},
        "Line break not permitted here.": {"category": "Error", "code": 1142},
        "'{' or ';' expected.": {"category": "Error", "code": 1144},
        "Modifiers not permitted on index signature members.": {
            "category": "Error",
            "code": 1145,
        },
        "Declaration expected.": {"category": "Error", "code": 1146},
        "Import declarations in a namespace cannot reference a module.": {
            "category": "Error",
            "code": 1147,
        },
        "Cannot compile modules unless the '--module' flag is provided with a valid module type. Consider setting the 'module' compiler option in a 'tsconfig.json' file.": {
            "category": "Error",
            "code": 1148,
        },
        "File name '{0}' differs from already included file name '{1}' only in casing": {
            "category": "Error",
            "code": 1149,
        },
        "'new T[]' cannot be used to create an array. Use 'new Array<T>()' instead.": {
            "category": "Error",
            "code": 1150,
        },
        "'const' declarations must be initialized": {"category": "Error", "code": 1155},
        "'const' declarations can only be declared inside a block.": {
            "category": "Error",
            "code": 1156,
        },
        "'let' declarations can only be declared inside a block.": {
            "category": "Error",
            "code": 1157,
        },
        "Unterminated template literal.": {"category": "Error", "code": 1160},
        "Unterminated regular expression literal.": {"category": "Error", "code": 1161},
        "An object member cannot be declared optional.": {
            "category": "Error",
            "code": 1162,
        },
        "A 'yield' expression is only allowed in a generator body.": {
            "category": "Error",
            "code": 1163,
        },
        "Computed property names are not allowed in enums.": {
            "category": "Error",
            "code": 1164,
        },
        "A computed property name in an ambient context must directly refer to a built-in symbol.": {
            "category": "Error",
            "code": 1165,
        },
        "A computed property name in a class property declaration must directly refer to a built-in symbol.": {
            "category": "Error",
            "code": 1166,
        },
        "A computed property name in a method overload must directly refer to a built-in symbol.": {
            "category": "Error",
            "code": 1168,
        },
        "A computed property name in an interface must directly refer to a built-in symbol.": {
            "category": "Error",
            "code": 1169,
        },
        "A computed property name in a type literal must directly refer to a built-in symbol.": {
            "category": "Error",
            "code": 1170,
        },
        "A comma expression is not allowed in a computed property name.": {
            "category": "Error",
            "code": 1171,
        },
        "'extends' clause already seen.": {"category": "Error", "code": 1172},
        "'extends' clause must precede 'implements' clause.": {
            "category": "Error",
            "code": 1173,
        },
        "Classes can only extend a single class.": {"category": "Error", "code": 1174},
        "'implements' clause already seen.": {"category": "Error", "code": 1175},
        "Interface declaration cannot have 'implements' clause.": {
            "category": "Error",
            "code": 1176,
        },
        "Binary digit expected.": {"category": "Error", "code": 1177},
        "Octal digit expected.": {"category": "Error", "code": 1178},
        "Unexpected token. '{' expected.": {"category": "Error", "code": 1179},
        "Property destructuring pattern expected.": {"category": "Error", "code": 1180},
        "Array element destructuring pattern expected.": {
            "category": "Error",
            "code": 1181,
        },
        "A destructuring declaration must have an initializer.": {
            "category": "Error",
            "code": 1182,
        },
        "An implementation cannot be declared in ambient contexts.": {
            "category": "Error",
            "code": 1183,
        },
        "Modifiers cannot appear here.": {"category": "Error", "code": 1184},
        "Merge conflict marker encountered.": {"category": "Error", "code": 1185},
        "A rest element cannot have an initializer.": {
            "category": "Error",
            "code": 1186,
        },
        "A parameter property may not be a binding pattern.": {
            "category": "Error",
            "code": 1187,
        },
        "Only a single variable declaration is allowed in a 'for...of' statement.": {
            "category": "Error",
            "code": 1188,
        },
        "The variable declaration of a 'for...in' statement cannot have an initializer.": {
            "category": "Error",
            "code": 1189,
        },
        "The variable declaration of a 'for...of' statement cannot have an initializer.": {
            "category": "Error",
            "code": 1190,
        },
        "An import declaration cannot have modifiers.": {
            "category": "Error",
            "code": 1191,
        },
        "Module '{0}' has no default export.": {"category": "Error", "code": 1192},
        "An export declaration cannot have modifiers.": {
            "category": "Error",
            "code": 1193,
        },
        "Export declarations are not permitted in a namespace.": {
            "category": "Error",
            "code": 1194,
        },
        "Catch clause variable name must be an identifier.": {
            "category": "Error",
            "code": 1195,
        },
        "Catch clause variable cannot have a type annotation.": {
            "category": "Error",
            "code": 1196,
        },
        "Catch clause variable cannot have an initializer.": {
            "category": "Error",
            "code": 1197,
        },
        "An extended Unicode escape value must be between 0x0 and 0x10FFFF inclusive.": {
            "category": "Error",
            "code": 1198,
        },
        "Unterminated Unicode escape sequence.": {"category": "Error", "code": 1199},
        "Line terminator not permitted before arrow.": {
            "category": "Error",
            "code": 1200,
        },
        # pylint: disable=line-too-long
        "Import assignment cannot be used when targeting ECMAScript 6 modules. Consider using 'import * as ns from \"mod\"', 'import {a} from \"mod\"', 'import d from \"mod\"', or another module format instead.": {
            "category": "Error",
            "code": 1202,
        },
        "Export assignment cannot be used when targeting ECMAScript 6 modules. Consider using 'export default' or another module format instead.": {
            "category": "Error",
            "code": 1203,
        },
        "Cannot compile modules into 'es2015' when targeting 'ES5' or lower.": {
            "category": "Error",
            "code": 1204,
        },
        "Decorators are not valid here.": {"category": "Error", "code": 1206},
        "Decorators cannot be applied to multiple get/set accessors of the same name.": {
            "category": "Error",
            "code": 1207,
        },
        "Cannot compile namespaces when the '--isolatedModules' flag is provided.": {
            "category": "Error",
            "code": 1208,
        },
        "Ambient const enums are not allowed when the '--isolatedModules' flag is provided.": {
            "category": "Error",
            "code": 1209,
        },
        "Invalid use of '{0}'. Class definitions are automatically in strict mode.": {
            "category": "Error",
            "code": 1210,
        },
        "A class declaration without the 'default' modifier must have a name": {
            "category": "Error",
            "code": 1211,
        },
        "Identifier expected. '{0}' is a reserved word in strict mode": {
            "category": "Error",
            "code": 1212,
        },
        "Identifier expected. '{0}' is a reserved word in strict mode. Class definitions are automatically in strict mode.": {
            "category": "Error",
            "code": 1213,
        },
        "Identifier expected. '{0}' is a reserved word in strict mode. Modules are automatically in strict mode.": {
            "category": "Error",
            "code": 1214,
        },
        "Invalid use of '{0}'. Modules are automatically in strict mode.": {
            "category": "Error",
            "code": 1215,
        },
        "Export assignment is not supported when '--module' flag is 'system'.": {
            "category": "Error",
            "code": 1218,
        },
        "Experimental support for decorators is a feature that is subject to change in a future release. Set the 'experimentalDecorators' option to remove this warning.": {
            "category": "Error",
            "code": 1219,
        },
        "Generators are only available when targeting ECMAScript 6 or higher.": {
            "category": "Error",
            "code": 1220,
        },
        "Generators are not allowed in an ambient context.": {
            "category": "Error",
            "code": 1221,
        },
        "An overload signature cannot be declared as a generator.": {
            "category": "Error",
            "code": 1222,
        },
        "'{0}' tag already specified.": {"category": "Error", "code": 1223},
        "Signature '{0}' must have a type predicate.": {
            "category": "Error",
            "code": 1224,
        },
        "Cannot find parameter '{0}'.": {"category": "Error", "code": 1225},
        "Type predicate '{0}' is not assignable to '{1}'.": {
            "category": "Error",
            "code": 1226,
        },
        "Parameter '{0}' is not in the same position as parameter '{1}'.": {
            "category": "Error",
            "code": 1227,
        },
        "A type predicate is only allowed in return type position for functions and methods.": {
            "category": "Error",
            "code": 1228,
        },
        "A type predicate cannot reference a rest parameter.": {
            "category": "Error",
            "code": 1229,
        },
        "A type predicate cannot reference element '{0}' in a binding pattern.": {
            "category": "Error",
            "code": 1230,
        },
        "An export assignment can only be used in a module.": {
            "category": "Error",
            "code": 1231,
        },
        "An import declaration can only be used in a namespace or module.": {
            "category": "Error",
            "code": 1232,
        },
        "An export declaration can only be used in a module.": {
            "category": "Error",
            "code": 1233,
        },
        "An ambient module declaration is only allowed at the top level in a file.": {
            "category": "Error",
            "code": 1234,
        },
        "A namespace declaration is only allowed in a namespace or module.": {
            "category": "Error",
            "code": 1235,
        },
        "The return type of a property decorator function must be either 'void' or 'any'.": {
            "category": "Error",
            "code": 1236,
        },
        "The return type of a parameter decorator function must be either 'void' or 'any'.": {
            "category": "Error",
            "code": 1237,
        },
        "Unable to resolve signature of class decorator when called as an expression.": {
            "category": "Error",
            "code": 1238,
        },
        "Unable to resolve signature of parameter decorator when called as an expression.": {
            "category": "Error",
            "code": 1239,
        },
        "Unable to resolve signature of property decorator when called as an expression.": {
            "category": "Error",
            "code": 1240,
        },
        "Unable to resolve signature of method decorator when called as an expression.": {
            "category": "Error",
            "code": 1241,
        },
        "'abstract' modifier can only appear on a class or method declaration.": {
            "category": "Error",
            "code": 1242,
        },
        "'{0}' modifier cannot be used with '{1}' modifier.": {
            "category": "Error",
            "code": 1243,
        },
        "Abstract methods can only appear within an abstract class.": {
            "category": "Error",
            "code": 1244,
        },
        "Method '{0}' cannot have an implementation because it is marked abstract.": {
            "category": "Error",
            "code": 1245,
        },
        "An interface property cannot have an initializer.": {
            "category": "Error",
            "code": 1246,
        },
        "A type literal property cannot have an initializer.": {
            "category": "Error",
            "code": 1247,
        },
        "A class member cannot have the '{0}' keyword.": {
            "category": "Error",
            "code": 1248,
        },
        "A decorator can only decorate a method implementation, not an overload.": {
            "category": "Error",
            "code": 1249,
        },
        "'with' statements are not allowed in an async function block.": {
            "category": "Error",
            "code": 1300,
        },
        "'await' expression is only allowed within an async function.": {
            "category": "Error",
            "code": 1308,
        },
        "Async functions are only available when targeting ECMAScript 6 and higher.": {
            "category": "Error",
            "code": 1311,
        },
        "'=' can only be used in an object literal property inside a destructuring assignment.": {
            "category": "Error",
            "code": 1312,
        },
        "The body of an 'if' statement cannot be the empty statement.": {
            "category": "Error",
            "code": 1313,
        },
        "Duplicate identifier '{0}'.": {"category": "Error", "code": 2300},
        "Initializer of instance member variable '{0}' cannot reference identifier '{1}' declared in the constructor.": {
            "category": "Error",
            "code": 2301,
        },
        "Static members cannot reference class type parameters.": {
            "category": "Error",
            "code": 2302,
        },
        "Circular definition of import alias '{0}'.": {
            "category": "Error",
            "code": 2303,
        },
        "Cannot find name '{0}'.": {"category": "Error", "code": 2304},
        "Module '{0}' has no exported member '{1}'.": {
            "category": "Error",
            "code": 2305,
        },
        "File '{0}' is not a module.": {"category": "Error", "code": 2306},
        "Cannot find module '{0}'.": {"category": "Error", "code": 2307},
        "Module {0} has already exported a member named '{1}'. Consider explicitly re-exporting to resolve the ambiguity.": {
            "category": "Error",
            "code": 2308,
        },
        "An export assignment cannot be used in a module with other exported elements.": {
            "category": "Error",
            "code": 2309,
        },
        "Type '{0}' recursively references itself as a base type.": {
            "category": "Error",
            "code": 2310,
        },
        "A class may only extend another class.": {"category": "Error", "code": 2311},
        "An interface may only extend a class or another interface.": {
            "category": "Error",
            "code": 2312,
        },
        "Type parameter '{0}' has a circular constraint.": {
            "category": "Error",
            "code": 2313,
        },
        "Generic type '{0}' requires {1} type argument(s).": {
            "category": "Error",
            "code": 2314,
        },
        "Type '{0}' is not generic.": {"category": "Error", "code": 2315},
        "Global type '{0}' must be a class or interface type.": {
            "category": "Error",
            "code": 2316,
        },
        "Global type '{0}' must have {1} type parameter(s).": {
            "category": "Error",
            "code": 2317,
        },
        "Cannot find global type '{0}'.": {"category": "Error", "code": 2318},
        "Named property '{0}' of types '{1}' and '{2}' are not identical.": {
            "category": "Error",
            "code": 2319,
        },
        "Interface '{0}' cannot simultaneously extend types '{1}' and '{2}'.": {
            "category": "Error",
            "code": 2320,
        },
        "Excessive stack depth comparing types '{0}' and '{1}'.": {
            "category": "Error",
            "code": 2321,
        },
        "Type '{0}' is not assignable to type '{1}'.": {
            "category": "Error",
            "code": 2322,
        },
        "Cannot redeclare exported variable '{0}'.": {
            "category": "Error",
            "code": 2323,
        },
        "Property '{0}' is missing in type '{1}'.": {"category": "Error", "code": 2324},
        "Property '{0}' is private in type '{1}' but not in type '{2}'.": {
            "category": "Error",
            "code": 2325,
        },
        "Types of property '{0}' are incompatible.": {
            "category": "Error",
            "code": 2326,
        },
        "Property '{0}' is optional in type '{1}' but required in type '{2}'.": {
            "category": "Error",
            "code": 2327,
        },
        "Types of parameters '{0}' and '{1}' are incompatible.": {
            "category": "Error",
            "code": 2328,
        },
        "Index signature is missing in type '{0}'.": {
            "category": "Error",
            "code": 2329,
        },
        "Index signatures are incompatible.": {"category": "Error", "code": 2330},
        "'this' cannot be referenced in a module or namespace body.": {
            "category": "Error",
            "code": 2331,
        },
        "'this' cannot be referenced in current location.": {
            "category": "Error",
            "code": 2332,
        },
        "'this' cannot be referenced in constructor arguments.": {
            "category": "Error",
            "code": 2333,
        },
        "'this' cannot be referenced in a static property initializer.": {
            "category": "Error",
            "code": 2334,
        },
        "'super' can only be referenced in a derived class.": {
            "category": "Error",
            "code": 2335,
        },
        "'super' cannot be referenced in constructor arguments.": {
            "category": "Error",
            "code": 2336,
        },
        "Super calls are not permitted outside constructors or in nested functions inside constructors.": {
            "category": "Error",
            "code": 2337,
        },
        "'super' property access is permitted only in a constructor, member function, or member accessor of a derived class.": {
            "category": "Error",
            "code": 2338,
        },
        "Property '{0}' does not exist on type '{1}'.": {
            "category": "Error",
            "code": 2339,
        },
        "Only public and protected methods of the base class are accessible via the 'super' keyword.": {
            "category": "Error",
            "code": 2340,
        },
        "Property '{0}' is private and only accessible within class '{1}'.": {
            "category": "Error",
            "code": 2341,
        },
        "An index expression argument must be of type 'string', 'number', 'symbol', or 'any'.": {
            "category": "Error",
            "code": 2342,
        },
        "Type '{0}' does not satisfy the constraint '{1}'.": {
            "category": "Error",
            "code": 2344,
        },
        "Argument of type '{0}' is not assignable to parameter of type '{1}'.": {
            "category": "Error",
            "code": 2345,
        },
        "Supplied parameters do not match any signature of call target.": {
            "category": "Error",
            "code": 2346,
        },
        "Untyped function calls may not accept type arguments.": {
            "category": "Error",
            "code": 2347,
        },
        "Value of type '{0}' is not callable. Did you mean to include 'new'?": {
            "category": "Error",
            "code": 2348,
        },
        "Cannot invoke an expression whose type lacks a call signature.": {
            "category": "Error",
            "code": 2349,
        },
        "Only a void function can be called with the 'new' keyword.": {
            "category": "Error",
            "code": 2350,
        },
        "Cannot use 'new' with an expression whose type lacks a call or construct signature.": {
            "category": "Error",
            "code": 2351,
        },
        "Neither type '{0}' nor type '{1}' is assignable to the other.": {
            "category": "Error",
            "code": 2352,
        },
        "Object literal may only specify known properties, and '{0}' does not exist in type '{1}'.": {
            "category": "Error",
            "code": 2353,
        },
        "No best common type exists among return expressions.": {
            "category": "Error",
            "code": 2354,
        },
        "A function whose declared type is neither 'void' nor 'any' must return a value.": {
            "category": "Error",
            "code": 2355,
        },
        "An arithmetic operand must be of type 'any', 'number' or an enum type.": {
            "category": "Error",
            "code": 2356,
        },
        "The operand of an increment or decrement operator must be a variable, property or indexer.": {
            "category": "Error",
            "code": 2357,
        },
        "The left-hand side of an 'instanceof' expression must be of type 'any', an object type or a type parameter.": {
            "category": "Error",
            "code": 2358,
        },
        "The right-hand side of an 'instanceof' expression must be of type 'any' or of a type assignable to the 'Function' interface type.": {
            "category": "Error",
            "code": 2359,
        },
        "The left-hand side of an 'in' expression must be of type 'any', 'string', 'number', or 'symbol'.": {
            "category": "Error",
            "code": 2360,
        },
        "The right-hand side of an 'in' expression must be of type 'any', an object type or a type parameter": {
            "category": "Error",
            "code": 2361,
        },
        "The left-hand side of an arithmetic operation must be of type 'any', 'number' or an enum type.": {
            "category": "Error",
            "code": 2362,
        },
        "The right-hand side of an arithmetic operation must be of type 'any', 'number' or an enum type.": {
            "category": "Error",
            "code": 2363,
        },
        "Invalid left-hand side of assignment expression.": {
            "category": "Error",
            "code": 2364,
        },
        "Operator '{0}' cannot be applied to types '{1}' and '{2}'.": {
            "category": "Error",
            "code": 2365,
        },
        "Type parameter name cannot be '{0}'": {"category": "Error", "code": 2368},
        "A parameter property is only allowed in a constructor implementation.": {
            "category": "Error",
            "code": 2369,
        },
        "A rest parameter must be of an array type.": {
            "category": "Error",
            "code": 2370,
        },
        "A parameter initializer is only allowed in a function or constructor implementation.": {
            "category": "Error",
            "code": 2371,
        },
        "Parameter '{0}' cannot be referenced in its initializer.": {
            "category": "Error",
            "code": 2372,
        },
        "Initializer of parameter '{0}' cannot reference identifier '{1}' declared after it.": {
            "category": "Error",
            "code": 2373,
        },
        "Duplicate string index signature.": {"category": "Error", "code": 2374},
        "Duplicate number index signature.": {"category": "Error", "code": 2375},
        "A 'super' call must be the first statement in the constructor when a class contains initialized properties or has parameter properties.": {
            "category": "Error",
            "code": 2376,
        },
        "Constructors for derived classes must contain a 'super' call.": {
            "category": "Error",
            "code": 2377,
        },
        "A 'get' accessor must return a value.": {"category": "Error", "code": 2378},
        "Getter and setter accessors do not agree in visibility.": {
            "category": "Error",
            "code": 2379,
        },
        "'get' and 'set' accessor must have the same type.": {
            "category": "Error",
            "code": 2380,
        },
        "A signature with an implementation cannot use a string literal type.": {
            "category": "Error",
            "code": 2381,
        },
        "Specialized overload signature is not assignable to any non-specialized signature.": {
            "category": "Error",
            "code": 2382,
        },
        "Overload signatures must all be exported or not exported.": {
            "category": "Error",
            "code": 2383,
        },
        "Overload signatures must all be ambient or non-ambient.": {
            "category": "Error",
            "code": 2384,
        },
        "Overload signatures must all be public, private or protected.": {
            "category": "Error",
            "code": 2385,
        },
        "Overload signatures must all be optional or required.": {
            "category": "Error",
            "code": 2386,
        },
        "Function overload must be static.": {"category": "Error", "code": 2387},
        "Function overload must not be static.": {"category": "Error", "code": 2388},
        "Function implementation name must be '{0}'.": {
            "category": "Error",
            "code": 2389,
        },
        "Constructor implementation is missing.": {"category": "Error", "code": 2390},
        "Function implementation is missing or not immediately following the declaration.": {
            "category": "Error",
            "code": 2391,
        },
        "Multiple constructor implementations are not allowed.": {
            "category": "Error",
            "code": 2392,
        },
        "Duplicate function implementation.": {"category": "Error", "code": 2393},
        "Overload signature is not compatible with function implementation.": {
            "category": "Error",
            "code": 2394,
        },
        "Individual declarations in merged declaration '{0}' must be all exported or all local.": {
            "category": "Error",
            "code": 2395,
        },
        "Duplicate identifier 'arguments'. Compiler uses 'arguments' to initialize rest parameters.": {
            "category": "Error",
            "code": 2396,
        },
        "Declaration name conflicts with built-in global identifier '{0}'.": {
            "category": "Error",
            "code": 2397,
        },
        "Duplicate identifier '_this'. Compiler uses variable declaration '_this' to capture 'this' reference.": {
            "category": "Error",
            "code": 2399,
        },
        "Expression resolves to variable declaration '_this' that compiler uses to capture 'this' reference.": {
            "category": "Error",
            "code": 2400,
        },
        "Duplicate identifier '_super'. Compiler uses '_super' to capture base class reference.": {
            "category": "Error",
            "code": 2401,
        },
        "Expression resolves to '_super' that compiler uses to capture base class reference.": {
            "category": "Error",
            "code": 2402,
        },
        "Subsequent variable declarations must have the same type.  Variable '{0}' must be of type '{1}', but here has type '{2}'.": {
            "category": "Error",
            "code": 2403,
        },
        "The left-hand side of a 'for...in' statement cannot use a type annotation.": {
            "category": "Error",
            "code": 2404,
        },
        "The left-hand side of a 'for...in' statement must be of type 'string' or 'any'.": {
            "category": "Error",
            "code": 2405,
        },
        "Invalid left-hand side in 'for...in' statement.": {
            "category": "Error",
            "code": 2406,
        },
        "The right-hand side of a 'for...in' statement must be of type 'any', an object type or a type parameter.": {
            "category": "Error",
            "code": 2407,
        },
        "Setters cannot return a value.": {"category": "Error", "code": 2408},
        "Return type of constructor signature must be assignable to the instance type of the class": {
            "category": "Error",
            "code": 2409,
        },
        "All symbols within a 'with' block will be resolved to 'any'.": {
            "category": "Error",
            "code": 2410,
        },
        "Property '{0}' of type '{1}' is not assignable to string index type '{2}'.": {
            "category": "Error",
            "code": 2411,
        },
        "Property '{0}' of type '{1}' is not assignable to numeric index type '{2}'.": {
            "category": "Error",
            "code": 2412,
        },
        "Numeric index type '{0}' is not assignable to string index type '{1}'.": {
            "category": "Error",
            "code": 2413,
        },
        "Class name cannot be '{0}'": {"category": "Error", "code": 2414},
        "Class '{0}' incorrectly extends base class '{1}'.": {
            "category": "Error",
            "code": 2415,
        },
        "Class static side '{0}' incorrectly extends base class static side '{1}'.": {
            "category": "Error",
            "code": 2417,
        },
        "Type name '{0}' in extends clause does not reference constructor function for '{0}'.": {
            "category": "Error",
            "code": 2419,
        },
        "Class '{0}' incorrectly implements interface '{1}'.": {
            "category": "Error",
            "code": 2420,
        },
        "A class may only implement another class or interface.": {
            "category": "Error",
            "code": 2422,
        },
        "Class '{0}' defines instance member function '{1}', but extended class '{2}' defines it as instance member accessor.": {
            "category": "Error",
            "code": 2423,
        },
        "Class '{0}' defines instance member function '{1}', but extended class '{2}' defines it as instance member property.": {
            "category": "Error",
            "code": 2424,
        },
        "Class '{0}' defines instance member property '{1}', but extended class '{2}' defines it as instance member function.": {
            "category": "Error",
            "code": 2425,
        },
        "Class '{0}' defines instance member accessor '{1}', but extended class '{2}' defines it as instance member function.": {
            "category": "Error",
            "code": 2426,
        },
        "Interface name cannot be '{0}'": {"category": "Error", "code": 2427},
        "All declarations of an interface must have identical type parameters.": {
            "category": "Error",
            "code": 2428,
        },
        "Interface '{0}' incorrectly extends interface '{1}'.": {
            "category": "Error",
            "code": 2430,
        },
        "Enum name cannot be '{0}'": {"category": "Error", "code": 2431},
        "In an enum with multiple declarations, only one declaration can omit an initializer for its first enum element.": {
            "category": "Error",
            "code": 2432,
        },
        "A namespace declaration cannot be in a different file from a class or function with which it is merged": {
            "category": "Error",
            "code": 2433,
        },
        "A namespace declaration cannot be located prior to a class or function with which it is merged": {
            "category": "Error",
            "code": 2434,
        },
        "Ambient modules cannot be nested in other modules or namespaces.": {
            "category": "Error",
            "code": 2435,
        },
        "Ambient module declaration cannot specify relative module name.": {
            "category": "Error",
            "code": 2436,
        },
        "Module '{0}' is hidden by a local declaration with the same name": {
            "category": "Error",
            "code": 2437,
        },
        "Import name cannot be '{0}'": {"category": "Error", "code": 2438},
        "Import or export declaration in an ambient module declaration cannot reference module through relative module name.": {
            "category": "Error",
            "code": 2439,
        },
        "Import declaration conflicts with local declaration of '{0}'": {
            "category": "Error",
            "code": 2440,
        },
        "Duplicate identifier '{0}'. Compiler reserves name '{1}' in top level scope of a module.": {
            "category": "Error",
            "code": 2441,
        },
        "Types have separate declarations of a private property '{0}'.": {
            "category": "Error",
            "code": 2442,
        },
        "Property '{0}' is protected but type '{1}' is not a class derived from '{2}'.": {
            "category": "Error",
            "code": 2443,
        },
        "Property '{0}' is protected in type '{1}' but public in type '{2}'.": {
            "category": "Error",
            "code": 2444,
        },
        "Property '{0}' is protected and only accessible within class '{1}' and its subclasses.": {
            "category": "Error",
            "code": 2445,
        },
        "Property '{0}' is protected and only accessible through an instance of class '{1}'.": {
            "category": "Error",
            "code": 2446,
        },
        "The '{0}' operator is not allowed for boolean types. Consider using '{1}' instead.": {
            "category": "Error",
            "code": 2447,
        },
        "Block-scoped variable '{0}' used before its declaration.": {
            "category": "Error",
            "code": 2448,
        },
        "The operand of an increment or decrement operator cannot be a constant.": {
            "category": "Error",
            "code": 2449,
        },
        "Left-hand side of assignment expression cannot be a constant.": {
            "category": "Error",
            "code": 2450,
        },
        "Cannot redeclare block-scoped variable '{0}'.": {
            "category": "Error",
            "code": 2451,
        },
        "An enum member cannot have a numeric name.": {
            "category": "Error",
            "code": 2452,
        },
        "The type argument for type parameter '{0}' cannot be inferred from the usage. Consider specifying the type arguments explicitly.": {
            "category": "Error",
            "code": 2453,
        },
        "Type argument candidate '{1}' is not a valid type argument because it is not a supertype of candidate '{0}'.": {
            "category": "Error",
            "code": 2455,
        },
        "Type alias '{0}' circularly references itself.": {
            "category": "Error",
            "code": 2456,
        },
        "Type alias name cannot be '{0}'": {"category": "Error", "code": 2457},
        "An AMD module cannot have multiple name assignments.": {
            "category": "Error",
            "code": 2458,
        },
        "Type '{0}' has no property '{1}' and no string index signature.": {
            "category": "Error",
            "code": 2459,
        },
        "Type '{0}' has no property '{1}'.": {"category": "Error", "code": 2460},
        "Type '{0}' is not an array type.": {"category": "Error", "code": 2461},
        "A rest element must be last in an array destructuring pattern": {
            "category": "Error",
            "code": 2462,
        },
        "A binding pattern parameter cannot be optional in an implementation signature.": {
            "category": "Error",
            "code": 2463,
        },
        "A computed property name must be of type 'string', 'number', 'symbol', or 'any'.": {
            "category": "Error",
            "code": 2464,
        },
        "'this' cannot be referenced in a computed property name.": {
            "category": "Error",
            "code": 2465,
        },
        "'super' cannot be referenced in a computed property name.": {
            "category": "Error",
            "code": 2466,
        },
        "A computed property name cannot reference a type parameter from its containing type.": {
            "category": "Error",
            "code": 2467,
        },
        "Cannot find global value '{0}'.": {"category": "Error", "code": 2468},
        "The '{0}' operator cannot be applied to type 'symbol'.": {
            "category": "Error",
            "code": 2469,
        },
        "'Symbol' reference does not refer to the global Symbol constructor object.": {
            "category": "Error",
            "code": 2470,
        },
        "A computed property name of the form '{0}' must be of type 'symbol'.": {
            "category": "Error",
            "code": 2471,
        },
        "Spread operator in 'new' expressions is only available when targeting ECMAScript 5 and higher.": {
            "category": "Error",
            "code": 2472,
        },
        "Enum declarations must all be const or non-const.": {
            "category": "Error",
            "code": 2473,
        },
        "In 'const' enum declarations member initializer must be constant expression.": {
            "category": "Error",
            "code": 2474,
        },
        "'const' enums can only be used in property or index access expressions or the right hand side of an import declaration or export assignment.": {
            "category": "Error",
            "code": 2475,
        },
        "A const enum member can only be accessed using a string literal.": {
            "category": "Error",
            "code": 2476,
        },
        "'const' enum member initializer was evaluated to a non-finite value.": {
            "category": "Error",
            "code": 2477,
        },
        "'const' enum member initializer was evaluated to disallowed value 'NaN'.": {
            "category": "Error",
            "code": 2478,
        },
        "Property '{0}' does not exist on 'const' enum '{1}'.": {
            "category": "Error",
            "code": 2479,
        },
        "'let' is not allowed to be used as a name in 'let' or 'const' declarations.": {
            "category": "Error",
            "code": 2480,
        },
        "Cannot initialize outer scoped variable '{0}' in the same scope as block scoped declaration '{1}'.": {
            "category": "Error",
            "code": 2481,
        },
        "The left-hand side of a 'for...of' statement cannot use a type annotation.": {
            "category": "Error",
            "code": 2483,
        },
        "Export declaration conflicts with exported declaration of '{0}'": {
            "category": "Error",
            "code": 2484,
        },
        "The left-hand side of a 'for...of' statement cannot be a previously defined constant.": {
            "category": "Error",
            "code": 2485,
        },
        "The left-hand side of a 'for...in' statement cannot be a previously defined constant.": {
            "category": "Error",
            "code": 2486,
        },
        "Invalid left-hand side in 'for...of' statement.": {
            "category": "Error",
            "code": 2487,
        },
        "Type must have a '[Symbol.iterator]()' method that returns an iterator.": {
            "category": "Error",
            "code": 2488,
        },
        "An iterator must have a 'next()' method.": {"category": "Error", "code": 2489},
        "The type returned by the 'next()' method of an iterator must have a 'value' property.": {
            "category": "Error",
            "code": 2490,
        },
        "The left-hand side of a 'for...in' statement cannot be a destructuring pattern.": {
            "category": "Error",
            "code": 2491,
        },
        "Cannot redeclare identifier '{0}' in catch clause": {
            "category": "Error",
            "code": 2492,
        },
        "Tuple type '{0}' with length '{1}' cannot be assigned to tuple with length '{2}'.": {
            "category": "Error",
            "code": 2493,
        },
        "Using a string in a 'for...of' statement is only supported in ECMAScript 5 and higher.": {
            "category": "Error",
            "code": 2494,
        },
        "Type '{0}' is not an array type or a string type.": {
            "category": "Error",
            "code": 2495,
        },
        "The 'arguments' object cannot be referenced in an arrow function in ES3 and ES5. Consider using a standard function expression.": {
            "category": "Error",
            "code": 2496,
        },
        "Module '{0}' resolves to a non-module entity and cannot be imported using this construct.": {
            "category": "Error",
            "code": 2497,
        },
        "Module '{0}' uses 'export =' and cannot be used with 'export *'.": {
            "category": "Error",
            "code": 2498,
        },
        "An interface can only extend an identifier/qualified-name with optional type arguments.": {
            "category": "Error",
            "code": 2499,
        },
        "A class can only implement an identifier/qualified-name with optional type arguments.": {
            "category": "Error",
            "code": 2500,
        },
        "A rest element cannot contain a binding pattern.": {
            "category": "Error",
            "code": 2501,
        },
        "'{0}' is referenced directly or indirectly in its own type annotation.": {
            "category": "Error",
            "code": 2502,
        },
        "Cannot find namespace '{0}'.": {"category": "Error", "code": 2503},
        "No best common type exists among yield expressions.": {
            "category": "Error",
            "code": 2504,
        },
        "A generator cannot have a 'void' type annotation.": {
            "category": "Error",
            "code": 2505,
        },
        "'{0}' is referenced directly or indirectly in its own base expression.": {
            "category": "Error",
            "code": 2506,
        },
        "Type '{0}' is not a constructor function type.": {
            "category": "Error",
            "code": 2507,
        },
        "No base constructor has the specified number of type arguments.": {
            "category": "Error",
            "code": 2508,
        },
        "Base constructor return type '{0}' is not a class or interface type.": {
            "category": "Error",
            "code": 2509,
        },
        "Base constructors must all have the same return type.": {
            "category": "Error",
            "code": 2510,
        },
        "Cannot create an instance of the abstract class '{0}'.": {
            "category": "Error",
            "code": 2511,
        },
        "Overload signatures must all be abstract or not abstract.": {
            "category": "Error",
            "code": 2512,
        },
        "Abstract method '{0}' in class '{1}' cannot be accessed via super expression.": {
            "category": "Error",
            "code": 2513,
        },
        "Classes containing abstract methods must be marked abstract.": {
            "category": "Error",
            "code": 2514,
        },
        "Non-abstract class '{0}' does not implement inherited abstract member '{1}' from class '{2}'.": {
            "category": "Error",
            "code": 2515,
        },
        "All declarations of an abstract method must be consecutive.": {
            "category": "Error",
            "code": 2516,
        },
        "Cannot assign an abstract constructor type to a non-abstract constructor type.": {
            "category": "Error",
            "code": 2517,
        },
        "A 'this'-based type guard is not compatible with a parameter-based type guard.": {
            "category": "Error",
            "code": 2518,
        },
        "Duplicate identifier '{0}'. Compiler uses declaration '{1}' to support async functions.": {
            "category": "Error",
            "code": 2520,
        },
        "Expression resolves to variable declaration '{0}' that compiler uses to support async functions.": {
            "category": "Error",
            "code": 2521,
        },
        "The 'arguments' object cannot be referenced in an async arrow function. Consider using a standard async function expression.": {
            "category": "Error",
            "code": 2522,
        },
        "'yield' expressions cannot be used in a parameter initializer.": {
            "category": "Error",
            "code": 2523,
        },
        "'await' expressions cannot be used in a parameter initializer.": {
            "category": "Error",
            "code": 2524,
        },
        "Initializer provides no value for this binding element and the binding element has no default value.": {
            "category": "Error",
            "code": 2525,
        },
        "A 'this' type is available only in a non-static member of a class or interface.": {
            "category": "Error",
            "code": 2526,
        },
        "The inferred type of '{0}' references an inaccessible 'this' type. A type annotation is necessary.": {
            "category": "Error",
            "code": 2527,
        },
        "A module cannot have multiple default exports.": {
            "category": "Error",
            "code": 2528,
        },
        "Duplicate identifier '{0}'. Compiler reserves name '{1}' in top level scope of a module containing async functions.": {
            "category": "Error",
            "code": 2529,
        },
        "JSX element attributes type '{0}' may not be a union type.": {
            "category": "Error",
            "code": 2600,
        },
        "The return type of a JSX element constructor must return an object type.": {
            "category": "Error",
            "code": 2601,
        },
        "JSX element implicitly has type 'any' because the global type 'JSX.Element' does not exist.": {
            "category": "Error",
            "code": 2602,
        },
        "Property '{0}' in type '{1}' is not assignable to type '{2}'": {
            "category": "Error",
            "code": 2603,
        },
        "JSX element type '{0}' does not have any construct or call signatures.": {
            "category": "Error",
            "code": 2604,
        },
        "JSX element type '{0}' is not a constructor function for JSX elements.": {
            "category": "Error",
            "code": 2605,
        },
        "Property '{0}' of JSX spread attribute is not assignable to target property.": {
            "category": "Error",
            "code": 2606,
        },
        "JSX element class does not support attributes because it does not have a '{0}' property": {
            "category": "Error",
            "code": 2607,
        },
        "The global type 'JSX.{0}' may not have more than one property": {
            "category": "Error",
            "code": 2608,
        },
        "Cannot emit namespaced JSX elements in React": {
            "category": "Error",
            "code": 2650,
        },
        "A member initializer in a enum declaration cannot reference members declared after it, including members defined in other enums.": {
            "category": "Error",
            "code": 2651,
        },
        "Merged declaration '{0}' cannot include a default export declaration. Consider adding a separate 'export default {0}' declaration instead.": {
            "category": "Error",
            "code": 2652,
        },
        "Non-abstract class expression does not implement inherited abstract member '{0}' from class '{1}'.": {
            "category": "Error",
            "code": 2653,
        },
        "Exported external package typings file cannot contain tripleslash references. Please contact the package author to update the package definition.": {
            "category": "Error",
            "code": 2654,
        },
        "Exported external package typings file '{0}' is not a module. Please contact the package author to update the package definition.": {
            "category": "Error",
            "code": 2656,
        },
        "JSX expressions must have one parent element": {
            "category": "Error",
            "code": 2657,
        },
        "Type '{0}' provides no match for the signature '{1}'": {
            "category": "Error",
            "code": 2658,
        },
        "'super' is only allowed in members of object literal expressions when option 'target' is 'ES2015' or higher.": {
            "category": "Error",
            "code": 2659,
        },
        "'super' can only be referenced in members of derived classes or object literal expressions.": {
            "category": "Error",
            "code": 2660,
        },
        "Cannot re-export name that is not defined in the module.": {
            "category": "Error",
            "code": 2661,
        },
        "Cannot find name '{0}'. Did you mean the static member '{1}.{0}'?": {
            "category": "Error",
            "code": 2662,
        },
        "Cannot find name '{0}'. Did you mean the instance member 'this.{0}'?": {
            "category": "Error",
            "code": 2663,
        },
        "Invalid module name in augmentation, module '{0}' cannot be found.": {
            "category": "Error",
            "code": 2664,
        },
        "Module augmentation cannot introduce new names in the top level scope.": {
            "category": "Error",
            "code": 2665,
        },
        "Exports and export assignments are not permitted in module augmentations.": {
            "category": "Error",
            "code": 2666,
        },
        "Imports are not permitted in module augmentations. Consider moving them to the enclosing external module.": {
            "category": "Error",
            "code": 2667,
        },
        "'export' modifier cannot be applied to ambient modules and module augmentations since they are always visible.": {
            "category": "Error",
            "code": 2668,
        },
        "Augmentations for the global scope can only be directly nested in external modules or ambient module declarations.": {
            "category": "Error",
            "code": 2669,
        },
        "Augmentations for the global scope should have 'declare' modifier unless they appear in already ambient context.": {
            "category": "Error",
            "code": 2670,
        },
        "Cannot augment module '{0}' because it resolves to a non-module entity.": {
            "category": "Error",
            "code": 2671,
        },
        "Import declaration '{0}' is using private name '{1}'.": {
            "category": "Error",
            "code": 4000,
        },
        "Type parameter '{0}' of exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4002,
        },
        "Type parameter '{0}' of exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4004,
        },
        "Type parameter '{0}' of constructor signature from exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4006,
        },
        "Type parameter '{0}' of call signature from exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4008,
        },
        "Type parameter '{0}' of public static method from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4010,
        },
        "Type parameter '{0}' of public method from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4012,
        },
        "Type parameter '{0}' of method from exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4014,
        },
        "Type parameter '{0}' of exported function has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4016,
        },
        "Implements clause of exported class '{0}' has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4019,
        },
        "Extends clause of exported class '{0}' has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4020,
        },
        "Extends clause of exported interface '{0}' has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4022,
        },
        "Exported variable '{0}' has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4023,
        },
        "Exported variable '{0}' has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4024,
        },
        "Exported variable '{0}' has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4025,
        },
        "Public static property '{0}' of exported class has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4026,
        },
        "Public static property '{0}' of exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4027,
        },
        "Public static property '{0}' of exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4028,
        },
        "Public property '{0}' of exported class has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4029,
        },
        "Public property '{0}' of exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4030,
        },
        "Public property '{0}' of exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4031,
        },
        "Property '{0}' of exported interface has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4032,
        },
        "Property '{0}' of exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4033,
        },
        "Parameter '{0}' of public static property setter from exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4034,
        },
        "Parameter '{0}' of public static property setter from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4035,
        },
        "Parameter '{0}' of public property setter from exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4036,
        },
        "Parameter '{0}' of public property setter from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4037,
        },
        "Return type of public static property getter from exported class has or is using name '{0}' from external module {1} but cannot be named.": {
            "category": "Error",
            "code": 4038,
        },
        "Return type of public static property getter from exported class has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4039,
        },
        "Return type of public static property getter from exported class has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4040,
        },
        "Return type of public property getter from exported class has or is using name '{0}' from external module {1} but cannot be named.": {
            "category": "Error",
            "code": 4041,
        },
        "Return type of public property getter from exported class has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4042,
        },
        "Return type of public property getter from exported class has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4043,
        },
        "Return type of constructor signature from exported interface has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4044,
        },
        "Return type of constructor signature from exported interface has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4045,
        },
        "Return type of call signature from exported interface has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4046,
        },
        "Return type of call signature from exported interface has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4047,
        },
        "Return type of index signature from exported interface has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4048,
        },
        "Return type of index signature from exported interface has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4049,
        },
        "Return type of public static method from exported class has or is using name '{0}' from external module {1} but cannot be named.": {
            "category": "Error",
            "code": 4050,
        },
        "Return type of public static method from exported class has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4051,
        },
        "Return type of public static method from exported class has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4052,
        },
        "Return type of public method from exported class has or is using name '{0}' from external module {1} but cannot be named.": {
            "category": "Error",
            "code": 4053,
        },
        "Return type of public method from exported class has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4054,
        },
        "Return type of public method from exported class has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4055,
        },
        "Return type of method from exported interface has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4056,
        },
        "Return type of method from exported interface has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4057,
        },
        "Return type of exported function has or is using name '{0}' from external module {1} but cannot be named.": {
            "category": "Error",
            "code": 4058,
        },
        "Return type of exported function has or is using name '{0}' from private module '{1}'.": {
            "category": "Error",
            "code": 4059,
        },
        "Return type of exported function has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4060,
        },
        "Parameter '{0}' of constructor from exported class has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4061,
        },
        "Parameter '{0}' of constructor from exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4062,
        },
        "Parameter '{0}' of constructor from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4063,
        },
        "Parameter '{0}' of constructor signature from exported interface has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4064,
        },
        "Parameter '{0}' of constructor signature from exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4065,
        },
        "Parameter '{0}' of call signature from exported interface has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4066,
        },
        "Parameter '{0}' of call signature from exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4067,
        },
        "Parameter '{0}' of public static method from exported class has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4068,
        },
        "Parameter '{0}' of public static method from exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4069,
        },
        "Parameter '{0}' of public static method from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4070,
        },
        "Parameter '{0}' of public method from exported class has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4071,
        },
        "Parameter '{0}' of public method from exported class has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4072,
        },
        "Parameter '{0}' of public method from exported class has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4073,
        },
        "Parameter '{0}' of method from exported interface has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4074,
        },
        "Parameter '{0}' of method from exported interface has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4075,
        },
        "Parameter '{0}' of exported function has or is using name '{1}' from external module {2} but cannot be named.": {
            "category": "Error",
            "code": 4076,
        },
        "Parameter '{0}' of exported function has or is using name '{1}' from private module '{2}'.": {
            "category": "Error",
            "code": 4077,
        },
        "Parameter '{0}' of exported function has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4078,
        },
        "Exported type alias '{0}' has or is using private name '{1}'.": {
            "category": "Error",
            "code": 4081,
        },
        "Default export of the module has or is using private name '{0}'.": {
            "category": "Error",
            "code": 4082,
        },
        "The current host does not support the '{0}' option.": {
            "category": "Error",
            "code": 5001,
        },
        "Cannot find the common subdirectory path for the input files.": {
            "category": "Error",
            "code": 5009,
        },
        "Cannot read file '{0}': {1}": {"category": "Error", "code": 5012},
        "Unsupported file encoding.": {"category": "Error", "code": 5013},
        "Failed to parse file '{0}': {1}.": {"category": "Error", "code": 5014},
        "Unknown compiler option '{0}'.": {"category": "Error", "code": 5023},
        "Compiler option '{0}' requires a value of type {1}.": {
            "category": "Error",
            "code": 5024,
        },
        "Could not write file '{0}': {1}": {"category": "Error", "code": 5033},
        "Option 'project' cannot be mixed with source files on a command line.": {
            "category": "Error",
            "code": 5042,
        },
        "Option 'isolatedModules' can only be used when either option '--module' is provided or option 'target' is 'ES2015' or higher.": {
            "category": "Error",
            "code": 5047,
        },
        "Option 'inlineSources' can only be used when either option '--inlineSourceMap' or option '--sourceMap' is provided.": {
            "category": "Error",
            "code": 5051,
        },
        "Option '{0}' cannot be specified without specifying option '{1}'.": {
            "category": "Error",
            "code": 5052,
        },
        "Option '{0}' cannot be specified with option '{1}'.": {
            "category": "Error",
            "code": 5053,
        },
        "A 'tsconfig.json' file is already defined at: '{0}'.": {
            "category": "Error",
            "code": 5054,
        },
        "Cannot write file '{0}' because it would overwrite input file.": {
            "category": "Error",
            "code": 5055,
        },
        "Cannot write file '{0}' because it would be overwritten by multiple input files.": {
            "category": "Error",
            "code": 5056,
        },
        "Cannot find a tsconfig.json file at the specified directory: '{0}'": {
            "category": "Error",
            "code": 5057,
        },
        "The specified path does not exist: '{0}'": {"category": "Error", "code": 5058},
        "Invalide value for '--reactNamespace'. '{0}' is not a valid identifier.": {
            "category": "Error",
            "code": 5059,
        },
        "Concatenate and emit output to single file.": {
            "category": "Message",
            "code": 6001,
        },
        "Generates corresponding '.d.ts' file.": {"category": "Message", "code": 6002},
        "Specifies the location where debugger should locate map files instead of generated locations.": {
            "category": "Message",
            "code": 6003,
        },
        "Specifies the location where debugger should locate TypeScript files instead of source locations.": {
            "category": "Message",
            "code": 6004,
        },
        "Watch input files.": {"category": "Message", "code": 6005},
        "Redirect output structure to the directory.": {
            "category": "Message",
            "code": 6006,
        },
        "Do not erase const enum declarations in generated code.": {
            "category": "Message",
            "code": 6007,
        },
        "Do not emit outputs if any errors were reported.": {
            "category": "Message",
            "code": 6008,
        },
        "Do not emit comments to output.": {"category": "Message", "code": 6009},
        "Do not emit outputs.": {"category": "Message", "code": 6010},
        "Allow default imports from modules with no default export. This does not affect code emit, just typechecking.": {
            "category": "Message",
            "code": 6011,
        },
        "Specify ECMAScript target version: 'ES3' (default), 'ES5', or 'ES2015' (experimental)": {
            "category": "Message",
            "code": 6015,
        },
        "Specify module code generation: 'commonjs', 'amd', 'system', 'umd' or 'es2015'": {
            "category": "Message",
            "code": 6016,
        },
        "Print this message.": {"category": "Message", "code": 6017},
        "Print the compiler's version.": {"category": "Message", "code": 6019},
        "Compile the project in the given directory.": {
            "category": "Message",
            "code": 6020,
        },
        "Syntax: {0}": {"category": "Message", "code": 6023},
        "options": {"category": "Message", "code": 6024},
        "file": {"category": "Message", "code": 6025},
        "Examples: {0}": {"category": "Message", "code": 6026},
        "Options:": {"category": "Message", "code": 6027},
        "Version {0}": {"category": "Message", "code": 6029},
        "Insert command line options and files from a file.": {
            "category": "Message",
            "code": 6030,
        },
        "File change detected. Starting incremental compilation...": {
            "category": "Message",
            "code": 6032,
        },
        "KIND": {"category": "Message", "code": 6034},
        "FILE": {"category": "Message", "code": 6035},
        "VERSION": {"category": "Message", "code": 6036},
        "LOCATION": {"category": "Message", "code": 6037},
        "DIRECTORY": {"category": "Message", "code": 6038},
        "Compilation complete. Watching for file changes.": {
            "category": "Message",
            "code": 6042,
        },
        "Generates corresponding '.map' file.": {"category": "Message", "code": 6043},
        "Compiler option '{0}' expects an argument.": {
            "category": "Error",
            "code": 6044,
        },
        "Unterminated quoted string in response file '{0}'.": {
            "category": "Error",
            "code": 6045,
        },
        "Argument for '--module' option must be 'commonjs', 'amd', 'system', 'umd', 'es2015', or 'none'.": {
            "category": "Error",
            "code": 6046,
        },
        "Argument for '--target' option must be 'ES3', 'ES5', or 'ES2015'.": {
            "category": "Error",
            "code": 6047,
        },
        "Locale must be of the form <language> or <language>-<territory>. For example '{0}' or '{1}'.": {
            "category": "Error",
            "code": 6048,
        },
        "Unsupported locale '{0}'.": {"category": "Error", "code": 6049},
        "Unable to open file '{0}'.": {"category": "Error", "code": 6050},
        "Corrupted locale file {0}.": {"category": "Error", "code": 6051},
        "Raise error on expressions and declarations with an implied 'any' type.": {
            "category": "Message",
            "code": 6052,
        },
        "File '{0}' not found.": {"category": "Error", "code": 6053},
        "File '{0}' has unsupported extension. The only supported extensions are {1}.": {
            "category": "Error",
            "code": 6054,
        },
        "Suppress noImplicitAny errors for indexing objects lacking index signatures.": {
            "category": "Message",
            "code": 6055,
        },
        "Do not emit declarations for code that has an '@internal' annotation.": {
            "category": "Message",
            "code": 6056,
        },
        "Specifies the root directory of input files. Use to control the output directory structure with --outDir.": {
            "category": "Message",
            "code": 6058,
        },
        "File '{0}' is not under 'rootDir' '{1}'. 'rootDir' is expected to contain all source files.": {
            "category": "Error",
            "code": 6059,
        },
        "Specifies the end of line sequence to be used when emitting files: 'CRLF' (dos) or 'LF' (unix).": {
            "category": "Message",
            "code": 6060,
        },
        "NEWLINE": {"category": "Message", "code": 6061},
        "Argument for '--newLine' option must be 'CRLF' or 'LF'.": {
            "category": "Error",
            "code": 6062,
        },
        "Argument for '--moduleResolution' option must be 'node' or 'classic'.": {
            "category": "Error",
            "code": 6063,
        },
        "Enables experimental support for ES7 decorators.": {
            "category": "Message",
            "code": 6065,
        },
        "Enables experimental support for emitting type metadata for decorators.": {
            "category": "Message",
            "code": 6066,
        },
        "Enables experimental support for ES7 async functions.": {
            "category": "Message",
            "code": 6068,
        },
        "Specifies module resolution strategy: 'node' (Node.js) or 'classic' (TypeScript pre-1.6).": {
            "category": "Message",
            "code": 6069,
        },
        "Initializes a TypeScript project and creates a tsconfig.json file.": {
            "category": "Message",
            "code": 6070,
        },
        "Successfully created a tsconfig.json file.": {
            "category": "Message",
            "code": 6071,
        },
        "Suppress excess property checks for object literals.": {
            "category": "Message",
            "code": 6072,
        },
        "Stylize errors and messages using color and context. (experimental)": {
            "category": "Message",
            "code": 6073,
        },
        "Do not report errors on unused labels.": {"category": "Message", "code": 6074},
        "Report error when not all code paths in function return a value.": {
            "category": "Message",
            "code": 6075,
        },
        "Report errors for fallthrough cases in switch statement.": {
            "category": "Message",
            "code": 6076,
        },
        "Do not report errors on unreachable code.": {
            "category": "Message",
            "code": 6077,
        },
        "Disallow inconsistently-cased references to the same file.": {
            "category": "Message",
            "code": 6078,
        },
        "Specify JSX code generation: 'preserve' or 'react'": {
            "category": "Message",
            "code": 6080,
        },
        "Argument for '--jsx' must be 'preserve' or 'react'.": {
            "category": "Message",
            "code": 6081,
        },
        "Only 'amd' and 'system' modules are supported alongside --{0}.": {
            "category": "Error",
            "code": 6082,
        },
        "Allow javascript files to be compiled.": {"category": "Message", "code": 6083},
        "Specifies the object invoked for createElement and __spread when targeting 'react' JSX emit": {
            "category": "Message",
            "code": 6084,
        },
        "Do not emit 'use strict' directives in module output.": {
            "category": "Message",
            "code": 6112,
        },
        "Variable '{0}' implicitly has an '{1}' type.": {
            "category": "Error",
            "code": 7005,
        },
        "Parameter '{0}' implicitly has an '{1}' type.": {
            "category": "Error",
            "code": 7006,
        },
        "Member '{0}' implicitly has an '{1}' type.": {
            "category": "Error",
            "code": 7008,
        },
        "'new' expression, whose target lacks a construct signature, implicitly has an 'any' type.": {
            "category": "Error",
            "code": 7009,
        },
        "'{0}', which lacks return-type annotation, implicitly has an '{1}' return type.": {
            "category": "Error",
            "code": 7010,
        },
        "Function expression, which lacks return-type annotation, implicitly has an '{0}' return type.": {
            "category": "Error",
            "code": 7011,
        },
        "Construct signature, which lacks return-type annotation, implicitly has an 'any' return type.": {
            "category": "Error",
            "code": 7013,
        },
        "Element implicitly has an 'any' type because index expression is not of type 'number'.": {
            "category": "Error",
            "code": 7015,
        },
        "Property '{0}' implicitly has type 'any', because its 'set' accessor lacks a type annotation.": {
            "category": "Error",
            "code": 7016,
        },
        "Index signature of object type implicitly has an 'any' type.": {
            "category": "Error",
            "code": 7017,
        },
        "Object literal's property '{0}' implicitly has an '{1}' type.": {
            "category": "Error",
            "code": 7018,
        },
        "Rest parameter '{0}' implicitly has an 'any[]' type.": {
            "category": "Error",
            "code": 7019,
        },
        "Call signature, which lacks return-type annotation, implicitly has an 'any' return type.": {
            "category": "Error",
            "code": 7020,
        },
        "'{0}' implicitly has type 'any' because it does not have a type annotation and is referenced directly or indirectly in its own initializer.": {
            "category": "Error",
            "code": 7022,
        },
        "'{0}' implicitly has return type 'any' because it does not have a return type annotation and is referenced directly or indirectly in one of its return expressions.": {
            "category": "Error",
            "code": 7023,
        },
        "Function implicitly has return type 'any' because it does not have a return type annotation and is referenced directly or indirectly in one of its return expressions.": {
            "category": "Error",
            "code": 7024,
        },
        "Generator implicitly has type '{0}' because it does not yield any values. Consider supplying a return type.": {
            "category": "Error",
            "code": 7025,
        },
        "JSX element implicitly has type 'any' because no interface 'JSX.{0}' exists": {
            "category": "Error",
            "code": 7026,
        },
        "Unreachable code detected.": {"category": "Error", "code": 7027},
        "Unused label.": {"category": "Error", "code": 7028},
        "Fallthrough case in switch.": {"category": "Error", "code": 7029},
        "Not all code paths return a value.": {"category": "Error", "code": 7030},
        "You cannot rename this element.": {"category": "Error", "code": 8000},
        "You cannot rename elements that are defined in the standard TypeScript library.": {
            "category": "Error",
            "code": 8001,
        },
        "'import ... =' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8002,
        },
        "'export=' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8003,
        },
        "'type parameter declarations' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8004,
        },
        "'implements clauses' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8005,
        },
        "'interface declarations' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8006,
        },
        "'module declarations' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8007,
        },
        "'type aliases' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8008,
        },
        "'{0}' can only be used in a .ts file.": {"category": "Error", "code": 8009},
        "'types' can only be used in a .ts file.": {"category": "Error", "code": 8010},
        "'type arguments' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8011,
        },
        "'parameter modifiers' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8012,
        },
        "'property declarations' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8014,
        },
        "'enum declarations' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8015,
        },
        "'type assertion expressions' can only be used in a .ts file.": {
            "category": "Error",
            "code": 8016,
        },
        "Only identifiers/qualified-names with optional type arguments are currently supported in a class 'extends' clauses.": {
            "category": "Error",
            "code": 9002,
        },
        "'class' expressions are not currently supported.": {
            "category": "Error",
            "code": 9003,
        },
        "JSX attributes must only be assigned a non-empty 'expression'.": {
            "category": "Error",
            "code": 17000,
        },
        "JSX elements cannot have multiple attributes with the same name.": {
            "category": "Error",
            "code": 17001,
        },
        "Expected corresponding JSX closing tag for '{0}'.": {
            "category": "Error",
            "code": 17002,
        },
        "JSX attribute expected.": {"category": "Error", "code": 17003},
        "Cannot use JSX unless the '--jsx' flag is provided.": {
            "category": "Error",
            "code": 17004,
        },
        "A constructor cannot contain a 'super' call when its class extends 'null'": {
            "category": "Error",
            "code": 17005,
        },
        "An unary expression with the '{0}' operator is not allowed in the left-hand side of an exponentiation expression. Consider enclosing the expression in parentheses.": {
            "category": "Error",
            "code": 17006,
        },
        "A type assertion expression is not allowed in the left-hand side of an exponentiation expression. Consider enclosing the expression in parentheses.": {
            "category": "Error",
            "code": 17007,
        },
        "JSX element '{0}' has no corresponding closing tag.": {
            "category": "Error",
            "code": 17008,
        },
        "'super' must be called before accessing 'this' in the constructor of a derived class.": {
            "category": "Error",
            "code": 17009,
        },
    }
