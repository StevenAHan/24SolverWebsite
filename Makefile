output: solver.o
	gcc solver.o -o solver

solver.o: solver.cpp
	gcc -c solver.cpp

clean:
	rm *.o