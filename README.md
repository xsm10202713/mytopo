## CRY: **CR**eate topolog **Y** 
## Notice: 里面的代码我只是放上去了，有些半年都没用过了，如果有问题，赶紧告诉我。

 - [Summary](#summary)
 - [The definition of Topo_Raw_File](#the-definition-of-topo_raw_file)
 - [How to Run topo in mininet](#how_to_run_topo_in_mininet)
 - [Contributor & Author](#contributor-author)

#### Summary

This project is used to create various topologies in Mininet. 

Also include: 

- Create Topo_Raw_File for Data Center Topo (e.g., FatTree, BCube, DCell)

- Create Topo_Raw_File for Internet Topo in TopoZoo (http://www.topology-zoo.org/)

- Topo_Raw_File for Internet Topo: Stanford, CAIDA


#### The definition of Topo_Raw_File

Eg. fattree_4.trf

> 20 32 2 0

> 8 0

> 9 0

> ...

The first line has four numbers: **n m k h**, representative this topo has **n**  switches, **m** links , k = 1 (single way (TODO)) or 2 (double way), **h** hosts

And then, **m** lines follows. 

**8 0** represents these is a link between switch 0 and switch 8. (The index of switches starts from **0**) 


#### How to Run topo in mininet

1. read [build_topo_in_mininet.py]() file
2. you should have the basic understanding of Mininet, and the understanding of parameters in function [Mininet()]()
3. use your TRF file to replace the file_name in the first line of [simpleTest()]()
4. run this python file 
 

#### Contributor & Author

 - Haibo created the primary archetype
 - Hou Kaiyu published the 1.0 version 