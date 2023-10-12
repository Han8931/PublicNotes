---
tags: web, html
---
- HTML (HyperText Markup Language)
```html
<!DOCTYPE html>
<html lang="en">
		<head>
				<title> The Han's Blog</title>
				<link rel='stylesheet' type='text/css' href='style.css'>
				<meta charset="utf-8"/>
		</head>

		<body>

		<h1>Han's Blog</h1>

		<img src="dir/some.img" alt="Han", title="This is Han">

		<p>This is a sentence</p>
		<p>Check out <a href="another.html">this</a> other page. </p>

		<h2>Sub-Heading</h2>

		<p>Here is another paragraph</p>

		<p>Let's format <b> gold text</b> or <i>italic</i> or <u>underlined text</u><p>

		<ol>
				<li> Here is an ordered list of items. </li>
				<li> Here is a list of items. </li>
				<li> Here is a list of items. </li>
				<li> Here is a list of items. </li>
		</ol>

		<ul>
				<li> Here is an unordered list of items. </li>
				<li> Here is a list of items. </li>
				<li> Here is a list of items. </li>
				<li> Here is a list of items. </li>
				<ul>
						<li> Here is a list of items. </li>
						<li> Here is a list of items. </li>
						<li> Here is a list of items. </li>
						<li> Here is a list of items. </li>
				</ul>
		</ul>

		<h3>Sub-Sub-Heading</h3>

		<p>Here is the <strong> strong</strong> tag with a line break <br /> and the  <em>emphatic</em> tag.<p>

		<p>Here is another paragraph</p>
		<h1>Another Heading</h1>

		</body>
</html>

```

## Tags

- Tags: angled brackets
- `<br>` : Line break. 
- `<p style="margin-top: 40px;"> <\p>`: paragraph with style (CSS)
- `<img src="/web1/img.jpg" width="100%">`: load an image
	- Attribute: src, width
	- CSS is used
- List
```html
<ul> 
	<li>1. HTML</li>
	<li>2. CSS</li>
	<li>3. JavaScript</li>
</ul>
<ol>
	<li>HTML</li>
	<li>CSS</li>
	<li>JavaScript</li>
</ol>
```

- A `<span>` element which is used to color a part of a text: 
	- `<p>My mother has <span style="color:blue">blue</span> eyes.</p>`


## Title, Meta, Head, Body, and HTML 

```html
<title>WEB1- HTML</title>
<meta charset="utf-8>" 
```
- `title`: title of a html file
- `meta`: tells web how to read your html file. 
	- utf-8
- `head`: wrap the above tags
- `body`: main context
- `html`: wrap head and body.

## Anchor
- `<a href="www.w3.org">Hypertext Markup Language (HTML)</a>` : link (anchor)
- `<a href="www.w3.org" target="_blank" title="HTML5 Spec">Hypertext Markup Language (HTML)</a>` : link (anchor)
	- `_blank`: open in a new tab
	- `title`: display extra info about the link when you put your cursor on the link
- LInk to other contexts:
	- Link ordered list to some contents
```html
<h1><a href="index.html">WEB</a></h1>

<ol>
	<li><a href="1.html">HTML</a></li>
	<li><a href="2.html">CSS</a></li>
</ol>
```


## GET & POST
- HTML `form` defines a way of communicating with a server. 
	- `GET` is a way of getting information
	- `POST` is a way of modifying data at the server. 

