---
tags: html, table
---
# Basics
```html
<table>
  <tr>
    <td>15</td>
    <td>15</td>
    <td>30</td>
  </tr>
  <tr>
    <td>45</td>
    <td>60</td>
    <td>45</td>
  </tr>
  <tr>
    <td>60</td>
    <td>90</td>
    <td>90</td>
  </tr>
</table>
```
- `tr`: table row
- `td`: table data

# Table Heading
```html
<table>
  <tr>
    <th></th>
    <th scope="col">Saturday</th>
    <th scope="col">Sunday</th>
  </tr>
  <tr>
    <th scope="row">Tickets sold:</th>
    <td>120</td>
    <td>135</td>
  </tr>
  <tr>
    <th scope="row">Total sales:</th>
    <td>$600</td>
    <td>$675</td>
  </tr>
</table> 
```
The `<th>` element is used just  like the `<td>` element but its  purpose is to represent the  heading for either a column or a row. (The th stands for table heading.) 

Even if a cell has no content, _you should still use a `<td>` or `<th>` element to represent the presence of an empty cell otherwise the table will not render correctly_. (The first cell in the first row of this example shows an empty cell.)

# Spanning Columns
```html
<table>
 <tr>
  <th></th>
  <th>9am</th>
  <th>10am</th>
  <th>11am</th>
  <th>12am</th>
 </tr>
 <tr>
  <th>Monday</th>
  <td colspan="2">Geography</td>
  <td>Math</td>
  <td>Art</td>
 </tr>
 <tr>
  <th>Tuesday</th>
  <td colspan="3">Gym</td>
  <td>Home Ec</td>
 </tr>
</table>
```
Sometimes you may need the entries in a table to stretch across more than one column. The colspan attribute can be used on a `<th>` or `<td>` element and indicates how many columns that cell should run across.

# Spanning Rows

```html
<table>
 <tr>
  <th></th>
  <th>ABC</th>
  <th>BBC</th>
  <th>CNN</th>
 </tr>
 <tr>
  <th>6pm - 7pm</th>
  <td rowspan="2">Movie</td>
  <td>Comedy</td>
  <td>News</td>
 </tr>
 <tr>
  <th>7pm - 8pm</th>
  <td>Sport</td>
  <td>Current Affairs</td>
 </tr>
</table>
```

# Long Table

```html
<table>
 <thead>
  <tr>
   <th>Date</th>
   <th>Income</th>
   <th>Expenditure</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>1st January</th>
   <td>250</td>
   <td>36</td>
  </tr>
  <tr>
   <th>2nd January</th>
   <td>285</td>
   <td>48</td>
  </tr>
  <!-- additional rows as above -->
  <tr>
   <th>31st January</th>
   <td>129</td>
   <td>64</td>
   </tr>
 </tbody>
 <tfoot>
  <tr>
   <td></td>
   <td>7824</td>
   <td>1241</td>
  </tr>
 </tfoot>
</table>
```

There are three elements that help distinguish between the main content of the table and the first and last rows (which can contain different content). 

These elements help people who use screen readers and also allow you to style these sections in a different manner than the rest of the table (as you will see when you learn about CSS).

- `thead`: The headings of the table should sit inside the `<thead>` element. 
- `tbody`: The body should sit inside the `<tbody>` element. 
- `tfoot`: The footer belongs inside the `<tfoot>` element.