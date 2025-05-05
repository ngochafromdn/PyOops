from antlr4 import *
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class SymbolTableVisitor(syntaxVisitor):
    def __init__(self):
        self.global_scope = {}
        self.scopes = [self.global_scope]
        self.all_scopes = [{'name': 'Global', 'symbols': self.global_scope}]
        self.current_function = None

    # Lấy phạm vi hiện tại từ đỉnh ngăn xếp
    @property
    def current_scope(self):
        return self.scopes[-1]

    # Thêm phạm vi mới bằng cách đẩy một từ điển trống vào ngăn xếp
    def push_scope(self, scope_name="Anonymous"):
        new_scope = {}
        self.scopes.append(new_scope)
        self.all_scopes.append({'name': scope_name, 'symbols': new_scope})

    # Thoát khỏi phạm vi hiện tại
    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
            # Không xóa khỏi all_scopes để giữ lại cho việc hiển thị

    # Đặt lại về phạm vi toàn cục
    def reset_to_global(self):
        while len(self.scopes) > 1:
            self.pop_scope()

    # Định nghĩa một ký hiệu mới trong phạm vi hiện tại
    def define(self, name, value, line=None, column=None):
        if name in self.current_scope:
            raise ValueError(f"[Error] Line {line}, Column {column}: Redeclaration of '{name}' in current scope.")
        self.current_scope[name] = value

    # Tìm ký hiệu từ phạm vi trên xuống phạm vi toàn cục
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    # Cập nhật giá trị của một ký hiệu
    def update(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                if isinstance(scope[name], dict):
                    if isinstance(value, dict):
                        scope[name].update(value)
                    else:
                        scope[name]['value'] = value
                else:
                    scope[name] = value
                return True
        return False

    # In tất cả các ký hiệu đã định nghĩa
    def printSymbols(self):
        print("=== Symbol Table ===")
        for scope in self.all_scopes:
            print(f"{scope['name']} Scope:")
            if not scope['symbols']:
                print("  (empty scope)")
            else:
                for name, value in scope['symbols'].items():
                    print(f"  {name}: {value}")

    # Update your SymbolTableVisitor class to handle function definitions
    # Định nghĩa hàm đầy đủ với metadata cho runtime
    def define_function(self, name, return_type, param_list, body_ctx):
        if name in self.global_scope:
            raise ValueError(f"Function '{name}' already defined.")

        self.global_scope[name] = {
            "type": "function",
            "return_type": return_type,
            "params": [{"type": t, "name": n} for t, n in param_list],
            "body": body_ctx
        }

