Grader
******

Grader is a custom assignment checker for a 3D modeling class, but it is flexible enough that it could be useful for some other purpose.
Written by Luis Naranjo

Installation
============

Pending

Usage
=====

When grader is run for the first time it creates a folder called 'grader' in My Documents (Windows) or Documents (Mac).

Here are the contents of 'grader':

settings.conf
students.txt
grader_files\
log.txt

settings.conf
-------------

Settings
^^^^^^^^

This file is where the projects are defined.

The file starts out with the following program settings:

**show members**

This controls whether the contents of a student's missing project are to be reported missing or not.

It can be either True or False

Example: show members = True

Putting this in settings.conf would make the grader report each missing file within a missing project.

If it were set to false, the grader would only report that the project is missing.

**capitalization**

This controls the capitalization of the student projects.

The grader relies on the consistency of the project/exercise naming.

Students are not the most reliable for correct formatting, so grader includes a way to normalize all of the files/folders in the grader_files folder.

capitalization has the following possible values: capitalize, lower, upper, title

capitalize only capitalizes the first word.

lower makes everything lower case.

upper makes everything upper case.

title capitalizes every word.

Example: capitalization = lower

This would make every folder and file in the grader_files folder lowercase.

Note:

* Watch out for upper and title, they can mess up your file extensions.
* If you don't set this correctly, grader won't function.

**log**

Projects
^^^^^^^^

This controls where grader's results are reported.

It can be either True or False

If it is True, the results are recorded in My Documents/grader/log.txt

If it is False, the results are printed to the command line and not saved.

You can define as many projects as you want
Each project can have as many exercises as you want.
Each exercise can have as many file extensions as you want.

grader_files
------------

This is the folder where you put the student projects.
Each folder should be named according to the following convention (things enclosed by brackets are variables):

{lastname} {projectname}

The exercises contained in these folders should follow the next convention:

{lastname} {exercisename}
