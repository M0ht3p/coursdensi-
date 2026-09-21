import sys
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Union

class TokenType(Enum):
    PTR_INC = auto()
    PTR_DEC = auto()
    VAL_INC = auto()
    VAL_DEC = auto()
    OUTPUT  = auto()
    INPUT   = auto()
    LOOP_L  = auto()
    LOOP_R  = auto()

@dataclass
class Token:
    type: TokenType
    char: str
    line: int
    column: int

class Lexer:
    TOKEN_MAP = {
        '>': TokenType.PTR_INC,
        '<': TokenType.PTR_DEC,
        '+': TokenType.VAL_INC,
        '-': TokenType.VAL_DEC,
        '.': TokenType.OUTPUT,
        ',': TokenType.INPUT,
        '[': TokenType.LOOP_L,
        ']': TokenType.LOOP_R,
    }

    def __init__(self, code: str):
        self.code = code

    def tokenize(self) -> List[Token]:
        tokens = []
        line = 1
        col = 1
        for char in self.code:
            if char in self.TOKEN_MAP:
                tokens.append(Token(type=self.TOKEN_MAP[char], char=char, line=line, column=col))
            if char == '\n':
                line += 1
                col = 1
            else:
                col += 1
        return tokens

class ASTNode:
    pass

@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)

@dataclass
class PointerShiftNode(ASTNode):
    amount: int

@dataclass
class ValueShiftNode(ASTNode):
    amount: int

@dataclass
class ZeroNode(ASTNode):
    pass

@dataclass
class OutputNode(ASTNode):
    pass

@dataclass
class InputNode(ASTNode):
    pass

@dataclass
class LoopNode(ASTNode):
    body: List[ASTNode] = field(default_factory=list)

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def parse(self) -> ProgramNode:
        root = ProgramNode()
        stack = [root.statements]

        for token in self.tokens:
            if token.type == TokenType.PTR_INC:
                stack[-1].append(PointerShiftNode(1))
            elif token.type == TokenType.PTR_DEC:
                stack[-1].append(PointerShiftNode(-1))
            elif token.type == TokenType.VAL_INC:
                stack[-1].append(ValueShiftNode(1))
            elif token.type == TokenType.VAL_DEC:
                stack[-1].append(ValueShiftNode(-1))
            elif token.type == TokenType.OUTPUT:
                stack[-1].append(OutputNode())
            elif token.type == TokenType.INPUT:
                stack[-1].append(InputNode())
            elif token.type == TokenType.LOOP_L:
                loop = LoopNode()
                stack[-1].append(loop)
                stack.append(loop.body)
            elif token.type == TokenType.LOOP_R:
                if len(stack) <= 1:
                    raise SyntaxError(f"Unmatched closing bracket ']' at line {token.line}, column {token.column}.")
                stack.pop()

        if len(stack) > 1:
            raise SyntaxError("Unmatched opening bracket '[' in Brainfuck code.")

        return root

class ASTOptimizer:
    @classmethod
    def optimize(cls, node: ASTNode) -> ASTNode:
        if isinstance(node, ProgramNode):
            node.statements = cls._optimize_statements(node.statements)
        elif isinstance(node, LoopNode):
            if len(node.body) == 1 and isinstance(node.body[0], ValueShiftNode):
                return ZeroNode()
            node.body = cls._optimize_statements(node.body)
        return node

    @classmethod
    def _optimize_statements(cls, statements: List[ASTNode]) -> List[ASTNode]:
        optimized: List[ASTNode] = []
        for stmt in statements:
            stmt = cls.optimize(stmt)
            if not optimized:
                optimized.append(stmt)
                continue

            prev = optimized[-1]

            if isinstance(prev, PointerShiftNode) and isinstance(stmt, PointerShiftNode):
                prev.amount += stmt.amount
                if prev.amount == 0:
                    optimized.pop()
            elif isinstance(prev, ValueShiftNode) and isinstance(stmt, ValueShiftNode):
                prev.amount += stmt.amount
                if prev.amount == 0:
                    optimized.pop()
            else:
                optimized.append(stmt)

        return optimized

class PythonEmitter:
    def __init__(self, indent_size: int = 4, tape_size: int = 30000):
        self.indent_size = indent_size
        self.tape_size = tape_size
        self.lines: List[str] = []

    def emit(self, ast: ProgramNode) -> str:
        self.lines = [
            "import sys\n",
            f"tape = [0] * {self.tape_size}",
            "ptr = 0\n"
        ]
        self._visit_statements(ast.statements, indent_level=0)
        return "\n".join(self.lines)

    def _visit_statements(self, statements: List[ASTNode], indent_level: int):
        indent = " " * (self.indent_size * indent_level)
        for stmt in statements:
            if isinstance(stmt, PointerShiftNode):
                if stmt.amount != 0:
                    sign = "+" if stmt.amount > 0 else "-"
                    val = abs(stmt.amount)
                    self.lines.append(f"{indent}ptr = (ptr {sign} {val}) % {self.tape_size}")
            elif isinstance(stmt, ValueShiftNode):
                if stmt.amount != 0:
                    sign = "+" if stmt.amount > 0 else "-"
                    val = abs(stmt.amount)
                    self.lines.append(f"{indent}tape[ptr] = (tape[ptr] {sign} {val}) % 256")
            elif isinstance(stmt, ZeroNode):
                self.lines.append(f"{indent}tape[ptr] = 0")
            elif isinstance(stmt, OutputNode):
                self.lines.append(f"{indent}sys.stdout.write(chr(tape[ptr]))")
            elif isinstance(stmt, InputNode):
                self.lines.append(f"{indent}tape[ptr] = ord(sys.stdin.read(1) or '\\0') % 256")
            elif isinstance(stmt, LoopNode):
                self.lines.append(f"{indent}while tape[ptr] != 0:")
                self._visit_statements(stmt.body, indent_level + 1)

def brainfuck_to_python(bf_code: str) -> str:
    tokens = Lexer(bf_code).tokenize()
    ast = Parser(tokens).parse()
    optimized_ast = ASTOptimizer.optimize(ast)
    return PythonEmitter().emit(optimized_ast)


if __name__ == "__main__":
    hello_bf = "++++++++++[>+++++++>++++++++++<<-]>+.>++."[cite: 1]
    
    python_script = brainfuck_to_python(hello_bf)[cite: 1]
    
    print("--- Generated Python Code ---")[cite: 1]
    print(python_script)[cite: 1]
    print("\n--- Execution Output ---")[cite: 1]
    exec(python_script)[cite: 1]
