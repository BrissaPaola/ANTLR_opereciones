# Generated from Oper.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,37,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,4,0,17,8,0,11,0,12,0,18,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,1,5,1,6,4,6,32,8,6,11,6,12,6,33,1,6,1,6,0,0,7,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,2,0,10,10,32,32,38,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,1,16,1,0,0,0,3,20,1,0,0,0,5,22,1,0,0,0,7,24,1,0,0,0,9,26,
        1,0,0,0,11,28,1,0,0,0,13,31,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,0,
        17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,2,1,0,0,0,20,21,5,43,
        0,0,21,4,1,0,0,0,22,23,5,45,0,0,23,6,1,0,0,0,24,25,5,42,0,0,25,8,
        1,0,0,0,26,27,5,47,0,0,27,10,1,0,0,0,28,29,5,94,0,0,29,12,1,0,0,
        0,30,32,7,1,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,35,1,0,0,0,35,36,6,6,0,0,36,14,1,0,0,0,3,0,18,33,1,6,
        0,0
    ]

class OperLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    MAS = 2
    MENOS = 3
    MULT = 4
    DIV = 5
    POT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MAS", "MENOS", "MULT", "DIV", "POT", "WS" ]

    ruleNames = [ "NUM", "MAS", "MENOS", "MULT", "DIV", "POT", "WS" ]

    grammarFileName = "Oper.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


