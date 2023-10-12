## Case Sensitivity
We can override Vim’s default case sensitivity using the `\c` and `\C` items. Lowercase `\c` causes the search pattern to ignore case, while the uppercase `\C` item forces case sensitivity. If either of these items is used in a search pattern, the value of `ignorecase` is overridden for that search.

Note that these items can be used anywhere in a pattern. If you realize that you need a case sensitive search after you typed out the full pattern, just tack `\C` on at the end, and it will affect everything that went before it.

## Regular Expression for Substitution
First search using `/`:
- `/[0-9]`
- Then, `:%s//<replace>/gc`

## Use the `\v` Pattern Switch for Regex Searches
It is caled _very magic_ search.

- `:%s/\v'(([^']|'\w)+)'/“\1”/g`

This is equivalent to
- `/\v'(([^']|'\w)+)'`
- `:%s//“\1”/g`
