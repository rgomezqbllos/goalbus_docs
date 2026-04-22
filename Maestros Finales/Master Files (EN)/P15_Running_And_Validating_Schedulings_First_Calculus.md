---
title: Running and Validating Scheduling's First Calculus
shortTitle: Calculate and validate
intro: Learn how to run Scheduling's first calculus, review the stage life cycle,
  validate the prepared solution, and leave the scenario ready for publication or
  subsequent audit.
contentType: how-tos
versions:
- '*'
---
## Running the scenario calculation

Now that you already have the scenario created and configured with the validated offer, the correct matrices and the models of vehicle rules and turns, the next step is to run the calculation.

At this stage, the engine takes:
1. the validated offer,
2. active rules,
3. the logistics of empty travel,
4. and the structure of the stage,

to build programmable logical tasks.

Use this quick start when you have the Scheduled scenario ready and need to get the first calculated solution before reviewing and validating it.

Before you start, make sure that:
1. You already set the stage at P14.
2. You've already selected the correct validated service.
3. You've already assigned the proper empty travel matrix.
4. You've already selected the right model of vehicle rules.
5. You've already selected the right model of shift rules.
6. You've already set up the Classic engine and the calculation parameters.

For this quick start, use this reference case:

> **I'm going to run the first calculation of the Scheduled scenario on line L1, check if the solution is consistent and leave the scenario ready for validation.**

To run the scenario calculation:
1. Open the scenario you want to calculate.
2. Check one last time that the stage tickets are correct.
3. Launch the **Calculate** or **Start calculation** action.
ref: P15_Imagen1.png | compact(3x)
ref: P15_Imagen2.png | compact
4. Check that the stage status changes from **Pending solution** to **Calculation of the solution**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Wait for the engine to finish the process.
ref: P15_Imagen5.png | compact(1x18)
6. Check the new stage state.
7. If the calculation concludes correctly, it confirms that the scenario passes to **Prepared solution**.
ref: P15_Imagen6.png | compact(x7)
8. If the solution requires manual adjustments, enter the **Editing** status for refinement.
9. If the engine does not return a valid solution, check again:
   1. the offer,
   2. the empty travel matrix,
   3. the rules,
   4. and the parameters of the scenario.

For the reference case, it confirms that:
1. The L1 scenario comes out of the initial state.
2. The engine completes the calculation without blocking.
3. The scenario comes to a prepared solution or a reasonable editing phase.

In addition, in case the type of scenario chosen is for vehicles and shifts, you can see the solution generated from shifts from the staff view.
ref: P15_Imagen12.png | compact

When you finish this section, you should have a first calculated solution or a clear signal of which part of the parameterization needs correction.

## Reviewing the state of the scenario and the result of the calculation

After running the calculation, you need to understand at which point in the life cycle the scenario has remained. This is important because each state has a different operational meaning and tells you what actions you can do next.

Before starting this section, make sure that:
1. You've already run the calculus.
2. You know the name of the stage you're reviewing.
3. You know if you were expecting a ready solution or a refinement phase.

To review the status and result:
1. Go back to the main scenario table or stay on stage.
2. Check the current state.
3. He interprets the state according to this logic:
   1. **Pending solution**: The scenario has not yet been calculated.
   2. **Calculation of the solution**: The engine is processing the solution.
   3. **Editing**: A user is manually adjusting the solution.
   4. **Prepared solution**: The calculation or editing phase is over and the scenario is ready for revision.
   5. **Validation**: The solution has already been approved and blocked.
   6. **Publication**: The solution is being incorporated into the operating calendar.
   7. **Published**: The solution was already implanted in the operation.
4. If the scenario is in **Prepared solution**, continue with the consistency review.
5. If the scenario is in **Editing**, finish the necessary manual settings first.
6. If the scenario is still in **Calculation of the solution** for too long, check whether there was an overly restrictive technical incidence or configuration.

For the reference case, you should expect the scenario to end at least in:
1. **Prepared solution**, if you no longer need to touch the structure,
2. or **Editing**, if you still want to refine manually.

When you finish this section, you should clearly understand what the current stage state means and what action follows.

## Checking KPI, errors and consistency before validating

Before validating the scenario, you need to review it. Validating is not a simple administrative click. It is the formal approval door that freezes the solution and prevents accidental subsequent changes.

Before starting this section, make sure that:
1. The stage is already in **Prepared solution** or you finished the **Editing** phase.
2. You know, after validating, the scenario will no longer be editable.
3. You're ready for a final review prior to approval.

To review the solution before validating it:
1. It opens the stage in its current state.
2. Check the available KPIs.
ref: P15_Imagen7.png | full
3. Check for visible errors, warnings, or inconsistencies.
ref: P15_Imagen8.png | compact(x7)
4. Use the available filters to inspect the solution from different angles.
ref: P15_Imagen9.png | compact(3x)
5. Checks that the mappings and scenario structure make operational sense.
6. If you detect a minor problem and the scenario is still editable, correct it before continuing.
7. If you detect a major problem after you have blocked it later, you must unlock it with appropriate permissions or return to an editable scenario.

For the reference case, make sure that:
1. The L1 solution KPIs are reasonable.
2. There are no serious errors that invalidate the solution.
3. The solution can now move from technical review to formal approval.

When you finish this section, you should have enough confidence to validate the scenario.

## Validating the stage and blocking the solution

Now you can run the **validation of the scenario**. This step marks the official closing of the calculation and editing phase. From here, the solution becomes protected, the scenario ceases to be editable and can no longer be recalculated while it remains validated.

Before starting this section, make sure that:
1. The stage is on **Prepared solution**.
2. You've finished the KPI review and errors.
3. You don't need to make any more manual adjustments before approving the solution.

To validate the scenario:
1. From the scenario table, open the action menu of the stage.
2. Select **Validate**.
3. If you prefer to do it from within the stage, use the **Validate** button at the top of the screen.
ref: P15_Imagen10.png | compact(2x)
4. Confirm the validation when the system requests it.
5. Check that the stage solution status changes to **Validate**.
ref: P15_Imagen11.png | compact(2x)
6. Check that:
   1. the scenario is no longer editable,
   2. can no longer be recalculated,
   3. and their main data are protected.
7. If you discover a last-minute error after validation, use the unlock flow only with the right permissions.

For the reference case, do not continue until you can state:
1. The L1 solution has already been reviewed.
2. The scenario solution changed to **Validate** status.
3. The organization can already treat that scenario as an approved version.

When you finish this section, you should have a formally approved and blocked solution to avoid accidental changes.

## Leaving the scenario ready for publication or subsequent audit

Once validated, the scenario is ready for two paths:
1. **publication**, if you want to take it to the actual operating calendar,
2. or **audit**, if you still need to review it before publishing.

At this point, the scenario remains an approved and protected solution. You can still consult it, review KPI, filter information and use it as a reference, but you should no longer treat it as a working draft.

Before you finish, make sure that:
1. The stage solution is already in **Validate** status.
2. You know the difference between validating and publishing.
3. You know if your next step will be to implant the solution or continue to audit it.

To leave the stage ready for the next step:
1. Check the scenario table and confirm the **Validate** status.
2. If the plan is already approved for implementation, prepare the **Publish** flow.
3. If you still need internal review, keep the validated scenario as an audit basis.
4. Use filters, information icons, and state review to control which scenarios are pending, validated, or already published.
5. If you need to iterate a new version, consider duplicating the scenario instead of altering one already approved.

For the reference case, finish this quick start only when you can say:
1. The L1 scenario has already been calculated.
2. The solution was reviewed.
3. The stage solution is **Validate**.
4. The next step is no longer to calculate, but to decide whether it is published or audited.

When you finish this section, you should have a calculated, revised and validated scenario, ready for production or final revision.

## Additional readings

- [Publishing the scenario on specific dates](publicacion-del-escenario)
