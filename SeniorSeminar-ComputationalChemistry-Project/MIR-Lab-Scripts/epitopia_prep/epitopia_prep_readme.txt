Epitopia Prep v2.1 Readme
Author: Colin Welsh
__________________________________________________________________________________________

Purpose: Adds SEQRES header to .pdb files that are required by Epitopia. Renumbers
protein sequence if necessary.
__________________________________________________________________________________________

Requirements: Python 3.4.3 or later
__________________________________________________________________________________________

To use: Place epitopia_prep.py into the directory containing your .pdb file you wish to
submit to Epitopia and run the file via the terminal.

To run from the terminal, open the terminal and enter:
	
			cd *directory of .pdb file here*
				example: Desktop/Research\ Program/PLA2R_models/
			
Then enter:

			python3 epitopia_prep.py
			
The program will run, prompting you to enter the filename of the .pdb file to be
converted. NOTE: You must include ".pdb" when entering the filename. The script will
then output a file with the name epitopia_*filename*.pdb.