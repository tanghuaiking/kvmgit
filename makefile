EXECS=king
CC=gcc

all=${EXECS}

king:hello.c
	$(CC)  hello.c -o king

clean:
	rm -f ${EXECS}
