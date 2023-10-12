### Doctypes
Because there have been several versions of HTML, each web page should begin with a DOCTYPE declaration to tell a browser which version of HTML the page is using (although browsers usually display the page even if it is not included). We will therefore be including one in each example for the rest of the book.
- HTML5:`<!DOCTYPE html>`

### ID Attribute
Every HTML element can carry the `id` attribute. It is used to uniquely identify that element from other elements on the page. Its value should start with a letter or an underscore (not a number or any other character). It is important that no two elements on the same page have the same value for their id attributes (otherwise the value is no longer unique).

The id attribute is known as a global attribute because it can be used on any element.

### Class Attribute

```html
<p class="important">For a one-year period from 
 November 2010, the Marugame Genichiro-Inokuma 
 Museum of Contemporary Art (MIMOCA) will host a 
 cycle of four Hiroshi Sugimoto exhibitions.</p>
<p>Each will showcase works by the artist 
 thematically contextualized under the headings 
 "Science," "Architecture," "History" and 
 "Religion" so as to present a comprehensive 
 panorama of the artist's oeuvre.</p>
<p class="important admittance">Hours: 10:00 – 18:00 
 (No admittance after 17:30)</p>
```

Every HTML element can also carry a class attribute. Sometimes, rather than uniquely identifying one element within a document, you will want a way to identify several elements as being different from the other elements on the page. For example, you might have some paragraphs of text that contain information that is more important than others and want to distinguish these elements, or you might want to differentiate between links that point to other pages on your own site and links that point to external sites. 

To do this you can use the class attribute. Its value should describe the class it belongs to. In the example on the left, key paragraphs have a class attribute whose value is important. The class attribute on any element can share the same value. So, in this example, the value of important could be used on headings and links, too.

### Grouping Text & Elements in a Block

The `<div>` element allows you to group a set of elements together in one block-level box.

For example, you might create a `<div>` element to contain all of the elements for the header of your site (the logo and the navigation), or you might create a `<div>` element to contain comments from visitors.
```html
<div id="header">
 <img src="images/logo.gif" alt="Anish Kapoor" />
 <ul>
 <li><a href="index.html">Home</a></li>
 <li><a href="biography.html">Biography</a></li>
 <li><a href="works.html">Works</a></li>
 <li><a href="contact.html">Contact</a></li>
 </ul>
</div><!-- end of header -->
```
In a browser, the contents of the `<div>` element will start on a new line, but other than this it will make no difference to the presentation of the page.

Using an `id` or `class` attribute on the `<div>` element, however, means that you can create CSS style rules to indicate how much space the `<div>` element should occupy on the screen and change the appearance of all the elements contained within it. It can also make it easier to follow your code if you have used `<div>` elements to hold each section of the page.

### Grouping Text & Elements Inline

```html
<p>Anish Kapoor won the Turner Prize in 1991 and 
 exhibited at the <span class="gallery">Tate 
 Modern</span> gallery in London in 2003.</p>
```

The `<span>` element acts like an inline equivalent of the `<div>` element. It is used to either:
1. Contain a section of text where there is no other suitable element to differentiate it from its surrounding text
2. Contain a number of inline elements

The most common reason why people use `<span>` elements is so that they can control the appearance of the content of these elements using CSS.

You will usually see that a class or id attribute is used with `<span>` elements:
- To explain the purpose of this `<span>` element 
- So that CSS styles can be applied to elements that have specific values for these attributes 

### Iframes
```html
<iframe 
 width="450" 
 height="350" 
 src="http://maps.google.co.uk/maps?q=moma+new+york
 &amp;output=embed">
</iframe>
```

An iframe is like a little window that has been cut into your page — and in that window you can see another page. The term iframe is an abbreviation of _inline frame_.

One common use of iframes (that you may have seen on various websites) is to embed a Google Map into a page. The content of the iframe can be any html page (either located on the same server or anywhere else on the web).

An iframe is created using the `<iframe>` element. There are a few attributes that you will need to know to use it:

## Information about Your Pages

The `<meta>` element lives inside the `<head>` element and contains information about that web page.

It is _not visible to users_ but fulfills a number of purposes such as telling search engines about your page, who created it, and whether or not it is time sensitive. (If the page is time sensitive, it can be set to expire.)

The `<meta>` element is an empty element so it _does not have a closing tag_. It uses attributes to carry the information.

The most common attributes are the `name` and `content` attributes, which tend to be used together. These attributes specify properties of the entire page. The value of the name attribute is the property you are setting, and the value of the content attribute is the value that you want to give to this property.

In the first line of the example, you can see a `<meta>` element where the name attribute indicates an intention to specify a description for the page. The content attribute is where this description is actually specified.

```html
<!DOCTYPE html>
<html>
 <head>
 <title>Information About Your Pages</title>
 <meta name="description" content="An Essay on Installation Art" />
 <meta name="keywords" content="installation, art, opinion" />
 <meta name="robots" content="nofollow" />
 <meta http-equiv="author" content="Jon Duckett" />
 <meta http-equiv="pragma" content="no-cache" />
 <meta http-equiv="expires" content="Fri, 04 Apr 2014 23:59:59 GMT" />
 </head>
 <body>
 </body>
</html>
```


- `keywords`: This contains a list of comma-separated words that a user might search on to find the page. _In practice, this no longer has any noticeable effect on how search engines index your site_. 
- `robots`: This indicates whether search engines should add this page to their search results or not. A value of `noindex` can be used if this page should not be added. A value of `nofollow` can be used if search engines should add this page in their results but not any pages that it links to.

The `<meta>` element also uses the `http-equiv` and content attributes in pairs. In our example, you can see three instances of the `http-equiv` attribute. Each one has a different purpose:
- `pragma`: This prevents the browser from caching the page. (That is, storing it locally to save time downloading it on subsequent visits.)
- `expires`: Because browsers often cache the content of a page, the expires option can be used to indicate when the page should expire (and no longer be cached). Note that the date must be specified in the format shown.