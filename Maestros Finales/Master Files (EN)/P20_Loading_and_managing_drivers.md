---
title: Loading and managing drivers
shortTitle: Drivers
intro: 'Learn how to create, import, and maintain the driver baseline in GoalBus, review the operational profile, and leave a reliable roster foundation before moving on to assignment, rules, and Rostering calculation.'
contentType: how-tos
versions:
  - '*'
---

## Creating or importing the driver roster baseline

Before talking about Rostering rules, absences, or duty assignment, you need a reliable driver baseline. In GoalBus, driver management acts as the primary source of truth for human operations: it supports manual creation and bulk upload, and centralizes identity, depot affiliation, and availability in a single directory.

Use this quick start when the transition from Scheduling to Rostering is clear and you need to prepare the real group of people who will participate in assignment.

Before you begin, make sure that:
1. You already closed the transition from Scheduling in P19.
2. You know which driver population will participate in calculation.
3. You know whether you will create a few drivers manually or need bulk import.
4. You have access with permissions to manage staff.

For this quick start, use this reference case:

> **I’m going to load and review the driver roster baseline that can cover the L1 solution before moving into assignment, rules, and availability.**

To create or import the driver baseline:
1. In GoalBus, go to **Configuration** > **Staff** > **Driver management**.
ref: P20_Imagen1.png | compact
2. Check whether the drivers for your case already exist in the list.
3. If you need to create a few drivers, click **New Driver**.
ref: P20_Imagen2.png | compact
4. If you need to load many drivers, run a bulk CSV import via **Staff upload**.
ref: P20_Imagen3.png | compact
5. If you choose bulk import, prepare the file with the minimum data your operation needs to correctly identify each person. The import window provides guidance to prepare the CSV.
ref: P20_Imagen4.png
6. Run the upload and review the result.
7. Return to the general list and confirm drivers appear correctly.
8. If you detect duplicates or incomplete records, fix them before proceeding.

For the reference case, finish this section only when you can state:
1. L1 drivers are created or imported.
2. The general list reflects a single baseline roster.
3. You can open each driver profile to review operational context.

When you finish this section, you should have a driver baseline loaded and visible in the system.

## Reviewing the driver profile and structural data

Once the baseline exists, review the **driver profile**. The profile is not only a contact card—it is the employee’s complete digital record inside operations. It contains static data, operational context, and attributes the system will later use to reason about eligibility.

Before you start this section, make sure that:
1. Drivers are visible in the general list.
2. You know which driver (or group) you will use as a sample.
3. You want to validate the record is operational, not only administrative.

To review the driver profile:
1. In the general list, click a driver’s name.
ref: P20_Imagen5.png | full
2. Review the side panel with static data.
3. Check at least these information groups:
   1. basic data such as name and code,
   2. operational data such as labor agreement or contract type,
   3. operational links such as primary depot, work group, area, or authorized vehicle types.
4. If a key structural datum is missing, complete it before proceeding.
5. Save any necessary changes.
6. Repeat across several drivers to confirm the baseline is consistent.

For the reference case, review at least:
1. Driver code.
2. Primary depot.
3. Work group.
4. The operational properties that will condition later assignment.

When you finish this section, you should be confident each driver has a coherent, usable operational record.

## Reviewing the driver’s operational context and dynamic data

Beyond structural data, the driver profile can include dynamic data that directly affects how the system reasons about the person. In the administration tab you may review counters and work patterns that will be used later by assignment logic.

Before you start this section, make sure that:
1. You already reviewed profile static data.
2. You know whether your operation uses counters or cyclical patterns.
3. You want to confirm the driver has interpretable operational context.

To review dynamic operational context:
1. Inside the driver profile, open **Administration details**.
2. Review driver **counters** or KPIs if they exist.
3. Check whether the driver is linked to any **work pattern**.
4. If your operation uses cyclical patterns, review the driver’s current offset/position in the pattern.
5. Confirm the data makes sense for the real context.
6. If dynamic information is not correct, adjust it before moving to rules or calculation.

For the reference case, ask yourself:
1. Does this driver have the pattern they should have?
2. Are counters/KPIs available if the process needs them?
3. Could the system reason correctly about this person during assignment?

When you finish this section, you should have validated not only driver identity, but also their dynamic operational context.

## Validating qualifications before using a driver in Rostering

Before treating a driver as eligible, review **qualifications/authorizations**. These answer: “Can this person legally or technically work in this depot, group, or unit?” They are managed on a timeline with start and end dates, and the system shows statuses such as active, future, expired, or expiring soon. If a person is not qualified for the required context, the engine will throw an error when trying to assign them.

Before you start this section, make sure that:
1. You already reviewed the driver profile.
2. You know which depot, group, or unit is needed for your case.
3. You understand a qualification is not the same as a temporary loan or assignment.

To review and validate qualifications:
1. Inside the driver profile, open **Qualifications / Certifications**.
2. Review whether there are valid records for:
   1. depots,
   2. work groups,
   3. business units.
3. Check each qualification’s visual status:
   1. active,
   2. future,
   3. expiring soon,
   4. expired.
4. If a needed qualification is missing, add it with correct dates.
5. If a qualification expired and should not be used, keep it as history—do not try to rewrite the past.
6. Save changes.
7. Confirm the driver is qualified for the context where you expect to use them.

For the reference case, do not proceed until you can state:
1. The driver is qualified for the correct depot.
2. The required work group is covered.
3. There are no expirations that break current eligibility.

When you finish this section, you should have drivers that not only exist in the roster, but are also operationally and legally eligible.

## Confirming the baseline is ready for the next Rostering layer

The last step is confirming the driver baseline is ready to move into operational assignment, rules, absences, and calculation. The goal is not just to have names loaded, but a coherent, traceable baseline the engine can use.

Before you finish, make sure that:
1. You loaded or imported the baseline.
2. You reviewed key profiles.
3. You checked structural and dynamic data.
4. You validated essential qualifications.

To confirm the baseline is ready:
1. Return to the general driver list.
2. Confirm the required population for your case is present.
3. Confirm critical profiles have no major information gaps.
4. Confirm the people you expect to use are qualified for the correct context.
5. Ask yourself whether the system could already use this baseline to:
   1. manage operational assignment,
   2. apply Rostering rules,
   3. and handle real availability.
6. If yes, continue with the next quick start.
7. If not, fix the driver baseline before proceeding.

For the reference case, finish this quick start only when you can state:
1. L1’s driver baseline is loaded.
2. Key profiles have been reviewed.
3. Essential qualifications are valid.
4. The baseline is ready to move into operational assignment.

When you finish this section, you should have a driver baseline solid enough to continue with the next Rostering layer.

## Additional reading

- [Managing the driver’s operational assignment](P21_Managing_driver_operational_assignment.md)

