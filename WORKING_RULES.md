# Working rules

Last updated: 2026-08-28

## Restart-safety and synchronization rule

This repository is the durable research state. Do not leave thesis-bearing progress only in a chat session.

During any active Lovejoy research run:

1. **Synchronize early and repeatedly.** As soon as a new evidentiary result, correction, negative result, branching decision, or superseded hypothesis becomes material, write it into the repository and commit it rather than waiting for the end of the session.
2. **Optimize for rollback/session-loss safety.** After each meaningful research unit, leave a restartable checkpoint that records: what was tested; sources/locators; result; confidence/warrant; what was rejected or superseded; and the exact next action.
3. **Maintain one living restart surface.** `CURRENT_STATE.md` remains the authority for project state. When a branch becomes large enough that full detail would bloat that file, keep a dated restart-safe handoff/sync log under `research_notes/` and make the state/next action explicit there.
4. **Commit before branching further.** A new high-value branch should normally begin only after the previous substantive result has been committed, so a conversation rollback cannot erase the reasoning path.
5. **Do not reconstruct from chat memory when repo state exists.** On restart, read the latest relevant handoff/state file and recent commits first; treat older frozen/HOLD/queue language as historical unless the living state explicitly reactivates it.
6. **Record negative controls and failed searches.** A bounded negative, failed locator, or rejected causal inference is part of the evidentiary state when it constrains future claims.
7. **Separate evidence from interpretation.** Preserve direct-primary quotation/page control, mediated evidence, analyst-level structural homology, and genealogy/influence claims at their appropriate warrant levels.

Compact rule:

> **Sync the repo continuously enough that losing the current conversation would cost at most one small research step.**

For the active logical-analysis / unit-identity branch, resume from:

- `research_notes/JHI_restart_handoff_logic_unit_identity_warrant_2026-08-28.md`

and then consult the newest commits for any later checkpoint.
