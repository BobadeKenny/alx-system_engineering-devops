#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main()
{
pid_t child_pid;
int i;
for(i = 0; i < 5; i++)
{
child_pid = fork();
printf("Zombie process created, PID: %d\n", child_pid);
if(child_pid > 0)
{
    sleep(1);
}
else
{
    exit(0);
}
}
infinite_while();
}
