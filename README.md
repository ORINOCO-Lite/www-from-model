# Metadata-based website of the Psychoinformatics group

This website is using hugo to build site content that is (mostly)
pulled from a metadata system, using a formal metadata model for
all content.

This repository should not see any manual content edits. All custom
editing is constraint to the presentation (looks/style). Content
changes are exclusively done via editing the respective records
in the underlying metadata system.

## Requirements

As per congo theme version 2.12.0 (2025-06-22), hugo 0.146.0 or later is required.


## Setup notes

Hugo doesn't like symlinks (cheers windows!). Hence all files are annexed in
unlocked mode (`git annex config --set annex.addunlocked true`).
