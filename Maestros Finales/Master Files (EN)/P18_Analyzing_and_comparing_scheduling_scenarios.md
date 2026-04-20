---
title: Analyzing and comparing Scheduling scenarios
shortTitle: Compare scenarios
intro: 'Learn how to compare Scheduling scenarios, review KPIs and operational differences, and decide with clear criteria which solution should remain the reference or advance as a new iteration.'
contentType: how-tos
versions:
  - '*'
---

## Identifying which scenarios you will compare

After creating, calculating, validating, and publishing scenarios, the natural next step is comparing them. Comparing scenarios is not just an intuitive “which looks better” exercise. It is about reviewing what changed, what impact that change had, and whether the new iteration truly improves the reference solution.

Use this quick start when you have at least two comparable scenarios (for example a published solution and a newly calculated iteration) and you need to decide which should remain the operational reference or which should move forward in the lifecycle.

Before you begin, make sure that:
1. You already created and calculated at least one base scenario.
2. You have a second version/iteration/variant you want to compare.
3. You know which line, day type, and operational context you are reviewing.
4. You know which version is the current reference.

For this quick start, use this reference case:

> **I’m going to compare the published scenario for line L1 with a newly calculated iteration to decide whether the new solution truly improves current scheduling.**

To correctly identify scenarios to compare:
1. In GoalBus, open the **Planning scenarios** module.
ref: P18_Imagen1.png | compact
2. Locate the scenario that acts as the current reference.
3. Locate the new scenario/iteration you want to evaluate.
4. Confirm both scenarios belong to the same functional context:
   1. same line (or comparable set of lines),
   2. same day type,
   3. same general operational logic.
5. Review the name, description, and status of each scenario.
6. Confirm which one is:
   1. the active/published reference,
   2. and which one is the new proposal.
7. If the scenarios are not comparable, do not proceed until you fix that.

For the reference case, make sure that:
1. Both scenarios belong to line L1.
2. Both are workday (or the same time context).
3. One is the reference and the other is the alternative.

When you finish this section, you should have clearly identified which scenarios you will compare and the role of each one.

## Reviewing KPIs, workload volume, and overall balance

Once scenarios are selected, start with a high-level comparison. The goal is to review general indicators before diving into duties or rule details. This helps you detect whether the new solution is truly better balanced or just different.

Before you start this section, make sure that:
1. You know which two scenarios you are comparing.
2. You identified which one is the reference.
3. You have access to visible KPIs or comparable metrics.

To review high-level KPIs:
1. Open the first scenario and review its key KPIs.
2. Note at least:
   1. total workload volume,
   2. number of duties,
   3. total time,
   4. total distance (or relevant magnitude),
   5. any other visible indicator.
3. Open the second scenario and review the same KPIs.
4. Compare whether the new iteration:
   1. reduces unnecessary complexity,
   2. improves balance,
   3. or simply moves the problem elsewhere.
5. Avoid accepting an iteration just because numbers change. The change must make operational sense.

For the reference case, ask yourself:
1. Does the new iteration reduce unnecessary duties?
2. Does overall balance look more reasonable?
3. Is total volume still coherent with the validated offer?
4. Is the improvement real—or only redistribution without clear benefit?

When you finish this section, you should have a global sense of whether the new solution deserves deeper review.

## Comparing impact on vehicles vs. duties

After reviewing global KPIs, compare functional logic by separating:
1. impact on **vehicles**,
2. and impact on **duties/shifts**.

This matters because an iteration can improve fleet logic and worsen duty logic, or vice versa. Mixing both makes interpretation confusing.

Before you start this section, make sure that:
1. You already reviewed global KPIs.
2. You know which vehicle/shift rules are involved in the change.
3. You know the goal of the iteration.

To compare vehicle impact:
1. Review how the solution behaves regarding:
   1. fleet used,
   2. compatibilities,
   3. departures from depots/parkings,
   4. non-productive mileage, if visible or inferable.
2. Check whether the iteration improves coherence between line, fleet, and infrastructure.
3. Detect whether the new scenario forces solutions that are less realistic than before.

To compare duty impact:
1. Review how duties/work blocks are constructed.
2. Confirm active shift types still make sense.
3. Observe whether the new solution:
   1. improves work clarity,
   2. worsens structure,
   3. or introduces unnecessary rigidity.
4. Connect the change back to the shift rules model you used.

For the reference case, ask yourself:
1. Does the new iteration improve vehicle logic without harming duty logic?
2. Does it improve duty logic without harming fleet logic?
3. Which dimension improves or degrades?
4. Is the overall result more robust—or just more different?

When you finish this section, you should understand where each scenario improves and where it worsens.

## Deciding whether the new iteration delivers real value

Now turn comparison into a decision. Not every new scenario deserves to move forward. Sometimes an iteration is only internal learning and the best decision is keeping the active version. Other times the improvement is clear enough to justify a new validation/publication cycle.

Before you continue, make sure that:
1. You compared high-level KPIs.
2. You reviewed vehicle vs. duty impact.
3. You know the original goal of the iteration.

To decide whether the iteration delivers real value:
1. Summarize the purpose of the new scenario.
2. Check whether that goal was clearly achieved.
3. Ask yourself whether the improvement is:
   1. operationally visible,
   2. technically defensible,
   3. stable enough to advance.
4. If the iteration clearly improves the reference, prepare it for validation or publication as appropriate.
5. If it does not improve the reference, keep it as learning and maintain the current version.
6. Do not promote an iteration just because it is newer—promote it only if it is better for the case.

For the reference case, finish this section only when you can state one of these:
1. The new L1 iteration clearly improves the published solution and should advance.
2. The published solution remains the best reference and the new iteration remains only as analysis.

When you finish this section, you should have a clear, defensible decision on which scenario remains the reference.

## Leaving traceability for future iterations

The last step is leaving a trace of the comparison. Comparing scenarios without traceability forces you to redo analysis later and makes it harder to explain why a version was promoted or discarded.

Before you finish, make sure that:
1. You already made a decision.
2. You know which scenario remains the reference.
3. You know the main reason behind the decision.

To leave traceability:
1. Review the name and description of both scenarios.
2. If needed, update the new scenario description to better reflect its purpose or outcome.
3. Keep the reference version clearly identified as:
   1. published,
   2. validated,
   3. or maintained as the official baseline.
4. Keep the non-promoted iteration as a comparative reference if it has historical value.
5. If your internal process requires it, record what changed and why the final decision was made.

For the reference case, make sure that:
1. You can explain why the new scenario does or does not improve the active L1.
2. The decision is reflected in names/descriptions or internal process.
3. A future iteration will not start from confusion.

When you finish this section, you should have not only a comparison, but a traceable decision that is useful for future iterations.

## Additional reading

- [Moving from Scheduling to Rostering](P19_Moving_from_scheduling_to_rostering.md)

