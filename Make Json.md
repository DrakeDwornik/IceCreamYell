#converting the CSV to JSON
##Done in a text editor with `regex` search and replace.
###probably not so useful, but it exists now

1.find: `(.*),(.*),(.*),(.*),(.*)`\
replace: `"id": \1, "female": \2, "ice_cream": \3, "video": \4, "puzzle": \5`


2. find: `(.*)`\
replace: `\{\1\}`

3. find: `(\{"id": )(\d+)(,)`\
replace: `'\2':\1\2\3`

4. add outermost `{}`

5. pretty print in PyCharm