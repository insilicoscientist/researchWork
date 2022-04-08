Enrichment Calculation to evaluate the performance of structural models and structure-based screening methods.

This exercise was conducted to distinguish experimentally active compounds from random compounds using computational method. Multiple in-house structural models of the kinase were tested with three computational screening engines. The kinase models differed in their ability to accomodate drug compounds in their pockets, while the screening engines varied in the degree of sophistication in their internal scientific equation (XP > SP > HTVS). Please note that the calculation cost is proportional to the sophistication (XP > SP > HTVS).

As the plot reveals, the more sophiticated screening engine performed better in identifying true positives. In addition, it is also evident that some kinase protein models performed better to distinguish the actives from inactives. We concluded that use of an ensemble of kinase strutural models will produce the best results. In order to validate the method, we have experimentally tested predicted true-positive compounds. Indeed, the wet-lab results validated the conclusion. More details in the publication: Mahasenan, K.V.; J. Chem. Inf. Model. 2012, 52 (5)1345. https://pubs.acs.org/doi/abs/10.1021/ci300040c

The plot was created with Python matplotlib. BASH linux scripting was used for automation of the workflow.

