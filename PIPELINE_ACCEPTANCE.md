# Peculiar Librarian
## Pipeline Acceptance Criteria

The Peculiar Librarian is considered operational when the
following pipeline executes without architectural changes.

------------------------------------------------------------

Research

↓

Notebook LM

↓

Structured Facts

↓

FinancialObservationFactory

↓

FinancialObservation

↓

KnowledgeCompiler

↓

ObservationCollectionBuilder

↓

Publisher

↓

Knowledge Collection

------------------------------------------------------------

Acceptance Checklist

[ ] Discovery discovers collections.

[ ] CollectionContract validates collections.

[ ] FinancialObservationFactory creates canonical observations.

[ ] KnowledgeCompiler produces canonical semantic observations.

[ ] ObservationCollectionBuilder produces canonical Turtle collections.

[ ] RDF Publisher publishes valid RDF.

[ ] Query 10 passes through the complete pipeline without manual restructuring.

[ ] Generated knowledge validates successfully.

------------------------------------------------------------

If every item above passes, the Peculiar Librarian kernel
is considered production-ready.

