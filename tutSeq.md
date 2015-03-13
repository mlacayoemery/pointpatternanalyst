#summary Tutorial: Sequence Creation Using PoP Analyst
#labels Tutorial

<a href='Hidden comment: 
Add table of contents.
'></a>

# Introduction #
This tutorial is a step-by-step guide on how to create sequences using PoP Analyst. PoP Analyst contains the tools needed to process point data and create sequence files that can be analyzed using Clustal G.


---


# Installation and Setup #
PoP Analyst can be downloaded from [http://pointpatternanalyst.googlecode.com](http://pointpatternanalyst.googlecode.com).

1. Go to [http://pointpatternanalyst.googlecode.com](http://pointpatternanalyst.googlecode.com) and click on the download tab.

[![](http://pointpatternanalyst.googlecode.com/svn/wiki/images/googlecode/downloads.png)](http://code.google.com/p/pointpatternanalyst/downloads/list)

2. Find the download called Point Pattern Analyst and click on the file name called [popanalyst.zip](http://pointpatternanalyst.googlecode.com/files/popanalyst.zip)

[http://pointpatternanalyst.googlecode.com/svn/wiki/images/googlecode/popanalyst.PNG](http://pointpatternanalyst.googlecode.com/files/popanalyst.zip)

| **Note:** The revision (rev) number of the download be different.|
|:-----------------------------------------------------------------|

3. Save [popanalyst.zip](http://pointpatternanalyst.googlecode.com/files/popanalyst.zip) to the location you desire and unzip it to the location where you want to store PoP Analyst.

| **Tips:** To install a new version of PoP Analyst **close ArcGIS** and delete the old folder and follow the normal installation and setup.|
|:------------------------------------------------------------------------------------------------------------------------------------------|

4. Open ArcMap. In the ArcToolbox frame right click on ArcToolbox icon and select "Add Toolbox..."
| **Additional Help:** If the ArcToolbox frame is closed it can be opened by selecting ArcToolbox in the Window menu.|
|:-------------------------------------------------------------------------------------------------------------------|

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/arctoolbox.PNG

5. Browse to folder containing PoP Analyst and open it. Select the appropriate toolbox for your version of ArcGIS.

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/addtoolbox.PNG

The ArcToolbox frame should now show the PoP Analyst Tools toolbox and is ready for use.

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/poptoolbox.PNG


| **Note:** The ArcToolboxes appear in alphabetic order.|
|:------------------------------------------------------|

| **Tips:** If would like the PoP Analyst Tools toolbox to appear next time you open ArcMap, right click on the ArcToolbox icon in the ArcToolbox frame and select "Save Settings" to save the current ArcToolbox to the default settings or a settings file.|
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


---


# Importing Data into PoP Analyst #
The tools in PoP Analyst require data to be in the database file (DBF) format. Data exported in the raw format from Tobii Studios and SensoMotoric software can be converted to the DBF format using the _Data File to Database File_ tool in the PoP Analyst _Data Preprocessing_ toolbox.

| **Tips:** See the [Tobii Studio Export Guide](http://code.google.com/p/pointpatternanalyst/wiki/TobiiExport) for an explanation on how to export data from Tobii Studios for PoP Analyst.|
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The following steps explain how to use _Data File to Database File_ tool:

1. Find the PoP Analyst Tools toolbox in the ArcToolbox frame click on plus icon next to the PoP Analyst Tools toolbox to expand the toolbox. (If the ArcToolbox frame is closed it can be opened by selecting ArcToolbox in the Window menu.)

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/poptools.PNG

2. Click on the plus icon next to _Data Processing_ toolbox and double click on the _Data File to Database File_ tool. This will open the dialog box.

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/dialogs/toDBF.PNG

| **Tips:** The ArcGIS dialog boxes contain help information for the tool and each of its parameters. Click on the "Show Help>>" button to display this information.|
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The dialog box has four parameters and is summarized in the following table:

| **Parameter** | **Description** |
|:--------------|:----------------|
|input data file|The input data file to read. This file can be in Tobii or SensoMotoric formats.|
|input data file format|The input data file format, either Tobii or SensoMotoric.|
|output database file|The output database file that will contain the input data.|
|detect data types|An optional mode that automatically detects the data types in a column. This mode is useful if the data will be processed further using  mathematical operations.|

| **Tips:** The detect data types mode, also called dynamically change types in other tools, provides an effective way to determine the data type in each column, however this process requires examining all values and so is only recommend when necessary.|
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

3. Click on the folder icon next to the "input data file" parameter and browse to the PoP Analyst folder. In the PoP Analyst folder open the folder called "dat" and select the file [user01.tsv](http://pointpatternanalyst.googlecode.com/svn/trunk/dat/user01.tsv). Set the input data file format to Tobii if this has not already been done.

4. Click on the folder icon next to the "output database file" parameter and browse to location you would like to save your work. Enter a the file name "user01.dbf" and be sure to include the ".dbf".

| **Additonal Help:** If you received an error message after entering the file name make sure that the file name ends in ".dbf" and contains no other peroids.|
|:------------------------------------------------------------------------------------------------------------------------------------------------------------|

The dialog box should now appear as below:

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/dialogs/toDBFtut.PNG

5. Click on the "OK" button. The conversion process will run, and may take a while depending on the file size. When the process finishes your database file will have been created. Close the process window and continue on to the next step of selecting data.


---


# Selecting and Filtering Data #
The sequence creation tools require that all data in a database file be gaze data. In the tutorial data that means that events recorded with the data need to be removed. This can be done using the _Select_ tool in the _Data Preprocessing Toolbox_.

| **Note:** In practice events are often very important, because the include information on the presentation of new stimuli and user interaction. In this tutorial there was only one stimulus and user interaction was not part of the design.|
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The following steps explain how to use the _Select_ tool:

1. Find the _Select_ tool in the _Data Preprocessing Toolbox_ and double click to open the dialog box.

The dialog box has eight parameters and is summarized in the following table:

| **Parameter** | **Description** |
|:--------------|:----------------|
|input database file|The input database file that contains the data to select.|
|field to filter on|The field in the database file on which the selection will be based.|
|filter type|The type of filter to use, either values to keep (include) or values to remove (exclude).|
|equal to value|If provided, a value to use for an equal comparison. If matching for a blank field add a space to this parameter.|
|minimum value|If provided, a value to use for an greater than or equal to comparison. Note: String fields use alphanumeric order for comparison.|
|output database file|The output database file that will contain the selected rows.|
|dynamically change data types|An optional mode that automatically changes the data types in a column based on the values it contains. This mode is useful if the data will be processed further using  mathematical operations.|

2. Click on the folder icon next to the "input database file" parameter and browse for the data file "user01.dbf" created from importing data into PoP Analyst. Click on the "Add" button once the file has been selected.

3. Click on the down arrow next to the "field to filter" on parameter and select the field called "Event".

4. Click on the down arrow just below and to right of the "filter type" parameter and select "Values to Keep" if it has not been done already.

5. Click in the box just below the "equal to value" label and enter a single space. Ignore the minimum value and maximum value parameters.

| **Tips:** The values of comparison parameters are not sensitive to leading or trailing whitespace, but to distinguish specifying a value as blank from ignoring a parameter whitespace must be added to the field. Be aware that this means that leading or trailing whitespace is ignored in all cases and cannot be used for distinguishing values.|
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

6. Click on the folder icon next to the "output database file" parameter and browse to location you would like to save your work. Enter the file name "user01\_select.dbf" and be sure to include the ".dbf".

The dialog box should now appear as below:

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/dialogs/selecttut.PNG

7. Click on the "OK" button. The conversion process will run, and may take a while depending on the file size. When the process finishes your database file will have been created. Close the process window and continue on to the next step of creating and coding an areas database file.


---


# Creating the Area of Interest (AOI) Codes #
Sequence creation requires area codes for AOIs so that a sequence can be coded. To accomplish this, a database file must be created that contains the area names and corresponding area codes. This can be done using the _Create Areas Database File_ tool in the _Computation_ toolbox.

The following steps explain how to use the _Create Areas Database File_ tool:

1. Find the _Create Areas Database File_ tool in the _Computation_ toolbox and double click to open the dialog box.

The dialog box has six parameters and is summarized in the following table:

| **Parameter** | **Description** |
|:--------------|:----------------|
|input database file|The input database file that contains a field with area names.|
|input area field|The field from the input database file that contains the area names.|
|output area code field|The field to create in the output database file that will contain the area codes.|
|length of area code|The length of the area. In automatic mode the minimum area code length is automatically determined. If the length selected is too short, automatic mode is activated.|
|output database file|The output database file that will contain the areas table.|
|area code type|The type of code to use for the area code. In automatic mode, the areas will be coded alphabetically using sequential strings. In manual mode, the user must later manually code each area.|

| **Explanation:** The codes created using the automatic area code type are sequential alphabetic strings. They start from A and go to Z and. For example a code length of two would cause the codes to be assigned as Aa, Ab, Ac, ... , Zz. Consequentially, in automatic length mode the length of the codes are equal to the log base 26 (as in 26 letters of the alphabet) of the number of areas. In manual area code type, the user must enter the code individually, however this allows for the use of meaningful codes.|
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

2. Click on the folder icon next to the "input database file" parameter and browse for the data file "user01\_select.dbf" created from selecting the imported data. Click on the "Add" button once the file has been selected.

3. Click on the down arrow on the right of the "input area field" parameter and select the field called "AoiNames".

4. Click on the "output area code field" box and type the name "Code" for the name of the code field in the area database file. Set the "length of area code" parameter to "automatic" if it is not already.

5. Click on the folder icon next to the "output database file" parameter and browse to location you would like to save your work. Enter the file name "user01\_aois.dbf" and be sure to include the ".dbf".  Click on the "Save" button.

The dialog box should now appear as below:

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/dialogs/aoistut.PNG

8. Click on the "OK" button. The process will run, and may take a while depending on the file size. When the process finishes your database file will have been created. Close the process window and continue on to the next step of creating a sequence.


---


# Sequence Creation #
All the prerequisites for sequence creation have been met and a sequence can now be created. Sequence creation creates a sequence from a gaze points database file by using the area codes database file to encoded gaze points AOIs. Once the AOIs are encoded, sequences can be produced by writing the codes to a file, while using the separation, order, and scale fields when specified. This can be done using the _Create Sequence from Database File_ tool in the _Computation_ toolbox.

The following steps explain how to use the _Create Sequence from Database File_ tool:

1. Find the _Create Sequence from Database File_ tool in the _Computation_ toolbox and double click to open the dialog box.

The dialog box has eleven parameters and is summarized in the following table:

| **Parameter** | **Description** |
|:--------------|:----------------|
|input data database file|The input data database file that contains area names.|
|input data area name field|The field in the input data database file that contains the area names.|
|input areas database file|The input areas database file that contains area names and area codes.|
|input areas area code field|The field in the input areas database file that contains the area codes.|
|input areas area name field|The field in the input areas database file that contains the area names.|
|output sequence file format|The format of the output sequence file.|
|output sequence file|The ouput sequence file destination.|
|sequence separation field|An optional field in the input data database file which specifies the unique values on which to separate sequences. |
|sequence order field|An optional field in the input data database file which specifies the values for order within a sequence.|
|sequence scale field|An optional field in the input data database file which specifies the values by which to scale parts within a sequence.|
|minimum scale unit|The minimum unit to use when scaling a sequence.|

2. Click on the folder icon next to the "input data database file" parameter and browse for the data file "user01\_select.dbf" created from selecting the imported data. Click on the "Add" button once the file has been selected.

3. Click on the down arrow on the right of the "input area name field" parameter and select the field called "AoiNames".

4. Click on the folder icon next to the "input areas database file" parameter and browse for the area codes database file "user01\_aois.dbf". Click on the "Add" button once the file has been selected.

5. Click on the down arrow on the right of the "input areas area code field" parameter and select the field called "Code".

6. Click on the down arrow on the right of the "input areas area name field" parameter and select the field called "AoiNames".

7. Click on the down arrow on the right of the "output sequence file format" parameter and select the format called "Clustal G"

8.Click on the folder icon next to the "output sequence file" parameter and browse to location you would like to save your work. Enter the file name "user01\_seq.txt" and click on the "Save" button.

The dialog box should now appear as below:

http://pointpatternanalyst.googlecode.com/svn/wiki/images/ArcGIS/dialogs/seqtut.PNG

9. Click on the "OK" button. The process will run, and may take a while depending on the file size. When the process finishes your sequence file will have been created. Close the process window and continue on to using your sequence analysis program.