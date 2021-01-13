# bnf-tokenizer
Bnf-like syntax tokenizer

Can correctly tokenize

```bnf
<sentence>  ::= <subj> <verb> <obj>
<subj>      ::= <art> <noun> | "the robot"
<art>       ::= "the" | "a"
<noun>      ::= "dog" | "cat" | "man" | "woman" | "robot"
<verb>      ::= "bit" | "kicked" | "stroked"
<obj>       ::= <art> <noun> | "two furry dice"
```

as well as

```bnf
<integer_definition> ::= "int "<identifier>" = "{<digit>}";"
```
