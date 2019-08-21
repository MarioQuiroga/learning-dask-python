#!/bin/bash
PIPENV="source bin/activate"
SCHEDULERON="dask-scheduler"
SCHEDULER_IP_PUB=$1
n_workers=$2
NTHREDS=$3
SCHEDULER_NODE="10.1.0.100"
WORKERON="dask-worker $SCHEDULER_NODE:8786 --nprocs $n_workers --nthreads $NTHREDS"
WORKERS=("nodo1" "nodo2" "nodo3" "nodo4" "nodo5" "nodo6" "nodo7" "nodo8" "nodo9" "nodo10" "nodo11" "nodo12" "nodo13" "nodo14" "nodo15" "nodo16")
CD="cd dask-env"
CD_WORK_SPACE="cd dask-worker-space"

ssh $SCHEDULER_IP_PUB -p 2244 -l mquiroga "$CD; $PIPENV; $CD_WORK_SPACE; $SCHEDULERON" &

for ((i=0;i<16; i++))
do  
    W="ssh ${WORKERS[$i]} \"$CD; $PIPENV; $CD_WORK_SPACE; $WORKERON\""
    ssh $SCHEDULER_IP_PUB -p 2244 -l mquiroga "$W" &
done

exit