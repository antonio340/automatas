from traductorPythonaJavaListener import traductorPythonaJavaListener
from traductorPythonaJavaParser import traductorPythonaJavaParser

class traductorListener(traductorPythonaJavaListener):
    def __init__(self):
        self.java_code = []

    def enterFuncDef(self, ctx: traductorPythonaJavaParser.FuncDefContext):
        func_name = ctx.ID().getText()
        params = [p.getText() for p in ctx.params().ID()]
        param_str = ", ".join(f"int {param}" for param in params)
        self.java_code.append(f"public static int {func_name}({param_str}) " + "{")

    def exitFuncDef(self, ctx: traductorPythonaJavaParser.FuncDefContext):
        self.java_code.append("}")

    def enterAssignmentStat(self, ctx: traductorPythonaJavaParser.AssignmentStatContext):
        var_name = ctx.ID().getText()
        expr = ctx.expr().getText()
        self.java_code.append(f"    int {var_name} = {expr};")

    def enterReturnStat(self, ctx: traductorPythonaJavaParser.ReturnStatContext):
        expr = ctx.expr().getText()
        self.java_code.append(f"    return {expr};")

    def enterPrintStat(self, ctx: traductorPythonaJavaParser.PrintStatContext):
        expr = ctx.exprList().getText()
        self.java_code.append(f"System.out.println({expr});")

    def getJavaCode(self):
        return "\n".join(self.java_code)
