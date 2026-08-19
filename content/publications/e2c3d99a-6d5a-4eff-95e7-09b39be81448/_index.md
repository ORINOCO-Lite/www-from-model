---
title: Predictive modeling of significance thresholding in activation likelihood estimation
  meta-analysis
persons:
- simon-eickhoff
params:
  graphRootNodePID: xyzrins:publications/e2c3d99a-6d5a-4eff-95e7-09b39be81448
  sortkey: "2025Predictive modeling of significance thresholding in activation likelihood estimation meta-analysis"
  pid: xyzrins:publications/e2c3d99a-6d5a-4eff-95e7-09b39be81448
  doi: 10.1162/imag_a_00423
  date: '2025'
  title: Predictive modeling of significance thresholding in activation likelihood estimation
    meta-analysis
  description: "Activation Likelihood Estimation (ALE) employs voxel- or cluster-level\
    \ family-wise error (vFWE or cFWE) correction or threshold-free cluster enhancement\
    \ (TFCE) to counter false positives due to multiple comparisons. These corrections\
    \ utilize Monte-Carlo simulations to approximate a null distribution of spatial\
    \ convergence, which allows for the determination of a corrected significance threshold.\
    \ The simulations may take many hours depending on the dataset and the hardware\
    \ used to run the computations. In this study, we aimed to replace the time-consuming\
    \ Monte-Carlo simulation procedure with an instantaneous machine-learning prediction\
    \ based on features of the meta-analysis dataset. These features were created from\
    \ the number of experiments in the dataset, the number of subjects per experiment,\
    \ and the number of foci reported per experiment. We simulated 68,100 training datasets,\
    \ containing between 10 and 150 experiments and computed the vFWE, cFWE, and TFCE\
    \ significance thresholds. We then used this data to train one XGBoost regression\
    \ model for each thresholding technique. Lastly, we validated the performance of\
    \ the three models using 11 independent real-life datasets (21 contrasts) from previously\
    \ published ALE meta-analyses. The vFWE model reached near-perfect prediction levels\
    \ (R\xB2 = 0.996), while the TFCE and cFWE models achieved very good prediction\
    \ accuracies of R\xB2 = 0.951 and R\xB2 = 0.938, respectively. This means that,\
    \ on average, the difference between predicted and standard (monte-carlo based)\
    \ cFWE thresholds was less than two voxels. Given that our model predicts significance\
    \ thresholds in ALE meta-analyses with very high accuracy, we advocate our efficient\
    \ prediction approach as a replacement for the currently used Monte-Carlo simulations\
    \ in future ALE analyses. This will save hours of computation time and reduce energy\
    \ consumption. Furthermore, the reduced compute time allows for easier implementation\
    \ of multi-analysis set-ups like leave-one-out sensitivity analysis or subsampling."
  kind: bibo:AcademicArticle
  author:
  - pid: null
    given_name: null
    family_name: null
  - pid: xyzrins:persons/simon-eickhoff
    given_name: Simon
    family_name: Eickhoff
  - pid: null
    given_name: null
    family_name: null
  topic: []

---

