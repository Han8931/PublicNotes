---
tags: css, web
---

**[CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)** (Cascading Style Sheets) allows you to create great-looking web pages, but how does it work under the hood? This article explains what CSS is with a simple syntax example and also covers some key terms about the language.

# What is CSS for?

As we have mentioned before, CSS is a language for specifying how documents are presented to users — how they are styled, laid out, etc.

A **document** is usually a text file structured using a markup language — [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML) is the most common markup language, but you may also come across other markup languages such as [SVG](https://developer.mozilla.org/en-US/docs/Glossary/SVG) or [XML](https://developer.mozilla.org/en-US/docs/Glossary/XML).

**Presenting** a document to a user means converting it into a form usable by your audience. [Browsers](https://developer.mozilla.org/en-US/docs/Glossary/Browser), like [Firefox](https://developer.mozilla.org/en-US/docs/Glossary/Mozilla_Firefox), [Chrome](https://developer.mozilla.org/en-US/docs/Glossary/Google_Chrome), or [Edge](https://developer.mozilla.org/en-US/docs/Glossary/Microsoft_Edge), are designed to present documents visually, for example, on a computer screen, projector, or printer.

>**Note:** A browser is sometimes called a [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent), which basically means a computer program that represents a person inside a computer system. Browsers are the main type of user agents we think of when talking about CSS, however, they are not the only ones. There are other user agents available, such as those that convert HTML and CSS documents into PDFs to be printed.

CSS can be used for very basic document text styling — for example, for changing the [color](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) and [size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) of headings and links. It can be used to create a layout — for example, [turning a single column of text into a layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Column_layouts) with a main content area and a sidebar for related information. It can even be used for effects such as [animation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations). Have a look at the links in this paragraph for specific examples.

# CSS syntax

CSS is a rule-based language — you define the rules by specifying groups of styles that should be applied to particular elements or groups of elements on your web page.

For example, you can decide to have the main heading on your page to be shown as large red text. The following code shows a very simple CSS rule that would achieve the styling described above:

```css
h1 {
  color: red;
  font-size: 5em;
}
```

- In the above example, the CSS rule opens with a [selector](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Selector). This _selects_ the HTML element that we are going to style. In this case, we are styling level one headings (`h1`).
- We then have a set of curly braces `{ }`.
- Inside the braces will be one or more **declarations**, which take the form of **property** and **value** pairs. We specify the property (`color` in the above example) before the colon, and we specify the value of the property after the colon (`red` in this example).
- This example contains two declarations, one for `color` and the other for `font-size`. Each pair specifies a property of the element(s) we are selecting (`h1` in this case), then a value that we'd like to give the property.

CSS [properties](https://developer.mozilla.org/en-US/docs/Glossary/Property/CSS) have different allowable values, depending on which property is being specified. In our example, we have the `color` property, which can take various [color values](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#color). We also have the `font-size` property. This property can take various [size units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#numbers_lengths_and_percentages) as a value.

A CSS stylesheet will contain many such rules, written one after the other.

```css
h1 {
  color: red;
  font-size: 5em;
}

p {
  color: black;
}
```

You will find that you quickly learn some values, whereas others you will need to look up. The individual property pages on MDN give you a quick way to look up properties and their values when you forget or when you want to know what else you can use as a value.

>**Note:** You can find links to all the CSS property pages (along with other CSS features) listed on the MDN [CSS reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference). Alternatively, you should get used to searching for "mdn _css-feature-name_" in your favorite search engine whenever you need to find out more information about a CSS feature. For example, try searching for "mdn color" and "mdn font-size"!
