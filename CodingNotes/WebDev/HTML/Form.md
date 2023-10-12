---
tags: html, form
---
# Basics

An [HTML Form](https://developer.mozilla.org/en-US/docs/Learn/Forms) is a group of one or more fields/widgets on a web page, which can be used to _collect information from users for submission to a server_. 
- Forms are a flexible mechanism for collecting user input because there are suitable widgets for entering many different types of data, including text boxes, checkboxes, radio buttons, date pickers and so on. 
- Forms are also a relatively secure way of sharing data with the server, as they allow us to send data in `POST` requests with cross-site request forgery protection.

Form controls live inside a `<form>` element. This element should always carry the action attribute and will usually have a method and id attribute too.
```html
<form action="http://www.example.com/subscribe.php" 
 method="get">
 <p>This is where the form controls will appear.
  </p>
</form>
```

- Every `<form>` element requires an action attribute. Its value is the URL for the page on the server that will receive the information in the form when it is submitted.
- Forms can be sent using one of two methods: `get` or `post`.
	- With the get method, the values from the form are added to the end of the URL specified in the action attribute. The get method is ideal for: 
		- short forms (such as search boxes) 
		- when you are just retrieving data from the web server (not sending information that should be added to or deleted from a database)
	- With the post method the values are sent in what are known as HTTP headers. As a rule of thumb you should use the post method if your form: 
		- allows users to upload a file 
		- is very long 
		- contains sensitive data (e.g. passwords) 
		- adds information to, or deletes information from, a database
- If the method attribute is not used, the form data will be sent using the get method.

## Input

```html
<form action="http://www.example.com/login.php">
 <p>Username:
 <input type="text" name="username" size="15" 
   maxlength="30" />
 </p>
</form>
```
- The `<input>` element is used to create several different form controls. The value of the type attribute determines what kind  of input they will be creating.
- `name`: When users enter information into a form, **the server needs to know which form control each piece of data was entered into**. (For example, in a login form, the server needs to know what has been entered as the username and what has been given as the password.) Therefore, each form control requires a name attribute. The value of this attribute identifies the form control and is sent along with the information they enter to the server.
- `size`: _The size attribute should not be used on new forms_. It was used in older forms to indicate the width of the text input (measured by the number of characters that would be seen). For example, a value of 3 would create a box wide enough to display three characters (although a user could enter more characters if they desired). In any new forms you write, CSS should be used to control the width of form elements. The size attribute is only mentioned here because you may come across it when looking 

## Password Input

```html
<form action="http://www.example.com/login.php">
 <p>Username:
 <input type="text" name="username" size="15" 
   maxlength="30" />
 </p>
 <p>Password:
  <input type="password" name="password" size="15" 
   maxlength="30" />
 </p>
</form>
```

`type="password"` When the type attribute has a value of password it creates a text box that acts just like a single-line text input, except the characters are blocked out. They are hidden in this way so that if someone is looking over the user's shoulder, they cannot see sensitive data such as passwords.

## Text Area

```html
<form action="http://www.example.com/comments.php">
 <p>What did you think of this gig?</p>
 <textarea name="comments" cols="20" rows="4">Enter 
 your comments...</textarea>
</form>
```
The `<textarea>` element is used to create a mutli-line text input. Unlike other input elements this is not an empty element. It should therefore have an opening and a closing tag. 

Any text that appears between the opening `<textarea>` and closing `</textarea>` tags will appear in the text box when the page loads. 

If the user does not delete any text between these tags, this message will get sent to the server along with whatever the user has typed. (Some sites use JavaScript to clear this information when the user clicks in the text area.)

## Radio Button
```html
<form action="http://www.example.com/profile.php">
 <p>Please select your favorite genre:
 <br />
  <input type="radio" name="genre" value="rock" 
  checked="checked" /> Rock
  <input type="radio" name="genre" value="pop" /> 
  Pop
  <input type="radio" name="genre" value="jazz" /> 
  Jazz
 </p>
</form>
```

## Check Box

```html
<form action="http://www.example.com/profile.php">
 <p>Please select your favorite music service(s):
 <br />
  <input type="checkbox" name="service" 
  value="itunes" checked="checked" /> iTunes
  <input type="checkbox" name="service" 
  value="lastfm" /> Last.fm
  <input type="checkbox" name="service" 
  value="spotify" /> Spotify
 </p>
</form>
```

## Drop Down List

```html
<form action="http://www.example.com/profile.php">
 <p>What device do you listen to music on?</p>
 <select name="devices">
  <option value="ipod">iPod</option>
  <option value="radio">Radio</option>
  <option value="computer">Computer</option>
 </select>
</form>
```

## Multiple Select Box
```html
<form action="http://www.example.com/profile.php">
 <p>Do you play any of the following instruments? 
 (You can select more than one option by holding 
 down control on a PC or command key on a Mac 
 while selecting different options.)</p>
 <select name="instruments" size="3" multiple="multiple">
 <option value="guitar" selected="selected">
  Guitar</option>
 <option value="drums">Drums</option>
 <option value="keyboard" 
  selected="selected">Keyboard</option>
 <option value="bass">Bass</option>
 </select>
</form>
```

## File Input Box
```html
<form action="http://www.example.com/upload.php"
 method="post">
 <p>Upload your song in MP3 format:</p>
 <input type="file" name="user-song" /><br />
 <input type="submit" value="Upload" />
</form>
```
If you want to allow users to upload a file (for example an image, video, mp3, or a PDF), you will need to use a file input box.

## Submit Button
```html
<form action="http://www.example.com/subscribe.php">
 <p>Subscribe to our email list:</p>
 <input type="text" name="email" />
 <input type="submit" name="subscribe" 
 value="Subscribe" />
</form>
```

## Image Button

```html
<form action="http://www.example.org/subscribe.php">
 <p>Subscribe to our email list:</p> 
 <input type="text" name="email" />
 <input type="image" src="images/subscribe.jpg" width="100" height="20" />
</form>
```

`type="image"` If you want to use an image for the submit button, you can give the type attribute a value of image. The src, width, height, and alt attributes work just like they do when used with the `<img>` element.

## Button and Hidden Controls

```html
<form action="http://www.example.com/add.php"> 
 <button><img src="images/add.gif" alt="add" width="10" height="10" /> Add</button>
 <input type="hidden" name="bookmark" value="lyrics" />
</form>
```

## Labelling form Controls

```html
<label>Age: <input type="text" name="age" /></label>
<br/ >
Gender:
<input id="female" type="radio" name="gender"
 value="f">
<label for="female">Female</label>
<input id="male" type="radio" name="gender" 
 value="m">
<label for="male">Male</label>
```

When introducing form controls, the code was kept simple by indicating the purpose of each one in text next to it. However, each form control should have its own `<label>` element as this makes the form accessible to vision-impaired users. The `<label>` element can be used in two ways. It can:

1. Wrap around both the text description and the form input (as shown on the first line of the example to your right).
2. Be kept separate from the form control and use the for attribute to indicate which form control it is a label for (as shown with the radio buttons).

The for attribute states which form control the label belongs to.  Note how the radio buttons use the id attribute. The value of the id attribute uniquely identifies an element from all other elements on a page. 

## Grouping Form Elements
```html
<fieldset>
 <legend>Contact details</legend>
 <label>Email:<br />
 <input type="text" name="email" /></label><br />
 <label>Mobile:<br />
 <input type="text" name="mobile" /></label><br />
 <label>Telephone:<br />
 <input type="text" name="telephone" /></label>
</fieldset>
```
- You can group related form controls together inside the `<fieldset>` element. This is particularly helpful for longer forms. Most browsers will show the fieldset with a line around the edge to show how they are related. The appearance of these lines can be adjusted using CSS.
- The `<legend>` element can come directly after the opening `<fieldset>` tag and contains a caption which helps identify the purpose of that group of form controls.

## HTML Form Validation

```html
<form action="http://www.example.com/login/" method="post"> 
 <label for="username">Username:</label>
 <input type="text" name="username"
 required="required" /></title><br /> 
 <label for="password">Password:</label>
 <input type="password" name="password"
 required="required" /> 
 <input type="submit" value="Submit" />
</form>
```

You have probably seen forms on the web that give users messages if the form control has not been filled in correctly; this is known as form validation. 

Traditionally, form validation has been performed using JavaScript (which is beyond the scope of this book). But HTML5 is introducing validation and leaving the work to the browser.

## HTML Date Input
```html
<form action="http://www.example.com/bookings/" 
 method="post">
 <label for="username">Departure date:</label>
 <input type="date" name="depart" />
 <input type="submit" value="Submit" />
</form> 
```

## Email & URL Input

```html
<form action="http://www.example.org/subscribe.php"> 
 <p>Please enter your email address:</p>
 <input type="email" name="email" />
 <input type="submit" value="Submit" />
</form>
```

```html
<form action="http://www.example.org/profile.php"> 
 <p>Please enter your website address:</p>
 <input type="url" name="website" />
 <input type="submit" value="Submit" />
</form>
```

## Search Input 
```html
<form action="http://www.example.org/search.php">
 <p>Search:</p>
 <input type="search" name="search" />
 <input type="submit" value="Search" />
</form>
```

On any text input, you can also use an attribute called placeholder whose value is text that will be shown in the text box until the user clicks in that area. Older browsers simply ignore this attribute.

```html
<form action="http://www.example.org/search.php">
 <p>Search:</p>
 <input type="search" name="search"  placeholder="Enter keyword" />
 <input type="submit" value="Search" />
</form>
```
