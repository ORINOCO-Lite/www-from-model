---
title: 'Lab in a box: A build-your- own-open-lab software toolkit'
persons:
- adina-wagner
- alex-waite
- christian-moench
- dac706d9-2188-4a84-91bd-a49c5e63c19c
- laura-waite
- michael-hanke
- stephan-heunis
- venkatesh-hariharapura-shivashankar
topics:
- research-data-management
- research-software-engineering
params:
  graphRootNodePID: xyzrins:publications/379d0ef3-c467-4cd4-9912-a15a6d082204
  sortkey: "NoneLab in a box: A build-your- own-open-lab software toolkit"
  pid: xyzrins:publications/379d0ef3-c467-4cd4-9912-a15a6d082204
  doi: 10.5281/zenodo.20583436
  date: null
  title: 'Lab in a box: A build-your- own-open-lab software toolkit'
  description: "Over the past two years, our team has been working on an interoperable\
    \ software toolstack that is open source, self-hosted, and covers basic relevant\
    \ needs of a computational neuroscience lab.Notably, a number of software solutions\
    \ came into existance or were deployed or further developed thanks to interactions\
    \ of different software communities during RDM workshops or the distribits conference\
    \ for distributed data management technologies (distribits.live).Our objective is\
    \ to design an approach that allows storing data of arbitrary size, flexible semantic\
    \ meta data, and the relations between these data; and to provide ways to query\
    \ those relations and access the underlying data, as well as exposing selected data\
    \ for websites, knowledge bases, or data catalogs.The system components are either\
    \ fully compatible or integrated with the DataLad (Halchenko et al., 2021) ecosystem\
    \ for data management.At the core of the stack, we have developed the following\
    \ software components:\n\n\n\nForgejo-aneksajo[1]: A lightweight collaboration hub\
    \ for code and data thanks to native git-annex support. It has a comparable feature\
    \ set to GitHub (CI/CD, private versus public repositories, container registry,\
    \ \u2026), but allows further customization (including, for example, nii-vue integrations\
    \ for DICOM and Nifti previews, self-hosted runners for CI/CD actions, self-hosted\
    \ container registries, \u2026).\n\nShacl-vue[2] and dumpthings[3]: The front- and\
    \ backend for a metadata annotation stack, tuned for flexibly and user-friendly\
    \ collecting, curating, storing, and quering metadata.\n\ndatalad-concepts[4]: A\
    \ set of pragmatic meta data schemas that enable alignment with arbitrary vocabularies.\
    \ The schemas feed directly into the metadata editor, and can also be easily extended.\n\
    \n\nIn addition, a set of existing open source softwares complements the stack:Hugo-based\
    \ website scaffolds can be bootstrapped from or extended with meta data from the\
    \ meta data stack.Hedgedoc, with authentication via a forgejo-annexajo hub, constitutes\
    \ a feature-rich collaborative editor.And a CalDAV-based calendar and task service\
    \ provides custom calendars and shared todo lists.While the components are all standalone\
    \ and can be deployed individually, they are tightly integrated and interopable,\
    \ enabling additional usecases when combined.For example, the metadata annotation\
    \ stack gains permission management and document upload routines when used together\
    \ with forgejo-aneksajo.In addition, the system is an optimal fit around the DataLad\
    \ tool for data versioning and publication.Importantly, the deployment for each\
    \ service is automated using pyinfra[5] to make initial setup, configuration and\
    \ maintenance effortless, even for scientists without experience in IT administration.\_\
    In conclusion, we have created a lab-in-a-box toolkit with self-hostable, open source\
    \ software solutions for the digital service needs of an open neuroscience lab.All\
    \ resources are openly available and can be found at https://hub.psychoinformatics.de/lab-in-a-box/liab-deploymentsThe\
    \ stack strengthens the digital sovereignty and resilience by replacing commercial\
    \ services whose available hinges on for-profit companies and that can be vulnerable\
    \ to political or technical instability.Successful roll-out in different neuroscientific\
    \ contexts have proven its initial utility, and ensure continuous improvement through\
    \ co-development and user feedback.\n\n\_\n\n\n\nhttps://codeberg.org/forgejo-aneksajo/forgejo-aneksajo\
    \ \u21A9\uFE0E\n\n\n\nhttps://github.com/psychoinformatics-de/shacl-vue \u21A9\uFE0E\
    \n\n\n\n\nhttps://github.com/christian-monch/dump-things-server \u21A9\uFE0E\n\n\
    \n\n\nhttps://concepts.datalad.org/ \u21A9\uFE0E\n\n\n\n\nhttps://hub.datalad.org/infra/deployments\
    \ \u21A9\uFE0E"
  kind: null
  author:
  - pid: xyzrins:persons/stephan-heunis
    given_name: Stephan
    family_name: Heunis
  - pid: xyzrins:persons/laura-waite
    given_name: Laura
    family_name: Waite
  - pid: xyzrins:persons/alex-waite
    given_name: Alex
    family_name: Waite
  - pid: xyzrins:persons/michael-hanke
    given_name: Michael
    family_name: Hanke
  - pid: xyzrins:persons/adina-wagner
    given_name: Adina
    family_name: Wagner
  - pid: xyzrins:persons/venkatesh-hariharapura-shivashankar
    given_name: Venkatesh
    family_name: Hariharapura Shivashankar
  - pid: xyzrins:persons/christian-moench
    given_name: Christian
    family_name: "M\xF6nch"
  - pid: xyzrins:persons/dac706d9-2188-4a84-91bd-a49c5e63c19c
    given_name: Matthias
    family_name: "Ri\xDFe"
  topic:
  - pid: xyzrins:topics/research-data-management
    display_label: Research data management (RDM)
  - pid: xyzrins:topics/research-software-engineering
    display_label: Research software engineering (RSE)

---

