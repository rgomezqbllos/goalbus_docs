---
title: Running and validating the first Scheduling calculation
shortTitle: Calculate and validate
intro: 'Learn how to run the first Scheduling calculation, review the scenario lifecycle, validate the prepared solution, and leave the scenario ready for publication or later audit.'
contentType: how-tos
versions:
  - '*'
---

## Running scenario calculation

Now that your scenario is created and configured with the validated offer, the correct matrices, and the vehicle/shift rules models, the next step is to run calculation.

In this phase, the engine takes:
1. the validated offer,
2. the active rules,
3. deadhead-trip logistics,
4. and the scenario structure,

to build schedulable logical duties.

Use this quick start when your Scheduling scenario is ready and you need to obtain the first calculated solution before reviewing and validating it.

Before you begin, make sure that:
1. You already created the scenario in P14.
2. You selected the correct validated service.
3. You assigned the appropriate deadhead-trip matrix.
4. You selected the correct vehicle rules model.
5. You selected the correct shift rules model.
6. You configured the Classic engine and calculation parameters.

For this quick start, use this reference case:

> **I’m going to run the first calculation of the Scheduling scenario for line L1, review whether the solution is coherent, and leave the scenario ready for validation.**

To run scenario calculation:
1. Open the scenario you want to calculate.
2. Review one last time that the scenario inputs are correct.
3. Run **Calculate** / **Start calculation**.
ref: P15_Imagen1.png | compact
ref: P15_Imagen2.png | compact
4. Confirm the scenario status changes from **Solution pending** to **Solution calculation**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Wait for the engine to finish.
ref: P15_Imagen5.png | full
6. Review the scenario’s new status.
7. If calculation completes successfully, confirm the scenario moves to **Solution prepared**.
ref: P15_Imagen6.png | compact
8. If the solution needs manual adjustments, enter **Edit** for refinement.
9. If the engine does not return a valid solution, review again:
   1. the offer,
   2. the deadhead-trip matrix,
   3. the rules,
   4. and the scenario parameters.

For the reference case, confirm that:
1. The L1 scenario leaves the initial status.
2. The engine completes without getting stuck.
3. The scenario reaches a prepared solution or a reasonable edit phase.

Also, if the chosen scenario type includes vehicles and duties, you can see the generated duty solution from the staff view.
ref: P15_Imagen12.png | compact

When you finish this section, you should have a first calculated solution—or a clear signal of which part of parameterization needs correction.

## Reviewing scenario status and calculation results

After running calculation, you need to understand where the scenario landed in the lifecycle. Each status has a different operational meaning and tells you what you can do next.

Before you start this section, make sure that:
1. You already ran calculation.
2. You know the name of the scenario you are reviewing.
3. You know whether you expected a ready solution or a refinement phase.

To review status and results:
1. Return to the main scenarios table or stay inside the scenario.
2. Review the current status.
3. Interpret the status using this logic:
   1. **Solution pending**: the scenario has not been calculated yet.
   2. **Solution calculation**: the engine is processing the solution.
   3. **Edit**: a user is manually adjusting the solution.
   4. **Solution prepared**: calculation/editing is finished and the scenario is ready for review.
   5. **Validated**: the solution has been approved and locked.
   6. **Publishing**: the solution is being inserted into the operational calendar.
   7. **Published**: the solution is already deployed to operations.
4. If the scenario is in **Solution prepared**, continue with the coherence review.
5. If the scenario is in **Edit**, finish the needed manual adjustments first.
6. If the scenario stays in **Solution calculation** too long, check whether there was a technical issue or overly restrictive configuration.

For the reference case, you should expect the scenario to end at least in:
1. **Solution prepared**, if you no longer need to adjust structure, or
2. **Edit**, if you still want to refine manually.

When you finish this section, you should clearly understand what the current status means and what action should follow.

## Reviewing KPIs, errors, and consistency before validating

Before validating the scenario, you need to review it. Validation is not just an administrative click. It is the formal approval gate that freezes the solution and prevents accidental changes later.

Before you start this section, make sure that:
1. The scenario is in **Solution prepared**, or you finished **Edit**.
2. You understand the scenario will stop being editable after validation.
3. You are ready for a final review before approval.

To review the solution before validating:
1. Open the scenario in its current status.
2. Review available KPIs.
ref: P15_Imagen7.png | full
3. Check for visible errors, warnings, or inconsistencies.
ref: P15_Imagen8.png | compact
4. Use available filters to inspect the solution from different angles.
ref: P15_Imagen9.png | compact
5. Confirm assignments and structure make operational sense.
6. If you find a minor problem and the scenario is still editable, fix it before continuing.
7. If you find a major issue after it is locked later, you will need to unlock with the appropriate permissions or return to an editable scenario.

For the reference case, make sure that:
1. L1 solution KPIs are reasonable.
2. There are no major errors that invalidate the solution.
3. The solution can move from technical review to formal approval.

When you finish this section, you should have enough confidence to validate the scenario.

## Validating the scenario and locking the solution

Now you can run **scenario validation**. This step officially closes calculation and editing. From here, the solution becomes protected, the scenario becomes non-editable, and it cannot be recalculated while it remains validated.

Before you start this section, make sure that:
1. The scenario is in **Solution prepared**.
2. You finished KPI and error review.
3. You do not need more manual adjustments before approval.

To validate the scenario:
1. From the scenarios table, open the scenario actions menu.
2. Select **Validate**.
3. If you prefer to do it inside the scenario, use the **Validate** button at the top of the screen.
ref: P15_Imagen10.png | compact
4. Confirm validation when prompted.
5. Confirm the scenario solution status changes to **Validated**.
ref: P15_Imagen11.png | compact
6. Verify that:
   1. the scenario is no longer editable,
   2. it can no longer be recalculated,
   3. and its key data are protected.
7. If you discover a last-minute issue after validation, use the unlock flow only with the appropriate permissions.

For the reference case, do not proceed until you can state:
1. L1’s solution has been reviewed.
2. The scenario solution changed to **Validated**.
3. The organization can treat the scenario as an approved version.

When you finish this section, you should have a formally approved, locked solution to prevent accidental changes.

## Leaving the scenario ready for publication or later audit

Once validated, the scenario is ready for two paths:
1. **publication**, if you want to deploy it to the operational calendar,
2. or **audit**, if you still need to review it before publishing.

At this point the scenario is an approved, protected solution. You can still consult it, review KPIs, filter, and use it as a reference—but it should no longer be treated as a working draft.

Before you finish, make sure that:
1. The scenario solution is **Validated**.
2. You know the difference between validating and publishing.
3. You know whether your next step is deploying or auditing.

To leave the scenario ready for the next step:
1. Review the scenarios table and confirm the **Validated** status.
2. If the plan is approved for deployment, prepare the **Publish** flow.
3. If you still need internal review, keep the scenario validated as an audit baseline.
4. Use filters, info icons, and status review to control which scenarios are pending, validated, or already published.
5. If you need to iterate, consider duplicating the scenario instead of altering an already approved one.

For the reference case, finish this quick start only when you can state:
1. The L1 scenario has been calculated.
2. The solution has been reviewed.
3. The scenario solution is **Validated**.
4. The next step is no longer calculation, but deciding whether to publish or audit.

When you finish this section, you should have a calculated, reviewed, validated scenario ready for production or final review.

## Additional reading

- [Publishing the scenario for specific dates](P16_Publishing_the_scenario_for_specific_dates.md)

