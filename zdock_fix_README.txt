zdock_fix v1.1 Readme
Author: Colin Welsh
__________________________________________________________________________________________

Purpose: Removes unnecessary information from files from ZDock that prevent the file
from being opened in Chimera.
__________________________________________________________________________________________

Requirements: Python 3.4.3 or later
__________________________________________________________________________________________

To use: Place zdock_fix.py into the directory containing the 10 prediction
files from ZDock (complex.1.pdb; complex.2.pdb) and run the file via the terminal.
To do this, open the terminal and enter:
	
			cd *directory of zdock files here*
				example: Desktop/top_preds/
			
Then enter:

			python3 zdock_fix.py
			
The program will run, first prompting you to enter an antibody name (ex. PLA2R) and
then a cap name, the 4 character identifier from PDB (ex. 5IMK). The program will run
and output ten new files that are compatible with Chimera. The program will also output 
the proteins.pdb files required by ROSIE in a separate folder in the same directory.