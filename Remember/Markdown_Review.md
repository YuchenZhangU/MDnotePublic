[TOC]



# This is an h1

## This is an h2
###### This is an h6


> This is a blockquote with one paragraphs
>
> This is the second paragraph

> This is another bloackquote with one paragraph


# Block Elements
## un-ordered list
* Red
* Green
* Blue

## ordered list
1. Red
2. Green
3. Blue

## Task List

- [ ] normal **formatting**, @mentions, #1234 refs
- [ ] incomplete
- [x] completed

## (Fenced) Code Blocks

Here's an example:

```
function test() {
  console.log("notice the blank line before this function?");
}
```

syntax highlighting

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```


## Math Blocks - MathJax (used in LaTeX)

$$
\mathbf{V}_1 \times \mathbf{V}_2 = 
$$


## Table

| First Header | Second Header |
| :----------: | :-----------: |
| Content Cell | Content Cell  |




## Footnotes

You can create footnotes like this [^footnote]

[^footnote]: Here is the *text* of the **footnote**



## Horizontal Rules

---

or 

***

## YAML Front Matters





# Span Elements


## Links

### Inline Link

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

[To Span](#Block_Elements)



### Reference Link

This is [an example][id] reference-style link.

Then, anywhere in the document, you define your link label like this, on a line by itself:

[id]: http://example.com/ "Optional Title Here"



**implicit link name**

[Google][]

And then define the link

[Google]: http://google.com/



## URLs



<i@typora.io>
<i@www.utulsa.edu>







## Images

![Alt Text](http://lorempixel.com/400/200/animals "Optional Title")


> You may specify a url prefix for image preview in local computer with property `typora-root-url` in YAML Front Matters. Input `typora-root-url:/User/Abner/Website/typora.io/` in YAML Front Matters, and then `![alt](/blog/img/test.png)` will be treated as `![alt](file:///User/Abner/Website/typora.io/blog/img/test.png)` in typora.









### Emphasis

#### <em>

*single asterisks*

_single underscores_



\*this is text surrounded by literal asterisks\*



### Strong

#### <stong>

**double asterisks**

__double underscores__



### Code

Use the `printf()` function.



### Strikethrough

~~Mistaken texts.~~



### Underline

<u>Underline</u>





### Emoji :happy:



### Inline Maths

$\lim_{x \to \infty} \exp(-x) = 0$



### Subscripte

H~2~0

### Superscipt

X^2^



### Highlight

==highlight==









