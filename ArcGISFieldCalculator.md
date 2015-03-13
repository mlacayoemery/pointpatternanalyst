#summary Tips on how to use the field calculator in ArcGIS.
<a href='Hidden comment: 
This text will be removed from the rendered page.
'></a>

# Introduction #

The field calculator in ArcGIS provides simple and advanced ways to change the values in a field.


# Details #

## String Processing ##

### Finding a Substring ###
```
InStr([Field Name],"substring")
```

### Leftmost Characters ###
```
Left([Field Name],integer)
```

## Commonly Combined Functions ##

### Removing a Delimited Suffix ###
```
Left([Field Name], InStr([Field Name],"delimter") - 1)
```


See http://webhelp.esri.com/arcgisdesktop/9.3/index.cfm?TopicName=Making_field_calculations for more information.