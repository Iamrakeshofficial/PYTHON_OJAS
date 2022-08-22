##x="python"
##y="on"
##dict={104:112}
##print(x.format_map("4"))
##print(x.casefold(y))
##print(x.center(20,'@'))
##print(x.count('p'))
##print(x.encode())
##print(x.endswith('n'))
##print(x.expandtabs())
##print(x.find("t"))
##print("{}".format(x))
##print("{}".format_map(y))
##print("index",x.index(y))
##print("isalnum",x.isalnum())
##print("isalpha",x.isalpha())
##print("isascii",x.isascii())
##print("isdecimal",x.isdecimal())
##print("isdigit",x.isdigit())
##print("isidentifier",x.isidentifier())
##print("islower",x.islower())
##print("isnumeric",x.isnumeric())
##print("isprintable",x.isprintable())
##print(x.isspace())
##print(x.istitle())
##print(x.isupper())
##print('-'.join(x))
##print(x.ljust(20,"@"))
##print(x.lower())
##print(x.lstripe())
##print(x.partition())
##print(x.removeprefix("p"))
##print(x.removesuffix("n"))
##print(x.replace(p,k))
##print(x.rfind())
##print(x.rindex())
##print(x.rjust())
##print(x.rpartition())
##print(x.rsplit())
##print(x.rstrip())
##print(x.split())
##print(x.splitlines())
##print(x.startswith())
##print(x.strip())
##print(x.swapcase())
##print(x.title())
##print(x.translate(dict))
##print(x.upper())
##print(x.zfill(20))
##
##"""|
## | casefold(self, /)
## |      Return a version of the string suitable for caseless comparisons.
## |
## |  center(self, width, fillchar=' ', /)
## |      Return a centered string of length width.
## |
## |      Padding is done using the specified fill character (default is a space).
## |
## |  count(...)
## |      S.count(sub[, start[, end]]) -> int
## |
## |      Return the number of non-overlapping occurrences of substring sub in
## |      string S[start:end].  Optional arguments start and end are
## |      interpreted as in slice notation.
## |
## |  encode(self, /, encoding='utf-8', errors='strict')
## |      Encode the string using the codec registered for encoding.
## |
## |      encoding
## |        The encoding in which to encode the string.
## |      errors
## |        The error handling scheme to use for encoding errors.
## |        The default is 'strict' meaning that encoding errors raise a
## |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
## |        'xmlcharrefreplace' as well as any other name registered with
## |        codecs.register_error that can handle UnicodeEncodeErrors.
## |
## |  endswith(...)
## |      S.endswith(suffix[, start[, end]]) -> bool
## |
## |      Return True if S ends with the specified suffix, False otherwise.
## |      With optional start, test S beginning at that position.
## |      With optional end, stop comparing S at that position.
## |      suffix can also be a tuple of strings to try.
## |
## |  expandtabs(self, /, tabsize=8)
## |      Return a copy where all tab characters are expanded using spaces.
## |
## |      If tabsize is not given, a tab size of 8 characters is assumed.
## |
## |  find(...)
## |      S.find(sub[, start[, end]]) -> int
## |
## |      Return the lowest index in S where substring sub is found,
## |      such that sub is contained within S[start:end].  Optional
## |      arguments start and end are interpreted as in slice notation.
## |
## |      Return -1 on failure.
## |
## |  format(...)
## |      S.format(*args, **kwargs) -> str
## |
## |      Return a formatted version of S, using substitutions from args and kwargs.
## |      The substitutions are identified by braces ('{' and '}').
## |
## |  format_map(...)
## |      S.format_map(mapping) -> str
## |
## |      Return a formatted version of S, using substitutions from mapping.
## |      The substitutions are identified by braces ('{' and '}').
## |
## |  index(...)
## |      S.index(sub[, start[, end]]) -> int
## |
## |      Return the lowest index in S where substring sub is found,
## |      such that sub is contained within S[start:end].  Optional
## |      arguments start and end are interpreted as in slice notation.
## |
## |      Raises ValueError when the substring is not found.
## |
## |  isalnum(self, /)
## |      Return True if the string is an alpha-numeric string, False otherwise.
## |
## |      A string is alpha-numeric if all characters in the string are alpha-numeric and
## |      there is at least one character in the string.
## |
## |  isalpha(self, /)
## |      Return True if the string is an alphabetic string, False otherwise.
## |
## |      A string is alphabetic if all characters in the string are alphabetic and there
## |      is at least one character in the string.
## |
## |  isascii(self, /)
## |      Return True if all characters in the string are ASCII, False otherwise.
## |
## |      ASCII characters have code points in the range U+0000-U+007F.
## |      Empty string is ASCII too.
## |
## |  isdecimal(self, /)
## |      Return True if the string is a decimal string, False otherwise.
## |
## |      A string is a decimal string if all characters in the string are decimal and
## |      there is at least one character in the string.
## |
## |  isdigit(self, /)
## |      Return True if the string is a digit string, False otherwise.
## |
## |      A string is a digit string if all characters in the string are digits and there
## |      is at least one character in the string.
## |
## |  isidentifier(self, /)
## |      Return True if the string is a valid Python identifier, False otherwise.
## |
## |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
## |      such as "def" or "class".
## |
## |  islower(self, /)
## |      Return True if the string is a lowercase string, False otherwise.
## |
## |      A string is lowercase if all cased characters in the string are lowercase and
## |      there is at least one cased character in the string.
## |
## |  isnumeric(self, /)
## |      Return True if the string is a numeric string, False otherwise.
## |
## |      A string is numeric if all characters in the string are numeric and there is at
## |      least one character in the string.
## |
## |  isprintable(self, /)
## |      Return True if the string is printable, False otherwise.
## |
## |      A string is printable if all of its characters are considered printable in
## |      repr() or if it is empty.
## |
## |  isspace(self, /)
## |      Return True if the string is a whitespace string, False otherwise.
## |
## |      A string is whitespace if all characters in the string are whitespace and there
## |      is at least one character in the string.
## |
## |  istitle(self, /)
## |      Return True if the string is a title-cased string, False otherwise.
## |
## |      In a title-cased string, upper- and title-case characters may only
## |      follow uncased characters and lowercase characters only cased ones.
## |
## |  isupper(self, /)
## |      Return True if the string is an uppercase string, False otherwise.
## |
## |      A string is uppercase if all cased characters in the string are uppercase and
## |      there is at least one cased character in the string.
## |
## |  join(self, iterable, /)
## |      Concatenate any number of strings.
## |
## |      The string whose method is called is inserted in between each given string.
## |      The result is returned as a new string.
## |
## |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
## |
## |  ljust(self, width, fillchar=' ', /)
## |      Return a left-justified string of length width.
## |
## |      Padding is done using the specified fill character (default is a space).
## |
## |  lower(self, /)
## |      Return a copy of the string converted to lowercase.
## |
## |  lstrip(self, chars=None, /)
## |      Return a copy of the string with leading whitespace removed.
## |
## |      If chars is given and not None, remove characters in chars instead.
## |
## |  partition(self, sep, /)
## |      Partition the string into three parts using the given separator.
## |
## |      This will search for the separator in the string.  If the separator is found,
## |      returns a 3-tuple containing the part before the separator, the separator
## |      itself, and the part after it.
## |
## |      If the separator is not found, returns a 3-tuple containing the original string
## |      and two empty strings.
## |
## |  removeprefix(self, prefix, /)
## |      Return a str with the given prefix string removed if present.
## |
## |      If the string starts with the prefix string, return string[len(prefix):].
## |      Otherwise, return a copy of the original string.
## |
## |  removesuffix(self, suffix, /)
## |      Return a str with the given suffix string removed if present.
## |
## |      If the string ends with the suffix string and that suffix is not empty,
## |      return string[:-len(suffix)]. Otherwise, return a copy of the original
## |      string.
## |
## |  replace(self, old, new, count=-1, /)
## |      Return a copy with all occurrences of substring old replaced by new.
## |
## |        count
## |          Maximum number of occurrences to replace.
## |          -1 (the default value) means replace all occurrences.
## |
## |      If the optional argument count is given, only the first count occurrences are
## |      replaced.
## |
## |  rfind(...)
## |      S.rfind(sub[, start[, end]]) -> int
## |
## |      Return the highest index in S where substring sub is found,
## |      such that sub is contained within S[start:end].  Optional
## |      arguments start and end are interpreted as in slice notation.
## |
## |      Return -1 on failure.
## |
## |  rindex(...)
## |      S.rindex(sub[, start[, end]]) -> int
## |
## |      Return the highest index in S where substring sub is found,
## |      such that sub is contained within S[start:end].  Optional
## |      arguments start and end are interpreted as in slice notation.
## |
## |      Raises ValueError when the substring is not found.
## |
## |  rjust(self, width, fillchar=' ', /)
## |      Return a right-justified string of length width.
## |
## |      Padding is done using the specified fill character (default is a space).
## |
## |  rpartition(self, sep, /)
## |      Partition the string into three parts using the given separator.
## |
## |      This will search for the separator in the string, starting at the end. If
## |      the separator is found, returns a 3-tuple containing the part before the
## |      separator, the separator itself, and the part after it.
## |
## |      If the separator is not found, returns a 3-tuple containing two empty strings
## |      and the original string.
## |
## |  rsplit(self, /, sep=None, maxsplit=-1)
## |      Return a list of the words in the string, using sep as the delimiter string.
## |
## |        sep
## |          The delimiter according which to split the string.
## |          None (the default value) means split according to any whitespace,
## |          and discard empty strings from the result.
## |        maxsplit
## |          Maximum number of splits to do.
## |          -1 (the default value) means no limit.
## |
## |      Splits are done starting at the end of the string and working to the front.
## |
## |  rstrip(self, chars=None, /)
## |      Return a copy of the string with trailing whitespace removed.
## |
## |      If chars is given and not None, remove characters in chars instead.
## |
## |  split(self, /, sep=None, maxsplit=-1)
## |      Return a list of the words in the string, using sep as the delimiter string.
## |
## |      sep
## |        The delimiter according which to split the string.
## |        None (the default value) means split according to any whitespace,
## |        and discard empty strings from the result.
## |      maxsplit
## |        Maximum number of splits to do.
## |        -1 (the default value) means no limit.
## |
## |  splitlines(self, /, keepends=False)
## |      Return a list of the lines in the string, breaking at line boundaries.
## |
## |      Line breaks are not included in the resulting list unless keepends is given and
## |      true.
## |
## |  startswith(...)
## |      S.startswith(prefix[, start[, end]]) -> bool
## |
## |      Return True if S starts with the specified prefix, False otherwise.
## |      With optional start, test S beginning at that position.
## |      With optional end, stop comparing S at that position.
## |      prefix can also be a tuple of strings to try.
## |
## |  strip(self, chars=None, /)
## |      Return a copy of the string with leading and trailing whitespace removed.
## |
## |      If chars is given and not None, remove characters in chars instead.
## |
## |  swapcase(self, /)
## |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
## |
## |  title(self, /)
## |      Return a version of the string where each word is titlecased.
## |
## |      More specifically, words start with uppercased characters and all remaining
## |      cased characters have lower case.
## |
## |  translate(self, table, /)
## |      Replace each character in the string using the given translation table.
## |
## |        table
## |          Translation table, which must be a mapping of Unicode ordinals to
## |          Unicode ordinals, strings, or None.
## |
## |      The table must implement lookup/indexing via __getitem__, for instance a
## |      dictionary or list.  If this operation raises LookupError, the character is
## |      left untouched.  Characters mapped to None are deleted.
## |
## |  upper(self, /)
## |      Return a copy of the string converted to uppercase.
## |
## |  zfill(self, width, /)
## |      Pad a numeric string with zeros on the left, to fill a field of the given width.
## |
## |      The string is never truncated."""

'''1)casefold():
-------------
The casefold() method returns a string where all the characters are lower case.
Syntax=string.casefold()'''
##Examples:
##---------
##s="Python Is An OOp Lang"
##print(s)
##s1=s.casefold()
##print(s1)

'''2)center():
-------------
The center() method will center align the string, using a specified character (space is default) as the fill character.

Syntax
string.center(length, character)'''

##Exmples:
##-------
##s="Python"
##print(s)
##s1=s.center(10,"0")
##print(s1)

'''3)count():
-------------
The count() method returns the number of times a specified value appears in the string.

Syntax:
string.count(value, start, end)'''
##Examples:
##---------
##s="Python is an oop Lang"
##print(s)
##s1=s.count("oop")
##print(s1)
'''4)encode():
--------------
The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

Syntax:
string.encode(encoding=encoding, errors=errors)'''

##Examples:
##---------
##s="Python is an oop Lang"
##print(s)
##s1=s.encode()
##print(s1)
'''5)endswith():
----------------
The endswith() method returns True if the string ends with the specified value, otherwise False.

Syntax:
string.endswith(value, start, end)'''
##Examples:
##---------
##s="Python is an oop Lang"
##print(s)
##s1=s.endswith("Lang")
##print(s1)

'''6)expandtabs():
------------------
The expandtabs() method sets the tab size to the specified number of whitespaces.

Syntax:
string.expandtabs(tabsize)'''
##Examples:
##---------
##s="P\ty\tt\th\to\tn"
##print(s)
##s1=s.expandtabs(2)
##
##print(s1)

'''7)find():
------------
=>This function is used finding the index of First Occurence of specified 
word / letter.
=>If the specified word is not present then we get ValueError 
Syntax:- Indexvalue=strobj.index(sub string)'''
##-------------------
##Example:
##-------------------
##s="Python is an oop lang"
##print(s)
##s1=s.index('oop')
##s2=s.index('is')
##print(s1)
##print(s2)          
           
'''8)format():
--------------
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

Syntax:
string.format(value1, value2...)'''
##Example:
##--------
#named indexes:
##txt1 = "My name is {fname}, I'm {age}".format(fname = "Rakesh", age = 23)
#numbered indexes:
##txt2 = "My name is {0}, I'm {1}".format("Rakesh",23)
#empty placeholders:
##txt3 = "My name is {}, I'm {}".format("Rakesh",23)
##print(txt1)
##print(txt2)
##print(txt3)

'''9)format_map():
------------------
Formats specified values in a string '''
##Example:
##--------
##s={"a":7,"b":8}
##print('{a} {b}'.format_map(s))

'''10)index():
--------------
Searches the string for a specified value and returns the position of where it was found '''
##Example:
##--------
s="python"
##print(s)
##print(s.index("t"))
##print(s.index("h"))

'''11)isalnum():
----------------
=>This returns True provided str data is a combination of str or digits or 
both
=>This returns False provided str data is a combination of str or digits 
with special symbols .
Syntax:- varname=strobj.isalnum()'''
##Examples:
##-------------------
##s="a1234b"
##print(s)
##b=s.isalnum()
##print(b)

'''12)isalpha:
--------------
=>This function returns True provided str data must contain purely 
alphabets.
136
 otherwise we get False
=>Syntax:- varname=strobj.isalpha()'''
##Examples:
##----------
##s="Rossum"
##print(s)
##b=s.isalpha()
##print(b)

'''13)isascii():
----------------
The isascii() method returns True if all the characters are ascii characters  (a-z).
Syntax:
string.isascii()'''
##Example:
##--------
##txt = "Company123"
##x = txt.isascii()
##print(x)

'''14)isdecimal():
-----------------
The isdecimal() method returns True if all the characters are decimals (0-9).

This method is used on unicode objects.

Syntax: string.isdecimal()'''
##Exaples:
##--------
##b = "\u0047"
##a = "12345"
##print(b.isdecimal())
##print(a.isdecimal())
'''15)isdigit():
----------------
 isdigit():
------------------
=> =>This function returns True provided str data must contain purely 
digits.
 otherwise we get False
=>Syntax:- varname=strobj.isdigit()'''
##--------------------
##Examples:
##--------------------
##s="1223"
##b=s.isdigit()
##print(s)
##print(b)


'''16)isidentifier():
--------------------
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

Syntax: string.isidentifier()'''
##Examples:
##---------
##s="python_12"
##p="1python"
##print(s.isidentifier())
##print(p.isidentifier())
'''17)islower():
----------------
8) islower() -->Returns True provided str object data is purely lower 
case data otherwise it returns False'''
##Examples:
##---------
##s="python"
##b=s.islower()
##print(b)

##s="Python"
##b=s.islower()
##print(b)
'''18)isnumeric():
------------------
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
Syntax:string.isnumeric()'''
##Examples:
##---------
##s="12345"
##print(s)
##s1=s.isnumeric()
##print(s1)
##s="Ram123"
##print(s)
##s1=s.isnumeric()
##print(s1)
'''19)isprintable():
-------------------
The isprintable() method returns True if all the characters are printable, otherwise False.
Example of none printable character can be carriage return and line feed.

Syntax:string.isprintable()'''
##Examples:
##---------
##txt = "Hello! Are you #1?"
##
##x = txt.isprintable()
##
##print(x)

'''20)isspace():
---------------
=>This Function returns True provided str object must contains purely 
spaces otherwise we get False.
137
Syntax:- varname=strobj.isspace()'''
##Examples:
##---------
##s=" Rossum "
##b=s.isspace()
##print(b)
##s=" "
##b=s.isspace()
##print(b)

'''21)istitle():
----------------
=>This function is used for converting First letter of every word of given 
string data.
=>Syntax:- varname=strobj.title()'''
##-----------
##Examples:
##----------
##s="python programming. python is an Fun Programming"
##print(s)
##s1=s.title()
##print(s1)

'''22)isupper():
----------------
isupper() -->Returns True provided str object data is purely upper case 
data otherwise it returns False'''
##Examples:
##---------
##s="PYThon"
##b=s.isupper()
##print(b)

##s="PYTHON"
##b=s.isupper()
##print(b)


'''23)join():
-------------
=>This is used for concatenating different str values of any iterable 
objects / Collection types.'''
##Examples:
##------------------
##l=["Python", " is ", " an ", " oop" " lang"]
##print(l,type(l))
##k=""
##k1=k.join(l)
##print(k1)

'''24)l just():
---------------
The ljust() method will left align the string, using a specified character (space is default) as the fill character.

Syntax:string.ljust(length, character)'''
##Examples:
##---------
##s= "Python"
##x = s.ljust(20, "O")
##print(x)

'''25)lower():
--------------
lower()-> This Function converts Upper Case data into lower case
Syntax: strobj1=strobj1.lower()'''
##Examples:
##---------
##s="PYTHON PROGRAMMING"
##print(s)
##l=s.lower()
##print(l)

'''26)lstrip():
---------------
The lstrip() method removes any leading characters (space is the default leading character to remove)

Syntax:string.lstrip(characters)'''
##Example:
##--------
##s= "     Python     "
##
##x = s.lstrip()
##
##print(x)

'''27)partition():
------------------
he partition() method searches for a specified string, and splits the string into a tuple containing three elements.
The first element contains the part before the specified string.
The second element contains the specified string.
The third element contains the part after the string.
Syntax:string.partition(value)'''
##Examples:
##---------
##txt = "I could eat bananas all day"
##
##x = txt.partition("bananas")
##
##print(x)

'''28)removeprefix():'''
##--------------------

'''29)removesuffix():'''
##-----------------
'''30)replace():
---------------
The replace() method replaces a specified phrase with another specified phrase.

Syntax: string.replace(oldvalue, newvalue, count)'''
##Examples:
##---------
##t= "I like bananas"
##x = t.replace("bananas", "apples")
##print(x)

'''31)rfind():
-------------
The rfind() method finds the last occurrence of the specified value.
The rfind() method returns -1 if the value is not found.
The rfind() method is almost the same as the rindex() method. See example below.

Syntax
string.rfind(value, start, end)'''
##Examples:
##---------
##txt = "Hello, welcome to my world."
##
##x = txt.rfind("e",5,10)
##print(x)

'''32)rindex():
---------------
The rindex() method finds the last occurrence of the specified value.
The rindex() method raises an exception if the value is not found.
The rindex() method is almost the same as the rfind() method. See example below.

Syntax:
string.rindex(value, start, end)'''
##Examples:
##---------
##t= "Hello, welcome to my world."
##
##x = t.rindex("e", 5, 10)
##
##print(x)

'''33)rjust():
--------------
The rjust() method will right align the string, using a specified character (space is default) as the fill character.

Syntax
string.rjust(length, character)'''
##Examples:
##---------
##s= "Python"
##
##x = s.rjust(20, "O")
##
##print(x)

'''s34)rpartition():
-------------------
The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
The first element contains the part before the specified string.
The second element contains the specified string.
The third element contains the part after the string.

Syntax
string.rpartition(value)'''
##Examples:
##---------
##txt = "I could read Python all day, Pytthon is  my favorite subject"
##
##x = txt.rpartition("Python")
##
##print(x)
'''35)rstrip():
---------------
he rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

Syntax
string.rstrip(characters)'''
##Examples:
##---------
##s= "     English     "
##
##x =s.rstrip()
##print(x)

'''36)rsplit():
---------------
he rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.
Syntax
string.rsplit(separator, maxsplit)'''
##Examples:
##---------
##s= "apple, banana, cherry"
##
##x = s.rsplit(" , ")
##
##print(x)

'''37)split():
--------------
=>This function is used for splitting the given str data into different 
Tokens based on delimeter. The default delimeter space.
=>We can also specify the programmer-defined delemiter.
Syntax: listobj=strobj.split( str delimeter)'''

##Examples:
##--------------------
##s="Python is an oop lang"
##print(s)
##l=s.split()
##print(l)

'''38)splitlines():
-------------------
The splitlines() method splits a string into a list. The splitting is done at line breaks.

Syntax:
string.splitlines(keeplinebreaks)'''
##Examples:
##---------
##s= "Thank you for the music\nWelcome to the jungle"
##print(s)
##x = s.splitlines()
##print(x)

'''39)startswith():
-------------------
The startswith() method returns True if the string starts with the specified value, otherwise False.

Syntax:
string.startswith(value, start, end)'''
##Examples:
##---------
##s= "Hello, welcome to my world."
##print(s)
##x = s.startswith("Hello")
##print(x)

'''40)strip();
-------------
The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

Syntax:string.strip(characters)'''
##Example:
##--------
##s = "     banana     "
##
##x = s.strip()
##print(x)

'''41)swapcase():
----------------
he swapcase() method returns a string where all the upper case letters are lower case and vice versa.

Syntax:string.swapcase()'''
##Examples:
##---------
##s= "Hello My Name Is PETER"
##
##x = s.swapcase()
##
##print(x)

'''42)title():
--------------
=>This function is used for converting First letter of every word of given 
string data.
=>Syntax:- varname=strobj.title()'''
##-----------
##Examples:
##---------
##s="python programming. python is an Fun Programming"
##print(s)
##s1=s.title()
##print(s1)


'''43)translate():
------------------
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary,
or in a mapping table.
Syntax:string.translate(table)'''
##Examples:
##----------
##s= "Hello Sam!"
##s2= s.maketrans("S", "P")
##print(s.translate(s2))

'''44)upper():
--------------
This Function converts lower Case data into upper case.
strobj1=strobj1.upper()'''
##----------
##Examples:
##---------
##s="Python is an oop lang"
##print(s)
##s1=s.upper()
##print(s1)

'''45)zfill():
--------------
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
If the value of the len parameter is less than the length of the string, no filling is done.

Syntax:
string.zfill(len)'''
##Examples:
##---------
##s= "50"
##x = s.zfill(10)
##
##print(x)
