
# import os
import time
from datetime import datetime
import subprocess
from subprocess import PIPE, Popen

# define user on Delta, avoid writing files to other user's dir
user = subprocess.check_output("whoami").strip().decode("ascii")
# define desired location for output files within user dir
# ensures a new subfolder every run as long as new run is not started within same day as last run
#output_subdir = datetime.now().strftime("%b-%d-%y")
# don't use subprocess to retrieve date for subdir because runs might span over 2 days if they go overnight
output_subdir = '2023-01-20'

''' get hostnames from slurm file '''
with open(f'/u/{user}/viz-workflow/slurm/nodes_array.txt', 'r') as f:
  hostnames = f.read().splitlines()

print("Syncing footprints to nodes:\n\t", '\n\t'.join(hostnames))

count = 0
for hostname in hostnames:  
  # to use ssh in rsync (over a remote sheel) use the following: `rsync -rv --rsh=ssh hostname::module /dest``
  # see https://manpages.ubuntu.com/manpages/focal/en/man1/rsync.1.html (USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION)
  
  # mkdir then sync
  mkdir = ['mkdir', '-p', f'/scratch/bbou/{user}/IWP/output/{output_subdir}/staged/{hostname}']
  process = Popen(mkdir, stdin=PIPE, stdout=PIPE, stderr=PIPE)
  time.sleep(0.2)
  
  ssh = ['ssh', f'{hostname}',]
  rsync = ['rsync', '-r', '--update', '/tmp/staged/', f'/scratch/bbou/{user}/IWP/output/{output_subdir}/staged/{hostname}']
  cmd = ssh + rsync
  print(f"'{count} of {len(hostnames)}'. running command: {cmd}")
  count += 1
  
  process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

print("All jobs launched! They will work in the background WITHOUT stdout printing. ")

# otpional improvement
# shlex.split(s)  -- turn cmd line args into a list. 