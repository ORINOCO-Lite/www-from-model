---
title: "HeuDiConv \u2014 flexible DICOM conversion into structured directory layouts"
persons:
- michael-hanke
- orcid:0000-0003-3456-2493
topics:
- neuroimaging
- research-data-management
- research-software-engineering
params:
  graphRootNodePID: xyzrins:publications/c650d00f-816d-4b12-af63-9ce812c2c09c
  sortkey: "2024-07-03HeuDiConv — flexible DICOM conversion into structured directory layouts"
  pid: xyzrins:publications/c650d00f-816d-4b12-af63-9ce812c2c09c
  doi: 10.21105/joss.05839
  date: '2024-07-03'
  title: "HeuDiConv \u2014 flexible DICOM conversion into structured directory layouts"
  description: "In order to support efficient processing, data must be formatted according\
    \ to standards thatare prevalent in the field and widely supported among actively\
    \ developed analysis tools. TheBrain Imaging Data Structure (BIDS) (Gorgolewski\
    \ et al., 2016) is an open standard designedfor computational accessibility, operator\
    \ legibility, and a wide and easily extendable scopeof modalities \u2014 and is\
    \ consequently used by numerous analysis and processing tools as thepreferred input\
    \ format in many fields of neuroscience. HeuDiConv (Heuristic DICOM Converter)enables\
    \ flexible and efficient conversion of spatially reconstructed neuroimaging data\
    \ fromthe DICOM format (quasi-ubiquitous in biomedical image acquisition systems,\
    \ particularlyin clinical settings) to BIDS, as well as other file layouts. HeuDiConv\
    \ provides a multi-stageoperator input workflow (discovery, manual tuning, conversion)\
    \ where a manual tuning step isoptional and the entire conversion can thus be seamlessly\
    \ integrated into a data processingpipeline. HeuDiConv is written in Python, and\
    \ supports the DICOM specification for input parsing, and the BIDS specification\
    \ for output construction. The support for these standardsis extensive, and HeuDiConv\
    \ can handle complex organization scenarios that arise for specificdata types (e.g.,\
    \ multi-echo sequences, or single-band reference volumes). In addition togenerating\
    \ valid BIDS outputs, additional support is offered for custom output layouts. Thisis\
    \ obtained via a set of built-in fully functional or example heuristics expressed\
    \ as simplePython functions. Those heuristics could be taken as a template or as\
    \ a base for developingcustom heuristics, thus providing full flexibility and maintaining\
    \ user accessibility. HeuDiConvfurther integrates with DataLad (Halchenko et al.,\
    \ 2021), and can automatically preparehierarchies of DataLad datasets with optional\
    \ obfuscation of sensitive data and metadata,including obfuscating patient visit\
    \ timestamps in the git version control system. As a result,given its extensibility,\
    \ large modality support, and integration with advanced data managementtechnologies,\
    \ HeuDiConv has become a mainstay in numerous neuroimaging workflows, andconstitutes\
    \ a powerful and highly adaptable tool of potential interest to large swathes of\
    \ theneuroimaging community."
  kind: bibo:AcademicArticle
  author:
  - pid: orcid:0000-0003-3456-2493
    given_name: Yaroslav
    family_name: Halchenko
  - pid: xyzrins:persons/michael-hanke
    given_name: Michael
    family_name: Hanke
  topic:
  - pid: xyzrins:topics/research-software-engineering
    display_label: Research software engineering (RSE)
  - pid: xyzrins:topics/neuroimaging
    display_label: Neuroimaging
  - pid: xyzrins:topics/research-data-management
    display_label: Research data management (RDM)

---

