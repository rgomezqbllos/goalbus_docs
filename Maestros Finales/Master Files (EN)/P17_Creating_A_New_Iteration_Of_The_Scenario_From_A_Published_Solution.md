---
title: Creating a new iteration of the scenario from a published solution
shortTitle: New Iteration
intro: Learn how to create a new iteration of an already published scenario to test
  improvements, adjust parameters or introduce changes without altering the version
  that is already in operation.
contentType: how-tos
versions:
- '*'
---
## Based on a published solution without altering the current version

After publishing a solution, it is normal that you need to keep working on it. You may want to adjust rules, try another turn logic, incorporate offer changes, or prepare an improvement for a future period. In that case, you should not directly modify the already published version. The correct thing is to create an **new iteration** of the scenario to maintain traceability and protect the version that is already in place.

Use this quick start when you already have a stage with a solution in **Published** status and need to generate a new variant without losing the historical reference of the implanted solution.

Before you start, make sure that:
1. You've already posted the previous scenario on P16.
2. The scenario solution you will take as your base is in **Published** status.
3. You know what you want to look like or improve on the next iteration.
4. It is clear that the new iteration should not automatically replace the current version until it passes through calculation, validation and publication again.

For this quick start, use this reference case:

> **I will create a new iteration of the published L1 scenario to test improvements in the solution without touching the version that is already in operation.**

For a securely published solution:
1. In GoalBus, open the **Planning scenarios** module.
2. Locates the scenario whose solution is in **Published** status.
3. Check your name, description, day type and associated lines.
4. Confirm that it is really the version you want to use as a reference.
5. Avoid editing that version directly as if it were a new draft.
6. Decide what change you want to make in the new iteration:
   1. rules,
   2. parameters,
   3. offer,
   4. or structural adjustments allowed.

When you finish this section, you should have clearly identified the published scenario that will serve as the basis for your new iteration.

## Creating the new iteration from the published scenario

Once the base is identified, the next step is to create an **new iteration**. The goal is to preserve the published version as a historical reference and open a new controlled branch of work on the same operational logic.

Before starting this section, make sure that:
1. You've already identified the correct published solution.
2. You know why you need a new iteration.
3. You are clear that the new iteration must be clearly differentiated from the previous version.

To create the new iteration:
1. From the scenario table, open the action menu of the published scenario.
2. Select the option for **create a new iteration** by clicking on **duplicate** the scenario as a working base.
ref: P17_Imagen1.png | compact
3. Enter an **new name** for iteration.
4. If applicable, update the **description** to reflect the change target.
5. Save the new iteration.
ref: P17_Imagen2.png | compact
6. Checks that the new scenario appears as a separate entity from the published scenario.
ref: P17_Imagen3.png | full
7. Check that the original published version remains intact and differentiated from the new one.

For the reference case, a valid option could be:
- **Classic Calculation - L1 workable - Iteration 2**
- **L1 workable - improvement of shift rules**

When you finish this section, you should have a new iteration created without losing the traceability of the published version.

## Defining which changes belong to the new iteration

After creating the iteration, you need to decide what you’re really going to change. Not all iterations pursue the same goal. Some serve to adjust rules, others to improve efficiency, others to reflect a new offer or future operational variation.

Before starting this section, make sure that:
1. You've created the new iteration.
2. You know what aspect of the above solution you want to review.
3. You're willing to limit the switch to a specific target so you don't mix too many variables.

To define the scope of iteration:
1. Open the new stage.
2. Check which items you want to keep exactly the same as in the published version.
3. Decide which item you're going to change first:
   1. **vehicle rules**,
   2. **rules of shift**,
   3. **engine parameters**,
   4. **service offer**,
   5. **Logistic matrices**.
4. Avoid changing too many things at once in the first iteration, unless strictly necessary.
5. Document in the name or description the purpose of the iteration.
6. Save the descriptive changes before going to the calculation.

For the reference case, use a logic like this:
1. Keep the same L1 workable offer.
2. Adjust only the model of shift rules.
3. Recalculate to compare the new solution with the published one.

When you finish this section, you should have a new iteration with a clear, narrowed target.

## Recalculating the iteration and comparing it to the previous version

Once the scope is defined, you need to recalculate the iteration. Here the advantage is that you no longer leave from scratch: parts from a known solution and you can better compare the impact of the change.

Before starting this section, make sure that:
1. You've created the new iteration.
2. You've already defined the goal of change.
3. You've already checked which rules, parameters, or entries you're going to modify.

To recalculate the new iteration:
1. Review the iterated scenario and confirm that its entries remain consistent.
2. Adjust the item you want to modify.
3. Save the settings.
4. Run the calculation of the new scenario.
5. Wait until the scenario completes the calculation phase.
6. Check if iteration passes to **Prepared solution** or **Editing**.
7. Compare the result to the previous version using:
   1. KPI,
   2. general structure,
   3. task logic,
   4. and operational coherence.
8. If the change improves the result, continue with the formal review.
9. If the change worsens the result, keep the published version as a reference and decide if you want to correct or discard this iteration.

For the reference case, compare:
1. The published L1 solution.
2. The new iteration with adjustment of rules.
3. What changed in quality, viability or balance.

When you finish this section, you should have a new calculated solution and a clear basis to compare it with the already published version.

## Deciding whether the new iteration will replace the current version

The last step is to decide whether this iteration deserves to become the new operational version. A new iteration does not automatically replace the previous publication. To arrive at production, you must go back through revision, validation and publication with your own life cycle.

Before you finish, make sure that:
1. You've already calculated the new iteration.
2. You've already compared the result to the published solution.
3. You know if the change brings a real improvement or just a variant with no operational value.

To close the decision on iteration:
1. Review the new solution from a technical and operational point of view.
2. If iteration clearly improves the current solution, prepare it for:
   1. validation,
   2. and subsequent publication.
3. If iteration does not improve the result, it retains the current published version as the current reference.
4. Do not delete the previous publication just because there is a new iteration.
5. Keep both versions well identified for audit and historical comparison.
6. If you decide to move forward, treat iteration as a new scenario that must travel its own flow until it reaches **Published**.

For the reference case, finish this quick start only when you can affirm one of these two things:
1. The new L1 iteration improves the published version and deserves to continue its cycle.
2. The current published version remains better and iteration will remain only as a trial or reference.

When you finish this section, you should have a new iteration calculated, compared and ready to become a new version or to be retained as an analysis variant.

## Additional readings

- [Running and Validating Scheduling's First Calculus](P15_Running_And_Validating_Schedulings_First_Calculus.md)
