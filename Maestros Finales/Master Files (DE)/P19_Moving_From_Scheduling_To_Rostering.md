---
title: Moving from Scheduling to Rostering
shortTitle: From Scheduling to Rostering
intro: Learn what should be ready in Scheduling before entering Rostering, what information
  inherits the staff assignment, and what problems should be solved before calculating
  real drivers.
contentType: how-tos
versions:
- '*'
---
## Confirming that it should be closed in Scheduling before moving to Rostering

Before entering Rostering, you need to check that Scheduling already left a sufficiently stable base. Rostering does not replace Scheduling. Rostering part of the work already built and decides how to assign it to real people.

Use this quick start when you already have a calculated and validated Scheduling solution, and you need to decide if you can start working with real staff.

Before you start, make sure that:
1. You've already created, calculated and validated Scheduling's scenario.
2. You've already reviewed the service offer and its overall consistency.
3. You know what lines, what kind of day and what solution you will use as a reference.
4. You're clear that Rostering isn't the place to fix a bad structural base for Scheduling.

For this quick start, use this reference case:

> **I'm going to confirm that Scheduling's validated solution for the L1 line is ripe enough to move to Rostering and start assigning work to real drivers.**

To confirm that Scheduling is ready:
1. Open the Scheduling scenario that you will use as a reference.
2. Check that your condition is already correct to stop treating it as a work draft.
3. Check that the offer used is still the right one.
4. Check that the logic of vehicles and the logic of shifts have already been applied.
5. It confirms that there are no obvious structural inconsistencies in the solution.
6. If you still need to redo the vehicle base, times, services or rules, go back to Scheduling before following.
7. If the solution is already stable, continue to the next step.

For the reference case, do not continue until you can state:
1. The L1 solution has already been calculated.
2. It's been checked out.
3. You no longer need structural corrections from Scheduling.
4. It can now be treated as a working base for staff.

By the time you finish this section, you should be clear whether Scheduling has already delivered a usable base for Rostering.

## Understanding what Rostering inherits from Scheduling

Once the base is confirmed, you need to understand what information happens from Scheduling to Rostering. Here the key is not to think that Rostering starts from scratch. Rostering inherits the already structured work and from there decides which real person can assume it.

Before starting this section, make sure that:
1. You've already identified the Scheduling solution you're going to use.
2. You know what part of that solution should stay stable.
3. You understand that Rostering works on work already built, not on an unstructured offer.

To understand what Rostering inherits:
1. Check the validated Scheduling solution.
2. Identify the tasks, blocks or work structures that will serve as a basis.
3. Check that the solution already has an operationally recognizable shape.
4. Keep in mind that, by moving to Rostering, the system is no longer creating abstract work, but trying to assign that work to real people.
5. Use this reading rule:
   1. Scheduling defines **what work exists**.
   2. Rostering defines **Who's gonna do that job?**.

For the reference case, ask yourself:
1. Does the L1 solution already have clear enough work to assign it?
2. Are the work blocks recognizable and usable?
3. Is the problem that remains to be solved already of people and not of structure?

When you finish this section, you should understand what Rostering inherits and what should not be redefined there again.

## Distinguishing which problems are solved in Scheduling and which in Rostering

Before you finally move on to the personnel layer, you need to separate very well responsibilities. This distinction is fundamental because many errors appear when you try to correct in Rostering something that should have been resolved earlier in Scheduling.

Before continuing, make sure that:
1. You know what stage Scheduling will be at the base.
2. You understand that Rostering consumes a previous solution.
3. You're prepared to distinguish structural problems from personnel problems.

To properly separate both domains:
1. It treats as a **Scheduling** problem any matter related to:
   1. structure of the service,
   2. Fleet logic,
   3. times,
   4. vehicle rules,
   5. types of shifts and their base construction.
2. It treats as a **Rostering** problem any matter related to:
   1. actual availability of the driver,
   2. secondment to deposit or group,
   3. absences,
   4. inactivity,
   5. transfers or transfers,
   6. real eligibility to receive a shift.
3. If you detect a working inconsistency that affects the entire structure, go back to Scheduling.
4. If you detect a person's incoherence, solve it in Rostering.

For the reference case, use this logic:
1. If the problem is that L1's work was badly built, go back to Scheduling.
2. If the problem is you don't know which real driver can take that job, you're getting into Rostering correctly.

When you finish this section, you should be able to explain clearly what should be corrected before you move on to staff and what does belong to the next module.

## Confirming what should be ready on the staff side before calculating Rostering

Now that you know what Rostering receives, you need to check what must exist on the staff side so that the following calculation makes sense. It’s not enough to have a good schedule if you still don’t have a minimum base of people, secondments and availability.

Before starting this section, make sure that:
1. You already have a valid base from Scheduling.
2. You know what groups, deposits, or operating contexts affect people.
3. You're ready to check the personnel layer.

To confirm that the staff base is ready:
1. Checks that there is already a staff group that can receive the job.
2. Check that people are attached to the correct context when applying.
3. Check that you're not entering Rostering without minimum availability information.
4. Check whether the necessary structure already exists for:
   1. Rostering rules,
   2. absences,
   3. inactivity,
   4. transfers or transfers, where applicable.
5. If you don't have this base yet, don't launch the staff calculation.
6. If the base already exists or is at least on track, continue with the following quick starts from Rostering.

For the reference case, ask yourself:
1. Does the staff already exist who will be able to receive the L1 solution?
2. Does that staff belong to the right realm?
3. Is the base of availability and secondment already minimally prepared?

When you finish this section, you should be clear whether the staff side is already ready to enter Rostering.

## Making clear the transition point between Scheduling and Rostering

The last step is to mentally close the transition. This quick start does not intend to calculate the staff assignment yet. It aims to make it very clear when Scheduling ends and when Rostering begins so that you do not mix both domains.

Before you finish, make sure that:
1. You've already checked Scheduling's solution.
2. You understand what Rostering inherits.
3. You've already separated structural problems from personnel problems.
4. You've already checked to see if there's a minimum staff base.

To close the transition correctly:
1. Treats the validated Scheduling solution as a formal Rostering input.
2. Don't keep altering that base unless you detect a real structural problem.
3. Use the following quick starts to prepare:
   1. Rostering rules,
   2. absences and inactivitys,
   3. transfers, assignments and secondment changes.
4. Considers that the objective changes from here:
   1. It's not about building work anymore,
   2. Now it's about assigning it to real people.
5. If you can state that clearly, the transition is well done.

For the reference case, finish this quick start only when you can say:
1. Scheduling has already left a stable L1 solution.
2. The next problem is no longer structural, but staff assignment.
3. You can now enter the Rostering rule layer.

When you finish this section, you should have a clear and controlled transition between Scheduling and Rostering.

## Additional readings

- [Defining Rostering rules for staff assignment](P20_Loading_And_Managing_Drivers.md)
