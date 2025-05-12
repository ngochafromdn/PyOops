# Generated from syntax.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .syntaxParser import syntaxParser
else:
    from syntaxParser import syntaxParser

# This class defines a complete generic visitor for a parse tree produced by syntaxParser.

class syntaxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by syntaxParser#program.
    def visitProgram(self, ctx:syntaxParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#AssignStmt.
    def visitAssignStmt(self, ctx:syntaxParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#VarDeclStmt.
    def visitVarDeclStmt(self, ctx:syntaxParser.VarDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#IfStmt.
    def visitIfStmt(self, ctx:syntaxParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#WhileStmt.
    def visitWhileStmt(self, ctx:syntaxParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#TryStmt.
    def visitTryStmt(self, ctx:syntaxParser.TryStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#ReturnStmt.
    def visitReturnStmt(self, ctx:syntaxParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#FuncStmt.
    def visitFuncStmt(self, ctx:syntaxParser.FuncStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#BlockStmt.
    def visitBlockStmt(self, ctx:syntaxParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#NewTypeDef.
    def visitNewTypeDef(self, ctx:syntaxParser.NewTypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#PrintStmt.
    def visitPrintStmt(self, ctx:syntaxParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#Continue.
    def visitContinue(self, ctx:syntaxParser.ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#Break.
    def visitBreak(self, ctx:syntaxParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#FuncCallStmt.
    def visitFuncCallStmt(self, ctx:syntaxParser.FuncCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#TypeDefDeclStmt.
    def visitTypeDefDeclStmt(self, ctx:syntaxParser.TypeDefDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#block.
    def visitBlock(self, ctx:syntaxParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#variable_declaration.
    def visitVariable_declaration(self, ctx:syntaxParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#assignment.
    def visitAssignment(self, ctx:syntaxParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#expression.
    def visitExpression(self, ctx:syntaxParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#LogicExpr.
    def visitLogicExpr(self, ctx:syntaxParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#CompExpr.
    def visitCompExpr(self, ctx:syntaxParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:syntaxParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:syntaxParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:syntaxParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#NotExpr.
    def visitNotExpr(self, ctx:syntaxParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#PrimaryExpr.
    def visitPrimaryExpr(self, ctx:syntaxParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#ParenExpr.
    def visitParenExpr(self, ctx:syntaxParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#TrueExpr.
    def visitTrueExpr(self, ctx:syntaxParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#FalseExpr.
    def visitFalseExpr(self, ctx:syntaxParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#ArrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:syntaxParser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:syntaxParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#IdExpr.
    def visitIdExpr(self, ctx:syntaxParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#NumberExpr.
    def visitNumberExpr(self, ctx:syntaxParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#StringExpr.
    def visitStringExpr(self, ctx:syntaxParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#CharExpr.
    def visitCharExpr(self, ctx:syntaxParser.CharExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#IntArray.
    def visitIntArray(self, ctx:syntaxParser.IntArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#CharArray.
    def visitCharArray(self, ctx:syntaxParser.CharArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#StringArray.
    def visitStringArray(self, ctx:syntaxParser.StringArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#function_call.
    def visitFunction_call(self, ctx:syntaxParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#arg_list.
    def visitArg_list(self, ctx:syntaxParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#if_stmt.
    def visitIf_stmt(self, ctx:syntaxParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#while_stmt.
    def visitWhile_stmt(self, ctx:syntaxParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#print_stmt.
    def visitPrint_stmt(self, ctx:syntaxParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#return_stmt.
    def visitReturn_stmt(self, ctx:syntaxParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#try_stmt.
    def visitTry_stmt(self, ctx:syntaxParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#type_defDeclaration.
    def visitType_defDeclaration(self, ctx:syntaxParser.Type_defDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#type_defVar.
    def visitType_defVar(self, ctx:syntaxParser.Type_defVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#type_defStatement.
    def visitType_defStatement(self, ctx:syntaxParser.Type_defStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#type_def_list.
    def visitType_def_list(self, ctx:syntaxParser.Type_def_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#param_list.
    def visitParam_list(self, ctx:syntaxParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#int_Array.
    def visitInt_Array(self, ctx:syntaxParser.Int_ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#char_Array.
    def visitChar_Array(self, ctx:syntaxParser.Char_ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#strArray.
    def visitStrArray(self, ctx:syntaxParser.StrArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#continue_stmt.
    def visitContinue_stmt(self, ctx:syntaxParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by syntaxParser#break_stmt.
    def visitBreak_stmt(self, ctx:syntaxParser.Break_stmtContext):
        return self.visitChildren(ctx)



del syntaxParser