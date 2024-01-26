#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - self-explanatory
 * Return: 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main program function
 * Return: EXIT_FAILURE if failed at creating a process, 0 otherwise
*/

int main(void)
{
	size_t i = 0;
	pid_t my_pid;

	for (i = 0; i < 5; i++)
	{
		my_pid = fork();
		if (my_pid)
			printf("Zombie process created, PID: %i\n", my_pid);
		else
			exit(EXIT_FAILURE);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
