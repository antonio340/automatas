from lenguajeTraductorParser import lenguajeTraductorParser
from lenguajeTraductorListener import lenguajeTraductorListener

class listener(lenguajeTraductorListener):
    def __init__(self):
        self.python_code = []
        self.indent_level = 0

    def add_line(self, line):
        self.python_code.append("    " * self.indent_level + line + "\n")

    def enterProgram(self, ctx: lenguajeTraductorParser.ProgramContext):
        self.add_line("# Código generado por el traductor")

    def enterAssignment(self, ctx: lenguajeTraductorParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = ctx.expression().getText()
        if value == 'verdadero':
            value = 'true'
        elif value == 'falso':
            value = 'false'
        self.add_line(f"{var_name} = {value}")

    def enterPrintStatement(self, ctx: lenguajeTraductorParser.PrintStatementContext):
        parts = []
        for child in ctx.children:
            if isinstance(child, lenguajeTraductorParser.ExpressionContext):
                parts.append(child.getText())
            elif child.getText().startswith('"'):
                parts.append(child.getText())
        concatenated_string = ' + '.join(parts)
        self.add_line(f"print({concatenated_string})")

    def enterConditionBoolean(self, ctx: lenguajeTraductorParser.ConditionBooleanContext):
        condition_text = ctx.getText()
        if ' es verdadero' in condition_text:
            condition_text = condition_text.replace(' es verdadero', ' == True')
        elif ' es falso' in condition_text:
            condition_text = condition_text.replace(' es falso', ' == False')
        return condition_text

    def enterIfStatement(self, ctx: lenguajeTraductorParser.IfStatementContext):
        condition = ctx.condition().getText()
        condition = self.enterConditionBoolean(ctx.condition())
        self.add_line(f"if {condition}:")
        self.indent_level += 1

    def exitIfStatement(self, ctx: lenguajeTraductorParser.IfStatementContext):
        self.indent_level -= 1

    def enterElseBlock(self, ctx: lenguajeTraductorParser.BlockContext):
        self.add_line("else:")
        self.indent_level += 1

    def exitElseBlock(self, ctx: lenguajeTraductorParser.BlockContext):
        self.indent_level -= 1

    def enterFunctionDeclaration(self, ctx: lenguajeTraductorParser.FunctionDeclarationContext):
        func_name = ctx.ID().getText()
        params = ctx.parameters().getText() if ctx.parameters() else ""
        self.add_line(f"def {func_name}({params}):")
        self.indent_level += 1

    def exitFunctionDeclaration(self, ctx: lenguajeTraductorParser.FunctionDeclarationContext):
        self.indent_level -= 1

    def enterReturnVariable(self, ctx: lenguajeTraductorParser.ReturnVariableContext):
        var_name = ctx.ID().getText()
        self.add_line(f"return {var_name}")

    def enterFunctionCall(self, ctx: lenguajeTraductorParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = ctx.arguments().getText() if ctx.arguments() else ""
        self.add_line(f"{func_name}({args})")

    def enterInputStatement(self, ctx: lenguajeTraductorParser.InputStatementContext):
        var_name = ctx.ID().getText()
        self.add_line(f"{var_name} = input()")

    def enterRepeatStatement(self, ctx: lenguajeTraductorParser.RepeatStatementContext):
        var_name = ctx.ID(0).getText()
        limit = ctx.ID(1).getText()
        self.add_line(f"for {var_name} in range({limit}):")
        self.indent_level += 1

    def exitRepeatStatement(self, ctx: lenguajeTraductorParser.RepeatStatementContext):
        self.indent_level -= 1

    def enterWhileStatement(self, ctx: lenguajeTraductorParser.WhileStatementContext):
        condition = ctx.condition().getText()
        condition = self.enterConditionBoolean(ctx.condition())
        self.add_line(f"while {condition}:")
        self.indent_level += 1

    def exitWhileStatement(self, ctx: lenguajeTraductorParser.WhileStatementContext):
        self.indent_level -= 1

    def getPythonCode(self):
        return ''.join(self.python_code)
