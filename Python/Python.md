## Usage
To use Snow in your Python program, download [this](https://github.com/TheNPCFISH/Snow/blob/master/Python/snow.py) to it

Then import the Snow:<br>
`import snow`

## How to use
To make a new list, create a new file. For example:
```
nameofthelist.snow
```
### List of functions
You don't have to type "nameofthelist.snow". Only "nameofthelist"
But now I'll show you some examples too with list called "test"
- addToList(text, listName) *add text to the list*

      addToList("Hello world", "test")
- getLineCount(listName) *get a number*

      if getLineCount("test") == 10:
        print("Length of my list is 10!")
- printList(listName) *print the whole list*

      printList("test")
- deleteFromList(text, listName) *delete text from the list*

      deleteFromList("Hello world", "test")
- clearList(listName) *clears the whole list (it will stay on your computer)*

      clearList("test")
- deleteList(listName) *this will delete the list from your computer*

      deleteList("test")
- checkIfInList(text, listName) *checks if list contains text*

      if checkIfInList("Hello world", "test") == False:
        print("Oh no!")
- deleteLine(lineNumber, listName) *deletes line*

      deleteLine(5, "test")
      or
      deleteLine("5.1", "test")
- getLineContent(line, listName) *gets line content*

      print(getLineContent(4, "test"))

*btw semicolon starts a new line*
