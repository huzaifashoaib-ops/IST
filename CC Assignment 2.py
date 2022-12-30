import re
import ast
from ast import parse

def tokenize(expression):
  # Define regular expressions for each type of token
  number_regex = r'[0-9_]'
  lowercase_regex = r'[abcdefghijklmnopqrstuvwxyz_]\d*'
  uppercase_regex = r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ_]\d*'
  operator_regex = r'[+*-/]'
  special_regex = r'[~`!@#$%^&()_=|";:<>,.?]'

  # Use the regular expressions to tokenize the input
  tokens = re.findall(f"{number_regex}|{lowercase_regex}|{uppercase_regex}|{operator_regex}|{special_regex}", expression)
  

  # Output the list of tokens
  return tokens

def parse_tree(expression):
  tree=ast.parse(expression,mode='exec')
  #print(eval(compile(tree,"",mode='eval')))
  print(ast.dump(tree))

# Test the tokenize function
expression = "5+8-2+huzaifa"
print(tokenize(expression))
print(parse_tree(expression))

