---
title: 'Confound-leakage: Confound Removal in Machine Learning Leads to Leakage'
persons:
- simon-eickhoff
params:
  graphRootNodePID: xyzrins:publications/b8f94ba8-0fd7-48d4-adf2-4186714f504a
  sortkey: "20323Confound-leakage: Confound Removal in Machine Learning Leads to Leakage"
  pid: xyzrins:publications/b8f94ba8-0fd7-48d4-adf2-4186714f504a
  doi: 10.1093/gigascience/giad071
  date: '20323'
  title: 'Confound-leakage: Confound Removal in Machine Learning Leads to Leakage'
  description: BackgroundMachine learning (ML) approaches are a crucial component of
    modern data analysis in many fields, including epidemiology and medicine. Nonlinear
    ML methods often achieve accurate predictions, for instance, in personalized medicine,
    as they are capable of modeling complex relationships between features and the target.
    Problematically, ML models and their predictions can be biased by confounding information
    present in the features. To remove this spurious signal, researchers often employ
    featurewise linear confound regression (CR). While this is considered a standard
    approach for dealing with confounding, possible pitfalls of using CR in ML pipelines
    are not fully understood.ResultsWe provide new evidence that, contrary to general
    expectations, linear confound regression can increase the risk of confounding when
    combined with nonlinear ML approaches. Using a simple framework that uses the target
    as a confound, we show that information leaked via CR can increase null or moderate
    effects to near-perfect prediction. By shuffling the features, we provide evidence
    that this increase is indeed due to confound-leakage and not due to revealing of
    information. We then demonstrate the danger of confound-leakage in a real-world
    clinical application where the accuracy of predicting attention-deficit/hyperactivity
    disorder is overestimated using speech-derived features when using depression as
    a confound.ConclusionsMishandling or even amplifying confounding effects when building
    ML models due to confound-leakage, as shown, can lead to untrustworthy, biased,
    and unfair predictions. Our expose of the confound-leakage pitfall and provided
    guidelines for dealing with it can help create more robust and trustworthy ML models.
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

