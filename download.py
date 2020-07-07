#!/bin/true
#
# git.py - part of autospec
# Copyright (C) 2015 Intel Corporation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Commit to git
#

import glob
import os
import sys
import subprocess
import hashlib
import re
import shlex
import urllib3
import shutil

def main():
# def clone_and_git_archive_all(path, name, url, branch = 'master', is_fatal=True):
	branch = 'master'
	is_fatal=True
	path=os.getcwd()
	url='https://github.com/so-fancy/diff-so-fancy.git'
	cmd_args = f'{branch} {url} clone_archive'
	clone_path = f'{path}'
	print('Teste: ' + 'git clone --depth=1 --branch ' + cmd_args + '\n')
	print('Teste: cwd=path ' + path + '\n')
	try:
		call(f'git clone --depth=1 --branch {cmd_args}', cwd=path)
	except subprocess.CalledProcessError as err:
		if is_fatal:
			print_fatal('Unable to clone {} in {}: {}'.format(url, clone_path, err))
			sys.exit(1)

def call(command, logfile=None, check=True, **kwargs):
	"""Subprocess.call convenience wrapper."""
	returncode = 1
	full_args = {
		"args": shlex.split(command),
		"universal_newlines": True,
	}
	full_args.update(kwargs)

	if logfile:
		full_args["stdout"] = open(logfile, "w")
		full_args["stderr"] = subprocess.STDOUT
		returncode = subprocess.call(**full_args)
		full_args["stdout"].close()
	else:
		returncode = subprocess.call(**full_args)

	if check and returncode != 0:
		raise subprocess.CalledProcessError(returncode, full_args["args"], None)

	return returncode

def print_fatal(message):
	"""Print fatal error, color coded for TTYs."""
	_print_message(message, 'FATAL', 'red')
	
def _supports_color():
	# FIXME: check terminfo instead
	return sys.stdout.isatty()


def _print_message(message, level, color=None):
	prefix = level
	if color and _supports_color():
		# FIXME: use terminfo instead
		if color == 'red':
			params = '31;1'
		elif color == 'green':
			params = '32;1'
		elif color == 'yellow':
			params = '33;1'
		elif color == 'blue':
			params = '34;1'
		prefix = f'\033[{params}m{level}\033[0m'
	print(f'[{prefix}] {message}')
	
if __name__ == '__main__':
	main()
