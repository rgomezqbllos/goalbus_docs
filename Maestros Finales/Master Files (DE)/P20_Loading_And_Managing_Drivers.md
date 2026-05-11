---
title: Loading and managing drivers
shortTitle: Drivers
intro: Learn how to create, import, and maintain the driver base in GoalBus, review
  your operating profile, and leave a reliable template before moving to Rostering
  secondment, rules, and calculation.
contentType: how-tos
versions:
- '*'
---
## Creating or importing driver template

Before talking about Rostering rules, absences or shift assignment, you need to have a reliable driver base. In GoalBus, driver management acts as the main source of truth for human operativity: it allows combining manual creation and mass loading, and concentrates identity, deposit affiliation and availability in the same directory. fileciteturn38file2L1-L24

Use this quick start when you are clear about the transition from Scheduling to Rostering and need to prepare the real group of people who will participate in the assignment.

Before you start, make sure that:
1. You've already closed the transition from Scheduling at P19.
2. It is clear to you which collective of drivers will participate in the calculation.
3. You know if you're gonna discharge a few drivers manually or if you need a massive load.
4. You have access to the environment with permissions to manage staff.

For this quick start, use this reference case:

> **I will load and review the driver template that can cover the L1 solution before going into secondment, rules and availability.**

To create or import the driver template:
1. In GoalBus, go to the **Settings** module > **Staff** > **Driver management**.
ref: P20_Imagen1.png | compact
2. Check if the case drivers already exist on the general list.
3. If you need to create few drivers, click **New Driver**.
ref: P20_Imagen2.png | compact(2x)
4. If you need to load many drivers, do a massive import using CSV file from **Personal Burden**.
ref: P20_Imagen3.png | compact
5. If you choose mass import, prepare the file with the minimum data your operation needs to correctly identify each person. The import window will help to prepare the load CSV.
ref: P20_Imagen4.png
6. Run the load and check the result.
7. Go back to the general list and check that drivers appear correctly.
8. If you detect duplicates or incomplete records, correct them before continuing.

For the reference case, finish this section only when you can state:
1. L1 drivers are already discharged or imported.
2. The general list reflects a single reference template.
3. You can now open the profile of each driver to review its operating context.

When you finish this section, you should have a driver template loaded and visible in the system. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Checking the driver profile and structural data

Once the template is created, you need to review the **driver profile**. The profile is not just a contact sheet: it is the employee's complete digital file within the operation. There they coexist static data, operating context and attributes that the system will later use to reason about its eligibility. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Before starting this section, make sure that:
1. You already have visible drivers on the general list.
2. You know which driver or group you'll use as a sample.
3. You want to validate that the record is not just administrative, but operational.

To check the driver profile:
1. In the general list, click on the name of a driver.
ref: P20_Imagen5.png | full
2. Check the static data sidebar.
3. Check at least these information groups:
   1. basic data, such as name and code,
   2. operational data, such as collective agreement or type of contract,
   3. operational links, such as main warehouse, working group, area or types of approved vehicles.
4. If any key structural data is missing, fill it out before proceeding.
5. Save any necessary change.
6. Repeat the review on multiple drivers to confirm consistency in the template.

For the reference case, check at least:
1. The driver's code.
2. Your main warehouse.
3. Your task force.
4. The operational properties that will condition your subsequent assignment.

When you finish this section, you should be clear that each driver has a consistent and usable operating file. fileciteturn38file0L8-L20

## Reviewing the operating context and dynamic driver data

In addition to structural data, the driver profile includes dynamic data that directly affect how the system reasons about the person. In the administration tab you can review counters and work patterns, which are part of the operating context used later by the mapping logic. fileciteturn38file0L12-L17

Before starting this section, make sure that:
1. You've already checked the static data on the profile.
2. You know if your operation uses counters or cyclic patterns.
3. You want to check that the driver not only exists, but has an interpretable operating context.

To review the dynamic operating context:
1. Inside the driver profile, open the **Administration details** tab.
2. Check the **counters** or KPI associated with the driver if they exist.
3. Check if the driver is linked to any **work pattern**.
4. If your operation uses cyclic patterns, also check the current driver's lag or position within the pattern.
5. Confirms that this data makes sense for the real context.
6. If dynamic information is not correct, adjust it before moving to rules or calculation.

For the reference case, ask yourself:
1. Does this driver have the pattern he should have?
2. Are your counters or KPIs available if the process needs them?
3. Could the system properly reason about this person in an assignment calculation?

When you finish this section, you should have validated not only the identity of the driver, but also his dynamic operating context. fileciteturn38file0L12-L17

## Validating ratings before using the driver in Rostering

Before considering a driver as eligible, you need to review your **ratings**. These ratings answer the question “Can this person work legally or technically on this deposit, group or unit?” They are managed in a time line with start and end date, and the system shows states as active, future, expired or close to expire to facilitate reading. If a person is not enabled for the required context, the engine generates an error when trying to assign it. fileciteturn38file0L17-L34

Before starting this section, make sure that:
1. You've already checked the driver's profile.
2. You know what deposit, group or unit you'll need for your case.
3. You understand that an empowerment is not the same as a temporary assignment or secondment.

To review and validate the ratings:
1. Within the driver profile, open the **Enabling/qualifying** tab.
2. Check for existing records for:
   1. deposits,
   2. working groups,
   3. Business units.
3. Check the visual status of each rating:
   1. active,
   2. future,
   3. next to expire,
   4. expired.
4. If a necessary rating is missing, add it with its correct dates.
5. If an habilitation has expired and should not be used, leave it as historical without attempting to rewrite the past.
6. Save the changes.
7. Confirm that the driver is already enabled for the context where you expect to use it.

For the reference case, do not continue until you can state:
1. The driver is enabled for the correct deposit.
2. The required working group is covered.
3. There are no expirations that break the current eligibility.

When you finish this section, you should have drivers who not only exist in the template, but are also eligible from an operational and regulatory point of view. fileciteturn38file0L17-L34

## Confirming that the template is already ready for the next layer of Rostering

The last step is to check that the driver base is ready to enter the following layer: operational secondment, rules, absences and calculation. Here the goal is not only to have names loaded, but a coherent, traceable and usable template by the engine.

Before you finish, make sure that:
1. You've already loaded or imported the template.
2. You've already checked the main profiles.
3. You've already checked structural and dynamic data.
4. You've already validated essential ratings.

To confirm that the template is already ready:
1. Go back to the general list of drivers.
2. Check that the collective needed for your case is present.
3. Check that critical profiles have no important information gaps.
4. Make sure that the people you expect to use are enabled for the right context.
5. Ask yourself if the system could already use this base as a starting point for:
   1. operational secondment,
   2. Rostering rules,
   3. and actual availability.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, correct the driver base before continuing.

For the reference case, finish this quick start only when you can say:
1. The L1 driver template is already loaded.
2. Key profiles have already been reviewed.
3. Essential ratings are already in place.
4. The base is now ready for operational secondment.

When you finish this section, you should have a strong enough driver template to continue with the next layer of Rostering.

## Additional readings

- [Managing the operational secondment of the driver](P21_Managing_The_Operational_Secondment_Of_The_Driver.md)
