---
title: {{ given_name }} {{ family_name }}
---

{{ description }}

{%- macro format_identifier(name, notation) %}
{% if name == "Debian" %}[Debian: {{ notation }}](https://qa.debian.org/developer.php?login={{ notation }})
{% elif name == "GitHub" %}[GitHub: {{ notation }}](https://github.com/{{ notation }})
{% elif name == "ORCID" %}[ORCID: {{ notation }}](https://orcid.org/{{ notation }})
{% elif name == "ResearchGate" -%}[ResearchGate: {{ notation }}](https://www.researchgate.net/profile/{{ notation }})
{% elif name == "XYZ" -%}[ResearchGate: {{ notation }}](https://www.researchgate.net/profile/{{ notation }})
{% else %}{{ name }}: {{ notation }}
{% endif %}
{% endmacro -%}

{% for identifier in identifiers if identifier.creator.name is defined %}
- {{ format_identifier(identifier.creator.name, identifier.notation) -}}
{% endfor -%}