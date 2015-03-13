PoP Analyst is released under the Lesser GNU Public License 3.0. See http://www.gnu.org for more details.

For Support Contact

Martin Lacayo-Emery

Email: popanalyst@gmail.com

---

# Introduction #
Point Pattern (PoP) Analyst is a library of functions and classes created to make the analysis and visualization of point pattern data usable in a variety of other applications, particularly geographic information systems and sequence analysis programs.

## Application Areas ##
PoP Analyst is useful for converting files with eye-tracking data and creating sequences from that data that can then be used sequence analysis.

## Install and Update ##
There are several options for installing and updating PoP Analyst. The preferred method is to download the latest release from http://pointpatternanalyst.googlecode.com. The download is available on the download page, which can be reached by click on the download tab. The available downloads are compressed into ZIP format and must be unzipped before using, but require no additional setup. updating a download of PoP Analyst only requires downloading the latest release and unzipping it to the same folder as the older release, overwriting the old files.

The other option for downloading PoP Analyst is to use an SVN client to retrieve the repository from http://pointpatternanalyst.googlecode.com/svn/trunk/. (For more information on SVN see the appendix.) Unlike the ZIP of PoP Analyst, the PoP Analyst SVN repository no longer includes the shapefile classes needed, which must also be downloaded and is available from http://shapefile.googlecode.com. Updating PoP Analyst can be preformed by either calling the SVN update command or downloading a patch if available from the download page. Note the SVN repository is where revisions to PoP Analyst are immediately available, and as such maybe unstable.

Python must be installed on the computer in order for PoP Analyst to work. If you do not have Python go to http://www.python.org and download it and follow the instructions for installation.

### Direct Download ###
This is the preferred method of installation.
  1. Go to http://pointpatternanalyst.googlecode.com
  1. Click on the Downloads tab
  1. Select the desired release and download
  1. Unzip the download to the desired location. (Usually short names without spaces works best for folders).
  1. Updates can be performed by repeating this process.

### SVN Client ###
This method should only be chosen by developers and testers.
  1. Create or choose a folder to use to checkout PoP Analyst. (Usually short names without spaces works best for folders).
  1. Checkout the repository at http://pointpatternanalyst.googlecode.com/svn/trunk/ to the desired folder.
  1. The folder now contains PoP Analyst, but requires an additional library.
  1. The PoP Analyst folder contains a folder named lib, inside the lib folder create a folder called shp.
  1. Checkout the repository at http://shapefile.googlecode.com/svn/trunk/ to the folder called shp.
  1. Updates can be performed by calling the SVN update function on both the PoP Analyst folder and the shp folder.

### Standalone GUI ###
The standalone GUI for PoP Analyst requires an additional library called WxPython, if you do not plan on using the standalone GUI you do not need it.
  1. Go to http://www.wxpython.org/
  1. Select the download link and choose the appropriate version for your system.
  1. Follow the installation instructions for your system.

### ArcGIS GUI ###
The ArcGIS GUI was created with ArcGIS 9.3 and exported into additional formats for ArcGIS versions 9.0-9.2.
  1. In ArcMap, from the Window menu select toolbox.
  1. Right click the toolbox area and click on Add Toolbox.
  1. Browse to the PoP Analyst folder and select the appropriate toolbox file (.tbx), then click open.
  1. Point Pattern Analyst Toolbox should now appear in the toolbox area. If desired right click the toolbox area and save the current setup by selecting "Save Settings...".

## Updates ##
If you used the direct download installation method, repeat the installation process. If are using a SVN client see the instruction manual for your SVN client on how to perform a update. Remember when using SVN you must update both the PoP Analyst folder and the shp folder contained in its lib folder.

---

# Features #
PoP Analyst is a software library with an accompanying graphical user interface (GUI). This means that PoP Analyst is mainly a collection of functions that can be used for point pattern analysis, however for ease of use these functions have been combined into common tasks that can be conveniently performed using the GUI. The tasks supported in the GUI are under development and are in pre-alpha, alpha, or beta development stages. Pre-alpha status means that it has not fully been defined or implemented. Alpha status means that it has not been fully implemented or tested by the developer. Beta tools are fully implemented, but are still in a user testing stage. All tools are in a beta stage unless otherwise noted.

## File Formats ##
The input file formats supported are the [Tobii Studio](http://www.tobii.com) and [SMI GazeTracker](http://www.smivision.com) (Animeye) data in tab separated values (TSV) format. The Animeye TSV format is a plain TSV format and begins with a column header line, and is readily usable for other TSV data.

## Data Processing ##
PoP Analyst contains the essential components for converting and processing all of the input file formats. Processing data files begins by validating their format and converting them to the Xbase (DBF) file format. Once in the DBF format, data files can be filtered and split to remove and separate rows. In order to create a sequence from data a coding scheme for the areas of interest must first be created. Coding scheme for areas of interest can be created automatically or manually using the area of interest tools. After a coding scheme is created it can then be applied to data, which results in a sequence using the specified scheme.

### Data Validation ###
Data validation ensures that the input data is compliant with the formats supported by PoP Analyst. All input formats have validation functions. These functions take the data file as input and produce a text report confirming compliance or detailing non-compliance. Optionally validation can also produce a file with the most common issues corrected. In the GUI these functions can be accessed using the _Validate Tobii TSV_ and _Validate Animeye TSV_ tools.

#### Validate Tobii TSV ####

http://pointpatternanalyst.googlecode.com/files/validTobii.PNG

| **Parameter** | **Description** |
|:--------------|:----------------|
|input Tobii TSV|The input file in Tobii tab separated value format.|
|report|The output text file for the validation report.|
|output Tobii TSV|An optional output file for the corrected Tobii tab separated values.|
|verbose mode|An optional mode providing detailed descriptions in the report.|

Validate Tobii TSV ignores the 24 line file header and checks the following column header line for punctuation and white space. If there is punctuation in the column header it is noted in the report as being non-compliant, in verbose mode the original column header and suggested corrected header are noted. If an output Tobii TSV is provided the suggested corrected header will be used.

#### Validate Animeye TSV ####

http://pointpatternanalyst.googlecode.com/files/validAnimeye.PNG

| **Parameter** | **Description** |
|:--------------|:----------------|
|input Animeye TSV|The input file in Animeye tab separated value format.|
|report|The output text file for the validation report.|
|output Animeye TSV|An optional output file for the corrected Animeye tab separated values.|
|verbose mode|An optional mode providing detailed descriptions in the report.|

Validate Animeye TSV checks the column header line for punctuation and white space. If there is punctuation in the column header it is noted in the report as being non-compliant, in verbose mode the original column header and suggested corrected header are noted. If an output Animeye TSV is provided the suggested corrected header will be used.

### Table Creation ###
Table creation converts from the input formats to the Xbase (DBF) file format. The DBF format serves as a common basis on which all other functions operate. All input formats have table creation functions. Optionally table creation can autodetect data types, which does not affect how data is stored, but can useful for some computation and visualization tasks. In the GUI theses functions can be accessed using the _Create DBF from Tobii TSV_ and _Create DBF from Animeye TSV_ tools.

#### Create DBF from Tobii TSV ####

![http://pointpatternanalyst.googlecode.com/files/dbfTobii.png](http://pointpatternanalyst.googlecode.com/files/dbfTobii.png)

| **Parameter** | **Description** |
|:--------------|:----------------|
|Input Tobii TSV|The input file in Tobii tab separated value format.|
|Output DBF|The output DBF file for the Tobii data.|
|Autodetect data type|An optional mode that automatically detects the data type in a column|

Create DBF from Tobii TSV ignores the 24 line file header in the Tobii TSV and uses the following column header line as column headers in the output DBF. All subsequent lines become rows in the output. If Autodetect data type mode is selected, columns will be dynamically. The possible types are integer, float, and string, which are checked in that order and the first that is compatible is selected. The minimum width and precision capable of storing the the data in the column are set as the width and precision. For strings it should be noted that leading or trailing whitespace is removed.

#### Create DBF from Animeye TSV ####

![http://pointpatternanalyst.googlecode.com/files/dbfAnimeye.png](http://pointpatternanalyst.googlecode.com/files/dbfAnimeye.png)

| **Parameter** | **Description** |
|:--------------|:----------------|
|Input Tobii TSV|The input file in Tobii tab separated value format.|
|Output DBF|The output DBF file for the Tobii data.|
|Autodetect data type|An optional mode that automatically detects the data type in a column|

Create DBF from Animeye TSV ignores uses the first line in the Animeye TSV as the column header line and automatically detects the number of columns needed for the AOIs (TopZones). All subsequent lines become rows in the output. If Autodetect data type mode is selected, columns will be dynamically. The possible types are integer, float, and string, which are checked in that order and the first that is compatible is selected. The minimum width and precision capable of storing the the data in the column are set as the width and precision. For strings it should be noted that leading or trailing whitespace is removed.

### Filtering ###
Filtering DBFs allows the removal of rows from a single file. Removal of rows can be done by specifying the rows to keep or rows to remove using a single less than, equal, or greater than rule. For strings, less than or greater than rules use alphanumeric order as a comparison. Filtering creates a new file from the input using the criterion, which can also optionally have data type autodetected. In the GUI this function can be accessed using the _Filter DBF by Variable_ tool.

#### Filter DBF by Variable ####

![http://pointpatternanalyst.googlecode.com/files/filter.png](http://pointpatternanalyst.googlecode.com/files/filter.png)

| **Parameter** | **Description** |
|:--------------|:----------------|
|Input|The input data in DBF format.|
|Field|The name of the field on which to filter.|
|Filter type|The type of filter, can be inclusive or exclusive|
|Equal|An optional value for the equals test.|
|Minimum|An optional value for the less than test.|
|Maximum|An optional value for the greater than test.|
|Output|The output DBF that will contain the remaining rows.|
|Dynamically change data types|An optional mode that will adjust the data type in each column to the new contents.|

Filter DBF by Variable is a tool to do simple filtering on a DBF. A filter can be used to remove values or keep only values that match the filter criteria. A value can be specified for an equals test, a less than test, greater than test. When multiple tests contain values the less than test and greater than test are applied together with the logic operation AND, while the equals test is applied by itself and combined with any other results. For strings it should be noted that the less than and greater than tests are applied using aplhanumeric order, and the equals test ignores leading or trailing whitespace.

### Splitting ###
Splitting a DBF allows the separation of multiple rows in a single file to rows in multiple files. Separation can currently be done only using the criterion of unique values. Splitting creates new files named with the values from the separation criterion in a specified folder, optionally preceded by the name of the input file. In the GUI this function can be accessed using the _Split DBF by Value_ (below) tool.

#### Split DBF by Value ####

![http://pointpatternanalyst.googlecode.com/files/split.png](http://pointpatternanalyst.googlecode.com/files/split.png)

| **Parameter** | **Description** |
|:--------------|:----------------|
|Input Table|The input data in DBF format.|
|Field|The column that contains the values on which to group the rows.|
|Output|The folder that is to contain the output DBFs.|
|Name with Filestem|An optional mode that precedes all file names with the input file name.|
|Name with|The scheme to use for naming the output files.|

Split DBF by Value separates a single DBF into multiple DBFs by grouping rows by the value in a single column. The user selects the output folder and the naming scheme to use for the output DBFs. Optionally the output file names can be preceded by the name of the input file.

### Coding Areas of Interest ###
The areas of interest (AOIs) in a DBF can be listed multiple times and in order to code them consistently for the creation of sequences it is useful to first create a coding scheme. In order to create a coding scheme it is necessary to first have a list of the unique AOIs. The AOI Set function creates a DBF for the coding scheme of AOIs. The DBF contains a column for the fixed width code for an AOI and a column with the unique AOI names. The width of the codes is specified by the user and the code for the AOIs can be generated automatically during scheme creation or entered manually by the user after the coding scheme table is created. In the GUI this function can be accessed using the _Create AOI Set DBF_ tool.

#### Create AOI Set DBF ####

![http://pointpatternanalyst.googlecode.com/files/aoi.png](http://pointpatternanalyst.googlecode.com/files/aoi.png)

| **Parameter** | **Description** |
|:--------------|:----------------|
|Input|The input data in DBF format.|
|Field name|The name of the field that contains the AOI names.|
|Output|The output DBF file.|
|Encoding label|The column label for the encodings in the output.|
|Encoding length|The length of the encodings for the AOIs.|
|Encoding value|The value mode for the encodings.|

Create AOI Set DBF creates a DBF with a column containing the unique AOIs in a DBF file and a column containing the codes that will be used in sequences to identify the AOIs. If the encoding length is too small to represent the number of AOIs a error message will be displayed with the minimum encoding length. Currently a maximum of length of 12 is allowed for encoding length. The encoding value mode is set to automatic by default, which will simply enumerate the AOIs using letter sequences. A manual encoding mode can be selected that will create empty cells for the codes which a user must enter later.

### Sequence Creation ###
Sequence creation allows the creation of sequences from a DBF using an existing coding scheme. A single sequence can be created from a DBF or optionally multiple sequences can be created if a column is selected for values on which to group the data. Additionally, a column can optionally be selected on which to sort the data otherwise it is assumed that data is listed in order. In the GUI this function can be accessed using the _Create Sequences from DBF_ tool.

#### Create Sequences from DBF ####

![http://pointpatternanalyst.googlecode.com/files/sequence.png](http://pointpatternanalyst.googlecode.com/files/sequence.png)

| **Parameter** | **Description** |
|:--------------|:----------------|
|Input Table|The input data in DBF format.|
|Separate Field|An optional field that contains the values on which to group the rows.|
|Order by Field|An optional field that contains values on which to sort the rows if not already in order.|
|Output File|The output file in Clustal G format.|
|AOI Table|The DBF that contains the AOI codes and labels.|
|AOI Code Field|The field that contains the codes for the AOIs.|
|AOI Label Field|The field that contains the labels for the AOIs.|

Create Sequences form DBF creates sequences from a DBF file using and AOI set DBF. A single sequence is created by default, however specifying a separate field will allow rows to be grouped by unique values and result in multiple sequences. By default the rows are considered to be in temporal order, however a column on which to sort the rows can be specified. A table that contains the AOI labels (names) and codes must be specified along with the corresponding columns contained in the table. The output file is in the Clustal G format.

## Geometry ##
Geometry tools are still under development.

---

# Appendix #

## Subversion (SVN) ##
Subversion (SVN) is a version control system for source code. SVN stores the most recent source code for a project and the differences between the current version and all previous versions. In such a way all versions of the source code can be obtained by reversing the differences in the current source code. Each time a change is made by the developer a optional comment is recorded, which allows the tracking of developments and changes.