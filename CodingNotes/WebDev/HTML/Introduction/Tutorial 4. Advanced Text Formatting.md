# Description lists

In HTML text fundamentals, we walked through how to mark up basic lists in HTML, but we didn't mention the third type of list you'll occasionally come across — **description lists**. The purpose of these lists is to mark up a set of items and their associated descriptions, such as terms and definitions, or questions and answers. 

Description lists use a different wrapper than the other list types — `<dl>`; in addition each term is wrapped in a `<dt>` (description term) element, and each description is wrapped in a `<dd>` (description definition) element.

## Description list example

Let's finish marking up our example:

```html
<dl>
  <dt>soliloquy</dt>
  <dd>
    In drama, where a character speaks to themselves, representing their inner
    thoughts or feelings and in the process relaying them to the audience (but
    not to other characters.)
  </dd>
  <dt>monologue</dt>
  <dd>
    In drama, where a character speaks their thoughts out loud to share them
    with the audience and any other characters present.
  </dd>
  <dt>aside</dt>
  <dd>
    In drama, where a character shares a comment only with the audience for
    humorous or dramatic effect. This is usually a feeling, thought, or piece of
    additional background information.
  </dd>
</dl>
```

The browser default styles will display description lists with the descriptions indented somewhat from the terms.

## Multiple descriptions for one term

Note that it is permitted to have a single term with multiple descriptions, for example:

```html
<dl>
  <dt>aside</dt>
  <dd>
    In drama, where a character shares a comment only with the audience for
    humorous or dramatic effect. This is usually a feeling, thought, or piece of
    additional background information.
  </dd>
  <dd>
    In writing, a section of content that is related to the current topic, but
    doesn't fit directly into the main flow of content so is presented nearby
    (often in a box off to the side.)
  </dd>
</dl>
```

# Quotations

HTML also has features available for marking up quotations; which element you use depends on whether you are marking up a block or inline quotation.

## Blockquotes

If a section of block level content (be it a paragraph, multiple paragraphs, a list, etc.) is quoted from somewhere else, you should wrap it inside a `<blockquote>` element to signify this, and include a URL pointing to the source of the quote inside a `cite` attribute. For example, the following markup is taken from the MDN `<blockquote>` element page:

```html
<p>
  The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or
  <em>HTML Block Quotation Element</em>) indicates that the enclosed text is an
  extended quotation.
</p>
```

To turn this into a block quote, we would just do this:

```html
<p>Here is a blockquote:</p>
<blockquote
  cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
  <p>
    The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or
    <em>HTML Block Quotation Element</em>) indicates that the enclosed text is
    an extended quotation.
  </p>
</blockquote>
```

Browser default styling will render this as an indented paragraph, as an indicator that it is a quote; the paragraph above the quotation is there to demonstrate that.

## Inline quotations

Inline quotations work in exactly the same way, except that they use the `<q>` element. For example, the below bit of markup contains a quotation from the MDN `<q>` page:

```html
<p>
  The quote element — <code>&lt;q&gt;</code> — is
  <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">
    intended for short quotations that don't require paragraph breaks.
  </q>
</p>
```

Browser default styling will render this as normal text put in quotes to indicate a quotation.

## Citations

The content of the `cite` attribute sounds useful, but unfortunately browsers, screen readers, etc. don't really do much with it. There is no way to get the browser to display the contents of `cite`, without writing your own solution using JavaScript or CSS. If you want to make the source of the quotation available on the page you need to make it available in the text via a link or some other appropriate way.

There is a `<cite>` element, but this is meant to contain the title of the resource being quoted, e.g. the name of the book. There is no reason, however, why you couldn't link the text inside `<cite>` to the quote source in some way:

```html
<p>
  According to the
  <a href="/en-US/docs/Web/HTML/Element/blockquote">
    <cite>MDN blockquote page</cite></a>:
</p>

<blockquote
  cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
  <p>
    The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or
    <em>HTML Block Quotation Element</em>) indicates that the enclosed text is
    an extended quotation.
  </p>
</blockquote>

<p>
  The quote element — <code>&lt;q&gt;</code> — is
  <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">
    intended for short quotations that don't require paragraph breaks.
  </q>
  — <a href="/en-US/docs/Web/HTML/Element/q"><cite>MDN q page</cite></a>.
</p>
```
Citations are styled in italic font by default.

# Abbreviations

Another fairly common element you'll meet when looking around the Web is `<abbr>` — this is used to wrap around an abbreviation or acronym. When including either, provide a full expansion of the term in plain text on first use, along with the `<abbr>` to mark up the abbreviation. This provides a hint to user agents on how to announce/display the content while informing all users what the abbreviation means.

If providing the expansion in addition to the abbreviation makes little sense, and the abbreviation or acronym is a fairly shortened term, provide the full expansion of the term as the value of `title` attribute:

## Abbreviation example

Let's look at an example.

```html
<p>
  We use <abbr>HTML</abbr>, Hypertext Markup Language, to structure our web
  documents.
</p>

<p>
  I think <abbr title="Reverend">Rev.</abbr> Green did it in the kitchen with
  the chainsaw.
</p>
```

These will come out looking something like this:

> **Note:** Earlier versions of html also included support for the `<acronym>` element, but it was removed from the HTML spec in favor of using `<abbr>` to represent both abbreviations and acronyms. `<acronym>` should not be used.


# Marking up contact details

HTML has an element for marking up contact details — `<address>`. This wraps around your contact details, for example:

```html
<address>Chris Mills, Manchester, The Grim North, UK</address>
```

It could also include more complex markup, and other forms of contact information, for example:

```html
<address>
  <p>
    Chris Mills<br />
    Manchester<br />
    The Grim North<br />
    UK
  </p>

  <ul>
    <li>Tel: 01234 567 890</li>
    <li>Email: me@grim-north.co.uk</li>
  </ul>
</address>
```

Note that something like this would also be OK, if the linked page contained the contact information:

```html
<address>
  Page written by <a href="../authors/chris-mills/">Chris Mills</a>.
</address>
```

>**Note:** The `<address>` element should only be used to provide contact information for the document contained with the nearest `<article>` or `<body>` element. It would be correct to use it in the footer of a site to include the contact information of the entire site, or inside an article for the contact details of the author, but not to mark up a list of addresses unrelated to the content of that page.

# Superscript and subscript

You will occasionally need to use superscript and subscript when marking up items like dates, chemical formulae, and mathematical equations so they have the correct meaning. The `<sup>` and `<sub>` elements handle this job. For example:

```html
<p>My birthday is on the 25<sup>th</sup> of May 2001.</p>
<p>
  Caffeine's chemical formula is
  C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>.
</p>
<p>If x<sup>2</sup> is 9, x must equal 3 or -3.</p>
```

# Representing computer code

There are a number of elements available for marking up computer code using HTML:

- `<code>`: For marking up generic pieces of computer code.
- `<pre>`: For retaining whitespace (generally code blocks) — if you use indentation or excess whitespace inside your text, browsers will ignore it and you will not see it on your rendered page. If you wrap the text in `<pre></pre>` tags however, your whitespace will be rendered identically to how you see it in your text editor.
- `<var>`: For specifically marking up variable names.
- `<kbd>`: For marking up keyboard (and other types of) input entered into the computer.
- `<samp>`: For marking up the output of a computer program.

>**Note**: The difference between code, sampl, and kbd is the semantic meaning. The default rendering is to use a monospace typeface because that's the most appropriate.
>- `<kbd>` represents keyboard input, though StackOverflow renders it like real keys.
>- `<samp>` represents sample computer output, and originally computers were monospaced :)
>- `<code>` represents programming code input, and the vast majority of programming languages are designed to assume a monospaced editor font - excepting C++'s book which prefers variable-width, for some reason, and some breeds of Python. Note that `<code>` is an inline element, whereas `<pre>` is used for block-level markup (i.e. paragraphs) of code.

Let's look at a few examples. You should try having a play with these (try grabbing a copy of our [other-semantics.html](https://github.com/mdn/learning-area/blob/main/html/introduction-to-html/advanced-text-formatting/other-semantics.html) sample file):

```html
<pre><code>const para = document.querySelector('p');

para.onclick = function() {
  alert('Owww, stop poking me!');
}</code></pre>

<p>
  You shouldn't use presentational elements like <code>&lt;font&gt;</code> and
  <code>&lt;center&gt;</code>.
</p>

<p>
  In the above JavaScript example, <var>para</var> represents a paragraph
  element.
</p>

<p>Select all the text with <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>A</kbd>.</p>

<pre>$ <kbd>ping mozilla.org</kbd>
<samp>PING mozilla.org (63.245.215.20): 56 data bytes
64 bytes from 63.245.215.20: icmp_seq=0 ttl=40 time=158.233 ms</samp></pre>
```

# Marking up times and dates

HTML also provides the `<time>` element for marking up times and dates in a machine-readable format. For example:

```html
<time datetime="2016-01-20">20 January 2016</time>
```

Why is this useful? Well, there are many different ways that humans write down dates. The above date could be written as:
- 20 January 2016
- 20th January 2016
- Jan 20 2016
- 20/01/16
- 01/20/16
- The 20th of next month
- 20e Janvier 2016
- 2016 年 1 月 20 日
- And so on

But these different forms cannot be easily recognized by computers — what if you wanted to automatically grab the dates of all events in a page and insert them into a calendar? The `<time>` element allows you to attach an unambiguous, machine-readable time/date for this purpose.

The basic example above just provides a simple machine readable date, but there are many other options that are possible, for example:

```html
<!-- Standard simple date -->
<time datetime="2016-01-20">20 January 2016</time>
<!-- Just year and month -->
<time datetime="2016-01">January 2016</time>
<!-- Just month and day -->
<time datetime="01-20">20 January</time>
<!-- Just time, hours and minutes -->
<time datetime="19:30">19:30</time>
<!-- You can do seconds and milliseconds too! -->
<time datetime="19:30:01.856">19:30:01.856</time>
<!-- Date and time -->
<time datetime="2016-01-20T19:30">7.30pm, 20 January 2016</time>
<!-- Date and time with timezone offset -->
<time datetime="2016-01-20T19:30+01:00">
  7.30pm, 20 January 2016 is 8.30pm in France
</time>
<!-- Calling out a specific week number -->
<time datetime="2016-W04">The fourth week of 2016</time>
```
