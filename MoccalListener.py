# Generated from Moccal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MoccalParser import MoccalParser
else:
    from MoccalParser import MoccalParser

# This class defines a complete listener for a parse tree produced by MoccalParser.
class MoccalListener(ParseTreeListener):

    # Enter a parse tree produced by MoccalParser#access_specifier.
    def enterAccess_specifier(self, ctx:MoccalParser.Access_specifierContext):
        pass

    # Exit a parse tree produced by MoccalParser#access_specifier.
    def exitAccess_specifier(self, ctx:MoccalParser.Access_specifierContext):
        pass


    # Enter a parse tree produced by MoccalParser#moccal.
    def enterMoccal(self, ctx:MoccalParser.MoccalContext):
        pass

    # Exit a parse tree produced by MoccalParser#moccal.
    def exitMoccal(self, ctx:MoccalParser.MoccalContext):
        pass


    # Enter a parse tree produced by MoccalParser#c.
    def enterC(self, ctx:MoccalParser.CContext):
        pass

    # Exit a parse tree produced by MoccalParser#c.
    def exitC(self, ctx:MoccalParser.CContext):
        pass


    # Enter a parse tree produced by MoccalParser#line.
    def enterLine(self, ctx:MoccalParser.LineContext):
        pass

    # Exit a parse tree produced by MoccalParser#line.
    def exitLine(self, ctx:MoccalParser.LineContext):
        pass


    # Enter a parse tree produced by MoccalParser#guarantee.
    def enterGuarantee(self, ctx:MoccalParser.GuaranteeContext):
        pass

    # Exit a parse tree produced by MoccalParser#guarantee.
    def exitGuarantee(self, ctx:MoccalParser.GuaranteeContext):
        pass


    # Enter a parse tree produced by MoccalParser#assumption.
    def enterAssumption(self, ctx:MoccalParser.AssumptionContext):
        pass

    # Exit a parse tree produced by MoccalParser#assumption.
    def exitAssumption(self, ctx:MoccalParser.AssumptionContext):
        pass


    # Enter a parse tree produced by MoccalParser#directive.
    def enterDirective(self, ctx:MoccalParser.DirectiveContext):
        pass

    # Exit a parse tree produced by MoccalParser#directive.
    def exitDirective(self, ctx:MoccalParser.DirectiveContext):
        pass


    # Enter a parse tree produced by MoccalParser#imp.
    def enterImp(self, ctx:MoccalParser.ImpContext):
        pass

    # Exit a parse tree produced by MoccalParser#imp.
    def exitImp(self, ctx:MoccalParser.ImpContext):
        pass


    # Enter a parse tree produced by MoccalParser#include.
    def enterInclude(self, ctx:MoccalParser.IncludeContext):
        pass

    # Exit a parse tree produced by MoccalParser#include.
    def exitInclude(self, ctx:MoccalParser.IncludeContext):
        pass


    # Enter a parse tree produced by MoccalParser#scope.
    def enterScope(self, ctx:MoccalParser.ScopeContext):
        pass

    # Exit a parse tree produced by MoccalParser#scope.
    def exitScope(self, ctx:MoccalParser.ScopeContext):
        pass


    # Enter a parse tree produced by MoccalParser#args.
    def enterArgs(self, ctx:MoccalParser.ArgsContext):
        pass

    # Exit a parse tree produced by MoccalParser#args.
    def exitArgs(self, ctx:MoccalParser.ArgsContext):
        pass


    # Enter a parse tree produced by MoccalParser#for.
    def enterFor(self, ctx:MoccalParser.ForContext):
        pass

    # Exit a parse tree produced by MoccalParser#for.
    def exitFor(self, ctx:MoccalParser.ForContext):
        pass


    # Enter a parse tree produced by MoccalParser#while.
    def enterWhile(self, ctx:MoccalParser.WhileContext):
        pass

    # Exit a parse tree produced by MoccalParser#while.
    def exitWhile(self, ctx:MoccalParser.WhileContext):
        pass


    # Enter a parse tree produced by MoccalParser#use.
    def enterUse(self, ctx:MoccalParser.UseContext):
        pass

    # Exit a parse tree produced by MoccalParser#use.
    def exitUse(self, ctx:MoccalParser.UseContext):
        pass


    # Enter a parse tree produced by MoccalParser#as.
    def enterAs(self, ctx:MoccalParser.AsContext):
        pass

    # Exit a parse tree produced by MoccalParser#as.
    def exitAs(self, ctx:MoccalParser.AsContext):
        pass


    # Enter a parse tree produced by MoccalParser#useas.
    def enterUseas(self, ctx:MoccalParser.UseasContext):
        pass

    # Exit a parse tree produced by MoccalParser#useas.
    def exitUseas(self, ctx:MoccalParser.UseasContext):
        pass


    # Enter a parse tree produced by MoccalParser#continue.
    def enterContinue(self, ctx:MoccalParser.ContinueContext):
        pass

    # Exit a parse tree produced by MoccalParser#continue.
    def exitContinue(self, ctx:MoccalParser.ContinueContext):
        pass


    # Enter a parse tree produced by MoccalParser#break.
    def enterBreak(self, ctx:MoccalParser.BreakContext):
        pass

    # Exit a parse tree produced by MoccalParser#break.
    def exitBreak(self, ctx:MoccalParser.BreakContext):
        pass


    # Enter a parse tree produced by MoccalParser#return.
    def enterReturn(self, ctx:MoccalParser.ReturnContext):
        pass

    # Exit a parse tree produced by MoccalParser#return.
    def exitReturn(self, ctx:MoccalParser.ReturnContext):
        pass


    # Enter a parse tree produced by MoccalParser#ctrl_block.
    def enterCtrl_block(self, ctx:MoccalParser.Ctrl_blockContext):
        pass

    # Exit a parse tree produced by MoccalParser#ctrl_block.
    def exitCtrl_block(self, ctx:MoccalParser.Ctrl_blockContext):
        pass


    # Enter a parse tree produced by MoccalParser#ifblock.
    def enterIfblock(self, ctx:MoccalParser.IfblockContext):
        pass

    # Exit a parse tree produced by MoccalParser#ifblock.
    def exitIfblock(self, ctx:MoccalParser.IfblockContext):
        pass


    # Enter a parse tree produced by MoccalParser#elifblock.
    def enterElifblock(self, ctx:MoccalParser.ElifblockContext):
        pass

    # Exit a parse tree produced by MoccalParser#elifblock.
    def exitElifblock(self, ctx:MoccalParser.ElifblockContext):
        pass


    # Enter a parse tree produced by MoccalParser#elseblock.
    def enterElseblock(self, ctx:MoccalParser.ElseblockContext):
        pass

    # Exit a parse tree produced by MoccalParser#elseblock.
    def exitElseblock(self, ctx:MoccalParser.ElseblockContext):
        pass


    # Enter a parse tree produced by MoccalParser#class.
    def enterClass(self, ctx:MoccalParser.ClassContext):
        pass

    # Exit a parse tree produced by MoccalParser#class.
    def exitClass(self, ctx:MoccalParser.ClassContext):
        pass


    # Enter a parse tree produced by MoccalParser#function.
    def enterFunction(self, ctx:MoccalParser.FunctionContext):
        pass

    # Exit a parse tree produced by MoccalParser#function.
    def exitFunction(self, ctx:MoccalParser.FunctionContext):
        pass


    # Enter a parse tree produced by MoccalParser#declaration.
    def enterDeclaration(self, ctx:MoccalParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MoccalParser#declaration.
    def exitDeclaration(self, ctx:MoccalParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MoccalParser#expr.
    def enterExpr(self, ctx:MoccalParser.ExprContext):
        pass

    # Exit a parse tree produced by MoccalParser#expr.
    def exitExpr(self, ctx:MoccalParser.ExprContext):
        pass


    # Enter a parse tree produced by MoccalParser#array_literal.
    def enterArray_literal(self, ctx:MoccalParser.Array_literalContext):
        pass

    # Exit a parse tree produced by MoccalParser#array_literal.
    def exitArray_literal(self, ctx:MoccalParser.Array_literalContext):
        pass



del MoccalParser