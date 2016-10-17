#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Some manual evaluation correction.
"""

correct_temp_pairs = [
    (
        "Find all *.csv files under /foo/bar and move them to some_dir\n",
        "find -exec mv File {} \; -name Pattern File"
    ),
    (
        "Find all .c and .h files in the current directory tree and search them for \"expr\"\n",
        "find -name Pattern File | xargs grep -r Pattern"
    ),
    (
        "Search the current directory tree for files containing \"sh\" in their names\n",
        "find -name Pattern File"
    ),
    (
        "display all the regular files in the folder \"$(FOLDER)\" which are modified in the last "
        "$(RETENTION)*24 hours and excluding hidden files\n",
        "find File -type Unknown -mtime Time ! -name Pattern"
    ),
    (
        "To list the number of directories in the `/usr/share' directory tree\n",
        "find /usr/share -type d | wc -l"
    ),
    (
        "search for a file in current folder excluding the search in the folder "
        "./ignored_directory\n",
        "find \\( -path File -prune -or -print \\) File"
    ),
    (
        "Delete files with inode number specified by [inode-number] under current directory\n",
        "find -exec ls -l {} \; -name Pattern -type d File"
    ),
    (
        "find all fonts which belong to a specific user\n",
        "find -print -user Pattern File"
    ),
    (
        "Remove all Thumbs.db files from the current directory tree\n",
        "find -name Pattern File | xargs rm -f"
    ),
    (
        "find all files in a folder that have a specific word in their name\n",
        "find -name Pattern -print -type f File"
    ),
    (
        "search for directories in the folder \"test\" which end with 5 digits using regular "
        "expressions\n",
        "find -regex Pattern -type d File"
    ),
    (
        "Search the current directory and its sub-directories for any file that has \"bsd\" "
        "somewhere in its name.\n",
        "find -name Pattern File"
    ),
    (
        "list all CSS files (and directories ending with “.css”) under the current directory\n",
        "find -ls -name Pattern File"
    ),
    (
        "find  file which case-insensitive name is too in currect directory\n",
        "find -path File File"
    ),
    (
        "Find files under current directory that contains the string '/bin/ksh'\n",
        "find -exec grep Pattern {} \; -print -type f File"
    ),
    (
        "find for a word in all the regular files in the current directory\n",
        "find -type f File | xargs grep -F Pattern"
    ),
    (
        "Find all files, starting from / but ignoring removable media, whose names end with "
        "\".rpm\"\n",
        "find ! -name Pattern File"
    ),
    (
        "search for a file in current folder excluding those that are present in a specific path\n",
        "find \\( -path File -prune -or -name Pattern \\) -print File"
    ),
    (
        "Find files with 777 permissions and change them to 755\n",
        "find -exec chmod Unknown {} \; -perm Permission -type f File"
    ),
    (
        "Find all files under and below the current working directory with the word California in "
        "the file, and count the number of lines in the output\n",
        "find -exec grep File Pattern {} \; -type f File | wc -l"
    ),
    (
        "Find the top 5 biggest files\n",
        "find -exec ls -s {} \; -type f File | sort -n -r | head -n Number"
    ),
    (
        "remove all the files in current folder which have the extension \"DS_Store\"\n",
        "find -exec rm -f {} \; -name Pattern -type f File"
    ),
    (
        "Move all Emacs backup files from the current directory tree to ~/backups/\n",
        "find -name Pattern File | xargs -I Pattern mv File {}"
    ),
    (
        "Return a list of files newer than file poop\n",
        "find -newer File -print File"
    ),
    (
        "find all files in the file system whose size is bigger than 3GB\n",
        "find -size Size -type f File"
    ),
    (
        "List all .svn files/directories under current directory\n",
        "find -name Pattern File | xargs ls -l"
    ),
    (
        "search for a word in all the files with the extension \"ch\" in the current folder\n",
        "find -exec grep Pattern {} + -name Pattern -type f File"
    ),
    (
        "search for a specific word in all the hidden files in the entire file system and display "
        "the file name along with the matched line\n",
        "find -name Pattern -print0 -type f File | xargs -0 -I {} grep -H -n Pattern {}"
    ),
    (
        "find the count of text files that are present in the current working directory.\n",
        "find -name Pattern File | wc -l"
    )]

error_temp_pairs = [
    (
        "find  file which case-insensitive name is too in currect directory\n",
        "find -name Pattern File"
    ),
    (
        "Search directory foo for files containing \"foo/bar\" in their full names\n",
        "find foo -type f -iname foo | grep foo"
    ),
    (
        "display all sqlite files in the current directory along with their timestamp\n",
        "find -name Pattern File"
    ),
    (
        "Find all *.tex regular files under current directory\n",
        "find -type Unknown File"
    ),
    (
        "List root's regular files with permissions 4000\n",
        "find -exec ls -l {} \; -perm Permission -type Unknown File"
    ),
    (
        "list regular file which file name end with 'cache' 'xml' or 'html' in current directory\n",
        "find -name Pattern -type Unknown File"
    ),
    (
        "search for a specific word in all the hidden files in the entire file system and display "
        "the file name along with the matched line\n",
        "find -name Pattern File | xargs grep Pattern"
    ),
    (
        "find all '*.c' files under $HOME directory which context contains sprintf\n",
        "find -exec grep -H File Pattern {} \; -name Pattern -type f File"
    ),
    (
        "change the ownership of all directories in the current folder\n",
        "find -exec chmod Unknown {} \; -type d File"
    ),
    (
        "find foo, Foo, FOo, FOO, etc.\n",
        "find -iname Pattern -type f File File"
    ),
    (
        "Delete all files in the \"${S}/bundled-libs\" folder except \"libbass.so\"\n",
        "find -delete \( -name Pattern -or -name Pattern -or -name Pattern \) -type f File"
    ),
    (
        "Find files that are 0 bytes in size in the current directory and remove them\n",
        "find -exec rm {} \; -size Size File"
    ),
    (
        "force delete all the directories in a folder which  have a specific name\n",
        "find -exec rm -f {} \; -name Pattern -type d File"
    ),
    (
        "copy the file header.shtml to each directory under dir1, dir2, dir3, or dir4\n",
        "find -exec cp File {} \; -name Pattern -type f File"
    )]

correct_str_pairs = [
    (
        "List all empty files in the current directory tree\n",
        "find . -empty"
    )]

error_str_pairs = [
    (
        "find  file which case-insensitive name is too in currect directory\n",
        "find . -iname \"filename\""
    ),
    (
        "search for files with the name \"temp\" in the /usr folder\n",
        "find /usr -name '*.sh'"
    ),
    (
        "Find all the files called FindCommandExamples.txt of owner root\n",
        "find / -user root -name tecmint.txt"
    ),
    (
        "Find all .c and .h files in the current directory tree and search them for \"expr\"\n",
        "find . -name '*.[ch]' | xargs grep -E 'expr'"
    ),
    (
        "Find all *.py files under and below the current directory and search them for \"xrange\"\n",
        "find . -name *.py | xargs grep some_function"
    ),
    (
        "Find all .c and .h files in the current directory tree and search them for \"expr\"\n",
        "find . -name \"*.c\" | xargs grep -E 'expr'"
    ),
    (
        "find all the swap files (files ending with ~) in the current folder and delete them\n",
        "find . -name \"*.sh\" -exec rm -r -f {} \;"
    ),
    (
        "display all files in the current directory excluding those that are present in the directories whose name starts with \"efence\" and do not search in the sub directories\n",
        "find \( -name Pattern -prune -or -name Pattern \) -print File"
    )]
