# Production Readiness Report

## Summary

Describe scope, detected stack, exposure assumptions, and the most important
evidenced risks. Do not give a false numeric readiness score.

## Critical

For each finding:

### Finding title
- **Location:** `path:line` or configuration location
- **Evidence:** What the code/configuration does
- **Impact:** Concrete production consequence
- **Remediation:** Smallest safe correction
- **Verification:** How to prove the fix

## High

Use the same structure.

## Medium

Use the same structure.

## Low

Use the same structure.

## Production Checklist

Use `templates/production-checklist.md`.

## Remediation Order

Order fixes by dependencies and operational risk. Do not manufacture findings
to populate every severity.
