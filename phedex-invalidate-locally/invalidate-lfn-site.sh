#!/bin/bash
SITE="T2_US_Caltech"
PHEDEX_ROOT=$(echo $PHEDEX_CONFIG_FILE | awk -F"Config" '{print $1}')
if [ -z "$(./search-replicas.sh $1 | grep "no other replica")" ] ; then
        #echo "other replicas in the grid, deleting : $1"
        #echo $PHEDEX_ROOT/Utilities/FileDeleteTMDB --db /wntmp/phedex/info/DBParam.Site:Prod/T2USCALTECH -node T2_US_Caltech  \
        echo "present in other locations than $SITE : $1"

else
        #echo "file is unique, report to transfers team : $1"
        echo "unique to $SITE : $1"
fi
