---
title: Regex, the ultimate tool for string validation, parsing and matching!
slug: regex-the-ultimate-string-parser-and-matcher
date: 2023-06-26T09:05:14.000Z
tags: Beginner
ogImage: ./assets/images/2023/06/coderpad-regex-the-complete-guide.jpg
featured: false
draft: false
authors:
  - arduano
  - sebasptsch
tags:
  - Beginner
description:
  Placeholder description for imported post from Ghost Blog 
---
![Featured Image](./assets/images/2023/06/coderpad-regex-the-complete-guide.jpg)

During the most recent programming competition that we ran as part of UTS TechFest, there was a question that involved making sure a username matched a certain set of rules. The task was simple on paper: match usernames that have a first name, last name, then 3 digits (e.g. `JohnDoe123`).

Regular Expressions were devised at the same time as the first computers as people needed a way to match certain outputs with inputs. It's implemented in every major programming language as part of the standard libraries and is especially easy to use in scripted languages such as Python and JavaScript.

Without Regex (Regular Expressions), the problem becomes significantly more complicated with many nested logical comparisons with chained logical operators, if/or/and. Whilst regex itself may look complicated and confusing at first, once you've got the basic rules down it becomes a _little_ less foreign.

<!-- more -->

Examples
--------

A popular example of regex use is checking if an Email address is valid. You'll probably come across this on any site that uses email addresses for login and registration. Here is an example expression that would match emails:

`^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$`

RegExr: Learn, Build, & Test RegEx

RegExr is an online tool to learn, build, & test Regular Expressions (RegEx / RegExp).

https://regexr.com/3e48o

Tip: you can play around with the text in the above website, and it highlights the matched text.

Another example of an effective application of regex would be the "Bot Problem" question from the previous programming competition, with the appropriate expression being the following:

`^[A-Z][a-z]+[A-Z][a-z]+[0-9]{3}$`

https://regexr.com/7g1t7

Although explaining all of regex in one post would be nearly impossible, we'll explain the basics, including how the bot problem regex works.

Regex tokens
------------

There are many "tokens" in regex, which tell the regex engine what kind of text can be matched. Let's start with the basics:

Most normal characters in regex get matched exactly as they are. If your regular expression is just `ge`, then if you input the string `regex` it would match the `re[ge]x`.

### Repetition

You can program repetition in regex using the following tokens:

The star token `*` means "repeat the previous item zero or more times". So `ab*` would match `a` or `ab` or `abbbbbbb` and so on. It wouldn't match things like just `b` because an "a" is still required.

The plus token `+` does the same as star, but instead, it's one or more times. So `ab+` would do the same as above, except `a` wouldn't be matched.

Curly braces can set a constant repetition count, such as `{3}` (repeat 3 times) or `{3,6}` (repeat between 3 and 6 times). So for example, `a{3}b{1-3}` would match `aaab` or `aaabb` or `aaabbb`.

### Character sets

Instead of writing out the characters manually, you can use character sets to match many kinds of characters at once.

The period `.` matches any character whatsoever. So `a.b` would match `aab` or `a5b` or `a b` or `aжb` if Unicode is enabled, and so on.

It's also possible to create your own character sets with square brackets. `[abc]` would match either `a`, `b` or `c`. It's possible to negate a character set using `^`, where `[^abc]` would match everything BUT a/b/c. You can also do character ranges using `-`, for example `[a-z]` would match all lowercase characters, `[A-Z]` would match all uppercase characters. You can have multiple ranges and multiple characters in the character sets, for example `[a-zA-Z]` would match all lowercase and uppercase characters, and `[a-zA-Z123]` would match the same but also the characters `1`, `2` and `3`.

However, typing these out can be fairly tedious, so there's many shorthand character sets, e.g. `\w` would match any "word" character, `\d` matches any digit (0-9), `\s` matches any whitespace, and so on.

### Other tokens

There are other important tokens to know, starting with the parentheses (also called "groups"). Parentheses allow us to group a sub-expression, and re-use it. So, for example, `foo(bar)+` would match `foobar` and `foobarbar` and `foobarbarbar` and so on.

Another important token is the pipe `|` (also known as "or" or "choice"). It chooses between the left or the right item. So `a|b` would match either `a` or `b`.

Pipes and groups work really well together, where for example: `(a+)|(b+)` would match either `aaaaaa` or `bbbbbb` but not `abababa`.

There's also the question mark `?` which says the item before it is optional. So `abc?` would match `ab` and `abc`.

### Anchors

Anchor tokens are a special kind of token that don't match actual characters, but instead match the context. The two most popular anchors are "line start" `^` and "line end" `$` which match the start/end of a line. Most regex implementations find matches _within_ a string rather than trying to match the entire string, and those characters help with controlling that. So, for example for the string `regex is useful`, `\w+` would match `[regex] [is] [useful]`, creating 3 separate matches. However, `^\w+` would only match `[regex] is useful` as only the first word starts at the beginning of the line, and conversely `\w+$` would match `regex is [useful]`.

Bringing it all together
------------------------

So let's say we want to match a string that has 2 names (one uppercase character followed by one or more lowercase characters), and then 3 digits. We can use character sets to define uppercase characters `[A-Z]` and lowercase characters `[a-z]` and digits `[0-9]`. A name would look like: `[A-Z][a-z]+`, because we only want one uppercase, and one or more lowercase. We want 3 digits, so we could do `[0-9]{3}`. Also, we want to make sure that we match the beginning/end of each line correctly too, so for example `fooJohnDoe123456` won't be matched just because it contains `JohnDoe123` inside.

Putting it all together, we get:

`^[A-Z][a-z]+[A-Z][a-z]+[0-9]{3}$`

Now there's multiple ways we can change this around. For example, the name part repeats twice, so we could do something like:

`^([A-Z][a-z]+){2}[0-9]{3}$`

Putting the name into a group, and making it repeat twice. We can also replace `[0-9]` with `\d` because they're the same thing, leaving us with:

`^([A-Z][a-z]+){2}\d{3}$`

But yeah at this point it's up to personal preference, I just hope that this was a descriptive example.

If you have any questions about regex or about this post, feel free to ask in our Discord server!
