# Generated from Oper.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OperParser import OperParser
else:
    from OperParser import OperParser

# This class defines a complete generic visitor for a parse tree produced by OperParser.

class OperVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OperParser#root.
    def visitRoot(self, ctx:OperParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperParser#expr.
    def visitExpr(self, ctx:OperParser.ExprContext):
        return self.visitChildren(ctx)



del OperParser