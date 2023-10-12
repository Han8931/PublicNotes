A CSS rule contains two parts: a selector and a declaration.
- **Selector**: 
	- `p`, `h1`, and so on
- **Declaration**: it indicates how the elements referred to in the selector should be styled. Declarations are split into two parts (a property and a value), and are separated by a colon. 
	- `font-family`

![[css_1.png]]

CSS declarations sit inside curly brackets and each is made up of two parts: a property and a value, separated by a colon.
![[css_2.png]]


## Using External CSS

```html
<!DOCTYPE html>
<html>
 <head>
 <title>Using External CSS</title>
 <link href="css/styles.css" type="text/css" rel="stylesheet" />
 </head>
 <body>
 <h1>Potatoes</h1>
 <p>There are dozens of different potato 
 varieties. They are usually described as 
 early, second early and maincrop.</p>
 </body>
</html>
```

### Link
The `<link>` element can be used in an HTML document to tell the browser where to **find the CSS file used to style the page**. It is an empty element (meaning it does not need a closing tag), and it lives inside the `<head>` element. It should use three attributes:

- `href` This specifies the path to the CSS file (which is often placed in a folder called css or styles).
- `type` This attribute specifies the type of document being linked to. The value should be text/css.
- `rel` This specifies the relationship between the HTML page and the file it is linked to. The value should be stylesheet when linking to a CSS file.

## Using Internal CSS

```html
<!DOCTYPE html>
<html>
 <head>
  <title>Using Internal CSS</title>
  <style type="text/css">
   body {
     font-family: arial;
     background-color: rgb(185,179,175);}
   h1 {
     color: rgb(255,255,255);}
  </style>
 </head>
 <body>
  <h1>Potatoes</h1>
  <p>There are dozens of different potato 
    varieties. They are usually described as 
    early, second early and maincrop.</p>
 </body>
</html>
```



```html
<!DOCTYPE html>
<html>
 <head>
  <title>CSS Selectors</title>
 </head>
 <body>
  <h1 id="top">Kitchen Garden Calendar</h1>
  <p id="introduction">Here you can read our 
    handy guide about what to do when.</p>
  <h2>Spring</h2>
  <ul>
   <li><a href="mulch.html">
       Spring mulch vegetable beds</a></li>
   <li><a href="potato.html">
       Plant out early potatoes</a></li>
   <li><a href="tomato.html">
       Sow tomato seeds</a></li>
   <li><a href="beet.html">
       Sow beet seeds</a></li>
   <li><a href="zucchini.html">
       Sow zucchini seeds</a></li>
   <li><a href="rhubarb.html">
       Deadhead rhubarb flowers</a></li>
  </ul>
  <p class="note">
    This page was written by 
   <a href="mailto:ivy@example.org">
     ivy@example.org</a> for 
   <a href="http://www.example.org">Example</a>.
  </p>
  <p>
   <a href="#top">Top of page</a>
  </p>
 </body>
</html>
```




