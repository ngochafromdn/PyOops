from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser
from SymbolTableVisitor import SymbolTableVisitor
from StatementAnalyzer import StatementAnalyzer
from ExpressionAnalyzer import ExpressionAnalyzer

class SemanticAnalyzer(syntaxVisitor):
    def __init__(self):
        self.symbol_table = SymbolTableVisitor()
        self.statement_check = StatementAnalyzer(self.symbol_table)
        self.expression_check = ExpressionAnalyzer(self.symbol_table)
    
    def visitProgram(self, ctx: syntaxParser.ProgramContext):
        pass
    
    # Checking statements
    def visitVarDeclStmt(self, ctx: syntaxParser.VarDeclStmtContext):
        return self.statement_check.visitVarDeclStmt(ctx)
    
    def visitAssignStmt(self, ctx: syntaxParser.AssignStmtContext):
        return self.statement_check.visitAssignStmt(ctx)
    
    def visitType_defStatement(self, ctx: syntaxParser.Type_defStatementContext):
        return self.statement_check.visitType_defStatement(ctx)
    
    def visitFuncStmt(self, ctx: syntaxParser.FuncStmtContext):
        return self.statement_check.visitFuncStmt(ctx)
    
    def visitBlockStmt(self, ctx: syntaxParser.BlockStmtContext):
        return self.statement_check.visitBlockStmt(ctx)
    
    def visitReturnStmt(self, ctx: syntaxParser.ReturnStmtContext):
        return self.statement_check.visitReturnStmt(ctx)
    
    def visitIf_stmt(self, ctx: syntaxParser.If_stmtContext):
        return self.statement_check.visitIf_stmt(ctx)
    
    def visitWhile_stmt(self, ctx: syntaxParser.While_stmtContext):
        return self.statement_check.visitWhile_stmt(ctx)
    
    def visitTry_Stmt(self, ctx: syntaxParser.TryStmtContext):
        return self.statement_check.visitTry_Stmt(ctx)
    
    def visitPrint_stmt(self, ctx: syntaxParser.Print_stmtContext):
        return self.statement_check.visitPrint_stmt(ctx)
    
    # Checking expressions
    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        return self.expression_check.visitNumberExpr(ctx)
    
    def visitStringExpr(self, ctx: syntaxParser.StringExprContext):
        return self.expression_check.visitStringExpr(ctx)
    
    def visitIdExpr(self, ctx: syntaxParser.IdExprContext):
        return self.expression_check.visitIdExpr(ctx)
    
    def visitMulDivExpr(self, ctx: syntaxParser.MulDivExprContext):
        return self.expression_check.visitMulDivExpr(ctx)
    
    def visitAddSubExpr(self, ctx: syntaxParser.AddSubExprContext):
        return self.expression_check.visitAddSubExpr(ctx)
    
    def visitLogicExpr(self, ctx: syntaxParser.LogicExprContext):
        return self.expression_check.visitLogicExpr(ctx)
    
    def visitCompExpr(self, ctx: syntaxParser.CompExprContext):
        return self.expression_check.visitCompExpr(ctx)
    
    def visitNotExpr(self, ctx: syntaxParser.NotExprContext):
        return self.expression_check.visitNotExpr(ctx)
    
    def visitParenExpr(self, ctx: syntaxParser.ParenExprContext):
        return self.expression_check.visitParenExpr(ctx)
    
    def visitTrueExpr(self, ctx: syntaxParser.TrueExprContext):
        return self.expression_check.visitTrueExpr(ctx)
    
    def visitFalseExpr(self, ctx: syntaxParser.FalseExprContext):
        return self.expression_check.visitFalseExpr(ctx)
    
    def visitCharExpr(self, ctx: syntaxParser.CharExprContext):
        return self.expression_check.visitCharExpr(ctx)