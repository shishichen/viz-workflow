# import os
import time
from datetime import datetime
import subprocess
from subprocess import PIPE, Popen
import pprint
import PRODUCTION_IWP_CONFIG
IWP_CONFIG = PRODUCTION_IWP_CONFIG.IWP_CONFIG

#import lake_change_config
#IWP_CONFIG = lake_change_config.IWP_CONFIG

# set config properties for current context
#IWP_CONFIG['dir_staged'] = IWP_CONFIG['dir_staged_local']
SOURCE = '/tmp/' + 'log.log'
IWP_CONFIG['dir_staged'] = IWP_CONFIG['dir_staged_remote']
DESTINATION = IWP_CONFIG['dir_staged']

print("Using config: ")
pprint.pprint(IWP_CONFIG)

# define user on Delta, avoid writing files to other user's dir
user = subprocess.check_output("whoami").strip().decode("ascii")
# define desired location for output files within user dir
# ensures a new subfolder every run as long as new run is not started within same day as last run
#output_subdir = datetime.now().strftime("%b-%d-%y")
# don't use subprocess to retrieve date for subdir because runs might span over 2 days if they go overnight
#output_subdir = "iwp_testRun_20230131"
#output_subdir = '2023-01-20'

''' get hostnames from slurm file '''
with open(f'/u/{user}/viz-workflow/slurm/nodes_array.txt', 'r') as f:
  hostnames = f.read().splitlines()

print("Syncing staged files to nodes:\n\t", '\n\t'.join(hostnames))

count = 0
for hostname in hostnames:  
  # to use ssh in rsync (over a remote sheel) use the following: `rsync -rv --rsh=ssh hostname::module /dest``
  # see https://manpages.ubuntu.com/manpages/focal/en/man1/rsync.1.html (USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION)
  
  # no need to mkdir for node cause was already made when transferred staged dir
  
  ssh = ['ssh', f'{hostname}',] # from juliet: does this have to end in comma cause it is concatenated with rsync command below?
  # old command before we separated paths into LOCAL and REMOTE:
  # rsync = ['rsync', '-r', '--update', '/tmp/staged/', f'/scratch/bbou/{user}/IWP/output/{output_subdir}/staged/{hostname}']
  # new command now that we separated paths into LOCAL and REMOTE:
  rsync = ['rsync', '-r', '--update', SOURCE, f"{DESTINATION}{hostname}/log.log"]
  cmd = ssh + rsync
  print(f"'{count} of {len(hostnames)}'. running command: {cmd}")
  count += 1
  
  process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

print("Job launched! It will work in the background WITHOUT stdout printing. ")
