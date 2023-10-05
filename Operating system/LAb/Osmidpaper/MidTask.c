#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int num;
    int pipefd[2];
    pid_t pid;

    if (pipe(pipefd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) 
    {             // child process
    
        close(pipefd[1]);  	// close unused write end of the pipe
        
        read(pipefd[0], &num, sizeof(num));  // read from pipe
        
        int fact = factorial(num);
        printf("Factorial of %d is %d\n", num, fact);
        
        close(pipefd[0]);  		// close read end of the pipe
        exit(EXIT_SUCCESS);
        
    } 
    else
     {  // parent process
     
        close(pipefd[0]);  // close unused read end of the pipe
        
        printf("Enter a number to find its factorial: ");
        scanf("%d", &num);
        
        write(pipefd[1], &num, sizeof(num));  // write to pipe
        
        close(pipefd[1]);  // close write end of the pipe
        
        wait(NULL);  // wait for child to finish
        
        exit(EXIT_SUCCESS);
    }
}

