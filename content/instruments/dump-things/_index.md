---
title: Dump Things Service
persons:
- christian-moench
params:
  graphRootNodePID: xyzrins:instruments/dump-things
  pid: xyzrins:instruments/dump-things
  doi: null
  date: null
  source_code_url: null
  documentation_url: null
  title: Dump Things Service
  description: 'The Dump Things Service is an implementation of a service that allows
    to store and retrieve data that is structured according to given schemata.


    Data is stored in collections. Each collection has a name and an associated schema.
    All data records in the collection have to adhere to the given schema.


    The canonical format for schemas is [LinkML](https://linkml.io/). The service supports
    schemas that are based on DataLad''s *Thing* schema, i.e. on https://concepts.datalad.org/s/things/v1/.
    It assumes that the classes of stored records are subclasses of `Thing`, and inherit
    the properties `pid` and `schema_type` from the `Thing`-baseclass.


    The general workflow in the service is as follows. We distinguish between two areas
    of a collection, an incoming area and a curated area. Data written to a collection
    is stored in a collection-specific incoming area. A curation process, which is outside
    the scope of the service, moves data from the incoming area of a collection to the
    curated area of the collection.


    To submit a record to a collection, a token is required. The token defines read-
    and write- permissions for the incoming areas of collections and read-permissions
    for the curated area of a collection. A token can carry permissions for multiple
    collections. In addition, the token carries a submitter ID. It also defines a token
    specific zone in the incoming area. So any read- and write-operations on an incoming
    area are actually restricted to the token-specific zone in the incoming area. Multiple
    tokens can share the same zone. That allows multiple submitters to work together
    when storing records in the service.


    The service provides an HTTP-based API to store and retrieve data objects, and to
    verify token capabilities.'
  kind: Software
  author:
  - pid: xyzrins:persons/christian-moench
    given_name: Christian
    family_name: "M\xF6nch"
  topic: []
  license: []

---

