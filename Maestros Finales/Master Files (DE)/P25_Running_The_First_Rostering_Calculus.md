---
title: Running the first Rostering calculus
shortTitle: Calculate Rostering
intro: Learn how to prepare and execute the first Rostering calculation, check whether
  the personnel solution is viable, and detect what problems belong to rules, availability,
  or secondment before validating the assignment.
contentType: how-tos
versions:
- '*'
---
## Preparing the base before launching the Rostering calculation

Before running the calculation, you need to check that the staff base is mature enough. Rostering should not be used to discover missing master data at the last minute. If the template, secondment, rules or availability are not well prepared, the calculation will fail or produce a misleading solution.

Use this quick start when you already have a stable Scheduling solution and have prepared all the personnel required to assign real work to drivers.

Before you start, make sure that:
1. You've already closed the transition from Scheduling at P19.
2. You already loaded and checked drivers on P20.
3. You've already validated the operational secondment to P21.
4. You've already set Rostering rules to P22.
5. You have already registered absences, inactivity and availability at P23.
6. You have already registered assignments, transfers or secondment changes in P24.
7. You're clear what Scheduling solution will act as input to the calculation.

For this quick start, use this reference case:

> **I'm going to run the first Rostering calculation for line L1, using an already stable Scheduling solution and a properly prepared driver base.**

To prepare the basis before calculation:
1. Opens the **Rostering** environment or module.
ref: P25_Imagen1.png | compact
2. Check which Scheduling solution will be the input of the calculation.
3. Confirms that the collective of drivers who will participate is available and belongs to the correct context.
4. Check that the active Rostering rules respond to the real case.
5. Checks that the main absences and inactivitys are already registered.
6. Confirms that relevant assignments or transfers are already reflected.
7. If you detect a master data problem, correct it before calculating.

For the reference case, do not continue until you can state:
1. The L1 solution no longer needs structural changes.
2. The collective of drivers already exists and is ready.
3. Rules and availability already represent the reality of the period.
4. You can try a real job assignment now.

When you finish this section, you should have a stable enough basis to launch Rostering.

## Selecting the correct entry from Scheduling

Rostering needs a clear work entry. That entry should not be an ambiguous mix of scenarios, but a well-known and usable Scheduling solution. At this stage, the important thing is to confirm that you are going to assign people to the right job.

Before starting this section, make sure that:
1. You know what Scheduling scenario or solution you'll use.
2. You know what line, kind of day or context you're gonna cover.
3. You can now distinguish between the current solution and an unconsolidated iteration.

To correctly select the input of the calculation:
1. In the Rostering module, open the calculation settings or the mapping scenario.
2. Select the **Scheduling solution** that will act as an entry, that is, which solution is published for a date range.
3. Check that the type of day matches the calculation you want to do.
4. Check that the line or set of lines correspond to the case.
5. If there are several possible versions, choose only the one you really want to use as a base.
6. Save the selection.
7. Check that the system already shows clearly what work will be assigned.

For the reference case, make sure that:
1. The entry corresponds to L1 workable.
2. You're not mixing a published version with an unapproved iteration.
3. The job that comes to Rostering is exactly what you want to cover.

When you finish this section, you should have a well-defined Scheduling entry for staff calculation.

## Configuring the Rostering calculation with the correct rules and collective

Once the entry is chosen, you need to check that the calculation uses the collective and the correct rules. In Rostering, a bad combination of collective, rules and availability can make a solution that in Scheduling was correct unviable.

Before starting this section, make sure that:
1. You've already selected the entry from Scheduling.
2. You know which staff group will participate.
3. You've already defined whether you'll use basic, advanced rules or a controlled combination.

To configure the Rostering calculation:
1. Begins the configuration of the mapping calculation by creating a new roasting scenario.
2. Select the following input data:
   1. The **Deposits** that will participate.
   2. Select the **dates** from the new roasting scenario.
   3. Check which **model rules** will apply to the calculation. Confirm that the active rules correspond to the correct group.
   4. Add an **description** if you want to give it more detail.
3. Save the settings.
ref: P25_Imagen2.png | compact(x10)
4. Check whether the calculation will consider:
   1. absences,
   2. inactivity,
   3. assignments,
   4. and availability restrictions.
5. Check that the calculation already has:
   1. entry work,
   2. eligible collective,
   3. applicable rules.

For the reference case, it confirms that:
1. The L1 driver group is the one to be used.
2. The active rules correspond to that group.
3. The configuration is not dragging restrictions from another context.

When you finish this section, you should have the Rostering calculation correctly parameterized before running it.

## Running the first assignment calculation

Now you can launch the calculation. At this point, the system will try to assign real people to work inherited from Scheduling, respecting rules, secondment and availability.

Before starting this section, make sure that:
1. You've already chosen the right entry.
2. You've set up the collective and the rules.
3. You've already reviewed the availability base and context changes.
4. You no longer lack essential master data.

To execute the Rostering calculation:
1. From the Rostering stage or module, it launches the **Calculate** or **Start calculation** action.
ref: P25_Imagen3.png | compact(3x)
2. Check that the system starts processing the assignment.
3. Wait till the calculus is over.
4. Check if the system returns:
   1. an assigned solution,
   2. a partial solution,
   3. or a clear sign of conflict.
5. If the calculation does not generate a usable solution, do not immediately assume that you are missing personal. Check first:
   1. rules too restrictive,
   2. incorrect secondment,
   3. mischarged absences,
   4. o diverging assignments and ratings.

For the reference case, it confirms that:
1. The calculation of L1 is executed on the expected collective.
2. The system tries to assign real work to real people.
3. The result allows you to review feasibility or detect specific conflicts.

When you finish this section, you should have a first Rostering solution or a clear sign of where the lock is.

## Interpreting whether the problem is rules, availability or secondment

After the calculation, you need to correctly interpret the result. Not all faults mean the same thing. If you don't distinguish the cause well, you can correct it in the wrong layer.

Before continuing, make sure that:
1. You've already run the calculus.
2. You saw if the solution was complete, partial or conflicted.
3. You're willing to diagnose before you touch data.

To correctly interpret the result:
1. If many assignments are missing, check the staff **availability** first.
2. If the system leaves out people who should be valid, check their **secondment** and their **ratings**.
3. If the assignment seems too rigid or impossible, check the **Rostering rules**.
4. If legacy work seems unworkable for any group, check again if the problem comes from **Scheduling**.
5. Do not correct by intuition. Find out first if the problem belongs to:
   1. rules,
   2. availability,
   3. secondment,
   4. or inherited structure.

For the reference case, ask yourself these questions:
1. Are people really missing or misconfigured?
2. The rule I activated made the assignment impossible?
3. Am I trying to use a driver in a context where it does not belong or is not enabled?
4. Did the problem already exist before entering Rostering?

When you finish this section, you should have a first diagnostic reading of the result of the calculation.

## Leaving the solution ready for functional review

The aim of this quick start is not yet to approve the solution definitively. The objective is to execute the first calculation and leave a ready basis for functional review: coverage, conflicts, balance and viability.

Before you finish, make sure that:
1. You've already run the calculus.
2. You've already checked whether the solution is complete or partial.
3. You've already identified whether the problems belong to rules, availability, secondment or Scheduling.

To close this first calculation usefully:
1. It retains the result of the calculation as a basis for review.
2. Do not make massive changes without first identifying the cause of the problem.
3. Decides whether the next step will be:
   1. review coverage conflicts,
   2. adjust rules,
   3. correcting personnel data,
   4. or return to Scheduling if the problem is structural.
4. It treats this first execution as a validation of the entire mapping model.
5. If the basis is reasonable, continue with the review of coverage and conflicts.

For the reference case, finish this quick start only when you can say:
1. You've already executed the first Rostering calculation for L1.
2. You know if the solution is viable or partial.
3. You already have a clear hypothesis about where the main conflicts are.
4. You are ready to review coverage and conflicts in more detail.

When you finish this section, you should have executed the first Rostering calculation and a clear basis for the next review phase.

## Additional readings

- [Reviewing Conflicts, Coverage and Feasibility of Personnel](P26_Reviewing_Conflicts_Coverage_And_Feasibility_Of_Personnel.md)
