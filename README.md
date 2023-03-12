# TFT_Parse
*Parsing the tables from a Tabular Firing Table (TFT) to add to a SQLite database*

The tabular firing table is the base for all manual field artillery calculations. They are published by The U.S. Army Armament Research, Development and Engineering Center (ARDEC) and are available to those in the artillery community. Since they contain all the technical firing data of current US howitzers, they are not available publicly.

This parser parses the tables of technical data from this PDF and organizes it so it can be used to populate a SQLite Database in a Django webapp
