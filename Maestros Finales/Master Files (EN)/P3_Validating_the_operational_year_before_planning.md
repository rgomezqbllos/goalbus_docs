---
title: Validating the operational year before planning
shortTitle: Operational year
intro: 'Learn how to validate the operational year that will support your planning case to avoid gaps, overlaps, or artificial breaks in the data before moving on to the network, infrastructure, and services.'
contentType: how-tos
versions:
  - '*'
---

## Creating or validating the operational year your planning will use

Before continuing with the network, times, services, or rules, you need to check that the period you want to plan falls within the **correct operational year**. In GoalBus, the operational year exists to adapt the system’s time logic to business reality. This matters because many operations do not follow the calendar year from January to December. For example, a school operation may run from September to August, and a fiscal or union contract may require a different range.

Use this quick start when you have already defined day types and holiday logic, when you want to prepare your first real planning case, or when you need to confirm the period you will use is supported by a valid timeline.

Before you begin, make sure that:
1. You already reviewed the planner role in P1.
2. You already configured or validated day types and holidays in P2.
3. You know exactly which period you want to plan.
4. You have access to the environment with permissions to view or edit time configuration.

For this quick start, use this reference case:

> **I’m going to plan January 2026 and I need to confirm that period falls within the correct operational year before continuing with my first planning work.**

To create or validate the operational year for your case:
1. In GoalBus, go to **Configuration**.
2. Open **Time Management** > **Operational years**.
ref: P3_Imagen1.png | compact
3. Review existing operational years and identify which one should cover the period you want to plan.
4. If a suitable operational year does not exist, click the option to create a new one by selecting **Create Operational Year**.
ref: P3_Imagen2.png | full
5. Define a **Unique Name** and, if needed, a **Description**.
6. Adjust the **Start date** and **End date** to match the operational or fiscal reality of your case.
7. Associate the **Business Units** if applicable.
8. Save the operational year.
ref: P3_Imagen3.png | compact
9. Confirm the period you want to plan is fully covered by that year.
10. If the year already existed, still verify it remains the right one for your case and that its dates are not ambiguous.

When you finish this section, you should have identified or created the operational year that truly supports your planning case.

## Reviewing time continuity and avoiding gaps or overlaps

After identifying the correct operational year, you need to verify that its time sequence is coherent. In GoalBus, continuity between operational years is not optional. The system is designed to prevent **gaps** or **overlaps** between years, because those errors would eventually affect accumulated metrics, annual KPIs, and downstream calculations.

Before you start this section, make sure that:
1. You already found the operational year that should cover your case.
2. You know its start date and end date.
3. You know whether there are previous or next years that belong to the same sequence.

To review the time continuity of the operational year:
1. Open the details of the operational year you will use as reference.
2. Review the **Start date** and **End date**.
3. Verify the period you want to plan falls within that range without ambiguity.
4. Review the previous or next operational year, if it exists, to ensure there are no:
   1. gaps between years, or
   2. overlaps between two time ranges.
5. If you need to create a new year at the end of the sequence, add it only at the end and verify it continues exactly where the previous one ends.
6. If you detect an inconsistency, correct the dates before you continue.
7. Confirm the system allows you to save the sequence without blocking due to continuity errors.

For the reference case, ask yourself:
1. Is January 2026 fully within a valid operational year?
2. Does that year connect correctly to the previous and the next one?
3. Could the system accumulate data without breaking continuity across the period?

When you finish this section, you should be confident there are no gaps or overlaps affecting your case.

## Checking the relationship between the operational year and calendar logic

Now that you validated the operational year and its continuity, you need to connect it with what you defined in P2. There is little value in having day types and holidays configured correctly if the time frame where those data live is not built correctly.

Before you continue, make sure that:
1. The correct operational year is already identified.
2. The day types and holidays for the case are already configured.
3. The period you will plan is still clear and bounded.

To check the operational year is ready to support planning:
1. Review the planning case you defined at the start of this article.
2. Confirm that period lives within the correct operational year.
3. Confirm the calendar logic defined in P2 also applies within that same time frame.
4. Ask yourself whether the system could already use, at the same time:
   1. the correct day type category,
   2. the correct holidays, and
   3. the correct operational year.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct the operational year or review coherence with the calendar before proceeding.

When you finish this section, you should be able to state that your case has a complete time foundation: the correct calendar and the correct operational year.

## Additional reading

- [Defining vehicle types and allowed fleet by line](P4_Defining_vehicle_types_and_allowed_fleet_by_line.md)

