# Generated from lenguajeTraductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .lenguajeTraductorParser import lenguajeTraductorParser
else:
    from lenguajeTraductorParser import lenguajeTraductorParser

# This class defines a complete listener for a parse tree produced by lenguajeTraductorParser.
class lenguajeTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by lenguajeTraductorParser#program.
    def enterProgram(self, ctx:lenguajeTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#program.
    def exitProgram(self, ctx:lenguajeTraductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#statement.
    def enterStatement(self, ctx:lenguajeTraductorParser.StatementContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#statement.
    def exitStatement(self, ctx:lenguajeTraductorParser.StatementContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#assignment.
    def enterAssignment(self, ctx:lenguajeTraductorParser.AssignmentContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#assignment.
    def exitAssignment(self, ctx:lenguajeTraductorParser.AssignmentContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#printStatement.
    def enterPrintStatement(self, ctx:lenguajeTraductorParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#printStatement.
    def exitPrintStatement(self, ctx:lenguajeTraductorParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#ifStatement.
    def enterIfStatement(self, ctx:lenguajeTraductorParser.IfStatementContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#ifStatement.
    def exitIfStatement(self, ctx:lenguajeTraductorParser.IfStatementContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#elseBlock.
    def enterElseBlock(self, ctx:lenguajeTraductorParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#elseBlock.
    def exitElseBlock(self, ctx:lenguajeTraductorParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:lenguajeTraductorParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:lenguajeTraductorParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#returnVariable.
    def enterReturnVariable(self, ctx:lenguajeTraductorParser.ReturnVariableContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#returnVariable.
    def exitReturnVariable(self, ctx:lenguajeTraductorParser.ReturnVariableContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#functionCall.
    def enterFunctionCall(self, ctx:lenguajeTraductorParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#functionCall.
    def exitFunctionCall(self, ctx:lenguajeTraductorParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#inputStatement.
    def enterInputStatement(self, ctx:lenguajeTraductorParser.InputStatementContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#inputStatement.
    def exitInputStatement(self, ctx:lenguajeTraductorParser.InputStatementContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#repeatStatement.
    def enterRepeatStatement(self, ctx:lenguajeTraductorParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#repeatStatement.
    def exitRepeatStatement(self, ctx:lenguajeTraductorParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#whileStatement.
    def enterWhileStatement(self, ctx:lenguajeTraductorParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#whileStatement.
    def exitWhileStatement(self, ctx:lenguajeTraductorParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#block.
    def enterBlock(self, ctx:lenguajeTraductorParser.BlockContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#block.
    def exitBlock(self, ctx:lenguajeTraductorParser.BlockContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#condition.
    def enterCondition(self, ctx:lenguajeTraductorParser.ConditionContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#condition.
    def exitCondition(self, ctx:lenguajeTraductorParser.ConditionContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#conditionBoolean.
    def enterConditionBoolean(self, ctx:lenguajeTraductorParser.ConditionBooleanContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#conditionBoolean.
    def exitConditionBoolean(self, ctx:lenguajeTraductorParser.ConditionBooleanContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#expression.
    def enterExpression(self, ctx:lenguajeTraductorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#expression.
    def exitExpression(self, ctx:lenguajeTraductorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#term.
    def enterTerm(self, ctx:lenguajeTraductorParser.TermContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#term.
    def exitTerm(self, ctx:lenguajeTraductorParser.TermContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#factor.
    def enterFactor(self, ctx:lenguajeTraductorParser.FactorContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#factor.
    def exitFactor(self, ctx:lenguajeTraductorParser.FactorContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#parameters.
    def enterParameters(self, ctx:lenguajeTraductorParser.ParametersContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#parameters.
    def exitParameters(self, ctx:lenguajeTraductorParser.ParametersContext):
        pass


    # Enter a parse tree produced by lenguajeTraductorParser#arguments.
    def enterArguments(self, ctx:lenguajeTraductorParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by lenguajeTraductorParser#arguments.
    def exitArguments(self, ctx:lenguajeTraductorParser.ArgumentsContext):
        pass



del lenguajeTraductorParser