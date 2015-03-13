# Introduction #
Point Pattern Analyst (PoP Analyst) is a software library with an ArcGIS toolbox interface that creates sequences from point data. Sequences can then be analyzed using sequence analysis software such as Clustal G or TraMineR. The primary advantage of using PoP Analyst in ArcGIS is that it serves as a platform that can easily process the attribute and spatial qualities of points.

# Installation #
  1. Download PoP Analyst from http://pointpatternanalyst.googlecode.com/files/popanalyst.zip.
  1. Unzip PoP Analyst into the desired folder.
  1. Run ArcMap.
  1. Open the ArcToolbox by selecting ArcToolbox from the Window menu.
  1. Right click inside the ArcToolbox and select the Add Toolbox option.
  1. Browse to the folder that contains PoP Analyst.
  1. Select the toolbox file for your version of ArcGIS. (e.g.  guiArcGIS93.tbx for ArcGIS 9.3)
  1. Click the Add button.
  1. Right click inside the ArcToolbox and select the Save Settings>To Default option.

# Upgrades #
  1. Close ArcMap.
  1. Delete the folder that contains PoP Analyst.
  1. Complete the installation process.

# Contents #
PoP Analyst contains 15 tools organized into 4 toolboxes and an additional toolbox with 3 models. These toolboxes are named Data Preprocessing, Computation, Visualization, Utilities, and Models, and are in order of typical use.

## Data Preprocessing ##
  * `*`Data File to Database File: Converts data to the DBF format
  * `*`Select: Creates a new file with only the desired data
  * Split: Splits data into multiple files

## Computation ##
  * `*`Create Areas Database File: Creates an encoding scheme for areas
  * `*`Create Sequence from Database File: Creates a sequence file using the encoding scheme

## Visualization ##
  * Georeference Imagery: Create the screen coordinate reference for imagery
  * Areas from Coordinates File: Create the areas using a coordinate file
  * Points from Database File: Create the points from a DBF file
  * Area from Coordinates: Create one area by specifying the coordinates
  * New Shapefile: Create an empty shapefile for editing later

`*`These tools are also available in batch form for processing all the files in a folder.

Each tool takes at least one file as input and produces at least one file as output. This modularity allows the use of graphical programming with ModelBuilder with the creation of intermediate files at each stage of processing. The Models toolbox contains models that have already been created using ModelBuilder and are intend to simplify the most common tasks.

For further information consult the [PoP Analyst Tutorial](tutSeq.md) and [User Guide](UserManual.md).