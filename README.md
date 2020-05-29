# string.xml-sorting-script
A simple python script to alphabetically sort string resource file based on key name.

### Limitations:
- This script cannot sort ```<string-array>, <integer-array> and <plurals>```
- String resouce should be in a single line. i.e:
```
<string name="app_name"> Droid Info</string>
<string name="button_text">Login</string>
```

- This script cannot sort string resource that is scattered in multiple line like this. i.e:
```
<string name="app_name"> 
Droid Info
</string>
```

### How to run:
```python main.py```

### Result:
- Result will be stored in a new file with name ```sorted.xml```.
- On each run the content of ```sorted.xml``` will get replaced with new result.
