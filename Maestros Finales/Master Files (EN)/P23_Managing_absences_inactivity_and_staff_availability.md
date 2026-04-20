---
title: Managing absences, inactivity, and staff availability
shortTitle: Staff availability
intro: 'Learn how to register absences, inactivity, and availability restrictions so Rostering assigns only truly eligible people and does not try to cover work with unavailable drivers.'
contentType: how-tos
versions:
  - '*'
---

## Understanding the difference between absence, inactivity, and availability

Before calculating Rostering, you need to control who is actually available to work. At this layer it is not enough that the driver exists, is assigned to the correct context, and has applicable rules. You also need to tell the system whether that person:
1. is available,
2. is absent,
3. is inactive,
4. or has partial/restricted availability.

Use this quick start when drivers are loaded, operational assignment is reviewed, and Rostering rules are prepared, and you need to prevent calculation from assigning work to ineligible people.

Before you begin, make sure that:
1. You loaded and reviewed drivers in P20.
2. You validated their operational assignment in P21.
3. You defined the Rostering rules baseline in P22.
4. You know which staff population will participate in calculation.
5. You know whether you must register vacations, sick leave, permissions, partial unavailability, or non-operational states.

For this quick start, use this reference case:

> **I’m going to register absences, inactivity, and availability restrictions for the drivers who will cover line L1 so Rostering assigns work only to truly eligible people.**

To interpret these concepts correctly:
1. Use an **absence** when the person belongs to the population but is unavailable during a specific period.
2. Use **inactivity** when the person must be excluded from operations (or calculation) in a more structural way or for a broader period.
3. Use an **availability restriction** when the person can work, but not at all times or not under all conditions.
4. Do not mix these concepts as if they were the same.
5. Use this reading rule:
   1. **absence** = cannot work during a specific period,
   2. **inactivity** = should not be treated as an operational resource in that context/period,
   3. **restricted availability** = can work, but with limits.

To define absence/inactivity/unavailability types:
1. In GoalBus, open **Configuration** > **Staff** > **Absence configuration**.
ref: P23_Imagen1.png | compact
2. Check whether all absence types you need are already created.
3. If you need to create a new type, click **Create new absence**.
ref: P23_Imagen2.png | compact
4. Fill at least these fields:
   1. **Absence name**
   2. **Short name**
   3. **GoalDriver ID** (if integrations are used)
   4. **Absence category** (e.g., Pure / Free / Work) and its relevant duration rules
   5. **Eligibility to assign work** (whether the driver can still be selected despite the absence)
   6. Whether this type is **Requestable by the driver**
5. Save the new absence type.
ref: P23_Imagen3.png | compact
6. Continue until you have all required absence types.
7. Confirm your planning has the full set of absence types it needs.

When you finish this section, you should know which absence types you can use in Rostering planning and assign to different drivers.

## Registering planned driver absences

Planned absences are one of the first elements to load before Rostering calculation. This includes vacations, permissions, sick leave, licenses, or any other period when a person should not receive work.

Before you start this section, make sure that:
1. You know which drivers will have absences within the calculation horizon.
2. You know the exact or approximate dates of those absences.
3. You want to remove ambiguity about which days the person cannot be used.
4. You already created the needed absence types.

To register absences:
1. In GoalBus, open **Configuration** > **Staff** > **Driver management**.
ref: P23_Imagen4.png | compact
2. Click the top bar button to load absence data.
ref: P23_Imagen5.png | compact
3. Select **Upload staff absences**.
ref: P23_Imagen6.png | compact
4. Upload the absences file in the modal. You can review the file format via instructions or by downloading an example template.
ref: P23_Imagen7.png | full
5. Confirm the upload.
6. Save the record.
7. Review loaded absences in each driver profile.

For the reference case, a minimal logic could be:
1. Driver A: vacation from 10 to 20
2. Driver B: permission on day 14
3. Driver C: sick leave for one specific week

When you finish this section, you should have the main absences registered that affect Rostering calculation.

## Checking Rostering correctly sees real eligibility

The last step is validating that the combination of drivers, operational assignment, rules, and availability reflects calculation reality. The goal is to ensure Rostering will not try to assign work to absent/inactive/mis-restricted people, and will not exclude people who should be eligible.

Before you finish, make sure that:
1. You registered relevant absences.
2. You configured partial availability restrictions if needed.
3. You know which population the next calculation will use.

To verify real availability is modeled correctly:
1. Return to the general driver list.
2. Review several representative profiles from the population.
3. Confirm absent people have their periods correctly registered.
4. Confirm partial restrictions are not mistakenly modeled as full absences.
5. Ask yourself whether the system could:
   1. exclude who should not work,
   2. include who can work,
   3. and respect partial restrictions without breaking calculation.
6. If yes, continue with the next quick start.
7. If no, correct records before proceeding.

For the reference case, do not proceed until you can state:
1. L1 drivers have their real availability correctly reflected.
2. Absences are loaded.
3. Inactivity is differentiated.
4. Partial restrictions were not confused with full absences.

When you finish this section, you should have an availability baseline reliable enough to move into loans/transfers and assignment changes.

## Additional reading

- [Managing transfers, loans, and assignment changes](P24_Managing_transfers_loans_and_assignment_changes.md)

