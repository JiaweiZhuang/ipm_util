program mpi_test
implicit none

include 'mpif.h'
integer rank, size, ierror

call MPI_INIT(ierror)
call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)
call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)
print*, 'node', rank, ': Hello world'

call MPI_Barrier(  MPI_COMM_WORLD, ierror)
if (rank .eq. 0) then
    call SLEEP(3)  ! delaying everyone else
end if
call MPI_Barrier(  MPI_COMM_WORLD, ierror)

call MPI_FINALIZE(ierror)

end
