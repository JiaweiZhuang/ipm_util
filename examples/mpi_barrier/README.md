Steps to re-generate the same log file

Install at IPM at $IPM_PREFIX and set:

    export LD_PRELOAD="$IPM_PREFIX/lib/libipm.so $IPM_PREFIX/lib/libipmf.so"
    IPM_LOG=terse

(My [IPM_Docker](https://github.com/JiaweiZhuang/IPM_Docker) image already have IPM set up)

Compile and run test script:

    mpif90 -o mpi_barrier_test.x mpi_barrier_test.f90
    mpirun -np 4 ./mpi_barrier_test.x
