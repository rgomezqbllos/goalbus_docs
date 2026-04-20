---
title: Publishing the scenario for specific dates
shortTitle: Publish scenario
intro: 'Learn how to publish a validated scenario for specific dates, control which solution enters operations, and maintain traceability across planning, validation, and operational deployment.'
contentType: how-tos
versions:
  - '*'
---

## Preparing the validated scenario before publishing

After calculating and validating a solution, the next step is deciding **when** it should become effective in real operations. Publishing a scenario is not just approving it—it is inserting that validated solution into the operational calendar for specific dates, without confusing it with a draft or a version still under review.

Use this quick start when you already have a scenario whose solution is in **Validated** status and you need to deploy it to operations for a specific period.

Before you begin, make sure that:
1. You already ran and validated the scenario in P15.
2. The scenario solution you want to publish is **Validated**.
3. You know the exact dates you want to cover.
4. You understand publishing changes the operational status of the solution and makes it visible as a deployed version.

For this quick start, use this reference case:

> **I’m going to publish the validated scenario for line L1 so it becomes effective during a specific workday period without affecting solutions that do not correspond to those dates.**

To prepare publishing:
1. Open the **Planning scenarios** module.
2. Locate the scenario you already validated.
3. Confirm the current solution status is **Validated**.
4. Review the scenario name, included line(s), day type, and description.
5. Confirm you are about to publish exactly the correct solution.
6. If the scenario is not validated yet, go back and complete P15 before continuing.
7. If it is correct, proceed to publishing.

When you finish this section, you should have clearly identified the validated scenario you want to deploy.

## Selecting the publication time window

Once the scenario is confirmed, you need to decide **which dates** it applies to. Publishing should not be ambiguous. It must be clear from when until when this solution will be the operational reference.

Before you start this section, make sure that:
1. You confirmed which scenario you will publish.
2. You know whether publication covers a day, a week, a continuous range, or a longer operational block.
3. You understand the chosen period must not contradict the scenario’s day type and time logic.

To select the publication time window:
1. From the validated scenario, open the **Publish** action.
ref: P16_Imagen1.png | compact
2. In the publishing form, define the **Date range**.
3. Add additional **Date ranges** if needed (optional).
ref: P16_Imagen2.png | compact
4. Confirm the dates make sense for:
   1. the scenario’s day type,
   2. the involved line(s),
   3. and the real operational window you want to cover.
5. Confirm you are not leaving an overly broad range by mistake.
6. If the scenario should apply only in a short period, limit the window precisely.
7. Confirm publishing for the selected date range(s).

For the reference case, ask yourself:
1. Does publication cover exactly the workdays I want to deploy?
2. Am I avoiding publishing more days than necessary?
3. Does the solution truly correspond to the selected dates?

When you finish this section, you should have a clear, controlled time window for deployment.

## Confirming publication and changing scenario status

After selecting the time range, confirm the publishing action. At this point, the solution stops being only a validated scenario and becomes an operational item in the calendar.

Before you continue, make sure that:
1. You selected the dates correctly.
2. You reviewed the validated scenario.
3. You are ready for the solution to advance in its lifecycle.

To publish the scenario:
1. Review the publishing summary one last time.
2. Confirm:
   1. the scenario name,
   2. the time range,
   3. and the operational context it applies to.
3. Run **Publish**.
4. Confirm the scenario status changes to **Publishing** while the system processes deployment.
5. Wait for the process to finish.
6. Confirm the final solution status changes to **Published**.
ref: P16_Imagen3.png | compact
7. If the status does not change as expected, check for a technical incident or an eligibility issue.

For the reference case, do not consider publishing complete until you can state:
1. L1’s scenario solution left **Validated**.
2. The platform processed publication.
3. The final scenario solution status is **Published**.

When you finish this section, you should have a scenario deployed to the operational calendar for the selected period.

## Verifying the published solution is the one in effect

After publishing, confirm the active solution is actually the correct one. Publishing should not be a blind step. You should be able to verify which scenario is in effect for the selected dates and maintain traceability for the deployed solution.

Before you start this section, make sure that:
1. The scenario solution is **Published**.
2. You know which dates it covers.
3. You know which line/service should be affected by publishing.

To verify deployment:
1. Return to the main scenarios table.
2. Filter or review scenarios by status.
3. Confirm the published scenario shows as **Published**.
4. Review its application dates if the view supports it.
5. Confirm you are not confusing it with another validated-but-not-deployed scenario.
6. If your internal process requires it, record or communicate that this version is now the active operational solution.
7. Preserve the name, description, and time range as traceability for later audit.

For the reference case, make sure that:
1. The published scenario corresponds to workday L1.
2. The dates match the period you wanted to deploy.
3. No other scenario was accidentally made active.

When you finish this section, you should be certain which solution is in effect and for which exact period.

## Maintaining traceability and preparing the next iteration

Once a scenario is published, the work does not disappear—it changes focus. The deployed solution can become a baseline for audit, comparison, or a future iteration. It is safer to create a new iteration when you need to propose improvements, rather than altering a published scenario for structural changes.

Before you finish, make sure that:
1. The scenario is published.
2. The covered time range is clear.
3. You know whether the next step is auditing results or preparing a new iteration.

To maintain traceability after publishing:
1. Keep the published scenario with a clear enough name and description.
2. Use the **Published** status to distinguish it from draft, calculating, or validated scenarios.
3. If you need to propose an improvement, create a new scenario instead of altering historical logic.
4. If your team does post-review, use the published version as the comparison baseline.
5. Keep an internal record of:
   1. what was published,
   2. when it was published,
   3. and for which dates it was in effect.

For the reference case, finish this quick start only when you can state:
1. L1’s solution is published.
2. You know exactly from which date it became effective.
3. You can distinguish this published version from any future iteration.

When you finish this section, you should have a published, traceable solution ready to serve as an operational reference or as the starting point for a new iteration.

## Additional reading

- [Creating a new scenario iteration from a published solution](P17_Creating_a_new_scenario_iteration.md)

