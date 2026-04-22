---
title: Validating the operating year before planning
shortTitle: Operational year
intro: Learn how to validate the operating year that will sustain your planning case
  to avoid gaps, overlaps or artificial cuts in data before moving to network, infrastructure
  and services.
contentType: how-tos
versions:
- '*'
---
## Creating or validating the operating year that will use your planning

Before you continue with network, times, services or rules, you need to check that the period you want to plan falls within the **correct operating year**. In GoalBus, the operating year exists to adapt the system's temporal logic to the reality of the business. This is important because many operations do not follow the calendar year from January to December. For example, a school operation can work from September to August, and a tax or union contract may need another rank.

Use this quick start when you already have defined the logic of day and holiday types, when you want to prepare your first real planning case, or when you need to confirm that the period you are going to use is supported by a valid timeline.

Before you start, make sure that:
1. You've already reviewed the role of the planner in P1.
2. You have already set or validated the types of holidays and days in P2.
3. You know exactly what period you want to plan.
4. You have access to the environment with permissions to query or edit the temporary settings.

For this quick start, use this reference case:

> **I will plan January 2026 and need to confirm that that period falls within the correct operating year before proceeding with my first planning.**

To create or validate the operating year of your case:
1. In GoalBus, go to **Settings**.
2. Opens the **Time Management** section > **Operational years**.
ref: P3_Imagen1.png | compact
3. Check existing operating years and find which one should cover the period you want to plan.
4. If there is no suitable operating year, click on the option to create a new one by clicking on **Create Operational Year**.
ref: P3_Imagen2.png | full
5. Define an **Unique name** and, if you need it, an **Description**.
6. Adjust the **Start date** and **End date** to suit the operational or fiscal reality of your case.
7. Associate the **Business Units** if there were any.
8. Save the operating year.
ref: P3_Imagen3.png | compact(x10)
9. Confirm that the period you want to plan is fully covered for that year.
10. If the year already existed, check also that it is still the right one for your case and that its dates do not give rise to doubts.

By the time you finish this section, you should have identified or created the operating year that really supports your planning case.

## Reviewing time continuity and avoiding gaps or overlaps

After identifying the correct operating year, you need to check that its time sequence is consistent. In GoalBus, continuity between operating years is not optional. The system is designed to prevent **Gaps** or **overlaps** from existing between years, because those errors would end up affecting accumulated metrics, annual KPIs and later calculations.

Before starting this section, make sure that:
1. You've already found the operating year that should cover your case.
2. You know his start date and his end date.
3. You know if there are previous or later years that are part of the same sequence.

To review the time continuity of the operating year:
1. Open the detail of the operating year you will use as a reference.
2. Check the **Start date** and the **End date**.
3. Check if the period you want to plan falls within that unambiguous range.
4. Review the previous or subsequent operating year, if any, to ensure that there are no:
   1. gaps between one year and another; or
   2. overlaps between two time ranges.
5. If you need to create a new year at the end of the sequence, add it only at the end and check to continue exactly where the previous one ends.
6. If you notice a inconsistency, correct the dates before continuing.
7. Confirms that the system allows to save the sequence without blocking the save due to continuity errors.

For the reference case, ask yourself these questions:
1. Is January 2026 fully in a valid operating year?
2. Does that year connect correctly with the previous year and the next year?
3. Could the system accumulate data without breaking the continuity of the period?

When you finish this section, you should be sure that there are no gaps or overlaps that affect your case.

## Checking the relationship between the operating year and the calendar logic

Now that you've validated the operating year and its continuity, you need to connect it to what you defined in P2. It's not helpful to have well-configured holiday and day types if the time frame where those data will live is not well built.

Before continuing, make sure that:
1. The correct operating year is already identified.
2. The types of days and holidays of the case are already configured.
3. The period you plan is still clear and narrowed down.

To check that the operating year is ready to sustain the planning:
1. Review the planning case you defined at the beginning of this article.
2. Confirms that this period lives within the correct operating year.
3. Checks that the calendar logic defined in P2 also applies within the same time frame.
4. Ask yourself if the system could already use simultaneously:
   1. the correct category of day type,
   2. the correct holidays; and
   3. the correct operating year.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct the operating year or review the consistency with the calendar before continuing.

At the end of this section, you should be able to state that your case has a full time base: correct calendar and correct operating year.

## Additional readings

- [Preparing the master network: stops, lines and routes](P4_Defining_Vehicle_Types_And_Fleet_Allowed_Per_Line.md)
