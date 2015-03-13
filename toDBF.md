#summary Conversion to a Databasefile from a Data File
#labels Tools

<a href='Hidden comment: 
End-User
'></a>
# Notes for General Users #
Conversion to a Databasefile from a Data File converts a data file into a databasefile (DBF). Currently support is only implemented for Tobii and SensoMotoric formats. See the documentation on [File Formats](fileformats.md) for further information.

<a href='Hidden comment: 
ArcGIS
'></a>
# Notes for ArcGIS Users #
The ArcGIS Toolbox interface to PoP Analyst allows common tasks to be performed using the PoP Analyst library. Below is a screen shot of this tool and a table desribing its parmeters. The PoP Analyst library was not created for exclusive use with ArcGIS and consequently does not use ArcGIS geoprocessor. In some cases this means that same tasks can be performed using built-in tools.

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/dialogs/toDBF.PNG

| **Parameter** | **Description** |
|:--------------|:----------------|
|input data file|The data file to convert to the databasefile format. This can be in either Tobii or SensoMotoric formats.|
|input data file format|The file format of the input data file. This format can be either Tobii or SensoMotoric formats. The default input data file format is Tobii.|
|detect data types|An optional mode that detects the data types in each column. This option is useful for some operations that require certain data types, such as mathmatical operations.|

<a href='Hidden comment: 
Research Description
'></a>
# Notes for Researchers #
File conversion is peformed by loading the input data into memory, making the necessary adjustments, and writing the data to a file. This modularity allows for easy use with ArcGIS, however in most instances this puts a high burden on computer memory and adds to task latency by requiring disk reads and writes. There are some option to address these issues, but they require a small amount of programming. Fortunatly, this programming is limited to only changing a few variables in code that can be generated automatically. See the documentation on [Model Builder](modelbuilder.md) and [Geoscripting](geoscripting.md) for more information.

<a href='Hidden comment: 
Programmer Description
'></a>
# Notes for Programmers #
This function is performed using one of the following scripts: TobiiToDBF.py or AnimeyeToDBF.py.

Conversion only from Tobii and SesoMotoric formats is currently implemented. Additional formats can be easily added by writing a parser and using the databasefile class to create a databasefile. See the documentation on the [Databasefile Class](databasefile.md) for more information.