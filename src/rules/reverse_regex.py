from src.rules.rule_tokenizer import ruleParser
from typing import List


def reverse_regex(tokenized_re: List[str]):
    tokenized_re.reverse()
    operator = {"*", "+", "?"}
    reversed_re = []
    stack = []
    prev = None
    temp_stack = []
    set_begin = False
    for i in tokenized_re:
        if i == "}":
            set_begin = True

        if set_begin:
            temp_stack.append(i)
            if i == "{":
                set_begin = False
            prev = i
            continue

        if prev == "{":
            temp_stack.append(i)
            temp_stack.reverse()
            reversed_re += temp_stack
            prev = i
            temp_stack = []
            continue

        if i == "(":
            # pop from stack
            reversed_re.append(")")
            pop_tok = stack.pop(-1)
            if pop_tok != "":
                reversed_re.append(pop_tok)

        elif i == ")":
            # add to stack
            if prev in operator:
                stack.append(prev)
            else:
                stack.append("")

            reversed_re.append("(")

        elif i in operator:
            pass

        else:
            reversed_re.append(i)
            if prev in operator:
                reversed_re.append(prev)

        prev = i

    return reversed_re


if __name__ == "__main__":
    ruleString = "($ * abbreviation ( & | $ ) * a{1, 3} )"
    parseResult = ruleParser(ruleString)
    print(parseResult)
    reversed_re = reverse_regex(parseResult)
    print(reversed_re)
