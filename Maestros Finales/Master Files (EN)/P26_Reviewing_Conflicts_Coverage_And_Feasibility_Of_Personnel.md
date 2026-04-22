---
title: Reviewing Conflicts, Coverage and Feasibility of Personnel
shortTitle: Conflicts and coverage
intro: Learn how to review the Rostering solution after calculation, identify coverage
  conflicts, distinguish whether the problem comes from rules, availability or secondment,
  and decide what to correct before validating the assignment.
contentType: how-tos
versions:
- '*'
---
## Understanding what you should review after the Rostering calculation

After running the first Rostering calculation, the next step is not to immediately validate the solution. First you need to check if the assignment is really viable. At this stage, the goal is to check if the system managed to cover the work with real people respecting labor restrictions, availability and operating context.

Use this quick start when you've already executed the Rostering calculation and need to analyze whether the solution can be considered complete, partial or conflicting.

Before you start, make sure that:
1. You've already run the first Rostering calculation on P25.
2. You know what Scheduling's solution acted as an entry.
3. You're already clear which group of drivers participated in the calculation.
4. You're ready to analyze the solution before you validate it.

For this quick start, use this reference case:

> **I'm going to review the Rostering solution on line L1 to check if the job was covered, if there are assignment conflicts and if the result is viable before validating it.**

To understand what to review after the calculation:
1. It treats the review as a diagnostic phase, not an automatic approval.
2. Always check three dimensions:
   1. **coverage**,
   2. **conflicts**,
   3. **general feasibility**.
3. Do not take a solution for granted just because the engine has finished the calculation.
4. Considers that a solution can:
   1. cover all the work,
   2. partially cover it,
   3. or produce conflicts that force a return to rules, availability or secondment.

When you finish this section, you should be clear about what it means to review a personnel solution and what questions to answer before validating it.

## Reviewing the coverage of assigned work

The first question to answer is simple: **Is all the work covered?**. It is not yet a question of why something failed, but of measuring whether the system managed to assign people to work inherited from Scheduling.

Before starting this section, make sure that:
1. You already have the calculated solution visible.
2. You know what total work you expected to cover.
3. You can now review the result by line, group or collective.

To review the coverage:
1. Opens the Rostering calculated solution.
2. Check the overall view of the result.
3. Identify:
   1. covered tasks,
   2. Uncovered tasks,
   3. and partial assignments, if any.
4. To do this, help yourself with the visible KPIs in the solution.
ref: P26_Imagen1.png | compact
4. Check if the coverage is complete or if there are gaps thanks to the visible daily KPIs.
ref: P26_Imagen2.png | full
5. If the system displays counters or coverage summaries (KPIs of drivers), check them.
ref: P26_Imagen3.png | compact
6. If the coverage is not complete, don't validate the solution yet.
7. Mentally mark where the gaps are to be analyzed later.

For the reference case, ask yourself:
1. Was L1's work completely covered?
2. Are there days or slots with holes?
3. Does the problem affect the entire line or only part of the service?

When you finish this section, you should know if the solution covers all the work or if there are unallocated tasks.

## Detecting conflicts and reading their probable cause

After reviewing the coverage, you need to identify conflicts. A conflict does not automatically mean that there is a lack of staff. It may mean that a rule is too restrictive, that a person is misattached, or that an absence or assignment was wrongly modeled.

Before starting this section, make sure that:
1. You've already identified if there are unmet tasks.
2. You're already willing to differentiate causes rather than correct by intuition.
3. You know what part of the solution to check first.

To review conflicts usefully:
1. Check the tasks that remained unallocated or in trouble.
2. See if the system displays associated messages, indicators or conflicts.
3. Try to classify the probable cause into one of these groups:
   1. **rules too restrictive**,
   2. **inadequate availability**,
   3. **incorrect secondment or habilitation**,
   4. **structure inherited from Scheduling**.
4. If the conflict seems to affect many people in the same group, review rules and secondment first.
5. If the conflict affects individual cases, check availability, absence or assignment first.
6. If the problem seems to come from inherited work, consider returning to Scheduling.

For the reference case, ask yourself these questions:
1. Was the task not covered because there was no person available?
2. Did the person exist, but was not enabled or attached to the correct context?
3. Did the Rostering rule block an assignment that did seem possible?
4. The problem is not personal, but inherited work?

When you finish this section, you should have a reasonable assumption about the cause of the major conflicts.

## Reviewing the overall feasibility of the solution

A solution can be almost covered and still not good. So, in addition to coverage and conflicts, you need to review the **general feasibility**. Here the question is not only whether the system assigned people, but whether the resulting assignment makes operational and human sense.

Before continuing, make sure that:
1. You've checked coverage.
2. You've already identified major conflicts.
3. You're ready to value quality, not just quantity.

To review the overall feasibility:
1. Check if the distribution of the work seems reasonable.
2. Check for signs of clear imbalance between people or groups.
3. Notes whether the solution appears to comply with:
   1. breaks,
   2. limits,
   3. basic criteria of equity,
   4. and operational consistency.
4. If the solution covers the work, but it does it very forcibly, don't validate it yet.
5. If the result seems operational, balanced and explicable, it continues towards the final decision.

For the reference case, ask yourself:
1. Was the coverage reasonably achieved or too forced?
2. Does the assignment look balanced between drivers?
3. Does the solution seem to be applicable in the real world or only valid on paper?

When you finish this section, you should have a more complete reading of whether the solution deserves to move forward or whether it needs correction.

## Deciding what to correct before validating

The last step is to turn analysis into a practical decision. Here the goal is not to fix everything at once, but to identify the next correct layer of correction.

Before you finish, make sure that:
1. You've checked coverage.
2. You've already analyzed conflicts.
3. You've already valued the overall viability.
4. You know if the solution can move forward or not.

To decide what to correct before validating:
1. If the main problem is **rules**, go back to P22.
2. If the main problem is **absences, inactivity or availability**, go back to P23.
3. If the main problem is **assignment, transfer or secondment**, return to P24 or P21 as appropriate.
4. If the main problem is inherited work, go back to Scheduling.
5. If the solution is sufficiently complete and feasible, prepare it for validation.
6. Do not validate a solution just because it “almost works.” Validate it when you understand why it works and why the remaining conflicts are acceptable or resolved.

For the reference case, finish this quick start only when you can affirm one of these two things:
1. The L1 solution is solid enough to be validated.
2. You know exactly what layer you need to correct before you recalculate.

When you finish this section, you should have a clear reading of coverage, conflicts and feasibility, and a practical decision on the next step.

## Additional readings

- [Validating and consolidating the Rostering solution](P27_Validating_And_Consolidating_The_Rostering_Solution.md)
