Hi! Welcome to our project for CS 230.

To clean the OASIS dataset:
1) Download all 12 disks of the OASIS 1 data from https://www.oasis-brains.org/
2) Unzip all images using tar.
3) Move all cross-sectional MRIs into their own folder (called oasis_images).
4) Run oasis_rename_files.py, which will rename all files to be simply the patient ID.
5) Run oasis_sort_clean.py, which will remove all files that do not have a CDR value, and thus cannot be classified.
