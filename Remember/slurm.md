## Resource Manager and Job Schdular

Where there is more work than resources, the job scheduler manages queues of work.

MPI
- flavors
    + OpenMPI
    + MPICH1
    + MVAPICH
    + MPICH2

Simple Linux Utility for Resource Management (Slurm)
- written in C
- various system-specific plugins


### Darmons

**slurmctld** - Central controller, one each cluster
**slurmd** - Compute node daemon, one each node
**slurmdbd** - Database Daemon, one per enterpise
**slurmstepd** - one per job step


```bash
# -c clear previous state, purge all job, step, partition state
# -D run in forgraound ,logs are written to stdout
# -v Verboase, more v means more messages
slurmctld -Dcvvvv
slurmd -Dcvvv

# -C print node's current configuration and exit, this can be used as input to SLURM configuration file
slurmd -C

```

### Commands
sbatch - Submit script for later execution
salloc - create job allocation and start a shell to use it (interactive mode)
srun - create a job allocation and lauch a job step (usally MPI)
sattch - Connect stdin/out/err for an existing job or job step
squeue --job ### - check job status
scancel ### - cancel a job given job number
```bash
sbatch -ntask=1 --time=10 pre_process.bash
# Submitted batch job 45001
sbatch --ntask=128 --time=60 --depend=45001 do_work.bash

# Submitted batch job 45002
sbatch --ntask=1 --time=30 --depend=45002 post_process.bash
```