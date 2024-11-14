# Generated from traductorPythonaJava.g4 by ANTLR 4.13.2
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
        4,1,12,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,4,1,4,5,4,54,8,
        4,10,4,12,4,57,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,5,8,74,8,8,10,8,12,8,77,9,8,1,9,1,9,1,9,1,9,3,9,83,
        8,9,1,9,1,9,1,9,5,9,88,8,9,10,9,12,9,91,9,9,1,10,1,10,1,10,3,10,
        96,8,10,1,10,1,10,1,11,1,11,1,11,5,11,103,8,11,10,11,12,11,106,9,
        11,1,11,0,1,18,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,107,0,25,1,
        0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,43,1,0,0,0,8,55,1,0,0,0,10,58,
        1,0,0,0,12,62,1,0,0,0,14,65,1,0,0,0,16,70,1,0,0,0,18,82,1,0,0,0,
        20,92,1,0,0,0,22,99,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,
        0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,32,3,4,2,0,30,
        32,3,14,7,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,1,0,
        0,34,35,5,10,0,0,35,37,5,6,0,0,36,38,3,6,3,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,5,7,0,0,40,41,5,8,0,0,41,42,3,8,4,0,
        42,5,1,0,0,0,43,48,5,10,0,0,44,45,5,9,0,0,45,47,5,10,0,0,46,44,1,
        0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,7,1,0,0,0,50,
        48,1,0,0,0,51,54,3,10,5,0,52,54,3,12,6,0,53,51,1,0,0,0,53,52,1,0,
        0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,9,1,0,0,0,57,55,
        1,0,0,0,58,59,5,10,0,0,59,60,5,4,0,0,60,61,3,18,9,0,61,11,1,0,0,
        0,62,63,5,2,0,0,63,64,3,18,9,0,64,13,1,0,0,0,65,66,5,3,0,0,66,67,
        5,6,0,0,67,68,3,16,8,0,68,69,5,7,0,0,69,15,1,0,0,0,70,75,3,18,9,
        0,71,72,5,9,0,0,72,74,3,18,9,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,
        1,0,0,0,75,76,1,0,0,0,76,17,1,0,0,0,77,75,1,0,0,0,78,79,6,9,-1,0,
        79,83,5,10,0,0,80,83,5,11,0,0,81,83,3,20,10,0,82,78,1,0,0,0,82,80,
        1,0,0,0,82,81,1,0,0,0,83,89,1,0,0,0,84,85,10,4,0,0,85,86,5,5,0,0,
        86,88,3,18,9,5,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,19,1,0,0,0,91,89,1,0,0,0,92,93,5,10,0,0,93,95,5,6,0,0,94,
        96,3,22,11,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,7,
        0,0,98,21,1,0,0,0,99,104,3,18,9,0,100,101,5,9,0,0,101,103,3,18,9,
        0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,
        0,105,23,1,0,0,0,106,104,1,0,0,0,11,27,31,37,48,53,55,75,82,89,95,
        104
    ]

class traductorPythonaJavaParser ( Parser ):

    grammarFileName = "traductorPythonaJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "'='", 
                     "'+'", "'('", "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "EQ", "PLUS", 
                      "LPAREN", "RPAREN", "COLON", "COMMA", "ID", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_funcDef = 2
    RULE_params = 3
    RULE_body = 4
    RULE_assignmentStat = 5
    RULE_returnStat = 6
    RULE_printStat = 7
    RULE_exprList = 8
    RULE_expr = 9
    RULE_funcCall = 10
    RULE_args = 11

    ruleNames =  [ "prog", "stat", "funcDef", "params", "body", "assignmentStat", 
                   "returnStat", "printStat", "exprList", "expr", "funcCall", 
                   "args" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    EQ=4
    PLUS=5
    LPAREN=6
    RPAREN=7
    COLON=8
    COMMA=9
    ID=10
    INT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPythonaJavaParser.StatContext)
            else:
                return self.getTypedRuleContext(traductorPythonaJavaParser.StatContext,i)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = traductorPythonaJavaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.stat()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDef(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.FuncDefContext,0)


        def printStat(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.PrintStatContext,0)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = traductorPythonaJavaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.funcDef()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.printStat()
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


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(traductorPythonaJavaParser.DEF, 0)

        def ID(self):
            return self.getToken(traductorPythonaJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(traductorPythonaJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(traductorPythonaJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(traductorPythonaJavaParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.BodyContext,0)


        def params(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.ParamsContext,0)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)




    def funcDef(self):

        localctx = traductorPythonaJavaParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(traductorPythonaJavaParser.DEF)
            self.state = 34
            self.match(traductorPythonaJavaParser.ID)
            self.state = 35
            self.match(traductorPythonaJavaParser.LPAREN)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 36
                self.params()


            self.state = 39
            self.match(traductorPythonaJavaParser.RPAREN)
            self.state = 40
            self.match(traductorPythonaJavaParser.COLON)
            self.state = 41
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPythonaJavaParser.ID)
            else:
                return self.getToken(traductorPythonaJavaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPythonaJavaParser.COMMA)
            else:
                return self.getToken(traductorPythonaJavaParser.COMMA, i)

        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = traductorPythonaJavaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(traductorPythonaJavaParser.ID)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 44
                self.match(traductorPythonaJavaParser.COMMA)
                self.state = 45
                self.match(traductorPythonaJavaParser.ID)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPythonaJavaParser.AssignmentStatContext)
            else:
                return self.getTypedRuleContext(traductorPythonaJavaParser.AssignmentStatContext,i)


        def returnStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPythonaJavaParser.ReturnStatContext)
            else:
                return self.getTypedRuleContext(traductorPythonaJavaParser.ReturnStatContext,i)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = traductorPythonaJavaParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==10:
                self.state = 53
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10]:
                    self.state = 51
                    self.assignmentStat()
                    pass
                elif token in [2]:
                    self.state = 52
                    self.returnStat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(traductorPythonaJavaParser.ID, 0)

        def EQ(self):
            return self.getToken(traductorPythonaJavaParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_assignmentStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStat" ):
                listener.enterAssignmentStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStat" ):
                listener.exitAssignmentStat(self)




    def assignmentStat(self):

        localctx = traductorPythonaJavaParser.AssignmentStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(traductorPythonaJavaParser.ID)
            self.state = 59
            self.match(traductorPythonaJavaParser.EQ)
            self.state = 60
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(traductorPythonaJavaParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_returnStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStat" ):
                listener.enterReturnStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStat" ):
                listener.exitReturnStat(self)




    def returnStat(self):

        localctx = traductorPythonaJavaParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(traductorPythonaJavaParser.RETURN)
            self.state = 63
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(traductorPythonaJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(traductorPythonaJavaParser.LPAREN, 0)

        def exprList(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.ExprListContext,0)


        def RPAREN(self):
            return self.getToken(traductorPythonaJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)




    def printStat(self):

        localctx = traductorPythonaJavaParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(traductorPythonaJavaParser.PRINT)
            self.state = 66
            self.match(traductorPythonaJavaParser.LPAREN)
            self.state = 67
            self.exprList()
            self.state = 68
            self.match(traductorPythonaJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPythonaJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(traductorPythonaJavaParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPythonaJavaParser.COMMA)
            else:
                return self.getToken(traductorPythonaJavaParser.COMMA, i)

        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)




    def exprList(self):

        localctx = traductorPythonaJavaParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.expr(0)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 71
                self.match(traductorPythonaJavaParser.COMMA)
                self.state = 72
                self.expr(0)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(traductorPythonaJavaParser.ID, 0)

        def INT(self):
            return self.getToken(traductorPythonaJavaParser.INT, 0)

        def funcCall(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.FuncCallContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPythonaJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(traductorPythonaJavaParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(traductorPythonaJavaParser.PLUS, 0)

        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = traductorPythonaJavaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(traductorPythonaJavaParser.ID)
                pass

            elif la_ == 2:
                self.state = 80
                self.match(traductorPythonaJavaParser.INT)
                pass

            elif la_ == 3:
                self.state = 81
                self.funcCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = traductorPythonaJavaParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 84
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 85
                    self.match(traductorPythonaJavaParser.PLUS)
                    self.state = 86
                    self.expr(5) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(traductorPythonaJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(traductorPythonaJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(traductorPythonaJavaParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(traductorPythonaJavaParser.ArgsContext,0)


        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = traductorPythonaJavaParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(traductorPythonaJavaParser.ID)
            self.state = 93
            self.match(traductorPythonaJavaParser.LPAREN)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==11:
                self.state = 94
                self.args()


            self.state = 97
            self.match(traductorPythonaJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPythonaJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(traductorPythonaJavaParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPythonaJavaParser.COMMA)
            else:
                return self.getToken(traductorPythonaJavaParser.COMMA, i)

        def getRuleIndex(self):
            return traductorPythonaJavaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = traductorPythonaJavaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.expr(0)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 100
                self.match(traductorPythonaJavaParser.COMMA)
                self.state = 101
                self.expr(0)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




