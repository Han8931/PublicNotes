# Basic sections of a document

Webpages can and will look pretty different from one another, but they all tend to share similar standard components, unless the page is displaying a fullscreen video or game, is part of some kind of art project, or is just badly structured:

### Header:
Usually a big strip across the top with a big heading, logo, and perhaps a tagline. This usually stays the same from one webpage to another.

### Navigation bar:
Links to the site's main sections; usually represented by menu buttons, links, or tabs. Like the header, this content usually remains consistent from one webpage to another — having inconsistent navigation on your website will just lead to confused, frustrated users. Many web designers consider the navigation bar to be part of the header rather than an individual component, but that's not a requirement; in fact, some also argue that having the two separate is better for [accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility), as screen readers can read the two features better if they are separate.

### Main content:
A big area in the center that contains most of the unique content of a given webpage, for example, the video you want to watch, or the main story you're reading, or the map you want to view, or the news headlines, etc. This is the one part of the website that definitely will vary from page to page!

### Sidebar:
Some peripheral info, links, quotes, ads, etc. Usually, this is contextual to what is contained in the main content (for example on a news article page, the sidebar might contain the author's bio, or links to related articles) but there are also cases where you'll find some recurring elements like a secondary navigation system.

### Footer:
A strip across the bottom of the page that generally contains fine print, copyright notices, or contact info. It's a place to put common information (like the header) but usually, that information is not critical or secondary to the website itself. The footer is also sometimes used for SEO purposes, by providing links for quick access to popular content.

A "typical website" could be structured something like this:

<img src="https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure/sample-website.png" alt="a simple website structure example featuring a main heading, navigation menu, main content, side bar, and footer." width=40%>

> **Note:** The image above illustrates the main sections of a document, which you can define with HTML. However, the _appearance_ of the page shown here - including the layout, colors, and fonts - is achieved by applying CSS to the HTML. In this module we're not teaching CSS, but once you have an understanding of the basics of HTML, try diving into our CSS first steps module to start learning how to style your site.

# HTML for structuring content

The simple example shown above isn't pretty, but it is perfectly fine for illustrating a typical website layout example. Some websites have more columns, some are a lot more complex, but you get the idea. With the right CSS, you could use pretty much any elements to wrap around the different sections and get it looking how you wanted, but as discussed before, we need to respect semantics and **use the right element for the right job**.

_This is because visuals don't tell the whole story_. We use color and font size to draw sighted users' attention to the most useful parts of the content, like the navigation menu and related links, but what about visually impaired people for example, who might not find concepts like "pink" and "large font" very useful?

> **Note:** [Roughly 8% of men and 0.5% of women](https://www.color-blindness.com/) are colorblind; or, to put it another way, approximately 1 in every 12 men and 1 in every 200 women. Blind and visually impaired people represent roughly 4-5% of the world population (in 2015 there were [940 million people with some degree of vision loss](https://en.wikipedia.org/wiki/Visual_impairment), while the total population was [around 7.5 billion](https://en.wikipedia.org/wiki/World_human_population#/media/File:World_population_history.svg)).

In your HTML code, you can mark up sections of content based on their _functionality_ — you can use elements that represent the sections of content described above unambiguously, and assistive technologies like screen readers can recognize those elements and help with tasks like "find the main navigation", or "find the main content." As we mentioned earlier in the course, there are a number of [consequences of not using the right element structure and semantics for the right job](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#why_do_we_need_structure).

To implement such semantic mark up, HTML provides dedicated tags that you can use to represent such sections, for example:
-   **header:** [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header).
-   **navigation bar:** [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav).
-   **main content:** [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main), with various content subsections represented by [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article), [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section), and [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) elements.
-   **sidebar:** [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside); often placed inside [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main).
-   **footer:** [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer).

# HTML layout elements in more detail

It's good to understand the overall meaning of all the HTML sectioning elements in detail — this is something you'll work on gradually as you start to get more experience with web development. You can find a lot of detail by reading our [HTML element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). For now, these are the main definitions that you should try to understand:

- `<main>` is for content _unique to this page._ Use `<main>` only _once_ per page, and put it directly inside `<body>`. Ideally this shouldn't be nested within other elements.
- `<article>` encloses a block of related content that makes sense on its own without the rest of the page (e.g., a single blog post).
- `<section>` is similar to `<article>`, but it is more for grouping together a single part of the page that constitutes one single piece of functionality (e.g., a mini map, or a set of article headlines and summaries), or a theme. It's considered best practice to begin each section with a heading; also note that you can break `<article>`s up into different `<section>`s, or `<section>`s up into different `<article>`s, depending on the context.
- `<aside>` contains content that is not directly related to the main content but can provide additional information indirectly related to it (glossary entries, author biography, related links, etc.).
- `<header>` represents a group of introductory content. If it is a child of `<body>` it defines the global header of a webpage, but if it's a child of an `<article>` or `<section>` it defines a specific header for that section (try not to confuse this with titles and headings).
- `<nav>` contains the main navigation functionality for the page. Secondary links, etc., would not go in the navigation.
- `<footer>` represents a group of end content for a page.

Each of the aforementioned elements can be clicked on to read the corresponding article in the "HTML element reference" section, providing more detail about each one.

## Non-semantic wrappers

Sometimes you'll come across a situation where you can't find an ideal semantic element to group some items together or wrap some content. Sometimes you might want to just group a set of elements together to affect them all as a single entity with some CSS or JavaScript. For cases like these, HTML provides the `<div>` and `<span>` elements. You should use these preferably with a suitable `class` attribute, to provide some kind of label for them so they can be easily targeted. 

`<span>` is an inline non-semantic element, which you should only use if you can't think of a better semantic text element to wrap your content, or don't want to add any specific meaning. For example:

```html
<p>
  The King walked drunkenly back to his room at 01:00, the beer doing nothing to
  aid him as he staggered through the door.
  <span class="editor-note">
    [Editor's note: At this point in the play, the lights should be down low].
  </span>
</p>
```

> The **`<span>`** element is a generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#class) or [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#id) attributes), or because they share attribute values, such as [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#lang). It should be used only when no other semantic element is appropriate. `<span>` is very much like a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) element, but [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) is a [block-level element](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content).

In this case, the editor's note is supposed to merely provide extra direction for the director of the play; it is not supposed to have extra semantic meaning. For sighted users, CSS would perhaps be used to distance the note slightly from the main text. 

`<div>` is a block level non-semantic element, which you should only use if you can't think of a better semantic block element to use, or don't want to add any specific meaning. For example, imagine a shopping cart widget that you could choose to pull up at any point during your time on an e-commerce site:

```html
<div class="shopping-cart">
  <h2>Shopping cart</h2>
  <ul>
    <li>
      <p>
        <a href=""><strong>Silver earrings</strong></a>: $99.95.
      </p>
      <img src="../products/3333-0985/thumb.png" alt="Silver earrings" />
    </li>
    <li>…</li>
  </ul>
  <p>Total cost: $237.89</p>
</div>
```

> The **`<div>`**  element is the generic container for flow content. It has no effect on the content or layout until styled in some way using [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS) (e.g. styling is directly applied to it, or some kind of layout model like [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout) is applied to its parent element). As a "pure" container, the `<div>` element does not inherently represent anything. Instead, it's used to group content so it can be easily styled using the [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#class) or [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#id) attributes, marking a section of a document as being written in a different language (using the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#lang) attribute), and so on.

This isn't really an `<aside>`, as it doesn't necessarily relate to the main content of the page (you want it viewable from anywhere). It doesn't even particularly warrant using a `<section>`, as it isn't part of the main content of the page. So a `<div>` is fine in this case. We've included a heading as a signpost to aid screen reader users in finding it.

> **Warning:** Divs are so convenient to use that it's easy to use them too much. As they carry no semantic value, they just clutter your HTML code. Take care to use them only when there is no better semantic solution and try to reduce their usage to the minimum otherwise you'll have a hard time updating and maintaining your documents.

## Line breaks and horizontal rules

Two elements that you'll use occasionally and will want to know about are `<br>` and `<hr>`.

### \<br\>: the line break element

`<br>` creates a line break in a paragraph; it is the only way to force a rigid structure in a situation where you want a series of fixed short lines, such as in a postal address or a poem. For example:

```html
<p>
  There once was a man named O'Dell<br />
  Who loved to write HTML<br />
  But his structure was bad, his semantics were sad<br />
  and his markup didn't read very well.
</p>
```

Without the `<br>` elements, the paragraph would just be rendered in one long line (as we said earlier in the course, [HTML ignores most whitespace](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#whitespace_in_html)); with `<br>` elements in the code, the markup renders like this:

### \<hr\>: the thematic break element

`<hr>` elements create a horizontal rule in the document that denotes a thematic change in the text (such as a change in topic or scene). Visually _it just looks like a horizontal line_. As an example:

```html
<p>
  Ron was backed into a corner by the marauding netherbeasts. Scared, but
  determined to protect his friends, he raised his wand and prepared to do
  battle, hoping that his distress call had made it through.
</p>
<hr />
<p>
  Meanwhile, Harry was sitting at home, staring at his royalty statement and
  pondering when the next spin off series would come out, when an enchanted
  distress letter flew through his window and landed in his lap. He read it
  hazily and sighed; "better get back to work then", he mused.
</p>
```

