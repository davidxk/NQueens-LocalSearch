## N Queens Local Search
This repository implements the following local search methods.

* Hill Climbing
* Random Restart
* Simulated Annealing
* Local Beam Search
* Stochastic Beam Search

For demonstration, these algorithms are tested on the classic N Queens problem. To run these algorithms for N Queens, use command

```shell
$ python TestLocalSearch.py
```

Most of these local search algorithms have parameters that can be tuned to work with a specific problem, shown in the following table: 

| Algorithm              | Parameter                             |
| ---------              | ---------                             |
| Hill Climbing          | None                                  |
| Random Restart         | Number of restarts allowed            |
| Simulated Annealing    | Cooling schedule                      |
| Local Beam Search      | Beam width                            |
| Stochastic Beam Search | Beam width, value-probability mapping |

Implementation of these algorithms can be adapted according to specific problems to get better performance. For example, `FastNQueens.py` implements an adapted version of simulated annealing which runs 4 times faster than the standard implementation. 

#### Sample output
```text
Running local search for N Queens Problem
 - Please input the size of the board (4~15): 8 

fast_simulated_annealing
 - Accuracy: 10/10	Running time: 0.455810
hill_climbing
 - Accuracy:  1/10	Running time: 0.104400
random_restart
 - Accuracy:  5/10	Running time: 1.047240
simulated_annealing
 - Accuracy: 10/10	Running time: 1.364582
local_beam_search
 - Accuracy: 10/10	Running time: 1.838199
stochastic_beam_search
 - Accuracy: 10/10	Running time: 5.537936
```
