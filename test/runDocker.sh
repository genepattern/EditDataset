#!/bin/sh
docker run -v $PWD:$PWD -w $PWD -it genepattern/editdataset $1
