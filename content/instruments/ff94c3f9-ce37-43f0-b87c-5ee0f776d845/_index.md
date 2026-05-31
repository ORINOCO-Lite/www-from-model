---
title: Lab-in-a-box deployments
params:
  graphRootNodePID: xyzrins:instruments/ff94c3f9-ce37-43f0-b87c-5ee0f776d845
  pid: xyzrins:instruments/ff94c3f9-ce37-43f0-b87c-5ee0f776d845
  doi: null
  date: null
  source_code_url: null
  documentation_url: null
  title: Lab-in-a-box deployments
  description: 'This is a collection of deployment workflows for

    self-hosted software services, implemented with [pyinfra](https://pyinfra.com).
    Most importantly, this collection includes the (meta)data tools of the developed
    by the [ORINOCO](https://www.psychoinformatics.de/projects/orinoco/) project, but
    the list of supported services also include a number of general purpose solutions,
    such as [Hedgedoc](https://hedgedoc.org) or [Gatus](https://gatus.io/).


    This effort does not aim to serve every use case and deployment scenario. Instead,
    it makes a few central assumptions:


    - Users have access to an account on a target machine that allows for root-access
    via `sudo`.

    - The base OS on a target machine is Debian (12+), or a sufficiently close derivative.
    There is no hard dependency, but nothing else has seen significant use (yet).

    - Users have means to configure the DNS for a domain they want to use for exposing
    deployed services.

    - [Caddy](https://caddyserver.com) is used as a web-server/reverse-proxy.

    - [Podman](https://podman.io) is used as a container solution.


    ## Conventions


    All provided deployments follow a common set of conventions:


    - One service, one user: Each deployment creates/uses a service-dedicated user account.
    All code runs in user-space.

    - Containerized environments: Code is generally deployed in virtual environments
    -- typically user-space podman containers, but [uv](https://docs.astral.sh/uv)-managed
    virtual environments for (small) Python packages.

    - Systemd: Services are managed via user-space [systemd](https://systemd.io) service
    units.

    - Subdomains: Services are assumed to be deployed using dedicated subdomains (`service.example.org`,
    rather than `example.org/service`).'
  kind: Software
  author: []
  topic: []
  license:
  - pid: spdxlic:MIT
    label: MIT License
    url: https://spdx.org/licenses/MIT

---

