from typing import List, Tuple

def make_token(rules: List[chr], end_char: chr) -> str:
    nonterminal_name: str = ""
    current_char: char = rules.pop(0)

    while(current_char != end_char):
        nonterminal_name += current_char
        current_char: char = rules.pop(0)

    return nonterminal_name

def make_IDA(rules: List[chr]) -> str:
    temp_IDA = ":"
    temp_IDA += rules.pop(0)
    temp_IDA += rules.pop(0)

    return temp_IDA

def tokenizeBnf(rules) -> List[Tuple[str,str]]:
    # Split rules into a list of individual characters
    rules_chars: List[chr] = [char for char in rules]

    # List of tokens
    tokens: List[Tuple[str,str]] = []

    current_char: char

    # For each char, decide what to do
    while(rules_chars):
        current_char = rules_chars.pop(0)

        if(current_char == '|'):
            tokens.append( ("separator", "|") )

        elif(current_char == "\n"):
            tokens.append( ("EOL", "\n") )

        elif(current_char == "{" or current_char == "}"):
            tokens.append( ("bracket", current_char) )

        elif(current_char == ":"):
            tokens.append( ("is_defined_as", make_IDA(rules_chars)) )

        elif(current_char == '<'):
            tokens.append( ("nonterminal",  make_token(rules_chars, '>')) )

        elif(current_char == '\"'):
            tokens.append( ("terminal",     make_token(rules_chars, '\"')) )
    
    return tokens
