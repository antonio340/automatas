# Generated from lenguajeTraductor.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,56,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,3,
        3,70,8,3,5,3,72,8,3,10,3,12,3,75,9,3,1,4,1,4,1,4,1,4,1,4,3,4,82,
        8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,91,8,6,1,6,1,6,1,6,1,7,1,7,1,
        7,3,7,99,8,7,1,8,1,8,1,8,1,8,3,8,105,8,8,1,8,1,8,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,5,12,124,
        8,12,10,12,12,12,127,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,139,8,13,1,14,1,14,1,15,1,15,1,15,5,15,146,8,15,10,
        15,12,15,149,9,15,1,15,3,15,152,8,15,1,16,1,16,1,16,5,16,157,8,16,
        10,16,12,16,160,9,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,168,8,17,
        1,18,1,18,1,18,5,18,173,8,18,10,18,12,18,176,9,18,1,19,1,19,1,19,
        5,19,181,8,19,10,19,12,19,184,9,19,1,19,0,0,20,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,0,3,1,0,21,22,2,0,3,3,23,23,
        1,0,24,25,193,0,41,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,61,1,0,0,
        0,8,76,1,0,0,0,10,83,1,0,0,0,12,86,1,0,0,0,14,98,1,0,0,0,16,100,
        1,0,0,0,18,108,1,0,0,0,20,111,1,0,0,0,22,117,1,0,0,0,24,121,1,0,
        0,0,26,130,1,0,0,0,28,140,1,0,0,0,30,151,1,0,0,0,32,153,1,0,0,0,
        34,167,1,0,0,0,36,169,1,0,0,0,38,177,1,0,0,0,40,42,3,2,1,0,41,40,
        1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,1,1,0,0,0,45,
        56,3,4,2,0,46,56,3,6,3,0,47,56,3,8,4,0,48,56,3,10,5,0,49,56,3,12,
        6,0,50,56,3,16,8,0,51,56,3,18,9,0,52,56,3,20,10,0,53,56,3,22,11,
        0,54,56,3,14,7,0,55,45,1,0,0,0,55,46,1,0,0,0,55,47,1,0,0,0,55,48,
        1,0,0,0,55,49,1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,
        55,53,1,0,0,0,55,54,1,0,0,0,56,3,1,0,0,0,57,58,5,27,0,0,58,59,5,
        1,0,0,59,60,3,30,15,0,60,5,1,0,0,0,61,64,5,2,0,0,62,65,5,29,0,0,
        63,65,3,30,15,0,64,62,1,0,0,0,64,63,1,0,0,0,65,73,1,0,0,0,66,69,
        5,3,0,0,67,70,5,29,0,0,68,70,3,30,15,0,69,67,1,0,0,0,69,68,1,0,0,
        0,70,72,1,0,0,0,71,66,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,7,1,0,0,0,75,73,1,0,0,0,76,77,5,4,0,0,77,78,3,26,13,0,
        78,79,5,5,0,0,79,81,3,24,12,0,80,82,3,10,5,0,81,80,1,0,0,0,81,82,
        1,0,0,0,82,9,1,0,0,0,83,84,5,6,0,0,84,85,3,24,12,0,85,11,1,0,0,0,
        86,87,5,7,0,0,87,88,5,27,0,0,88,90,5,8,0,0,89,91,3,36,18,0,90,89,
        1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,9,0,0,93,94,3,24,12,
        0,94,13,1,0,0,0,95,96,5,10,0,0,96,99,5,27,0,0,97,99,3,30,15,0,98,
        95,1,0,0,0,98,97,1,0,0,0,99,15,1,0,0,0,100,101,5,11,0,0,101,102,
        5,27,0,0,102,104,5,8,0,0,103,105,3,38,19,0,104,103,1,0,0,0,104,105,
        1,0,0,0,105,106,1,0,0,0,106,107,5,9,0,0,107,17,1,0,0,0,108,109,5,
        12,0,0,109,110,5,27,0,0,110,19,1,0,0,0,111,112,5,13,0,0,112,113,
        5,27,0,0,113,114,5,14,0,0,114,115,5,27,0,0,115,116,3,24,12,0,116,
        21,1,0,0,0,117,118,5,15,0,0,118,119,3,26,13,0,119,120,3,24,12,0,
        120,23,1,0,0,0,121,125,5,16,0,0,122,124,3,2,1,0,123,122,1,0,0,0,
        124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,
        127,125,1,0,0,0,128,129,5,17,0,0,129,25,1,0,0,0,130,138,3,30,15,
        0,131,132,5,18,0,0,132,139,3,30,15,0,133,134,5,19,0,0,134,139,3,
        30,15,0,135,136,5,20,0,0,136,139,3,30,15,0,137,139,3,28,14,0,138,
        131,1,0,0,0,138,133,1,0,0,0,138,135,1,0,0,0,138,137,1,0,0,0,139,
        27,1,0,0,0,140,141,7,0,0,0,141,29,1,0,0,0,142,147,3,32,16,0,143,
        144,7,1,0,0,144,146,3,32,16,0,145,143,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,152,1,0,0,0,149,147,1,0,0,0,150,
        152,5,27,0,0,151,142,1,0,0,0,151,150,1,0,0,0,152,31,1,0,0,0,153,
        158,3,34,17,0,154,155,7,2,0,0,155,157,3,34,17,0,156,154,1,0,0,0,
        157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,33,1,0,0,0,160,
        158,1,0,0,0,161,168,5,28,0,0,162,168,5,27,0,0,163,164,5,8,0,0,164,
        165,3,30,15,0,165,166,5,9,0,0,166,168,1,0,0,0,167,161,1,0,0,0,167,
        162,1,0,0,0,167,163,1,0,0,0,168,35,1,0,0,0,169,174,5,27,0,0,170,
        171,5,26,0,0,171,173,5,27,0,0,172,170,1,0,0,0,173,176,1,0,0,0,174,
        172,1,0,0,0,174,175,1,0,0,0,175,37,1,0,0,0,176,174,1,0,0,0,177,182,
        3,30,15,0,178,179,5,26,0,0,179,181,3,30,15,0,180,178,1,0,0,0,181,
        184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,39,1,0,0,0,184,182,
        1,0,0,0,17,43,55,64,69,73,81,90,98,104,125,138,147,151,158,167,174,
        182
    ]

class lenguajeTraductorParser ( Parser ):

    grammarFileName = "lenguajeTraductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'mostrar'", "'+'", "'si'", "'entonces'", 
                     "'sino'", "'funcion'", "'('", "')'", "'devolver'", 
                     "'activar'", "'guardar entrada en'", "'repetir'", "'hasta el valor de'", 
                     "'mientras'", "'{'", "'}'", "'>'", "'<'", "'=='", "' es verdadero '", 
                     "' es falso '", "'-'", "'*'", "'/'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_printStatement = 3
    RULE_ifStatement = 4
    RULE_elseBlock = 5
    RULE_functionDeclaration = 6
    RULE_returnVariable = 7
    RULE_functionCall = 8
    RULE_inputStatement = 9
    RULE_repeatStatement = 10
    RULE_whileStatement = 11
    RULE_block = 12
    RULE_condition = 13
    RULE_conditionBoolean = 14
    RULE_expression = 15
    RULE_term = 16
    RULE_factor = 17
    RULE_parameters = 18
    RULE_arguments = 19

    ruleNames =  [ "program", "statement", "assignment", "printStatement", 
                   "ifStatement", "elseBlock", "functionDeclaration", "returnVariable", 
                   "functionCall", "inputStatement", "repeatStatement", 
                   "whileStatement", "block", "condition", "conditionBoolean", 
                   "expression", "term", "factor", "parameters", "arguments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    ID=27
    NUMBER=28
    STRING=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.StatementContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.StatementContext,i)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = lenguajeTraductorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.statement()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 402701780) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.AssignmentContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.PrintStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.IfStatementContext,0)


        def elseBlock(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ElseBlockContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.FunctionDeclarationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.FunctionCallContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.InputStatementContext,0)


        def repeatStatement(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.RepeatStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.WhileStatementContext,0)


        def returnVariable(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ReturnVariableContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = lenguajeTraductorParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.elseBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.functionDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.functionCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.inputStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.repeatStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 53
                self.whileStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 54
                self.returnVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = lenguajeTraductorParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(lenguajeTraductorParser.ID)
            self.state = 58
            self.match(lenguajeTraductorParser.T__0)
            self.state = 59
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(lenguajeTraductorParser.STRING)
            else:
                return self.getToken(lenguajeTraductorParser.STRING, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.ExpressionContext,i)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = lenguajeTraductorParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(lenguajeTraductorParser.T__1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 62
                self.match(lenguajeTraductorParser.STRING)
                pass
            elif token in [8, 27, 28]:
                self.state = 63
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 66
                self.match(lenguajeTraductorParser.T__2)
                self.state = 69
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29]:
                    self.state = 67
                    self.match(lenguajeTraductorParser.STRING)
                    pass
                elif token in [8, 27, 28]:
                    self.state = 68
                    self.expression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.BlockContext,0)


        def elseBlock(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = lenguajeTraductorParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(lenguajeTraductorParser.T__3)
            self.state = 77
            self.condition()
            self.state = 78
            self.match(lenguajeTraductorParser.T__4)
            self.state = 79
            self.block()
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 80
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.BlockContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)




    def elseBlock(self):

        localctx = lenguajeTraductorParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(lenguajeTraductorParser.T__5)
            self.state = 84
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ParametersContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = lenguajeTraductorParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(lenguajeTraductorParser.T__6)
            self.state = 87
            self.match(lenguajeTraductorParser.ID)
            self.state = 88
            self.match(lenguajeTraductorParser.T__7)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 89
                self.parameters()


            self.state = 92
            self.match(lenguajeTraductorParser.T__8)
            self.state = 93
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_returnVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnVariable" ):
                listener.enterReturnVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnVariable" ):
                listener.exitReturnVariable(self)




    def returnVariable(self):

        localctx = lenguajeTraductorParser.ReturnVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnVariable)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(lenguajeTraductorParser.T__9)
                self.state = 96
                self.match(lenguajeTraductorParser.ID)
                pass
            elif token in [8, 27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def arguments(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = lenguajeTraductorParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(lenguajeTraductorParser.T__10)
            self.state = 101
            self.match(lenguajeTraductorParser.ID)
            self.state = 102
            self.match(lenguajeTraductorParser.T__7)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 402653440) != 0):
                self.state = 103
                self.arguments()


            self.state = 106
            self.match(lenguajeTraductorParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)




    def inputStatement(self):

        localctx = lenguajeTraductorParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(lenguajeTraductorParser.T__11)
            self.state = 109
            self.match(lenguajeTraductorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lenguajeTraductorParser.ID)
            else:
                return self.getToken(lenguajeTraductorParser.ID, i)

        def block(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.BlockContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_repeatStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatStatement" ):
                listener.enterRepeatStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatStatement" ):
                listener.exitRepeatStatement(self)




    def repeatStatement(self):

        localctx = lenguajeTraductorParser.RepeatStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repeatStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(lenguajeTraductorParser.T__12)
            self.state = 112
            self.match(lenguajeTraductorParser.ID)
            self.state = 113
            self.match(lenguajeTraductorParser.T__13)
            self.state = 114
            self.match(lenguajeTraductorParser.ID)
            self.state = 115
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.BlockContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = lenguajeTraductorParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(lenguajeTraductorParser.T__14)
            self.state = 118
            self.condition()
            self.state = 119
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.StatementContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.StatementContext,i)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = lenguajeTraductorParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(lenguajeTraductorParser.T__15)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 402701780) != 0):
                self.state = 122
                self.statement()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(lenguajeTraductorParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.ExpressionContext,i)


        def conditionBoolean(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ConditionBooleanContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = lenguajeTraductorParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expression()
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 131
                self.match(lenguajeTraductorParser.T__17)
                self.state = 132
                self.expression()
                pass
            elif token in [19]:
                self.state = 133
                self.match(lenguajeTraductorParser.T__18)
                self.state = 134
                self.expression()
                pass
            elif token in [20]:
                self.state = 135
                self.match(lenguajeTraductorParser.T__19)
                self.state = 136
                self.expression()
                pass
            elif token in [21, 22]:
                self.state = 137
                self.conditionBoolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_conditionBoolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionBoolean" ):
                listener.enterConditionBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionBoolean" ):
                listener.exitConditionBoolean(self)




    def conditionBoolean(self):

        localctx = lenguajeTraductorParser.ConditionBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_conditionBoolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.TermContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.TermContext,i)


        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = lenguajeTraductorParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.term()
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 143
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.term() 
                    self.state = 149
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(lenguajeTraductorParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.FactorContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.FactorContext,i)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = lenguajeTraductorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.factor()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.factor()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(lenguajeTraductorParser.NUMBER, 0)

        def ID(self):
            return self.getToken(lenguajeTraductorParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(lenguajeTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = lenguajeTraductorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(lenguajeTraductorParser.NUMBER)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(lenguajeTraductorParser.ID)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(lenguajeTraductorParser.T__7)
                self.state = 164
                self.expression()
                self.state = 165
                self.match(lenguajeTraductorParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lenguajeTraductorParser.ID)
            else:
                return self.getToken(lenguajeTraductorParser.ID, i)

        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = lenguajeTraductorParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(lenguajeTraductorParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 170
                self.match(lenguajeTraductorParser.T__25)
                self.state = 171
                self.match(lenguajeTraductorParser.ID)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeTraductorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(lenguajeTraductorParser.ExpressionContext,i)


        def getRuleIndex(self):
            return lenguajeTraductorParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = lenguajeTraductorParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expression()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 178
                self.match(lenguajeTraductorParser.T__25)
                self.state = 179
                self.expression()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





