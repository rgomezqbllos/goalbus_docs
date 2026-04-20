---
title: Moving from Scheduling to Rostering
shortTitle: Scheduling to Rostering
intro: 'Learn what must be ready in Scheduling before entering Rostering, what information staff assignment inherits, and which problems must be resolved before calculating real drivers.'
contentType: how-tos
versions:
  - '*'
---

## Confirming what must be closed in Scheduling before moving to Rostering

Before entering Rostering, you need to confirm Scheduling already left a sufficiently stable foundation. Rostering does not replace Scheduling. Rostering starts from already-built work and decides how to assign it to real people.

Use this quick start when you already have a calculated and validated Scheduling solution and need to decide whether you can start working with real staff.

Before you begin, make sure that:
1. You already created, calculated, and validated the Scheduling scenario.
2. You already reviewed the service offer and its overall coherence.
3. You know which lines, day type, and solution you will use as reference.
4. You understand Rostering is not where you fix a structurally weak Scheduling baseline.

For this quick start, use this reference case:

> **I’m going to confirm that the validated Scheduling solution for line L1 is mature enough to move to Rostering and start assigning work to real drivers.**

To confirm Scheduling is ready:
1. Open the Scheduling scenario you will use as reference.
2. Confirm its status is the right one to stop treating it as a working draft.
3. Confirm the offer used is still the correct one.
4. Confirm vehicle logic and shift logic have already been applied.
5. Confirm there are no obvious structural inconsistencies in the solution.
6. If you still need to rebuild vehicle, time, service, or rules foundations, go back to Scheduling before proceeding.
7. If the solution is stable, continue to the next step.

For the reference case, do not proceed until you can state:
1. L1’s solution has been calculated.
2. It has been reviewed.
3. It no longer needs structural Scheduling corrections.
4. It can be treated as the working baseline for staff assignment.

When you finish this section, you should know whether Scheduling delivered a usable foundation for Rostering.

## Understanding what Rostering inherits from Scheduling

Once the foundation is confirmed, understand what passes from Scheduling to Rostering. The key is not to think Rostering starts from zero. Rostering inherits already-structured work and then decides which real person can take it.

Before you start this section, make sure that:
1. You identified the Scheduling solution you will use.
2. You know which parts of that solution must remain stable.
3. You understand Rostering works on already-built work, not on an unstructured offer.

To understand what Rostering inherits:
1. Review the validated Scheduling solution.
2. Identify the duties/blocks/work structures that will be the baseline.
3. Confirm the solution is recognizable from an operational point of view.
4. Keep in mind that in Rostering, the system is not creating abstract work—it is trying to assign that work to real people.
5. Use this reading rule:
   1. Scheduling defines **what work exists**.
   2. Rostering defines **who will do that work**.

For the reference case, ask yourself:
1. Does L1’s solution contain work that is clear enough to assign?
2. Are work blocks recognizable and usable?
3. Is the remaining problem about people rather than structure?

When you finish this section, you should understand what Rostering inherits—and what should not be redefined there.

## Separating which problems are solved in Scheduling vs. in Rostering

Before fully moving into the staff layer, keep responsibilities clearly separated. Many errors happen when people try to fix in Rostering what should have been fixed earlier in Scheduling.

Before you continue, make sure that:
1. You know which Scheduling scenario is the baseline.
2. You understand Rostering consumes a prior solution.
3. You are ready to separate structural problems from staff problems.

To separate the two domains correctly:
1. Treat as a **Scheduling** problem anything related to:
   1. service structure,
   2. fleet logic,
   3. times,
   4. vehicle rules,
   5. shift types and base duty construction.
2. Treat as a **Rostering** problem anything related to:
   1. real driver availability,
   2. depot/group assignment,
   3. absences,
   4. inactivity,
   5. loans/transfers,
   6. real eligibility to receive a duty.
3. If you detect a work inconsistency that affects the entire structure, go back to Scheduling.
4. If you detect a person inconsistency, solve it in Rostering.

For the reference case:
1. If the problem is that L1 work was built incorrectly, go back to Scheduling.
2. If the problem is which real driver can take that work, you are correctly entering Rostering.

When you finish this section, you should be able to clearly explain what must be corrected before moving to staff and what belongs to the next module.

## Confirming what must be ready on the staff side before calculating Rostering

Now that you know what Rostering receives, review what must exist on the staff side for the next calculation to make sense. A good Scheduling is not enough if you do not have a minimum baseline of people, assignments, and availability.

Before you start this section, make sure that:
1. You have a valid baseline from Scheduling.
2. You know which groups, depots, or operational contexts affect staff.
3. You are ready to review the staff layer.

To confirm the staff foundation is ready:
1. Confirm there is a staff population that can receive the work.
2. Confirm people are assigned to the correct context when applicable.
3. Confirm you are not entering Rostering without minimum availability information.
4. Review whether the necessary structures exist for:
   1. Rostering rules,
   2. absences,
   3. inactivity,
   4. transfers/loans, when applicable.
5. If you do not have this baseline yet, do not run staff calculation.
6. If the baseline exists (or is at least on track), continue with the next Rostering quick starts.

For the reference case, ask yourself:
1. Does the staff who will receive L1’s solution already exist?
2. Does that staff belong to the correct scope?
3. Is availability and assignment baseline minimally prepared?

When you finish this section, you should know whether the staff side is ready to enter Rostering.

## Clarifying the transition point between Scheduling and Rostering

The last step is closing the transition mentally. This quick start is not meant to calculate staff assignment yet. It is meant to make it crystal clear where Scheduling ends and Rostering begins so you do not mix the two domains.

Before you finish, make sure that:
1. You reviewed the Scheduling solution.
2. You understand what Rostering inherits.
3. You separated structural vs. staff problems.
4. You checked whether a minimum staff baseline exists.

To close the transition correctly:
1. Treat the validated Scheduling solution as the formal input to Rostering.
2. Do not keep altering that baseline unless you detect a real structural issue.
3. Use the next quick starts to prepare:
   1. Rostering rules,
   2. absences and inactivity,
   3. transfers, loans, and assignment changes.
4. Consider the objective changes from here:
   1. you are no longer building work,
   2. you are now assigning it to real people.
5. If you can state that clearly, the transition is done correctly.

For the reference case, finish this quick start only when you can state:
1. Scheduling already left a stable L1 solution.
2. The next problem is no longer structural, but staff assignment.
3. You can now move into Rostering rules.

When you finish this section, you should have a clear, controlled transition between Scheduling and Rostering.

## Additional reading

- [Loading and managing drivers](P20_Loading_and_managing_drivers.md)

