# Simulation: 10 Prisoners

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/100_prisoners_problem_qtl1.svg/310px-100_prisoners_problem_qtl1.svg.png)](https://en.wikipedia.org/wiki/File:100_prisoners_problem_qtl1.svg)

The Python 3 script `prisoners.py` performs a simple simulation set up to explore the [100 Prisoners problem](https://en.wikipedia.org/wiki/100_prisoners_problem) (but with 10 prisoners by default; change the values of `PRISONERS` and `GUESSES` in the script as needed) originally formulated by Peter Bro Miltersen and expressed by Philippe Flajolet and Robert Sedgewick as follows:

> The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. The drawers are closed again afterwards. If, during this search, every prisoner finds his number in one of the drawers, all prisoners are pardoned. If just one prisoner does not find his number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy—but may not communicate once the first prisoner enters to look in the drawers. What is the prisoners' best strategy?

## Use

`prisoners.py` can be run from the console:

```
python prisoners.py [options]
```

### Options

|[options]|Action|
|:--|:--|
|`--help` or `-h`|Display script use instructions|
|`--random` or `-r`|Produce a verbose example simulation in which prisoners randomly pick drawers|
|`--random N` or `-r N`|(`N` an integer) Perform `N` simulations in which prisoners randomly pick drawers|
|`--sequence` or `-s`|Produce a verbose example simulation in which prisoners sequentially pick drawers|
|`--sequence N` or `-s N`|(`N` an integer) Perform `N` simulations in which prisoners sequentially pick drawers|

### Examples

* Simulate prisoners searching drawers sequentially:

```
python prisoners.py -s > example-seq.txt
```

Example output (`example-seq.txt`):

```txt
Call: prisoners.py -s

Method: sequential

Card placement:

Drawer	Card
1     	4
2     	7
3     	9
4     	8
5     	10
6     	5
7     	2
8     	6
9     	1
10    	3

  Prisoner 1's turn...
    Guess 1: Peeks in drawer 1...
      Finds card 4.
    Guess 2: Peeks in drawer 4...
      Finds card 8.
    Guess 3: Peeks in drawer 8...
      Finds card 6.
    Guess 4: Peeks in drawer 6...
      Finds card 5.
    Guess 5: Peeks in drawer 5...
      Finds card 10.
        Too bad!

  Prisoner 2's turn...
    Guess 1: Peeks in drawer 2...
      Finds card 7.
    Guess 2: Peeks in drawer 7...
      Finds card 2.
        Success!

  Prisoner 3's turn...

    .
    .
    .


  Prisoner 10's turn...
    Guess 1: Peeks in drawer 10...
      Finds card 3.
    Guess 2: Peeks in drawer 3...
      Finds card 9.
    Guess 3: Peeks in drawer 9...
      Finds card 1.
    Guess 4: Peeks in drawer 1...
      Finds card 4.
    Guess 5: Peeks in drawer 4...
      Finds card 8.
        Too bad!

Total successes: 2
```

* Simulate prisoners searching draws sequentially:

```
python prisoners.py -s 10000 > example-seq-10000.txt
```

Example output (`example-seq-10000.txt`):

```
Call: prisoners.py -s 10000


10000 simulations, sequential searching:
  Average number of prisoners finding their cards: 4.9982
  Number of simulations in which all 10 prisoners found their cards: 3554

Data:

10	10	10	10	10	0 	4 	10	4 	0 	3 	10	2 	0 	10	0 	3 	0 	2 	4 
3 	2 	3 	3 	3 	10	10	3 	10	0 	0 	3 	10	4 	4 	10	3 	4 	10	4 

   .
   .
   .

```

## This repository's contents

* `README.md`, this file.
* `prisoners.py`, the script.
* `example-rand.txt`, verbose, single simulation, random method.
* `example-rand-100000.txt`, data output for 100000 simulations, random method.
* `example-seq.txt`, verbose, single simulation, sequential method.
* `example-seq-100000.txt`, data output for 100000 simulations, sequential method.

