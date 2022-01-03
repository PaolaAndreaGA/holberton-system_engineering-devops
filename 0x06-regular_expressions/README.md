# Regular Expressions. Get to know them and Lose your fear of them

Published13 years ago

Last updated9 years ago

A regular expression is a string of characters that is used to describe or find patterns within other strings, based on the use of delimiters and certain syntax rules. Most programmers don't take the time to learn how to apply regular expressions, which is a pity as they are very useful. Once you learn how to apply regular expressions, you will realise how powerful they are, how many problems they can solve, and how much they will increase your programming productivity.

If you're new to the concept of regular expressions - also known as "regex" in programming jargon - you'll be encouraged to know that you've probably already used them without even knowing it, at least in their most basic form. For example, the command dir *.txt to get a list of all files with a txt extension is a very simple form of regular expression, where the * pattern matches any string of characters.

Let's look at a simple example of a pattern and the strings it might match:

am // this is our pattern. If we match it with:
am // matches
ambition // matches
camp // matches
mano // does not match

It is simply a matter of matching a pattern - which in this example is the sequence of letters 'am' - with a string (subject) and see if the same sequence exists within it. If it exists, we say that we have found a match.

These examples are very simple as they use literal patterns, i.e. we only find matches when there is an exact occurrence. In fact, it is usually not necessary to use regular expressions if we go to exact texts. All languages have string functions for this purpose. The power of regular expressions lies precisely in the flexibility of the patterns, which can be matched against any word or string that has a known structure.


Characters and meta-characters
Our pattern can consist of a set of characters (letters, numbers or signs) accompanied by metacharacters that represent other characters or allow a contextual search.
Metacharacters are so called because they do not represent themselves, but are interpreted in a special way. For example, through metacharacters we can define different conditions such as groupings, alternatives, wildcards, multipliers and so on.

The most commonly used metacharacters are: . * ? + [ ] ( ) { } ^ $ | \.

These are explained in detail below.

Positioning metacharacters, or anchors
The '^' and '$' signs are used to indicate where our pattern must be placed in the string to be considered a match. When we use the '^' sign we mean that the pattern must appear at the beginning of the compared string. When we use the '$' sign we mean that the pattern must appear at the end of the character set. Or more precisely, before a newline character.

Example:

![](http://www.sg.com.mx/images/stories/200705/programacion1.gif)

In the same way, the expression ^$ can be used to find empty lines, where the beginning of a line is immediately followed by the end of the line.

The metacharacters '^' and '$' are also known as anchors because they do not represent other characters, but positions in a string.

Escaping characters
It may happen that we need to include in our pattern a metacharacter as a literal sign, that is, for itself and not for what it represents. To indicate this purpose, we will use the backslash character 'back-slash' as an escape character. As a general rule, the backslash '\' converts special characters to normal.

Example:

![](http://www.sg.com.mx/images/stories/200705/programacion2.gif)

The wildcard '.
The metacharacter '.' (dot) is the ultimate wildcard. A dot in the pattern represents any character except newline.

Example:

![](http://www.sg.com.mx/images/stories/200705/programacion2a.gif)

Notice in the example above how the pattern matches any character (including the whitespace character) followed by an l.

Character classes
The square brackets '[ ]' define a character class and allow you to find any of the characters within a group. Let's imagine that we want to find the word "child", but we also want to find in case it was written with n instead of ñ. We could achieve this with a character class, so that the regular expression ni[ñn]o would be interpreted as "n, followed by i, followed by either ñ or n, followed by o".

Most metacharacters lose their meaning when used within character classes. Thus the expression [a.] literally refers to the letter a and the character dot. A special case is the character '^', which when used at the beginning of a character class means negation. That is, the expression [^a] refers to any string that does NOT contain the letter a. This meaning is lost if the '^' is not at the beginning of the character class, so the expression [a^] refers to the letter a and the ^ character literally.

Just as most metacharacters lose their special meaning when used inside square brackets, there is one character that only when used inside square brackets acquires a special meaning. This is the '-' (hyphen) character, which is used within a character class to indicate a range. For example, if we want to refer to a hexadecimal character, instead of defining the class [0123456767890abcdefABCDEF] we would use [0-9a-fA-F], which is much more convenient.

Let's see examples with some character classes:

![](http://www.sg.com.mx/images/stories/200705/programacion_x.gif)

Some programming languages define shortcuts for commonly used character classes. The following table shows some of the most common shortcuts:

![](http://www.sg.com.mx/images/stories/200705/programacion4.gif)

Delimitation
Parentheses can be used to define a subset within an expression. For example, to capture the hostname part of a url, I would use an expression like http://([^/]). What I am saying with this expression is that first I have the character sequence "http://" and followed by this I have a sub-expression, which I am delimiting with the parentheses, and I apply an expression to this specific segment, in this case I am looking for a string that matches any character except the '/'.
Alternatives
The metacharacter '|' (vertical bar) stands for "or". It allows you to search for different alternative expressions (or rather subexpressions), within a single expression.

That definition sounded very convoluted, so let's explain it with an example. Let's imagine that we have the expression Dona and the expression Don. Each is a separate expression, but if we define the expression Don|Doña then we have a single expression that matches either of the two subexpressions.

We can also use parentheses to delimit the scope of an alternative. In this case, the expression Do(n|ña) would give the same result as the expression Don|Doña. However, we must be careful with abusing the use of parentheses, because we can end up with expressions that are difficult to understand, and therefore to maintain.

Quantifiers or Multipliers
The metacharacters we have seen tell us if our pattern matches the string to be compared. But what if we want to compare with our string a pattern that can be zero, one or more times? For this we use a special kind of metacharacters: multipliers.

These metacharacters are applied to the character (or grouping) that precedes them, and indicate the number of times that element can be encountered for there to be an occurrence. The three quantifier metacharacters are '?' '*' '+'. The '?' indicates a multiplicity of 0 or 1, the '*' indicates a multiplicity of 0 to n, and the '+' indicates a multiplicity of 1 to n. The following examples make this clearer:

![](http://www.sg.com.mx/images/stories/200705/programacion5.gif)
It is also possible to indicate the exact multiplicity that is acceptable for a quantifier. The braces '{ }' are used for this, and the syntax is to first indicate the minimum value of the multiplicity, followed by a comma, and then the maximum value of the multiplicity.

![](http://www.sg.com.mx/images/stories/200705/programacion6.gif)
Conclusion
In this article we have studied the syntax and metacharacters used to define regular expressions. Now all that remains is for you to choose the programming language of your choice and start experimenting with the use of regular expressions. I guarantee it is a skill that will be of great use to you.

**References
- Anonymous author. "Regular Expressions.  
**www.ignside.net/man/php/regex.php**  
- Mike Malone. "The bare minimum that every programmer should know about regular expressions".  
**http://immike.net/blog**