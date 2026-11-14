---
name: internal-knowledge-agent
description: Build or assess a sourced, permission-aware internal knowledge assistant. Use for company policies, project documents, handbooks, procedures, and private knowledge bases.
---

# Internal knowledge agent

Provide useful answers while preserving the limits of the underlying company knowledge.

## Choose a bounded knowledge domain

Start with a real question set and a manageable corpus: onboarding, support procedures, sales enablement, policies, or project documentation. Name the document owners, freshness expectations, users, and systems of record. Do not use a vector database as a substitute for access control or content ownership.

## Answer with traceability

Retrieve only documents the requesting person is permitted to access. Present concise answers with the source title, location, and last-updated date when available. Separate sourced statements from inference. When the corpus lacks evidence, say so and route the question to an owner rather than inventing a policy.

## Maintain the knowledge

Provide a path to report an incorrect or stale answer. Route feedback to the content owner and preserve the original source rather than silently editing facts. Establish document ingestion, removal, and permission-sync behavior before inviting broad use.

## Validate before launch

Test permitted and denied users, stale documents, contradictory documents, missing answers, sensitive terms, and prompt-injection content within source files. Log retrieval and feedback events without exposing private document content unnecessarily.

## Measure

Track resolved questions, unanswered-question themes, source freshness, feedback rate, and time saved for the target team. Expand scope only after users trust the citations and access boundaries.
