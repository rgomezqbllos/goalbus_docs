---
title: Managing the driver’s operational assignment
shortTitle: Operational assignment
intro: 'Learn how to link each driver to their depot, business unit, and work group, and understand how this assignment conditions real eligibility before moving on to rules, absences, and Rostering calculation.'
contentType: how-tos
versions:
  - '*'
---

## Understanding a driver’s operational assignment

Before defining advanced rules, absences, or Rostering calculations, you need to understand how each driver is **assigned** within the organization. In GoalBus, operational assignment is not a single field. It is built by combining three main coordinates:
1. **Depot**
2. **Business unit**
3. **Work group**

This combination defines where the person works from, which division they belong to, and what type of duties they can receive. It also affects resource visibility for planners and managers.

Use this quick start when your driver baseline is loaded and you need to ensure each person is placed in the correct operational context before moving on to rules and availability.

Before you begin, make sure that:
1. You loaded and reviewed drivers in P20.
2. You know which depots, units, and groups your operation uses.
3. You know which staff population will participate in Rostering calculation.
4. You understand a wrong assignment can make a person ineligible even if they exist in the system.

For this quick start, use this reference case:

> **I’m going to review that the drivers who will cover line L1 are assigned to the correct depot, business unit, and work group before configuring rules and availability.**

To understand operational assignment:
1. Treat **depot** as the resource’s base physical location.
2. Treat **business unit** as the strategic/modal division the person belongs to.
3. Treat **work group** as the function that determines what type of duties they can receive.
4. Use this reading rule:
   1. depot answers **where they work**,
   2. unit answers **which business/mode they operate in**,
   3. group answers **what work they can do**.
5. Do not mix these three concepts as if they were the same.

When you finish this section, you should understand operational assignment is a composed structure, not a single isolated attribute.

## Reviewing depot, business unit, and work group in the driver profile

Once the logic is clear, confirm how it is configured in the real driver profile. These fields are part of the employee’s “structural DNA” and define operational context. If they are wrong, downstream assignment is contaminated from the start.

Before you start this section, make sure that:
1. Drivers exist in the baseline.
2. You know which driver or sample group you will review.
3. You want to review structural assignment, not a temporary loan.

To review assignment in the profile:
1. From the general driver list, open a driver profile.
2. Review the structural data side panel.
3. Check at least:
   1. **Primary depot**
   2. **Business unit**
   3. **Work group**
   4. **Area**, if your operation uses it
4. Confirm those values match where the person should actually work.
5. If a value is wrong, update it in the profile.
6. Save changes.
7. Repeat across several drivers to confirm baseline consistency.

For the reference case, confirm that:
1. L1 drivers belong to the correct depot.
2. The business unit matches the expected mode/business.
3. The work group is truly **Drivers** and not another role.

When you finish this section, you should have reviewed structural assignment for the drivers participating in calculation.

## Understanding the difference between primary assignment, qualification, and temporary loan

Before proceeding, distinguish three concepts that are often confused:
1. **Primary assignment**
2. **Qualification**
3. **Temporary loan/transfer**

Primary assignment defines where a person belongs structurally. Qualification answers whether they **can** work legally/technically in another context. Loan/transfer answers where the person **is actually working** during a time period. These layers coexist, but they are not the same.

Before you start this section, make sure that:
1. You reviewed the primary assignment in the profile.
2. You understand some people can work outside their primary context.
3. You want to avoid misreading “belongs to” vs. “can work in” vs. “is working in”.

To distinguish correctly:
1. Use **primary assignment** to describe the driver’s base structural context.
2. Use **qualification** to indicate the driver can work in another depot, group, or unit.
3. Use **loan** to indicate the driver is temporarily moved to another context.
4. Do not use a loan to correct a misconfigured primary assignment.
5. Do not use a qualification as if it were an active move.
6. Keep these questions as a guide:
   1. Where does this person belong? → primary assignment
   2. Where could they work legally? → qualification
   3. Where are they working right now? → loan

For the reference case, ask yourself:
1. Does the driver belong to North Depot?
2. Can they work at another depot if needed?
3. Are they temporarily loaned to another base, or still in their usual context?

When you finish this section, you should have a correct reading of the hierarchy between assignment, qualification, and loan.

## Validating that assignment enables correct filtering and assignment

Assignment is not only descriptive—it affects how the system sees the driver and which duties they can receive. A wrongly assigned person can be filtered out, appear in the wrong place, or receive duties that do not belong to them. The opposite can also happen: a valid person can be hidden or made ineligible due to incorrect assignment.

Before you continue, make sure that:
1. You reviewed depot, unit, and group across multiple profiles.
2. You understand the difference between assignment and loan.
3. You know which population will participate in the next calculation.

To validate assignment’s operational impact:
1. Review which set of drivers should be visible for your calculation context.
2. Confirm the correct people appear under the correct depot, unit, and group.
3. Check whether any drivers are in the wrong group.
4. Check whether any drivers who should belong do not appear as such.
5. If you detect an assignment error, fix it before moving to rules or availability.
6. Save the final configuration for affected profiles.

For the reference case, make sure that:
1. Drivers who will cover L1 appear in the correct operational context.
2. They are not mixed with populations that should not receive driving duties.
3. The system could filter and assign only relevant staff.

When you finish this section, you should have an operational assignment baseline that helps the system see and use the right people.

## Confirming operational assignment is ready for the next layer

The last step is confirming assignment is solid enough to continue with rules, absences, and calculation. The goal is not just to fill fields, but to leave a clear structure the engine can interpret unambiguously.

Before you finish, make sure that:
1. You reviewed structural assignment for key profiles.
2. You can distinguish assignment vs. qualification vs. loan.
3. You validated the visible population is the correct one.
4. You fixed major misalignments.

To confirm assignment is ready:
1. Return to the general driver list.
2. Confirm the population relevant to your case appears in the correct context.
3. Confirm there are no obvious depot/unit/group errors.
4. Ask yourself whether the system could:
   1. filter case drivers correctly,
   2. apply rules for the correct population,
   3. and treat them as the baseline for availability and calculation.
5. If yes, continue with the next quick start.
6. If no, fix assignment before proceeding.

For the reference case, do not proceed until you can state:
1. L1 drivers are assigned to the correct context.
2. You can distinguish who belongs, who can work, and who is loaned.
3. The baseline is ready to apply Rostering rules and availability.

When you finish this section, you should have an operational assignment baseline clear enough to continue with the next process layer.

## Additional reading

- [Defining Rostering rules for staff assignment](P22_Defining_rostering_rules_for_staff_assignment.md)

