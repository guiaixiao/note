Help on module fnmatch:

NAME
    fnmatch - Filename matching with shell patterns.

DESCRIPTION
    fnmatch(FILENAME, PATTERN) matches according to the local convention.
    fnmatchcase(FILENAME, PATTERN) always takes case in account.

    The functions operate by translating the pattern into a regular
    expression.  They cache the compiled regular expressions for speed.

    The function translate(PATTERN) returns a regular expression
    corresponding to PATTERN.  (It does not compile it.)

FUNCTIONS
    filter(names, pat)
        Return the subset of the list NAMES that match PAT.

    fnmatch(name, pat)
        Test whether FILENAME matches PATTERN.

        Patterns are Unix shell style:

        *       matches everything
        ?       matches any single character
        [seq]   matches any character in seq
        [!seq]  matches any char not in seq

        An initial period in FILENAME is not special.
        Both FILENAME and PATTERN are first case - normalized
        if the operating system requires it.
        If you don't want this, use fnmatchcase(FILENAME, PATTERN).

    fnmatchcase(name, pat)
        Test whether FILENAME matches PATTERN, including case.

        This is a version of fnmatch() which doesn't case - normalize
        its arguments.

    translate(pat)
        Translate a shell PATTERN to a regular expression.

        There is no way to quote meta - characters.

DATA
    __all__ = ['filter', 'fnmatch', 'fnmatchcase', 'translate']

FILE
    d: \python\lib\fnmatch.py

fnmatch 模块专门用来进行文件名匹配，支持使用通配符进行字符串匹配

fnmatch 只有4个函数：
1、
