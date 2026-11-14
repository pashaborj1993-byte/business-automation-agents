---
name: document-intelligence-ops
description: Convert incoming business documents into reviewed structured data and routed work. Use for invoices, forms, contracts, reports, photos, and PDF-heavy operations; not for unreviewed high-stakes determinations.
---

# Document intelligence operations

Turn documents into reliable work records while preserving a review path for uncertainty.

## Select the document workflow

Define the document type, arrival channel, business decision it supports, destination system, retention rule, and permitted users. Start with one document class and one output workflow; do not mix invoices, contracts, and identity documents in the first release.

## Extract with evidence

For each field, retain the source document, page or location when practical, normalized value, extraction confidence, and validation result. Validate stable fields using deterministic checks: required data, dates, arithmetic, known suppliers, contract identifiers, or account matches.

## Route based on confidence and consequence

Automate low-risk, high-confidence preparation only. Send missing, conflicting, low-confidence, duplicate, or consequential records to a named human queue. Do not automatically approve payments, execute contracts, alter accounting records, reject applicants, or make legal, medical, credit, or employment decisions.

## Recovery and governance

Use idempotent document identifiers to prevent double processing. Make correction easy and capture the reason so the validation rules can improve. Define retention, deletion, access, and export rules before storing customer documents.

## Measure

Measure touchless-preparation rate, human-correction rate, processing time, duplicate rate, and exception age. Expand to another document class only after the first workflow remains accurate and recoverable.
