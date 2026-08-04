---
title: 'Voxel-wise or Region-wise Nuisance Regression for Functional Connectivity Analyses:
  Does it matter?'
persons:
- simon-eickhoff
params:
  graphRootNodePID: xyzrins:publications/3c5cdd23-c3be-443e-88ca-c4f357451b15
  sortkey: "NoneVoxel-wise or Region-wise Nuisance Regression for Functional Connectivity Analyses: Does it matter?"
  pid: xyzrins:publications/3c5cdd23-c3be-443e-88ca-c4f357451b15
  doi: 10.1101/2024.12.10.627766
  date: null
  title: 'Voxel-wise or Region-wise Nuisance Regression for Functional Connectivity
    Analyses: Does it matter?'
  description: Removal of nuisance signals (such as motion) from the BOLD time series
    is an important aspect of preprocessing to obtain meaningful resting-state functional
    connectivity (rs-FC). The nuisance signals are commonly removed using denoising
    procedures at the finest resolution, i.e. the voxel time series. Typically the voxel-wise
    time series are then aggregated into predefined regions or parcels to obtain a rs-FC
    matrix as the correlation between pairs of regional time series. Computational efficiency
    can be improved by denoising the aggregated regional time series instead of the
    voxel time series. However, a comprehensive comparison of the effects of denoising
    on these two resolutions is missing.In this study, we systematically investigate
    the effects of denoising at different time series resolutions (voxel- and region-level)
    in 370 unrelated subjects from the  1HCP-YA dataset. Alongside the time series resolution,
    we considered additional factors such as aggregation method (Mean and first eigenvariate
    [EV]) and parcellation granularity (100, 400, and 1,000 regions). To assess the
    effect of those choices on the utility of the resulting whole-brain rs-FC, we evaluated
    the individual specificity (fingerprinting) and the capacity to predict age and
    three cognitive scores.Our findings show generally equal or better performance for
    region-level denoising with notable differences depending on the aggregation method.
    Using mean aggregation yielded equal individual specificity and prediction performance
    for voxel- and region-level denoising. When EV was employed for aggregation, the
    individual specificity of voxel-level denoising was reduced compared to region-level
    denoising. Increasing parcellation granularity generally improved individual specificity.
    For the prediction of age and cognitive test scores, only fluid intelligence indicated
    worse performance for voxel-level denoising in the case of aggregating with the
    EV.Based on these results, we recommend the adoption of region-level denoising for
    brain-behavior investigations when using mean aggregation. This approach offers
    equal individual specificity and prediction capacity with reduced computational
    resources for the analysis of rs-FC patterns.
  kind: bibo:Manuscript
  author:
  - pid: null
    given_name: null
    family_name: null
  - pid: null
    given_name: null
    family_name: null
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

