# Generated from syntax.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .syntaxParser import syntaxParser
else:
    from syntaxParser import syntaxParser

# This class defines a complete listener for a parse tree produced by syntaxParser.
class syntaxListener(ParseTreeListener):

    # Enter a parse tree produced by syntaxParser#program.
    def enterProgram(self, ctx:syntaxParser.ProgramContext):
        pass

    # Exit a parse tree produced by syntaxParser#program.
    def exitProgram(self, ctx:syntaxParser.ProgramContext):
        pass


    # Enter a parse tree produced by syntaxParser#AssignStmt.
    def enterAssignStmt(self, ctx:syntaxParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#AssignStmt.
    def exitAssignStmt(self, ctx:syntaxParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#VarDeclStmt.
    def enterVarDeclStmt(self, ctx:syntaxParser.VarDeclStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#VarDeclStmt.
    def exitVarDeclStmt(self, ctx:syntaxParser.VarDeclStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#IfStmt.
    def enterIfStmt(self, ctx:syntaxParser.IfStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#IfStmt.
    def exitIfStmt(self, ctx:syntaxParser.IfStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#WhileStmt.
    def enterWhileStmt(self, ctx:syntaxParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#WhileStmt.
    def exitWhileStmt(self, ctx:syntaxParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#TryStmt.
    def enterTryStmt(self, ctx:syntaxParser.TryStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#TryStmt.
    def exitTryStmt(self, ctx:syntaxParser.TryStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#ReturnStmt.
    def enterReturnStmt(self, ctx:syntaxParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#ReturnStmt.
    def exitReturnStmt(self, ctx:syntaxParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#FuncStmt.
    def enterFuncStmt(self, ctx:syntaxParser.FuncStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#FuncStmt.
    def exitFuncStmt(self, ctx:syntaxParser.FuncStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#BlockStmt.
    def enterBlockStmt(self, ctx:syntaxParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#BlockStmt.
    def exitBlockStmt(self, ctx:syntaxParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#NewTypeDef.
    def enterNewTypeDef(self, ctx:syntaxParser.NewTypeDefContext):
        pass

    # Exit a parse tree produced by syntaxParser#NewTypeDef.
    def exitNewTypeDef(self, ctx:syntaxParser.NewTypeDefContext):
        pass


    # Enter a parse tree produced by syntaxParser#PrintStmt.
    def enterPrintStmt(self, ctx:syntaxParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#PrintStmt.
    def exitPrintStmt(self, ctx:syntaxParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#Continue.
    def enterContinue(self, ctx:syntaxParser.ContinueContext):
        pass

    # Exit a parse tree produced by syntaxParser#Continue.
    def exitContinue(self, ctx:syntaxParser.ContinueContext):
        pass


    # Enter a parse tree produced by syntaxParser#Break.
    def enterBreak(self, ctx:syntaxParser.BreakContext):
        pass

    # Exit a parse tree produced by syntaxParser#Break.
    def exitBreak(self, ctx:syntaxParser.BreakContext):
        pass


    # Enter a parse tree produced by syntaxParser#FuncCallStmt.
    def enterFuncCallStmt(self, ctx:syntaxParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#FuncCallStmt.
    def exitFuncCallStmt(self, ctx:syntaxParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#TypeDefDeclStmt.
    def enterTypeDefDeclStmt(self, ctx:syntaxParser.TypeDefDeclStmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#TypeDefDeclStmt.
    def exitTypeDefDeclStmt(self, ctx:syntaxParser.TypeDefDeclStmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#block.
    def enterBlock(self, ctx:syntaxParser.BlockContext):
        pass

    # Exit a parse tree produced by syntaxParser#block.
    def exitBlock(self, ctx:syntaxParser.BlockContext):
        pass


    # Enter a parse tree produced by syntaxParser#variable_declaration.
    def enterVariable_declaration(self, ctx:syntaxParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by syntaxParser#variable_declaration.
    def exitVariable_declaration(self, ctx:syntaxParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by syntaxParser#assignment.
    def enterAssignment(self, ctx:syntaxParser.AssignmentContext):
        pass

    # Exit a parse tree produced by syntaxParser#assignment.
    def exitAssignment(self, ctx:syntaxParser.AssignmentContext):
        pass


    # Enter a parse tree produced by syntaxParser#expression.
    def enterExpression(self, ctx:syntaxParser.ExpressionContext):
        pass

    # Exit a parse tree produced by syntaxParser#expression.
    def exitExpression(self, ctx:syntaxParser.ExpressionContext):
        pass


    # Enter a parse tree produced by syntaxParser#LogicExpr.
    def enterLogicExpr(self, ctx:syntaxParser.LogicExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#LogicExpr.
    def exitLogicExpr(self, ctx:syntaxParser.LogicExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#CompExpr.
    def enterCompExpr(self, ctx:syntaxParser.CompExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#CompExpr.
    def exitCompExpr(self, ctx:syntaxParser.CompExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:syntaxParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:syntaxParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:syntaxParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:syntaxParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:syntaxParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:syntaxParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#NotExpr.
    def enterNotExpr(self, ctx:syntaxParser.NotExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#NotExpr.
    def exitNotExpr(self, ctx:syntaxParser.NotExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:syntaxParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:syntaxParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#ParenExpr.
    def enterParenExpr(self, ctx:syntaxParser.ParenExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#ParenExpr.
    def exitParenExpr(self, ctx:syntaxParser.ParenExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#TrueExpr.
    def enterTrueExpr(self, ctx:syntaxParser.TrueExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#TrueExpr.
    def exitTrueExpr(self, ctx:syntaxParser.TrueExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#FalseExpr.
    def enterFalseExpr(self, ctx:syntaxParser.FalseExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#FalseExpr.
    def exitFalseExpr(self, ctx:syntaxParser.FalseExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#ArrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:syntaxParser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#ArrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:syntaxParser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:syntaxParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:syntaxParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#IdExpr.
    def enterIdExpr(self, ctx:syntaxParser.IdExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#IdExpr.
    def exitIdExpr(self, ctx:syntaxParser.IdExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#NumberExpr.
    def enterNumberExpr(self, ctx:syntaxParser.NumberExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#NumberExpr.
    def exitNumberExpr(self, ctx:syntaxParser.NumberExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#StringExpr.
    def enterStringExpr(self, ctx:syntaxParser.StringExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#StringExpr.
    def exitStringExpr(self, ctx:syntaxParser.StringExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#CharExpr.
    def enterCharExpr(self, ctx:syntaxParser.CharExprContext):
        pass

    # Exit a parse tree produced by syntaxParser#CharExpr.
    def exitCharExpr(self, ctx:syntaxParser.CharExprContext):
        pass


    # Enter a parse tree produced by syntaxParser#IntArray.
    def enterIntArray(self, ctx:syntaxParser.IntArrayContext):
        pass

    # Exit a parse tree produced by syntaxParser#IntArray.
    def exitIntArray(self, ctx:syntaxParser.IntArrayContext):
        pass


    # Enter a parse tree produced by syntaxParser#CharArray.
    def enterCharArray(self, ctx:syntaxParser.CharArrayContext):
        pass

    # Exit a parse tree produced by syntaxParser#CharArray.
    def exitCharArray(self, ctx:syntaxParser.CharArrayContext):
        pass


    # Enter a parse tree produced by syntaxParser#StringArray.
    def enterStringArray(self, ctx:syntaxParser.StringArrayContext):
        pass

    # Exit a parse tree produced by syntaxParser#StringArray.
    def exitStringArray(self, ctx:syntaxParser.StringArrayContext):
        pass


    # Enter a parse tree produced by syntaxParser#TypedefField.
    def enterTypedefField(self, ctx:syntaxParser.TypedefFieldContext):
        pass

    # Exit a parse tree produced by syntaxParser#TypedefField.
    def exitTypedefField(self, ctx:syntaxParser.TypedefFieldContext):
        pass


    # Enter a parse tree produced by syntaxParser#function_call.
    def enterFunction_call(self, ctx:syntaxParser.Function_callContext):
        pass

    # Exit a parse tree produced by syntaxParser#function_call.
    def exitFunction_call(self, ctx:syntaxParser.Function_callContext):
        pass


    # Enter a parse tree produced by syntaxParser#arg_list.
    def enterArg_list(self, ctx:syntaxParser.Arg_listContext):
        pass

    # Exit a parse tree produced by syntaxParser#arg_list.
    def exitArg_list(self, ctx:syntaxParser.Arg_listContext):
        pass


    # Enter a parse tree produced by syntaxParser#if_stmt.
    def enterIf_stmt(self, ctx:syntaxParser.If_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#if_stmt.
    def exitIf_stmt(self, ctx:syntaxParser.If_stmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#while_stmt.
    def enterWhile_stmt(self, ctx:syntaxParser.While_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#while_stmt.
    def exitWhile_stmt(self, ctx:syntaxParser.While_stmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#print_stmt.
    def enterPrint_stmt(self, ctx:syntaxParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#print_stmt.
    def exitPrint_stmt(self, ctx:syntaxParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#return_stmt.
    def enterReturn_stmt(self, ctx:syntaxParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#return_stmt.
    def exitReturn_stmt(self, ctx:syntaxParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#try_stmt.
    def enterTry_stmt(self, ctx:syntaxParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#try_stmt.
    def exitTry_stmt(self, ctx:syntaxParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#type_defDeclaration.
    def enterType_defDeclaration(self, ctx:syntaxParser.Type_defDeclarationContext):
        pass

    # Exit a parse tree produced by syntaxParser#type_defDeclaration.
    def exitType_defDeclaration(self, ctx:syntaxParser.Type_defDeclarationContext):
        pass


    # Enter a parse tree produced by syntaxParser#type_defVar.
    def enterType_defVar(self, ctx:syntaxParser.Type_defVarContext):
        pass

    # Exit a parse tree produced by syntaxParser#type_defVar.
    def exitType_defVar(self, ctx:syntaxParser.Type_defVarContext):
        pass


    # Enter a parse tree produced by syntaxParser#type_defStatement.
    def enterType_defStatement(self, ctx:syntaxParser.Type_defStatementContext):
        pass

    # Exit a parse tree produced by syntaxParser#type_defStatement.
    def exitType_defStatement(self, ctx:syntaxParser.Type_defStatementContext):
        pass


    # Enter a parse tree produced by syntaxParser#type_def_list.
    def enterType_def_list(self, ctx:syntaxParser.Type_def_listContext):
        pass

    # Exit a parse tree produced by syntaxParser#type_def_list.
    def exitType_def_list(self, ctx:syntaxParser.Type_def_listContext):
        pass


    # Enter a parse tree produced by syntaxParser#param_list.
    def enterParam_list(self, ctx:syntaxParser.Param_listContext):
        pass

    # Exit a parse tree produced by syntaxParser#param_list.
    def exitParam_list(self, ctx:syntaxParser.Param_listContext):
        pass


    # Enter a parse tree produced by syntaxParser#int_Array.
    def enterInt_Array(self, ctx:syntaxParser.Int_ArrayContext):
        pass

    # Exit a parse tree produced by syntaxParser#int_Array.
    def exitInt_Array(self, ctx:syntaxParser.Int_ArrayContext):
        pass


    # Enter a parse tree produced by syntaxParser#char_Array.
    def enterChar_Array(self, ctx:syntaxParser.Char_ArrayContext):
        pass

    # Exit a parse tree produced by syntaxParser#char_Array.
    def exitChar_Array(self, ctx:syntaxParser.Char_ArrayContext):
        pass


    # Enter a parse tree produced by syntaxParser#strArray.
    def enterStrArray(self, ctx:syntaxParser.StrArrayContext):
        pass

    # Exit a parse tree produced by syntaxParser#strArray.
    def exitStrArray(self, ctx:syntaxParser.StrArrayContext):
        pass


    # Enter a parse tree produced by syntaxParser#continue_stmt.
    def enterContinue_stmt(self, ctx:syntaxParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#continue_stmt.
    def exitContinue_stmt(self, ctx:syntaxParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by syntaxParser#break_stmt.
    def enterBreak_stmt(self, ctx:syntaxParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by syntaxParser#break_stmt.
    def exitBreak_stmt(self, ctx:syntaxParser.Break_stmtContext):
        pass



del syntaxParser