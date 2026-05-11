---
title: Managing transfers, assignments and secondment changes
shortTitle: Assignments and changes
intro: Learn how to manage changes in the operating context of drivers, distinguishing
  between transfer, assignment and change of secondment so that Rostering uses each
  person in the right area without losing traceability.
contentType: how-tos
versions:
- '*'
---
## Understanding the difference between transfer, assignment and change of secondment

Before calculating Rostering, you need to correctly distinguish staff movements between operational contexts. Not all situations mean the same thing. A driver may still belong to his main deposit, but work temporarily on another. He may also change secondment more stablely. If you mix these concepts, staff eligibility becomes confusing and calculation can assign work in the wrong context.

Use this quick start when you already have the drivers loaded, review their main secondment and model their absences and inactivitys, and you need to reflect real movements between tanks, groups or units.

Before you start, make sure that:
1. You already loaded and checked drivers on P20.
2. You've already validated the operational secondment to P21.
3. You've already set Rostering rules to P22.
4. You have already registered absences, inactivity and availability at P23.
5. You know what people will change context and during what period.

For this quick start, use this reference case:

> **I'm going to record that one of the drivers that normally belongs to the North Deposit will temporarily work in another context, and that another driver will change secondment more stablely before the Rostering calculation.**

To correctly distinguish each movement:
1. He uses an **assignment** when the person still belongs to his main context, but will temporarily work on another.
2. Use an **transfer** when the person changes context more structurally or permanently.
3. Use an **change of secondment** when you need to formally update the tank, group, or base unit from which the system should treat the driver.
4. Do not use an absence to model an operating context change.
5. Do not use an assignment to correct a misconfigured main secondment.

Keep these questions as a guide:
1. Where does this person normally belong?
2. Where will you really work during this period?
3. Is that movement temporary or structural?

When you finish this section, you should be clear what type of record corresponds to each context change.

## Recording a temporary transfer of the driver

The cession serves to reflect that a driver will temporarily work out of his usual context without losing his base secondment. This is useful when a person continues to belong to his deposit, unit or main group, but will operate for some time in another environment.

Before starting this section, make sure that:
1. You've already identified the person who will be transferred.
2. You know what their main context is.
3. You already know the temporary destination context and application dates.

To register a temporary assignment:
1. Open the driver's profile on the general list.
2. Go to the **movements**, **temporary secondment** or **assignments** section, depending on the view available.
3. Creates a new assignment record.
4. Define:
   1. the **origin context**,
   2. the **destination context**,
   3. the **start date**,
   4. the **End date**,
   5. and any necessary observations.
5. Keep the record.
6. Check that the driver still retains his main secondment.
7. It finds that during the period of assignment the system can deal with it in the correct time frame.

For the reference case, a valid assignment would be:
1. driver attached to the North Depot,
2. ceded for two weeks to the South Deposit,
3. without changing its historical main secondment.

When you finish this section, you should have a temporary assignment correctly modeled without losing structural traceability.

## Recording a more stable transfer or change

Unlike the cession, a transfer responds to a more structural movement. Here it is no longer just a question of working temporarily in another context, but of moving more stablely the operational belonging of the driver.

Before starting this section, make sure that:
1. You've already identified the person who will change context in a more lasting way.
2. You know what deposit, unit or group will become its new main context.
3. You are no longer talking about a temporary or exceptional need.

To record a transfer or structural change:
1. Open the driver's profile.
2. Review your current main secondment.
3. Create the transfer movement or update the main secondment, depending on the flow your environment uses.
4. Define:
   1. the new **main deposit**,
   2. the new **business unit**,
   3. the new **working group**, if changed,
   4. and the date of effectiveness.
5. Save the changes.
6. Check that the profile already reflects the new main context.
7. Checks that the change has not left contradictory data between main secondment and ratings.

For the reference case, a valid transfer would be:
1. driver who ceases to belong to the North Depot,
2. becomes a stable member of the South Deposit,
3. and from that date it should be treated as an appeal against that new basis.

When you finish this section, you should have correctly modeled a structural context change.

## Reviewing the impact of movement on ratings and eligibility

After registering assignments or transfers, you need to review their operational impact. Moving a person between contexts is useless if their ratings or eligibility does not accompany the change. Here you must confirm that the driver not only changed context in the profile, but can also be used correctly in that new environment.

Before continuing, make sure that:
1. You've already registered at least one transfer or transfer.
2. You know in what operational context the person should be seen from now on.
3. You understand that a context change may require reviewing current ratings.

To review the operational impact of the movement:
1. Go back to the driver's **ratings/qualifications** tab.
2. Checks for current ratings for the target context.
3. If missing, add them with correct dates before calculation.
4. Checks that the person is not simultaneously visible in incompatible contexts due to a configuration error.
5. Checks that the system may consider the eligible person in the correct area during the relevant period.
6. If you detect contradictions, correct them before going to Rostering's calculation.

For the reference case, make sure that:
1. the transferred driver may work legally or technically in the destination context,
2. the transferred driver already has his ratings according to the new context,
3. eligibility coincides with the registered movement.

When you finish this section, you should have personnel movements that are also operationally usable.

## Confirming that context changes are already ready for the Rostering calculation

The last step is to check that the combination between main secondment, assignments, transfers and ratings is already clear enough to feed the calculation. Here the goal is to avoid two errors:
1. assign a person in a context where it should not appear,
2. or leave out a person who should be eligible for a change already registered.

Before you finish, make sure that:
1. You've already recorded the necessary temporal or structural movements.
2. You've already reviewed their impact on eligibility.
3. You know which collective will participate in the following calculation.

To confirm that this layer is already ready:
1. Go back to the general list of drivers.
2. Review various profiles affected by context changes.
3. Checks that:
   1. the assignments are seen as temporary,
   2. transfers are reflected as structural changes,
   3. and the main secondment remains consistent where appropriate.
4. Ask yourself if the system could already:
   1. use the correct driver in the correct context,
   2. during the correct period,
   3. without confusing structural belonging with temporary displacement.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct movements or ratings before continuing.

For the reference case, do not continue until you can state:
1. The context changes of L1 drivers are already recorded correctly.
2. You know who's ceded, who was transferred, and who keeps their original secondment.
3. The base is already ready to execute the first Rostering calculation.

When you finish this section, you should have the staff organizational context clear enough to move on to assignment calculation.

## Additional readings

- [Running the first Rostering calculus](P25_Running_The_First_Rostering_Calculus.md)
