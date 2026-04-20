---
title: Creating a new scenario iteration from a published solution
shortTitle: New iteration
intro: 'Learn how to create a new iteration of an already published scenario to test improvements, adjust parameters, or introduce changes without altering the version currently in effect.'
contentType: how-tos
versions:
  - '*'
---

## Starting from a published solution without altering the active version

After publishing a solution, it is normal to keep working on it. You may want to adjust rules, try different shift logic, incorporate offer changes, or prepare an improvement for a future period. In that case, you should not modify the published version directly. The correct approach is to create a **new scenario iteration** to maintain traceability and protect the version currently in effect.

Use this quick start when you already have a scenario whose solution is **Published** and you need to generate a new variant without losing the historical reference of the deployed solution.

Before you begin, make sure that:
1. You already published the previous scenario in P16.
2. The scenario solution you will use as base is **Published**.
3. You know which aspect you want to review or improve in the next iteration.
4. You understand the new iteration must not automatically replace the active version until it goes through calculation, validation, and publication again.

For this quick start, use this reference case:

> **I’m going to create a new iteration of the published scenario for line L1 to test improvements without touching the version currently in effect.**

To safely start from a published solution:
1. In GoalBus, open the **Planning scenarios** module.
2. Locate the scenario whose solution is **Published**.
3. Review its name, description, day type, and associated lines.
4. Confirm it is truly the version you want to use as reference.
5. Avoid editing that version directly as if it were a new draft.
6. Decide what change you want to introduce in the new iteration:
   1. rules,
   2. parameters,
   3. offer,
   4. or allowed structural adjustments.

When you finish this section, you should have clearly identified the published scenario that will serve as the base for your iteration.

## Creating the new iteration from the published scenario

Once the base is identified, the next step is creating a **new iteration**. The goal is to keep the published version as historical reference and open a controlled new work branch on the same operational logic.

Before you start this section, make sure that:
1. You identified the correct published solution.
2. You know why you need a new iteration.
3. You understand the new iteration must be clearly differentiated from the previous version.

To create the new iteration:
1. From the scenarios table, open the actions menu for the published scenario.
2. Select the option to **create a new iteration** by **duplicating** the scenario as a working baseline.
ref: P17_Imagen1.png | compact
3. Enter a **new name** for the iteration.
4. If applicable, update the **description** to reflect the goal of the change.
5. Save the new iteration.
ref: P17_Imagen2.png | compact
6. Confirm the new scenario appears as a separate entity from the published one.
ref: P17_Imagen3.png | full
7. Confirm the original published version remains intact and clearly differentiated.

For the reference case, valid options could be:
- **Classic calculation - L1 workday - Iteration 2**
- **L1 workday - shift rules improvement**

When you finish this section, you should have a new iteration created without losing traceability of the published version.

## Defining which changes belong to the new iteration

After creating the iteration, decide what you will actually change. Not all iterations have the same goal. Some adjust rules, others improve efficiency, others reflect a new offer or a future operational variation.

Before you start this section, make sure that:
1. You created the new iteration.
2. You know which aspect of the previous solution you want to review.
3. You are willing to limit the change to a clear goal so you do not mix too many variables.

To define iteration scope:
1. Open the new scenario.
2. Review which elements you want to keep exactly the same as in the published version.
3. Decide which element you will change first:
   1. **vehicle rules**,
   2. **shift rules**,
   3. **engine parameters**,
   4. **service offer**,
   5. **logistics matrices**.
4. Avoid changing too many things at once in the first iteration unless strictly necessary.
5. Document the goal in the name or description.
6. Save descriptive changes before running calculation.

For the reference case, use logic like:
1. Keep the same workday offer for L1.
2. Adjust only the shift rules model.
3. Recalculate to compare the new solution with the published one.

When you finish this section, you should have a new iteration with a clear, bounded goal.

## Recalculating the iteration and comparing with the previous version

Once scope is defined, recalculate the iteration. The advantage is you are not starting from scratch—you are starting from a known solution and can compare the impact more clearly.

Before you start this section, make sure that:
1. You created the new iteration.
2. You defined the change goal.
3. You reviewed which rules, parameters, or inputs you will modify.

To recalculate the new iteration:
1. Review the iterated scenario and confirm inputs are still coherent.
2. Adjust the element you want to modify.
3. Save configuration.
4. Run calculation for the new scenario.
5. Wait for the calculation phase to complete.
6. Review whether the iteration moves to **Solution prepared** or **Edit**.
7. Compare results with the previous version using:
   1. KPIs,
   2. overall structure,
   3. duty logic,
   4. and operational coherence.
8. If the change improves the result, continue with formal review.
9. If the change worsens the result, keep the published version as reference and decide whether to fix or discard the iteration.

For the reference case, compare:
1. L1’s published solution,
2. the new iteration with adjusted rules,
3. and what changed in quality, feasibility, or balance.

When you finish this section, you should have a newly calculated solution and a clear baseline to compare it to the previously published version.

## Deciding whether the new iteration will replace the active version

The last step is deciding whether this iteration should become the new operational version. A new iteration does not automatically replace the previous publication. To reach production, it must go through review, validation, and publication in its own lifecycle.

Before you finish, make sure that:
1. You calculated the new iteration.
2. You compared the result with the published solution.
3. You know whether the change delivers real improvement or only a non-operational variant.

To close the iteration decision:
1. Review the new solution from a technical and operational perspective.
2. If it clearly improves the active solution, prepare it for:
   1. validation,
   2. and later publication.
3. If it does not improve the result, keep the current published version as the active reference.
4. Do not remove the previous publication just because a new iteration exists.
5. Keep both versions well identified for audit and historical comparison.
6. If you move forward, treat the iteration as a new scenario that must follow its own flow until it becomes **Published**.

For the reference case, finish this quick start only when you can state one of these:
1. The new L1 iteration improves the published version and should continue its lifecycle.
2. The current published version is still better, and the iteration will remain only as a test or analysis reference.

When you finish this section, you should have a new iteration calculated, compared, and ready to become a new version—or to remain as an analysis variant.

## Additional reading

- [Running and validating the first Scheduling calculation](P15_Running_and_validating_the_first_scheduling_calculation.md)

