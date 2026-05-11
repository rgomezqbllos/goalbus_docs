---
title: Managing absences, inactivity and staff availability
shortTitle: Personal availability
intro: Learn how to register absences, inactivity and availability restrictions so
  that Rostering assigns only to really eligible people and does not attempt to cover
  work with unavailable drivers.
contentType: how-tos
versions:
- '*'
---
## Understanding the difference between absence, inactivity and availability

Before calculating Rostering, you need to control which people are really available to work. In this layer it is no longer enough for the driver to exist, be attached to the correct context and have applicable rules. You also need to tell the system if that person:
1. is available,
2. is absent,
3. It's inactive,
4. or has a partial or restricted availability.

Use this quick start when you already have the drivers loaded, review their operational secondment and prepare the Rostering rule base, and you need to prevent the calculation from trying to assign work to ineligible people.

Before you start, make sure that:
1. You already loaded and checked drivers on P20.
2. You've already validated his operational secondment to P21.
3. You've already defined Rostering's rule base in P22.
4. It is clear to you which staff group will participate in the calculation.
5. You know if in your operation you need to register vacations, casualties, permits, partial unavailabilitys or non-operational states.

For this quick start, use this reference case:

> **I'm going to record absences, inactivity and availability restrictions on drivers who will cover line L1 to make sure that Rostering only assigns work to really eligible people.**

To understand these concepts correctly:
1. Use an **absence** when the person exists and belongs to the collective, but is not available for a specific period.
2. Use an **inactivity** when the person must be left out of operation for a more structural period or must not participate in the calculation.
3. Use an **restriction of availability** when the person can work, but not at all times or not under all conditions.
4. Don't mix these concepts as if they were the same.
5. Use this reading rule:
   1. **absence** = cannot work for a specific period,
   2. **inactivity** = should not be treated as an operating resource in that context or period,
   3. **restricted availability** = can work, but with limits.

To record the types of absences, inactivitys or unavailabilitys:
1. In GoalBus, you must open **Settings** > **Staff** > **Absentance Settings**.
ref: P23_Imagen1.png | compact
2. Check if all types of absence you need are created.
3. If there is no absence or you need to create a new one, click the **Create New Absence** button.
ref: P23_Imagen2.png | compact(2x)
4. To create a new type of absence the following fields must be filled in:
   1. **Name of Absence**: name of the absence type to be created.
   2. **Short name**: for compact views.
   3. **GoalDriver ID**: internal code if you work with integrations.
   4. **Absence category**: It can be **Pure**, **Free** or **Work**. Depending on what you choose, a duration (**Time** or **Full day**), a duration of **Working time** or **Maximum days** should be assigned.
   5. **Eligibility to Assign Work**: Whether you can choose the driver to assign you work or not, despite your absence.
   6. Select if this type of absence will be **Requestable by the driver**.
5. Save the new kind of absence.
ref: P23_Imagen3.png | compact(x10)
6. It continues to record all the necessary types of absence.
7. Confirm that you have all the types of absence needed for your planning.

When you finish this section, you should have a clear view of what type of absences you will be able to use in your roasting planning and that you will be able to assign to different drivers. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

## Recording planned driver absences

Planned absences are one of the first items to load before the Rostering calculation. Here comes vacations, permits, disabilities, licenses or any other period in which a person should not receive a job.

Before starting this section, make sure that:
1. You know which drivers will have absences within the calculation horizon.
2. You know the exact or approximate dates of those absences.
3. You want to leave the system unambiguous about what days a person cannot be used.
4. You've already created all the necessary types of absence.

To record absences from the driver profile:
1. In GoalBus, you must open **Settings** > **Staff** > **Driver management**.
ref: P23_Imagen4.png | compact
2. Click the button on the top bar to load the absences data.
ref: P23_Imagen5.png | compact(3x)
3. Select the **Charge staff absences** action.
ref: P23_Imagen6.png | compact
4. Load the staff absences file in the pop-up window. In that window you can review the format of the absences file, either by reading the instructions or downloading an example template.
ref: P23_Imagen7.png | full
5. Confirms the file load.
6. Keep the record.
7. Now you can check the loaded absences in the profile of each driver.

For the reference case, a minimum logic could be:
1. Driver A: vacation from 10 to 20
2. Driver B: permit on the 14th
3. Driver C: Incapacity for a specific week

When you finish this section, you should have recorded the main absences that affect the Rostering calculation.

## Checking that Rostering already sees the actual eligibility correctly

The last step is to validate that the combination between drivers, secondment, rules and availability already reflects the reality of the calculation. Here the goal is to ensure that Rostering will not attempt to assign work to absent, inactive or ill-restricted people, nor will it leave out people who should be eligible.

Before you finish, make sure that:
1. You've already registered relevant absences.
2. You've already configured partial availabilitys if necessary.
3. You know which collective will use the following calculation.

To check that the actual availability is already well modeled:
1. Go back to the general list of drivers.
2. Review several representative profiles of the collective.
3. Confirms that absentees have their periods correctly registered.
4. Confirms that partial restrictions are not modeled as total absences by mistake.
5. Ask yourself if the system could already:
   1. exclude those who should not work,
   2. including those who can work,
   3. and respect partial restrictions without breaking the calculation.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, correct the records before continuing.

For the reference case, do not continue until you can state:
1. L1 drivers already have their real availability well reflected.
2. The absences are loaded.
3. Inactivity is differentiated.
4. Partial restrictions were not confused with complete absences.

When you finish this section, you should have a sufficiently reliable availability base to move to assignments, transfers, and secondment changes.

## Additional readings

- [Managing transfers, assignments and secondment changes](P24_Managing_Transfers_Assignments_And_Secondment_Changes.md)
