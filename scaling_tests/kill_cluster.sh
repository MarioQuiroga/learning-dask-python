#!/bin/bash
SCHEDULER_IP_PUB=$1
SCHEDULER_NODE="10.1.0.100"
WORKERS=("10.1.0.1" "10.1.0.2" "10.1.0.3" "10.1.0.4" "10.1.0.5" "10.1.0.6" "10.1.0.7" "10.1.0.8" "10.1.0.9" "10.1.0.10" "10.1.0.11" "10.1.0.12" "10.1.0.13" "10.1.0.14" "10.1.0.15" "10.1.0.16")

KILLSCHEDULER="pkill dask-scheduler"
KILLWORKER="pkill dask-worker"

$KILLSCHEDULER

for ((i=0;i<16; i++))
do  
    ssh ${WORKERS[$i]} "$KILLWORKER" &
done
rm -R /storage/mquiroga/dask-env/dask-worker-space/*
exit