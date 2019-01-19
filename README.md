CYK Algorithm Solver
====================

This was a side project to make some homework problems easier in CS 4413, Automata and Formal Language Theory

It uses the [Cocke-Younger-Kasami algorithm](https://en.wikipedia.org/wiki/CYK_algorithm) 
to check if a string is accepted by a given context-free grammar.

Input is a text file containing a series of production rules for the grammar, all in [Chomsky Normal Form](https://en.wikipedia.org/wiki/Chomsky_normal_form)

The program outputs whether the string is accepted, as well as outputting the normally hand-written table to a CSV.