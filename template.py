#template.py
import fileinput, re
# pattern object to match the field to be replaced, for efficient processing

field_pat = re.compile(r"""\[  # To make 're' know this is no character set but a regular bracket open
                    (  # begin group to use to capture what's in the field
                    .+?  # few repetitions of non-newline characters; at least one repeat. Ungreedy match
                    )  # end group
                    \] # close bracket
                    """, re.VERBOSE)

scope = {}      # Dictionary to serve as global scope for eval and exec

# replacement takes a MatchObject
def replacement(m):
    code = m.group(1)  # returns occurrences of group 1 in 'm' as a string

    try:
        return str(eval(code, scope)) # This works if code is a valid python expression. eval() returns the type it evals,reason for "stringing" it
    except SyntaxError:
        exec(code, scope)       #if eval don't work, it means code is a statement so we use exec
        return ""               # exec() doesn't return anything, so we return an empty string. exec()'s result is stored in scope though

lines = []  # List to hold all the lines in file to be passed as cmd args

for line in fileinput.input():      #fileinput.input returns an iterable object from the file(s) passed to it
    lines.append(line)

entire_text = " ".join(lines)       # Long string - the entire lines of the file

# sub is used as a method of the PatternObject 'field_pat' returned by re.compile
# re.sub returns "entire_text" with every substring matched by "field_pat" replaced by the result of replacement()'s processing
print(field_pat.sub(replacement, entire_text))
