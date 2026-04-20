---
title: Creating the calendar foundation with day types and holidays
shortTitle: Day types and holidays
intro: 'Learn how to configure day types and holidays so planning logic applies the correct operating pattern before moving on to routes, travel times, and service creation.'
contentType: how-tos
versions:
  - '*'
---

## Creating the day type you will use for planning

Before creating services or running planning calculations, you need to define the calendar logic that tells the system what type of day it is working with. In GoalBus, day types are operational categories that group days such as standard workdays, Fridays, weekends, or special days, so you don’t have to build planning logic date by date.

Use this quick start when you are preparing your first planning case, when you need to create or validate the day type your scenario will use, or when you want to make sure holiday logic is ready before you continue.

Before you begin, make sure that:
1. You have access to the environment with permissions to view or edit calendar configuration.
2. You already know what planning case you want to build.
3. You already know what period you want to prepare, for example January 2026.
4. You already reviewed your planner role and the overall flow in P1.

For this quick start, use this reference case:

> **I am preparing the calendar foundation for a workday scenario for January 2026, including the correct holiday behavior.**

To create or validate the day type for your case:
1. In GoalBus, go to **Configuration** > **Time Management** > **Day type management**.
ref: P2_Imagen1.png | compact
2. Review the existing day types and check whether one already represents the operating logic you need.
3. If a suitable day type already exists, confirm that:
   1. Its name is clear.
   2. Its short name is clear.
   3. It truly represents the operating pattern you need.
4. If a suitable day type does not exist, click **Create day type**.
ref: P2_Imagen2.png | full
5. Define the **name** and **short name** for the new day type.
ref: P2_Imagen3.png | compact
6. Select the days of the week that apply to that day type.
ref: P2_Imagen4.png | compact
7. If the day type should also apply to holidays, enable the option to apply the day type to holidays.
ref: P2_Imagen5.png | compact
8. Save the day type.
9. Review the result and confirm the day type now clearly represents the case you are preparing.

When you finish this section, you should have a day type the system can use as the operational category for your planning case.

## Registering holidays that change the normal calendar logic

After defining the general day type, you need to tell the system what to do with exceptional dates. Holidays matter because the calendar may say a date is Tuesday, while operations should behave like a Sunday or another special pattern. If holidays are not registered correctly, the system may apply the wrong plan when you later publish or calculate scenarios.

Before you start this section, make sure that:
1. You already created or confirmed the day type your case will use.
2. You know whether the planning period includes holidays or special dates.
3. You are ready to decide which operating pattern each holiday should follow.

To register and validate the holidays for your case:
1. In the same day type management section, switch to the **Holidays** tab.
ref: P2_Imagen6.png | compact
2. Check whether the holiday you need already exists in the system.
3. If the holiday does not exist, create a new holiday record.
4. If the holiday already exists, open it and review its configuration.
5. Enter or confirm the holiday **name**.
6. Assign the correct **day type** to that holiday.
ref: P2_Imagen7.png | compact
7. Save the holiday record.
8. Repeat this process for any other holiday that affects the period you are preparing.
9. Review the holiday list and confirm every exceptional date points to the correct operating pattern.

For the reference case, ask yourself:
1. Does January 2026 include any holiday that should behave differently from a standard workday?
2. Should that holiday behave like a Sunday, a Saturday, or another special day type?
3. If you published a scenario for this period, would the system know exactly which pattern to apply on that date?

When you finish this section, the system should be able to override normal calendar behavior on the holiday dates that matter for your case.

## Checking that your calendar foundation is ready for planning

Now that you defined the general day type and holiday exceptions, you need to confirm the calendar foundation is actually usable. This is where you verify that the structure you created can support the next quick starts without introducing avoidable errors.

Before you continue, make sure that:
1. The day type exists and has the correct weekly logic.
2. The relevant holidays are registered.
3. Each holiday is linked to the correct day type.
4. Your planning case is still clear and specific.

To validate your calendar foundation before moving to the next quick start:
1. Review the planning case you defined at the start of this article.
2. Confirm the day type you created or validated matches that case.
3. Confirm any holiday within the planning period has been registered and associated with the correct day type.
4. Check whether the holiday-application option you enabled in the day type truly reflects the behavior you want.
5. Ask yourself whether the system could already distinguish:
   1. the normal days in the period, and
   2. the exceptional dates that must follow a different operating pattern.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, go back and correct the day type or holiday associations before proceeding.

When you finish this section, you should be able to state that your planning case has a reliable calendar foundation and that the next quick starts can build on it without inheriting a time-logic error.

## Additional reading

- [Validating the operational year before planning](P3_Validating_the_operational_year_before_planning.md)

