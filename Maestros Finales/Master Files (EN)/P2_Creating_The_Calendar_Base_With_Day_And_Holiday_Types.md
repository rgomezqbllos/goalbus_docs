---
title: Creating the calendar base with day and holiday types
shortTitle: Types of days and holidays
intro: Learn how to set up day types and holidays so that the planning logic applies
  the correct operating pattern before moving on to routes, travel times and service
  creation.
contentType: how-tos
versions:
- '*'
---
## Creating the type of day you will use to plan

Before you create services or launch planning calculations, you need to define the calendar logic that tells the system what kind of day you are working with. At GoalBus, day types are the operational categories that group days as standard jobs, Fridays, weekends or special days, so you don't have to build the planning logic date by date.

Use this quick start when you're preparing your first planning case, when you need to create or validate the type of day your stage will use, or when you want to make sure that the holiday logic is ready before continuing.

Before you start, make sure that:
1. You have access to the environment with permissions to view or edit the calendar settings.
2. You know what planning case you want to build.
3. You know what period you want to prepare, for example January 2026.
4. You've already reviewed your planning role and the overall flow in P1.

For this quick start, use this reference case:

> **I am preparing the calendar basis for a working scenario of January 2026, including the correct behavior of the holidays.**

To create or validate the day type of your case:
1. In GoalBus, go to **Settings** > **Time Management** > **Management of day types**.
ref: P2_Imagen1.png | compact
2. Check existing day types and see if there is already one that represents the operational logic you need.
3. If an appropriate type of day already exists, it confirms that:
   1. His name is clear.
   2. His short name is clear.
   3. It really represents the operating pattern you need.
4. If no proper day type exists, click **Create Day Type**.
ref: P2_Imagen2.png | compact(2x)
5. Define the **name** and **short name** for the new day type.
ref: P2_Imagen3.png | compact(8.5x)
6. Select the days of the week that apply to that type of day.
ref: P2_Imagen4.png | compact(8.5x8)
7. If the type of day should also apply to public holidays, activate the option to apply the type of day to public holidays.
ref: P2_Imagen5.png | compact(8.5x8)
8. Save the day guy.
9. Check the result and confirm that the type of day now clearly represents the case you're preparing.

When you finish this section, you should have a kind of day that the system can use as an operating category for your planning case.

## Recording holidays that alter the normal logic of the calendar

After defining the general day type, you need to tell the system what to do with the exceptional dates. Holidays are important because the calendar can say that a date is Tuesday, while the operation should behave like a Sunday or as another special pattern. If you do not register the holidays well, the system can apply the wrong plan when you later publish or calculate scenarios.

Before starting this section, make sure that:
1. You've created or confirmed the kind of day your case is going to use.
2. You know if the planning period includes holidays or special dates.
3. You're ready to decide which operating pattern each holiday should follow.

To register and validate the holidays of your case:
1. In the same day-type management section, switch to the **Holidays** tab.
ref: P2_Imagen6.png | compact
2. Check if the holiday you need already exists in the system.
3. If the holiday does not exist, create a new holiday record.
4. If the holiday already exists, open it and check its settings.
5. Enter or confirm the **name** of the holiday.
6. Assign the correct **type of day** to that holiday.
ref: P2_Imagen7.png | compact
7. Keep the record of the holiday.
8. Repeat this process for any other holiday that affects the period you are preparing.
9. Check the list of holidays and confirm that each exceptional date points to the correct operating pattern.

For the reference case, ask yourself these questions:
1. Does January 2026 include a holiday that should behave different from a standard workable?
2. Should that holiday behave like Sunday, like Saturday, or as another kind of special day?
3. If you published a scenario for this period, would the system know exactly what pattern to apply on that date?

When you finish this section, the system should be able to replace normal calendar behavior on the holiday dates that matter to you.

## Checking that your calendar base is ready to plan

Now that you have already defined the general day type and holiday exceptions, you need to confirm that the calendar base is really usable. This is the step in which you check that the structure you created can hold the following quick starts without introducing avoidable errors.

Before continuing, make sure that:
1. The type of day exists and has the correct weekly logic.
2. The relevant holidays are registered.
3. Each holiday is linked to the right type of day.
4. Your planning case remains clear and concrete.

To validate your calendar base before moving on to the next quick start:
1. Review the planning case you defined at the beginning of this article.
2. Confirm that the kind of day you created or validated matches that case.
3. Confirm that any holiday within the planning period has been registered and associated with the correct day type.
4. Check if the holiday app option you activated in the day type really reflects the behavior you want.
5. Ask yourself if the system could already distinguish:
   1. normal days of the period; and
   2. the exceptional dates to be followed by another operating pattern.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, go back and correct the type of day or the holiday association before continuing.

At the end of this section, you should be able to state that your planning case has a reliable calendar basis and that the following quick starts can rely on it without inheriting a temporary logic error.

## Additional readings

- [Validating the operating year before planning](P3_Validating_The_Operating_Year_Before_Planning.md)
