ROSIE Preparer v1.0 Readme
Author: Colin Welsh
__________________________________________________________________________________________

Purpose: Removes unnecessary information from .pdb files that result in ROSIE errors and
correctly formats files for use by ROSIE.

Proper file format includes:
	* Only ATOM, TER, and END lines
	* TER lines between chains
	* Appropriate length lines that seem to reduce the probability of ROSIE returning
	  an error.
	  
NOTE: This script does NOT properly name your chains. You must do that manually via
Chimera.
__________________________________________________________________________________________

Requirements: Python 3.4.3 or later
__________________________________________________________________________________________

To use: Place rosie_prep.py into the directory containing your .pdb file you wish to
run on ROSIE and run the file via the terminal.

To run from the terminal, open the terminal and enter:
	
			cd *directory of zdock files here*
				example: Desktop/top_preds/
			
Then enter:

			python3 rosie_prep.py
			
The program will run, prompting you to enter the filename of the .pdb file to be
converted. NOTE: You must include ".pdb" when entering the filename. The script will
then output a file called proteins.pdb that is ready to be used with ROSIE.

NOTE: The script will overwrite any file called "proteins.pdb" that is preexisting in
its directory. Make sure that there is no file called "proteins.pdb" where you place
the script.