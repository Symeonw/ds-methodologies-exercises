.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit 
\w      - Word Character
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace
\b      - Word Boundary
\B      - Not a word Boundry
^       - Beginning of a String
$       - End of a String

[]      - Matches Character in brackets
[^ ]    - Matches Characters NOT in brackets

|       - Either or
( )     - Group
example for Mr., Mr, Ms, and Mrs.:
r'M(r|s|rs)\.?\s[A-Z]\w+



Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers
