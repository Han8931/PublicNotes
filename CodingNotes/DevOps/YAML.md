Most formatting languages display data in a non-human readable format. Even JSON, the most popular data format in use, has poor code readability.

YAML is an alternative to JSON that formats data in a natural, easy-to-read, and concise manner.

This article will introduce you to the YAML markup language. We cover the basic concepts behind this markup language, explain its key features, and show what YAML offers to DevOps teams.

## What is YAML?

YAML is a data serialization language. Back when it came out in 2001, YAML stood for "_Yet Another Markup Language_." The acronym was later changed to "_YAML Ain’t Markup Language_" to emphasize that the language is intended for data and not documents.

It is not a programming language in the true sense of the word. YAML files store information, so they do not include actions and decisions.

Unlike XML or JSON, YAML presents data in a way that makes it easy for a human to read. The simple syntax does not impact the language’s capabilities. Any data or structure added to an XML or JSON file can also be stored in YAML.

Besides human-readable code, YAML also features:
- Readable code
- Short syntax
- Cross-language data portability
- A consistent data model
- One-pass processing
- Ease of implementation and use

Users can write code for reading and generating YAML in any programming language. The extensions in YAML are _.yaml_ and _.yml_. Both extensions stand for the same file type.

## Yaml Features

YAML has several features that make it an excellent option for data formatting.

### Multi-Document Support

Users can add multiple documents to a single YAML file. Separate different documents with three dashes (**`---`**), like this:
```yaml
---

time: 19:04:12

player: playerOne

action: strike (miss)

---

time: 20:03:47

player: playerTwo

action: strike (hit)
...
```
Three dots ("_..._") mark the end of a document without starting a new one.

### Built-In Comments

YAML allows users to add comments to their code. YAML comments start with the **_`#`_** symbol and do not have to be on a separate line:
```yaml
key: #This is a single line comment 

   - value line 10

   #This is a 

   #multi-line comment

   - value line 20
```

### Clean Syntax

Like Python, YAML relies on indentations to show the levels and structure in the data. There are no usual format symbols, such as braces, square brackets, closing tags, or quote marks. The syntax is clean and easy to scan through.

The clean syntax is why several popular tools rely on YAML, such as [Ansible](https://phoenixnap.com/kb/install-ansible-on-windows), [Kubernetes, and OpenStack](https://phoenixnap.com/blog/kubernetes-vs-openstack).

### No Tabs

YAML does not allow tabs. Spaces are the only way to achieve indentation. It is good practice to display whitespace characters in your [text editor](https://phoenixnap.com/kb/best-linux-text-editors-for-coding) to prevent accidental uses of tabs.

The recommended way to indent YAML files is to **use two spaces per level of indentation**, as tabs can cause parsing errors. You can use a YAML linter or formatter to check and correct your indentation automatically

### Precise Feedback

YAML feedback refers to specific lines [in the file](https://phoenixnap.com/glossary/what-is-a-file). You can quickly find and fix errors when you know where to look.

### Support for Complex Structures

YAML provides the ability to reference other data objects. With referencing, you can write recursive data in the YAML file and build [advanced data structures](https://phoenixnap.com/kb/data-structures).

### Explicit Data Types with Tags

YAML auto-detects the type of data, but users are free to specify the type they need. To specify the type of data, you include a “!!” symbol:

```yaml
# The value should be an int:

is-an-int: !!int 5.6

# Turn any value to a string:

is-a-str: !!str 90.88

# The next value should be a boolean:

is-a-bool: !!bool yes
```

### No Executable Commands

_YAML is a data-representation format. There are no executable commands_, which makes the language highly secure when exchanging files with third parties.

If a user wishes to add an executable command, YAML must be integrated with other languages. Add [Perl](https://phoenixnap.com/glossary/what-is-perl) parsers, for example, to enable Perl code execution.


