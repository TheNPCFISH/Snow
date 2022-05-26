# Snow
Snow is datastore (for Python now).

## How to use
To make a new list, create a new file. For example:
```
nameofthelist.snow
```
### List of functions
You don't have to type "nameoflist.snow". Only "nameoflist"
- addToList(text, listName) *add text to the list*

      addToList("Hello world", "test")
- lengthOfList(listName) *get a number*

      if lengthOfList("test") == 10:
        print("Length of my "test" list is 10!")
- printList(listName) *print the whole list*

      printList("test")
- deleteFromList(text, listName) *delete text from the list*

      deleteFromList("Hello world", "test"
- clearList(listName) *clears the whole list (it will stay on your computer)*

      clearList("test")
- deleteList(listName) *this will delete the list from your computer*

      deleteList("test")
- checkIfInList(text, listName) *checks if list contains text*

      if checkIfInList("Hello world", "test") == False:
        print("Oh no!")
- deleteLine(lineNumber, listName) *deletes line*

      deleteLine(5, "test")
- getLineContent(line, listName) *gets line content*

      print(getLineContent(4, "test"))

## Todo
- Make a copy for other languages
- More features
