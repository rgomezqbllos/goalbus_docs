---
title: Publishing the scenario on specific dates
shortTitle: Publish Scenario
intro: Learn how to publish a validated scenario on specific dates, control what solution
  goes into operation, and maintain traceability between planning, validation, and
  operational deployment.
contentType: how-tos
versions:
- '*'
---
## Preparing the validated scenario before publishing

After calculating and validating a solution, the next step is to decide **when** must enter into force in the actual operation. Publishing a scenario is not just about approving it: it is about inserting that validated solution into the operating calendar for a specific date, without confusing it with a draft or a version still under revision.

Use this quick start when you already have a stage with a solution in **Validate** status and need to take it to operation for a specific period.

Before you start, make sure that:
1. You've already run and validated the scenario on P15.
2. The scenario solution you want to publish is in **Validate** status.
3. You know what exact dates you want to cover.
4. You are clear that publishing changes the operating status of the solution and makes it visible as an implanted version.

For this quick start, use this reference case:

> **I will publish the validated scenario of line L1 so that it will enter into force during a specific working period without affecting solutions that do not correspond to those dates.**

To prepare the publication of the scenario:
1. Open the **Planning scenarios** module.
2. Locate the scenario you've already validated.
3. Check that the current state of the solution is **Validate**.
4. Check the name of the stage, the line(s) included, the day type and the description.
5. Confirm that you are about to publish exactly the right solution.
6. If the scenario is not yet validated, go back and finish P15 before continuing.
7. If the scenario is correct, continue with the publication.

When you finish this section, you should have clearly identified the validated scenario you want to implement.

## Selecting the temporary publishing window

Once the scenario is confirmed, you need to decide **on which dates** is going to apply. Publication should not be made ambiguously. It should be clear from when and until when that solution will be operational reference.

Before starting this section, make sure that:
1. You've already confirmed what scenario you're going to publish.
2. You know if the publication will cover a day, a week, a continuous range, or a longer operating block.
3. You are already clear that the chosen period should not contradict the type of day and the temporal logic of the scenario.

To select the temporary publishing window:
1. From the validated scenario, open the **Publish** action.
ref: P16_Imagen1.png | compact
2. In the publication form, you define the **Date range**.
3. Add another **Date ranges**, if you consider it and post for other non-selected days (optional).
ref: P16_Imagen2.png | compact(x12)
4. Check that the dates make sense for:
   1. the stage day guy,
   2. the line(s) involved,
   3. And the real operating window you want to cover.
5. Confirm that you are not leaving a range too wide by mistake.
6. If the scenario should only be applied in a short period, it limits the window precisely.
7. Confirms publication for the chosen date/s range/s.

For the reference case, ask yourself:
1. Does the publication cover exactly the working days I want to implement?
2. Am I avoiding publishing more days than is necessary?
3. Does the solution really correspond to the dates selected?

When you finish this section, you should have a clear, controlled time window defined for implantation.

## Confirming publication and changing scenario status

After selecting the time range, you need to confirm the publishing action. At this point, the solution ceases to be just a validated scenario and becomes operational within the calendar.

Before continuing, make sure that:
1. You've already selected the dates correctly.
2. You've already checked the validated scenario.
3. You are already ready for the solution to advance in its life cycle.

To publish the scenario:
1. Review the publication summary for the last time.
2. Confirms:
   1. the name of the stage,
   2. the time range,
   3. and the operational context to which it will apply.
3. Run the **Publish** action.
4. Check that the stage status changes to **Publication** while the system processes the implantation.
5. Wait till the process is over.
6. Check that the final state of the solution changes to **Published**.
ref: P16_Imagen3.png | compact
7. If the state doesn't change as expected, check if there was a technical incidence or a scenario eligibility problem.

For the reference case, do not terminate the publication until you can state:
1. The L1 scenario solution has already come out of **Validate**.
2. The platform processed the publication.
3. The final stage state solution is **Published**.

When you finish this section, you should have a scenario already implanted in the operating calendar for the selected period.

## Verifying that the published solution is the one in force

After publishing, you need to check that the solution that was active is really the right one. Publishing should not be a blind step. You should be able to verify which scenario was valid for the chosen dates and keep traceability on the implemented solution.

Before starting this section, make sure that:
1. The scenario solution has already reached **Published** status.
2. You know what dates it covers.
3. You know which service or line should be affected by the publication.

To verify the implementation of the solution:
1. Go back to the main scenario table.
2. Filter or review the scenarios by status.
3. Confirms that the published scenario solution appears as **Published**.
4. Check your application dates, if the view allows.
5. Check that you're not confusing this scenario with another validated but not implanted.
6. If your internal process requires it, register or communicate that this version is already the current operating solution.
7. It retains the name, description and time range as the traceability base for subsequent audit.

For the reference case, make sure that:
1. The published scenario corresponds to L1 workable.
2. The dates match the period you wanted to implement.
3. No other scenario was activated by mistake.

When you finish this section, you should be sure what solution was in place and for what exact period.

## Maintaining traceability and preparing the next iteration

Once the scenario is published, the work does not disappear: it changes focus. From here, the implemented solution can become a reference for audit, comparison or future iteration. It is not advisable to reuse without control an already published scenario to undergo structural changes; the safest thing is to create a new iteration when you need to propose an improvement or a variant.

Before you finish, make sure that:
1. The scenario is already published.
2. It is clear what time range it covers.
3. You know if the next thing will be to audit results or prepare a new iteration.

To maintain traceability after publication:
1. It preserves the published scenario with a sufficiently clear name and description.
2. Use the **Published** status as a reference to distinguish it from scenarios in draft, calculation or validation.
3. If you need to propose an improvement, create a new scenario instead of altering the historical logic of the implanted scenario.
4. If your team works with later revision, use this published version as a baseline comparison.
5. Keep an internal record of:
   1. what was published,
   2. when it was published,
   3. and for what dates it was valid.

For the reference case, finish this quick start only when you can say:
1. The L1 solution is already published.
2. You know exactly when it came into effect.
3. You can distinguish this published version from any future iteration.

When you finish this section, you should have a published, traceable and ready solution to serve as an operational reference or as a starting point for a new iteration.

## Additional readings

- [Creating a new iteration of the scenario from a published solution](iteracion-del-escenario)
