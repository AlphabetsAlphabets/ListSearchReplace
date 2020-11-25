# Documentation for the ListSearchReplace algorithm
1. For example use cases, refer to the file [example.py](https://github.com/YJH16120/ListSearchReplace/blob/master/example.py)

### Prefered way to import ListSearchReplace
from LSR import ListSearchReplace as LSR

# LSR(self, board, nested=False)
`self` is the object itself
`board` is the list
`nested` by default is set to __False__. Accepts either __True__ or __False__. If the list is nested set `nested` to __True__, otherwise set it to __False__ or let the default take over.

# search(self, element_to_search)
`self` is the object itself.
`element_to_search` is used to search for elements in the list. In the event that the `element_to_search` **does not exist**, it will return nothing.
if `nested` is set to False it will return **one** value, if `nested` is set to __True__ it will return 2 values.

# replace(self, element_to_replace, replacement, all_elements=False)
`element_to_replace` is what you want to replace.
`replacement` is what you want to replace `element_to_replace` with.
`all_elements` by default is set to __False__ and will replace the first instance the `element_to_replace` appears. But if it is set to __True__ it will **replace all** elements matching `element_to_replace` with the replacement.

# typecast(self, to_type)
`self` is the object itself
`to_type` is the type you want the list elements to be changed to. If the elements in the list are integers, setting `to_type` to 'str' will change all the element types to a string.
Accepted arguments:
1. str
2. int
