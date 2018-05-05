#!/usr/bin/env sh

rm -f gor4/_gor4.so
make gor4/_gor4.so

pip install -r requirements.txt
