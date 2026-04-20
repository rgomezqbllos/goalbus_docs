---
title: Running the first Rostering calculation
shortTitle: Calculate Rostering
intro: 'Learn how to prepare and run the first Rostering calculation, review whether the staff solution is viable, and detect whether problems belong to rules, availability, or assignment before validating.'
contentType: how-tos
versions:
  - '*'
---

## Preparing the baseline before running Rostering calculation

Before running calculation, confirm the staff baseline is mature enough. Rostering should not be used to discover missing master data at the last minute. If the roster, assignment, rules, or availability are not well prepared, calculation will fail or produce a misleading solution.

Use this quick start when you already have a stable Scheduling solution and you prepared the staff layer needed to assign real work to real drivers.

Before you begin, make sure that:
1. You closed the transition from Scheduling in P19.
2. You loaded and reviewed drivers in P20.
3. You validated operational assignment in P21.
4. You configured Rostering rules in P22.
5. You registered absences, inactivity, and availability in P23.
6. You registered loans/transfers/assignment changes in P24.
7. You know which Scheduling solution will be the calculation input.

For this quick start, use this reference case:

> **I’m going to run the first Rostering calculation for line L1 using a stable Scheduling solution and a properly prepared driver baseline.**

To prepare the baseline:
1. Open the **Rostering** environment/module.
ref: P25_Imagen1.png | compact
2. Review which Scheduling solution will be the input.
3. Confirm the driver population participating is available and assigned to the correct context.
4. Confirm active Rostering rules match the real case.
5. Confirm main absences and inactivity are registered.
6. Confirm relevant loans/transfers are reflected.
7. If you detect a master-data issue, fix it before calculating.

For the reference case, do not proceed until you can state:
1. L1’s solution no longer needs structural changes.
2. The driver population exists and is ready.
3. Rules and availability represent the period’s reality.
4. You can attempt a real staff assignment.

When you finish this section, you should have a stable enough baseline to run Rostering.

## Selecting the correct Scheduling input

Rostering needs a clear work input. That input should not be an ambiguous mix of scenarios, but a known, usable Scheduling solution. The key is confirming you will assign people to the correct work.

Before you start this section, make sure that:
1. You know which Scheduling scenario/solution you will use.
2. You know which line, day type, or context you will cover.
3. You can distinguish the active solution from an iteration not yet consolidated.

To select the correct input:
1. In Rostering, open the calculation configuration / assignment scenario configuration.
2. Select the **Scheduling solution** that will be the input (i.e., the solution published for a date range).
3. Confirm day type matches what you want to calculate.
4. Confirm the line(s) match the case.
5. If multiple versions are available, select only the one you truly want as baseline.
6. Save selection.
7. Confirm the system clearly shows which work will be assigned.

For the reference case, make sure that:
1. The input corresponds to workday L1.
2. You are not mixing a published version with an unapproved iteration.
3. The work coming into Rostering is exactly what you want to cover.

When you finish this section, you should have a well-defined Scheduling input for staff calculation.

## Configuring Rostering calculation with the correct rules and population

Once input is selected, confirm calculation uses the correct population and rules. In Rostering, a bad combination of population, rules, and availability can make a solution infeasible even if Scheduling was correct.

Before you start this section, make sure that:
1. You selected the Scheduling input.
2. You know which staff population participates.
3. You decided whether to use basic rules, advanced rules, or a controlled combination.

To configure Rostering calculation:
1. Start assignment calculation configuration by creating a new Rostering scenario.
2. Select these inputs:
   1. the participating **Depots**,
   2. the **dates** for the new Rostering scenario,
   3. the applied **rules model**, confirming active rules match the correct group,
   4. a **description** if you want to add detail.
3. Save configuration.
ref: P25_Imagen2.png | compact
4. Confirm calculation considers:
   1. absences,
   2. inactivity,
   3. loans,
   4. and availability restrictions.
5. Confirm calculation has:
   1. input work,
   2. eligible population,
   3. applicable rules.

For the reference case, confirm that:
1. L1’s driver group is the one being used.
2. Active rules match that group.
3. Configuration is not inheriting constraints from another context.

When you finish this section, you should have Rostering calculation correctly parameterized before running it.

## Running the first assignment calculation

Now you can run calculation. The system will try to assign real people to work inherited from Scheduling, respecting rules, assignment, and availability.

Before you start this section, make sure that:
1. You selected the correct input.
2. You configured population and rules.
3. You reviewed availability and context changes.
4. You are not missing essential master data.

To run Rostering calculation:
1. From the Rostering scenario/module, run **Calculate** / **Start calculation**.
ref: P25_Imagen3.png | compact
2. Confirm the system starts processing assignment.
3. Wait for calculation to finish.
4. Check whether the system returns:
   1. an assigned solution,
   2. a partial solution,
   3. or a clear conflict signal.
5. If calculation does not produce a usable solution, do not immediately assume you lack staff. First review:
   1. rules that are too restrictive,
   2. incorrect assignment,
   3. absences loaded incorrectly,
   4. or inconsistent loans and qualifications.

For the reference case, confirm:
1. L1 calculation runs on the expected population.
2. The system attempts to assign real work to real people.
3. The result lets you assess feasibility or identify concrete conflicts.

When you finish this section, you should have a first Rostering solution or a clear signal of where the blockage is.

## Interpreting whether the problem is rules, availability, or assignment

After calculation, interpret the result correctly. Not all failures mean the same thing. If you misread the cause, you can fix the wrong layer.

Before you continue, make sure that:
1. You already ran calculation.
2. You saw whether the solution is complete, partial, or conflicting.
3. You are willing to diagnose before changing data.

To interpret the result:
1. If many assignments are missing, review staff **availability** first.
2. If the system excludes people who should be valid, review **assignment** and **qualifications**.
3. If assignment seems too rigid or impossible, review **Rostering rules**.
4. If inherited work looks infeasible for any population, review whether the problem comes from **Scheduling**.
5. Do not fix by intuition. First locate whether the problem belongs to:
   1. rules,
   2. availability,
   3. assignment,
   4. or inherited structure.

For the reference case, ask:
1. Do I truly lack people, or are they misconfigured?
2. Did an enabled rule make assignment impossible?
3. Am I trying to use a driver in a context they do not belong to or are not qualified for?
4. Did the problem already exist before entering Rostering?

When you finish this section, you should have an initial diagnostic reading of the calculation result.

## Leaving the solution ready for functional review

The goal of this quick start is not yet to approve the solution. The goal is to run the first calculation and leave a baseline ready for functional review: coverage, conflicts, balance, and feasibility.

Before you finish, make sure that:
1. You ran calculation.
2. You reviewed whether the solution is complete or partial.
3. You identified whether issues belong to rules, availability, assignment, or Scheduling.

To close the first calculation in a useful way:
1. Keep the calculation result as the review baseline.
2. Avoid massive changes before identifying the cause.
3. Decide whether the next step is:
   1. reviewing coverage conflicts,
   2. adjusting rules,
   3. correcting staff data,
   4. or returning to Scheduling if the issue is structural.
4. Treat this first run as validation of the full assignment model.
5. If the baseline is reasonable, continue with conflict and coverage review.

For the reference case, finish this quick start only when you can state:
1. You ran the first Rostering calculation for L1.
2. You know whether the solution is viable or partial.
3. You have a clear hypothesis about the main conflicts.
4. You are ready to review coverage and conflicts in more detail.

When you finish this section, you should have run the first Rostering calculation and have a clear baseline for the next review phase.

## Additional reading

- [Reviewing staff conflicts, coverage, and feasibility](P26_Reviewing_staff_conflicts_coverage_and_feasibility.md)

