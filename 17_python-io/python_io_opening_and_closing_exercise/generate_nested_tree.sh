#!/bin/bash

if [ -d "dir_to_remove" ]; then
  rm -rf dir_to_remove
fi

mkdir -p dir_to_remove/dir1/dir11
mkdir -p dir_to_remove/dir1/dir12
mkdir -p dir_to_remove/dir2/dir21/dir211/dir111
mkdir -p dir_to_remove/dir2/dir21/dir211
mkdir -p dir_to_remove/empty_subdir

touch dir_to_remove/text1.txt
touch dir_to_remove/text2.txt
touch dir_to_remove/dir1/dir11/text1.txt
touch dir_to_remove/dir1/dir11/text2.txt
touch dir_to_remove/dir2/dir21/dir211/dir111/text_document.txt
touch dir_to_remove/dir2/dir21/dir211/text_document.txt
touch dir_to_remove/dir2/dir21/text1.txt
touch dir_to_remove/dir2/dir21/text2.txt
touch dir_to_remove/dir2/text1.txt
touch dir_to_remove/dir2/text2.txt
