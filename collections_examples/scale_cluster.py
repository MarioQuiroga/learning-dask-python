import os
import time
 
def init_cluster(scheduler_ip, n_workers, n_cores):
    os.system('./init_cluster.sh ' + scheduler_ip + ' ' + n_workers + ' ' + n_cores)
    
def kill_cluster(scheduler_ip):
    os.system('./kill_cluster.sh ' + scheduler_ip)

    
    