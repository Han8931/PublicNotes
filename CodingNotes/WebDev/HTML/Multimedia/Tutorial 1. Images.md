# How do we put an image on a webpage?

In order to put a simple image on a web page, we use the `<img>` element. This is a void element (meaning, it cannot have any child content and cannot have an end tag) that requires two attributes to be useful: `src` and `alt`. The `src` attribute contains a URL pointing to the image you want to embed in the page. As with the `href` attribute for `<a>` elements, the `src` attribute can be a relative URL or an absolute URL. Without a `src` attribute, an `img` element has no image to load.

>**Note:** Elements like `<img>` and `<video>` are sometimes referred to as **replaced elements**. This is because the element's content and size are defined by an external resource (like an image or video file), not by the contents of the element itself. You can read more about them at [Replaced elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Replaced_element).

## Examples
```html
<img
  src="images/dinosaur.jpg"
  alt="The head and torso of a dinosaur skeleton;
          it has a large head with long sharp teeth"
  width="400"
  height="341"
  title="A T-Rex on display in the Manchester University Museum" />
```

```html
<figure>
  <img
    src="images/dinosaur.jpg"
    alt="The head and torso of a dinosaur skeleton;
            it has a large head with long sharp teeth"
    width="400"
    height="341" 
    align="left"
    />

  <figcaption>
    A T-Rex on display in the Manchester University Museum.
  </figcaption>
</figure>
```