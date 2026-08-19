---
title: Translating phenotypic prediction models from big to small anatomical MRI data using
  meta-matching
persons:
- simon-eickhoff
params:
  graphRootNodePID: xyzrins:publications/1864cabc-1f89-48f7-83b0-8500a4bf0ed9
  sortkey: "2024Translating phenotypic prediction models from big to small anatomical MRI data using meta-matching"
  pid: xyzrins:publications/1864cabc-1f89-48f7-83b0-8500a4bf0ed9
  doi: 10.1162/imag_a_00251
  date: '2024'
  title: Translating phenotypic prediction models from big to small anatomical MRI data
    using meta-matching
  description: "Individualized phenotypic prediction based on structural magnetic resonance\
    \ imaging (MRI) is an important goal in neuroscience. Prediction performance increases\
    \ with larger samples, but small-scale datasets with fewer than 200 participants\
    \ are often unavoidable. We have previously proposed a \u201Cmeta-matching\u201D\
    \ framework to translate models trained from large datasets to improve the prediction\
    \ of new unseen phenotypes in small collection efforts. Meta-matching exploits correlations\
    \ between phenotypes, yielding large improvement over classical machine learning\
    \ when applied to prediction models using resting-state functional connectivity\
    \ as input features. Here, we adapt the two best performing meta-matching variants\
    \ (\u201Cmeta-matching finetune\u201D and \u201Cmeta-matching stacking\u201D) from\
    \ our previous study to work with T1-weighted MRI data by changing the base neural\
    \ network architecture to a 3D convolution neural network. We compare the two meta-matching\
    \ variants with elastic net and classical transfer learning using the UK Biobank\
    \ (N = 36,461), the Human Connectome Project Young Adults (HCP-YA) dataset (N =\
    \ 1,017), and the HCP-Aging dataset (N = 656). We find that meta-matching outperforms\
    \ elastic net and classical transfer learning by a large margin, both when translating\
    \ models within the same dataset and when translating models across datasets with\
    \ different MRI scanners, acquisition protocols, and demographics. For example,\
    \ when translating a UK Biobank model to 100 HCP-YA participants, meta-matching\
    \ finetune yielded a 136% improvement in variance explained over transfer learning,\
    \ with an average absolute gain of 2.6% (minimum = \u20130.9%, maximum = 17.6%)\
    \ across 35 phenotypes. Overall, our results highlight the versatility of the meta-matching\
    \ framework."
  kind: bibo:AcademicArticle
  author:
  - pid: xyzrins:persons/simon-eickhoff
    given_name: Simon
    family_name: Eickhoff
  topic: []

---

