import os
import sys
import shutil
import logging
from datetime import datetime

from configobj import ConfigObj

DEBUG = False
show_members = True

home = os.path.expanduser('~')
source_root = os.path.abspath(os.path.dirname(__file__))
skeleton_grader = os.path.join(source_root, 'skeleton_grader')


if sys.platform == 'win32':
    documents = os.path.join(home, 'My Documents')

if sys.platform in ['linux2', 'darwin']:
    documents = os.path.join(home, 'Documents')

project_root = os.path.join(documents, 'grader')


if not os.path.isdir(project_root):
    shutil.copytree(skeleton_grader, project_root)

settings_path = os.path.join(project_root,'settings.conf')
students_path = os.path.join(project_root, 'students.txt')
log_path = os.path.join(project_root, 'log.txt')
grader_path = os.path.join(project_root, 'grader_files')

for filepath in [settings_path, students_path, log_path]:
    try:
        assert os.path.isfile(filepath)
    except AssertionError, error:
        print error

if not DEBUG:
    logging.basicConfig(format='%(message)s', filename=log_path)

if DEBUG:
    logging.basicConfig(format='%(levelname)s:%(message)s')

config = ConfigObj(settings_path)
#{'project 3': {'exercise 1': ['.jpg', '.3dm'], 'exercise 2': '.3dm'}}

students = list()
#[('Luis Naranjo', ' 3B'), ('Miguel Pobre', ' 3B'), ('Christina Oglesby', None)]

with open(students_path) as fh:
    students = [line.strip() for line in fh.readlines()]

date = datetime.now().strftime('%B %d %Y %I:%M %P')
entry_title = "log entry on %r" % date

logging.warning(entry_title.center(70))

for project in config:
    project = project.lower()
    for lastname in students:
        lastname = lastname.lower()
        exercises = config[project]  # {'exercise 1': ['.jpg', '.3dm'], 'exercise 2': '.3dm'}
        expected_foldername = '%s %s' % (lastname, project)
        expected_folder = os.path.join(grader_path, expected_foldername)
        if not os.path.isdir(expected_folder):
            warning = "%s is missing %s folder" % (lastname, project)
            logging.warning(warning)
            if not show_members: continue

        for exercise in exercises:
            extensions = exercises[exercise]
            if isinstance(extensions, str):
                extensions = [extensions]

            assert isinstance(extensions, list)

            for ext in extensions:
                expected_exercise_name = '%s %s%s' % (lastname, exercise, ext)

                expected_exercise = os.path.join(expected_folder, expected_exercise_name)
                if not os.path.isfile(expected_exercise):
                    logging.warning('%s is missing %s:%s' % (lastname, project, exercise+ext))

logging.warning('')



