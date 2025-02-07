#!/bin/bash

if [ -d "flat_dir_to_remove" ]; then
  rm -rf flat_dir_to_remove
fi

mkdir flat_dir_to_remove

touch flat_dir_to_remove/text1.txt
touch flat_dir_to_remove/text2.txt
