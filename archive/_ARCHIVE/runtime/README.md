# PADI Runtime (Reserved)

This directory is reserved for the Semantic Compiler Runtime.

Current runtime implementation temporarily resides under:

    peculiarlibrary/ingestion/

to preserve compatibility during the first compiler milestone.

After the first successful end-to-end compilation, the following modules
will be migrated here:

- compiler.py
- ingestion_pipeline.py
- doctrine_enforcer.py
- mapping_rules.py
- shacl_validator.py

Migration target: v0.6.0
