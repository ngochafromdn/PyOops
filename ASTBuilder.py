from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser 

class ASTNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class PyoopsSyntaxVisitor(syntaxVisitor):
    def visitAssignStmt(self, ctx: syntaxParser.AssignStmtContext):
        var_name = ctx.ID().getText()  # Lấy tên biến
        expr = self.visit(ctx.expr())   # Thực hiện duyệt biểu thức phía bên phải dấu "="
        assign_node = ASTNode(f"Assign: {var_name}")
        assign_node.add_child(expr)
        return assign_node

    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        return ASTNode(int(ctx.NUMBER().getText()))  # Tạo node AST cho số

    def visitAddSubExpr(self, ctx: syntaxParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))  # Duyệt biểu thức bên trái
        right = self.visit(ctx.expr(1))  # Duyệt biểu thức bên phải
        op = ctx.op.text  # Lấy toán tử (cộng hoặc trừ)
        add_sub_node = ASTNode(f"AddSub: {op}")
        add_sub_node.add_child(left)
        add_sub_node.add_child(right)
        return add_sub_node
