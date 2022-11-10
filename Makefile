output: solver.o
	g++ solver.o -o solver

solver.o: solver.cpp
	g++ -c solver.cpp

clean:
	rm *.o