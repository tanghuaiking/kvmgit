EXECS=king
cc=gcc

all:${EXECS}
king:hello.c
	$ cc  hello.c -o king

clean:
	rm -f ${EXECS}
