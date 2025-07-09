# BQ SQL Examples
The BQ_SQL_Examples/bq_ecosys_bq_useful_join.csv file is a collection of useful SQL examples to display in the BQ Table Search. This file needs to be saved as a CSV UTF-8 file.

1. The first line is the header.
2. Each column is separated by a comma (,) character.
3. Each line is separated by a carriage return (\r\n). 
4. There are 7 columns.
	1) Program: List of applicable programs separated by semicolons (e.g., BEATAML1_0; CMI; CPTAC; TARGET).
	2) Data Type: List of data types separated by semicolons (e.g., Clinical Data;Gene Expression).
	3) Title: The title of the join example, wrapped by double quotes (")
	4) Description: A short description of the joins example, wrapped in double quotes ("").
	5) Table: List of tables in a template format, separated by semicolons (e.g., isb-cgc-bq).[PROGRAM].clinical_gdc_current; isb-cgc-bq.[PROGRAM].RNAseq_hg38_gdc_current)
	6) Join condition: The condition that goes into the 'JOIN ON [CONDITION]' (e.g., clin.submitter_id = rnaseq.case_barcode)
	7) SQL Query: The example in the SQL statement. The first line usually starts with a comment starting with a '#' character. Each line within the SQL statement is separated by a newline feed (\n) and not by a carriage return (\r).

Tips: It's easier to edit the content in an Excel spreadsheet. When saving, ensure the file is saved with a CSV UTF-8 format (important!).

