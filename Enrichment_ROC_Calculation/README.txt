Enrichment Calculation to evaluate the performance of models and programs.

This exercise was conducted to distinguish experimentally active compounds from random compounds using computational method. Multiple in-house built models of the drug-target were tested with three commercial computational screening engines. The drug-target models differed in their ability to accomodate drug compounds in their pockets, while the screening engines varied in the degree of sophistication in their internal scientific equation (XP > SP > HTVS). Please note that the calculation cost is proportional to the sophistication (XP > SP > HTVS).

As the plot reveals, the more sophiticated screening engine performed better in identifying true positives. In addition, it is also evident that some drug-target models performed better to distinguish the actives from inactives. We concluded that use of an enseble of drug-target models will produce the best results. In order to validate the method, we have purchased predicted true-positive compounds and tested experimentally. Indeed, the results confirmed the conclusion. More details in the publication: Mahasenan, K.V.; J. Chem. Inf. Model. 2012, 52 (5)1345

The plot was created with Python matplotlib. BASH linux scripting was used for automation of the workflow.

