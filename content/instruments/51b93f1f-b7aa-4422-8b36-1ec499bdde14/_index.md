---
title: datalad-remake
persons:
- christian-moench
- malgorzata-wierzba
- michal-szczepanik
params:
  graphRootNodePID: xyzrins:instruments/51b93f1f-b7aa-4422-8b36-1ec499bdde14
  pid: xyzrins:instruments/51b93f1f-b7aa-4422-8b36-1ec499bdde14
  doi: null
  date: null
  source_code_url: https://github.com/datalad/datalad-remake
  documentation_url: null
  title: datalad-remake
  description: This extension equips DataLad with the functionality to (re)compute file
    content on demand, based on a specified set of instructions. In particular, it features
    a datalad make command for capturing instructions on how to compute a given file,
    allowing the file content to be safely removed. It also implements a git-annex special
    remote, which enables the (re)computation of the file content based on the captured
    instructions. This is particularly useful when the file content can be produced
    deterministically. If storing the file content is more expensive than (re)producing
    it, this functionality can lead to more effective resource utilization. Thus, this
    extension may be of interest to a wide, interdisciplinary audience, including researchers,
    data curators, and infrastructure administrators.
  kind: Software
  author:
  - pid: xyzrins:persons/michal-szczepanik
    given_name: "Micha\u0142"
    family_name: Szczepanik
  - pid: xyzrins:persons/christian-moench
    given_name: Christian
    family_name: "M\xF6nch"
  - pid: xyzrins:persons/malgorzata-wierzba
    given_name: "Ma\u0142gorzata"
    family_name: Wierzba
  topic: []
  license:
  - pid: spdxlic:MIT
    label: MIT License
    url: https://spdx.org/licenses/MIT

---

