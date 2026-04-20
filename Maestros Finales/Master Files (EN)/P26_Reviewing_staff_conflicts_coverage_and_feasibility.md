---
title: Reviewing staff conflicts, coverage, and feasibility
shortTitle: Conflicts and coverage
intro: 'Learn how to review the Rostering solution after calculation, identify coverage conflicts, distinguish whether issues come from rules, availability, or assignment, and decide what to correct before validating.'
contentType: how-tos
versions:
  - '*'
---

## Understanding what to review after Rostering calculation

After running the first Rostering calculation, the next step is not validating immediately. First you need to review whether assignment is actually viable. The goal is to confirm whether the system covered the work with real people while respecting labor constraints, availability, and operational context.

Use this quick start when you already ran Rostering calculation and need to analyze whether the solution should be considered complete, partial, or conflictive.

Before you begin, make sure that:
1. You ran the first Rostering calculation in P25.
2. You know which Scheduling solution was the input.
3. You know which driver population participated.
4. You are ready to analyze the solution before validating it.

For this quick start, use this reference case:

> **I’m going to review the Rostering solution for line L1 to check coverage, identify assignment conflicts, and confirm feasibility before validating.**

To understand what to review:
1. Treat review as diagnosis, not automatic approval.
2. Always review three dimensions:
   1. **coverage**,
   2. **conflicts**,
   3. **overall feasibility**.
3. Do not accept a solution just because the engine finished.
4. Consider a solution can:
   1. cover all work,
   2. cover work partially,
   3. or produce conflicts that require returning to rules, availability, or assignment.

When you finish this section, you should know what it means to review a staff solution and which questions to answer before validation.

## Reviewing coverage of assigned work

The first question is simple: **Is all work covered?** Here you are not yet diagnosing why something failed—you are measuring whether the system successfully assigned people to work inherited from Scheduling.

Before you start this section, make sure that:
1. The calculated solution is visible.
2. You know the total work you expected to cover.
3. You can review results by line, group, or population.

To review coverage:
1. Open the calculated Rostering solution.
2. Review the overall results view.
3. Identify:
   1. covered duties,
   2. uncovered duties,
   3. and partial assignments, if any.
4. Use visible KPIs to support the analysis.
ref: P26_Imagen1.png | compact
4. Check whether coverage is complete or has gaps using daily KPIs.
ref: P26_Imagen2.png | full
5. If the system shows coverage summaries (driver KPIs), review them.
ref: P26_Imagen3.png | compact
6. If coverage is not complete, do not validate the solution yet.
7. Note where the gaps are so you can analyze them next.

For the reference case, ask yourself:
1. Is L1’s work fully covered?
2. Are there days or time bands with gaps?
3. Does the issue affect the whole line or only part of the service?

When you finish this section, you should know whether the solution covers all work or leaves duties unassigned.

## Detecting conflicts and reading the likely cause

After coverage review, identify conflicts. A conflict does not automatically mean you lack staff. It can mean a rule is too restrictive, a person is assigned incorrectly, or an absence/loan was modeled incorrectly.

Before you start this section, make sure that:
1. You identified whether there are uncovered duties.
2. You are willing to distinguish causes rather than fixing by intuition.
3. You know which part of the solution you will inspect first.

To review conflicts usefully:
1. Review duties that are uncovered or problematic.
2. Check whether the system shows messages, indicators, or attached conflicts.
3. Classify the likely cause into one of these groups:
   1. **rules too restrictive**,
   2. **insufficient availability**,
   3. **incorrect assignment or qualifications**,
   4. **structure inherited from Scheduling**.
4. If the conflict affects many people in the same population, review rules and assignment first.
5. If it affects individual cases, review availability, absence, or loan first.
6. If it seems to come from inherited work, consider going back to Scheduling.

For the reference case, ask:
1. Is the duty uncovered because there was no available person?
2. Does the person exist but is not qualified/assigned to the correct context?
3. Did a Rostering rule block an assignment that looked possible?
4. Is the issue not staff, but inherited work structure?

When you finish this section, you should have a reasonable hypothesis about the main conflict causes.

## Reviewing overall feasibility of the solution

A solution can be nearly covered and still be poor. Beyond coverage and conflicts, review **overall feasibility**. The question is not only whether people were assigned, but whether the resulting assignment makes operational and human sense.

Before you continue, make sure that:
1. You reviewed coverage.
2. You identified main conflicts.
3. You are ready to assess quality, not only quantity.

To review overall feasibility:
1. Check whether work distribution looks reasonable.
2. Check for clear imbalance signals across people or groups.
3. Confirm the solution appears to comply with:
   1. rests,
   2. limits,
   3. basic fairness criteria,
   4. operational consistency.
4. If the solution covers work but does so in a very forced way, do not validate it yet.
5. If the result looks operational, balanced, and explainable, move toward the decision.

For the reference case, ask:
1. Was coverage achieved reasonably or too forcefully?
2. Does assignment look balanced across drivers?
3. Does the solution look applicable in the real world, or only valid on paper?

When you finish this section, you should have a fuller reading of whether the solution should advance or needs correction.

## Deciding what to correct before validating

The last step is turning analysis into a practical decision. The goal is not fixing everything at once, but identifying the correct next correction layer.

Before you finish, make sure that:
1. You reviewed coverage.
2. You analyzed conflicts.
3. You assessed overall feasibility.
4. You know whether the solution can advance.

To decide what to correct:
1. If the main issue is **rules**, return to P22.
2. If the main issue is **absences/inactivity/availability**, return to P23.
3. If the main issue is **loans/transfers/assignment**, return to P24 or P21 as appropriate.
4. If the main issue is inherited work, return to Scheduling.
5. If the solution is sufficiently complete and feasible, prepare it for validation.
6. Do not validate a solution just because it “almost works”. Validate when you understand why it works and why remaining conflicts are acceptable or resolved.

For the reference case, finish this quick start only when you can state one of these:
1. L1’s solution is solid enough to validate.
2. You know exactly which layer you must correct before calculating again.

When you finish this section, you should have a clear reading of coverage, conflicts, and feasibility—and a practical next-step decision.

## Additional reading

- [Validating and consolidating the Rostering solution](P27_Validating_and_consolidating_the_rostering_solution.md)

