#!/bin/bash
PIPENV="source bin/activate"
SCHEDULERON="dask-scheduler"
SCHEDULER_IP_PUB=$1
n_workers=$2
NTHREDS=$3
SCHEDULER_NODE="10.1.0.100"
WORKERON="dask-worker $SCHEDULER_NODE:8786 --nprocs 1 --nthreads $NTHREDS"
WORKERS=("10.1.0.1" "10.1.0.2" "10.1.0.3" "10.1.0.4" "10.1.0.5" "10.1.0.6" "10.1.0.7" "10.1.0.8" "10.1.0.9" "10.1.0.10" "10.1.0.11" "10.1.0.12" "10.1.0.13" "10.1.0.14" "10.1.0.15" "10.1.0.16")
CD="cd /storage/mquiroga/dask-env"
CD_WORK_SPACE="cd dask-worker-space"


$CD
$PIPENV
$CD_WORK_SPACE
$SCHEDULERON &

for ((i=0;i<n_workers; i++))
do  
    W="$CD; $PIPENV; $CD_WORK_SPACE; $WORKERON"
    ssh ${WORKERS[$i]} "$W" &
done

exit