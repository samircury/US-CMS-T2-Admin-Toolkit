#!/bin/bash
SITE="T2_US_Caltech"
if [ -z "$(./search-replicas.sh $1 | grep "no other replica")" ] ; then
        echo "other replicas in the grid, deleting : $1"
else
        echo "file is unique, report to transfers team : $1"
fi
