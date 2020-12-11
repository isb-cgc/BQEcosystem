#!/usr/bin/env bash

cd ~/your/dir/here

for i in *.json ; do
    mv -v ${i} ${i%09.json}11.json
done