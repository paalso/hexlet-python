#!/usr/bin/env python3
# https://ru.hexlet.io/code_reviews/460386

def stringify(value, replacer=' ', spaces_count=1):
    def walk(value, depth):
        if type(value) in (str, bool, int):
            return str(value)

        tokens = ['{']
        right_bracket_indent = f'{(depth * spaces_count) * replacer}'
        content_indent = right_bracket_indent + spaces_count * replacer
        for key, value in value.items():
            tokens.append(f'{content_indent}{key}: {walk(value, depth + 1)}')
        tokens.append(('' if depth == 0 else right_bracket_indent) +'}')
        return '\n'.join(tokens)
    
    return walk(value, 0)
