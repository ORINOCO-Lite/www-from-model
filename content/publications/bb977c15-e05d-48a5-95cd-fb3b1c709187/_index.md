---
title: 'Multilayer meta-matching: translating phenotypic prediction models from multiple
  datasets to small data'
persons:
- simon-eickhoff
params:
  graphRootNodePID: xyzrins:publications/bb977c15-e05d-48a5-95cd-fb3b1c709187
  sortkey: "NoneMultilayer meta-matching: translating phenotypic prediction models from multiple datasets to small data"
  pid: xyzrins:publications/bb977c15-e05d-48a5-95cd-fb3b1c709187
  doi: 10.1101/2023.12.05.569848
  date: null
  title: 'Multilayer meta-matching: translating phenotypic prediction models from multiple
    datasets to small data'
  description: Resting-state functional connectivity (RSFC) is widely used to predict
    phenotypic traits in individuals. Large sample sizes can significantly improve prediction
    accuracies. However, for studies of certain clinical populations or focused neuroscience
    inquiries, small-scale datasets often remain a necessity. We have previously proposed
    a "meta-matching" approach to translate prediction models from large datasets to
    predict new phenotypes in small datasets. We demonstrated large improvement of meta-matching
    over classical kernel ridge regression (KRR) when translating models from a single
    source dataset (UK Biobank) to the Human Connectome Project Young Adults (HCP-YA)
    dataset. In the current study, we propose two meta-matching variants ("meta-matching
    with dataset stacking" and "multilayer meta-matching") to translate models from
    multiple source datasets across disparate sample sizes to predict new phenotypes
    in small target datasets. We evaluate both approaches by translating models trained
    from five source datasets (with sample sizes ranging from 862 participants to 36,834
    participants) to predict phenotypes in the HCP-YA and HCP-Aging datasets. We find
    that multilayer meta-matching modestly outperforms meta-matching with dataset stacking.
    Both meta-matching variants perform better than the original "meta-matching with
    stacking" approach trained only on the UK Biobank. All meta-matching variants outperform
    classical KRR and transfer learning by a large margin. In fact, KRR is better than
    classical transfer learning when less than 50 participants are available for finetuning,
    suggesting the difficulty of classical transfer learning in the very small sample
    regime. The multilayer meta-matching model is publicly available at GITHUB_LINK.
  kind: bibo:Manuscript
  author:
  - pid: null
    given_name: null
    family_name: null
  - pid: xyzrins:persons/simon-eickhoff
    given_name: Simon
    family_name: Eickhoff
  topic: []

---

