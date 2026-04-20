---
title: Managing transfers, loans, and assignment changes
shortTitle: Loans and changes
intro: 'Learn how to manage drivers’ operational context changes, distinguishing between transfer, temporary loan, and assignment change so Rostering uses each person in the right scope without losing traceability.'
contentType: how-tos
versions:
  - '*'
---

## Understanding the difference between transfer, loan, and assignment change

Before calculating Rostering, you need to correctly distinguish staff movement between operational contexts. Not all situations mean the same thing. A driver can still belong to their primary depot but temporarily work elsewhere. They can also change assignment more permanently. If you mix these concepts, staff eligibility becomes confusing and calculation can assign work in the wrong context.

Use this quick start when drivers are loaded, primary assignment is reviewed, and absences/inactivity are modeled, and you need to reflect real movements between depots, groups, or units.

Before you begin, make sure that:
1. You loaded and reviewed drivers in P20.
2. You validated operational assignment in P21.
3. You configured Rostering rules in P22.
4. You registered absences, inactivity, and availability in P23.
5. You know who will change context and for what period.

For this quick start, use this reference case:

> **I’m going to register that one driver who normally belongs to North Depot will temporarily work in another context, and another driver will change assignment more permanently before Rostering calculation.**

To distinguish each movement correctly:
1. Use a **loan** when the person still belongs to their primary context but will work temporarily in another.
2. Use a **transfer** when the person changes context in a more structural or permanent way.
3. Use an **assignment change** when you need to formally update the primary depot/group/unit the system should treat the driver under.
4. Do not use an absence to model an operational context change.
5. Do not use a loan to correct a misconfigured primary assignment.

Keep these questions as a guide:
1. Where does this person normally belong?
2. Where will they actually work during this period?
3. Is the movement temporary or structural?

When you finish this section, you should know which type of record applies to each context change.

## Registering a temporary loan

A loan reflects that a driver will work temporarily outside their usual context without losing their primary assignment. This is useful when someone still belongs to their main depot/unit/group but will operate for a while in another environment.

Before you start this section, make sure that:
1. You identified the person who will be loaned.
2. You know their primary context.
3. You know the destination context and the effective dates.

To register a temporary loan:
1. Open the driver profile from the general list.
2. Go to the **movements**, **temporary assignment**, or **loans** section (depending on the view).
3. Create a new loan record.
4. Define:
   1. **origin context**,
   2. **destination context**,
   3. **start date**,
   4. **end date**,
   5. and any needed notes.
5. Save the record.
6. Confirm the driver keeps their primary assignment.
7. Confirm that during the loan period, the system can treat the driver under the correct temporary context.

For the reference case, a valid loan is:
1. driver assigned to North Depot,
2. loaned for two weeks to South Depot,
3. without changing their primary historical assignment.

When you finish this section, you should have a correctly modeled temporary loan without losing structural traceability.

## Registering a transfer or more stable change

Unlike a loan, a transfer is a structural movement. This is not only about temporarily working elsewhere, but about changing the driver’s operational belonging in a more durable way.

Before you start this section, make sure that:
1. You identified the person who will change context more durably.
2. You know which depot/unit/group will become the new primary context.
3. This is not a temporary or exceptional need.

To register a transfer / structural change:
1. Open the driver profile.
2. Review the current primary assignment.
3. Create the transfer movement or update primary assignment, depending on your environment flow.
4. Define:
   1. the new **primary depot**,
   2. the new **business unit**,
   3. the new **work group**, if it changes,
   4. and the effective date.
5. Save changes.
6. Confirm the profile now reflects the new primary context.
7. Confirm the change did not leave contradictions between primary assignment and qualifications.

For the reference case, a valid transfer is:
1. a driver who stops belonging to North Depot,
2. moves to belong to South Depot on a stable basis,
3. and from that date should be treated as a resource of the new base.

When you finish this section, you should have correctly modeled a structural context change.

## Reviewing the impact on qualifications and eligibility

After registering loans or transfers, review operational impact. Moving a person between contexts is useless if qualifications/eligibility do not follow. Confirm the driver not only changed context in the profile, but can be used correctly in that new environment.

Before you continue, make sure that:
1. You registered at least one loan or transfer.
2. You know in which operational context the person should be seen now.
3. You understand a context change may require reviewing active qualifications.

To review operational impact:
1. Return to the driver’s **Qualifications / Certifications** tab.
2. Confirm there are valid qualifications for the destination context.
3. If missing, add them with correct dates before calculation.
4. Confirm the person is not simultaneously visible in incompatible contexts due to a configuration error.
5. Confirm the system can treat the person as eligible in the correct scope during the relevant period.
6. If you detect contradictions, fix them before running Rostering calculation.

For the reference case, make sure that:
1. the loaned driver can legally/technically work in the destination context,
2. the transferred driver has qualifications aligned with the new context,
3. eligibility matches the recorded movement.

When you finish this section, you should have staff movements that are operationally usable.

## Confirming context changes are ready for Rostering calculation

The last step is confirming the combination of primary assignment, loans/transfers, and qualifications is clear enough to feed calculation. Avoid two errors:
1. assigning someone in a context where they should not appear,
2. excluding someone who should be eligible due to a recorded change.

Before you finish, make sure that:
1. You registered required temporary or structural movements.
2. You reviewed the impact on eligibility.
3. You know which population will participate in the next calculation.

To confirm this layer is ready:
1. Return to the general driver list.
2. Review several profiles affected by context changes.
3. Confirm that:
   1. loans appear as temporary,
   2. transfers appear as structural changes,
   3. and primary assignment remains coherent where applicable.
4. Ask yourself whether the system could:
   1. use the right driver in the right context,
   2. during the right period,
   3. without confusing structural belonging with temporary displacement.
5. If yes, continue with the next quick start.
6. If no, fix movements or qualifications before proceeding.

For the reference case, do not proceed until you can state:
1. L1 driver context changes are correctly recorded.
2. You know who is loaned, who is transferred, and who keeps primary assignment.
3. The baseline is ready to run the first Rostering calculation.

When you finish this section, you should have staff organizational context clear enough to move into assignment calculation.

## Additional reading

- [Running the first Rostering calculation](P25_Running_the_first_rostering_calculation.md)

