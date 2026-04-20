---
title: Defining Rostering rules for staff assignment
shortTitle: Rostering rules
intro: 'Learn how to configure basic and advanced Rostering rules so staff assignment respects labor limits, fairness criteria, and real operational constraints before calculating the roster.'
contentType: how-tos
versions:
  - '*'
---

## Understanding what Rostering rules control

Before calculating staff assignments, you need to define the **Rostering rules** that will guide how employees are assigned to duties. These rules do not build the work—that was already solved by Scheduling. Here you control how that work is distributed across real people, respecting operational policies, fairness criteria, and labor constraints.

Use this quick start when you already have a sufficiently stable Scheduling solution, a loaded driver baseline, and a reviewed operational assignment.

Before you begin, make sure that:
1. You closed the transition from Scheduling in P19.
2. You loaded and reviewed drivers in P20.
3. You validated operational assignment in P21.
4. You know which Scheduling solution will be the baseline.
5. You know which staff population/work group is affected by calculation.

For this quick start, use this reference case:

> **I’m going to configure Rostering rules for line L1 and its driver group so calculation assigns real staff while respecting rest, work limits, and operational criteria.**

To understand the role of these rules:
1. Treat Rostering rules as constraints and preferences on assigning people.
2. Use these rules when you want to control:
   1. rests,
   2. work time,
   3. weekly patterns,
   4. work group,
   5. pairing,
   6. and other fairness/internal-policy criteria.
3. Do not use these rules to fix problems in:
   1. offer,
   2. times,
   3. fleet,
   4. or base duty construction.
4. If you detect the issue is still structural, go back to Scheduling before proceeding.

When you finish this section, you should be clear that Rostering rules govern people—not the base structure of work.

## Distinguishing basic rules vs. advanced rules

Before creating a rules model, distinguish two configuration levels:
1. **Basic rules**
2. **Advanced rules**

Basic rules are designed to quickly configure common constraints. They are useful for fast parameterization or an initial trial. Advanced rules are designed to model constraints and preferences more precisely through limits and penalties.

Before you start this section, make sure that:
1. You know whether your case needs speed or precision.
2. You understand basic rules have less modeling flexibility than advanced rules.
3. You know whether you will need different models for different uses.

To choose the appropriate rule type:
1. Use **basic rules** if you want to quickly cover common constraints.
2. Use **advanced rules** if you need to precisely model complex policies, agreements, or specific operational conditions.
3. Keep in mind active basic rules apply both in daily operations and in assignment calculation scenarios.
4. If you need distinct models for distinct contexts (e.g., daily operations vs. a future calculation), use advanced rules.
5. Decide your approach before parameterizing.

For the reference case:
1. If you are starting and want an initial control layer, start with basic rules.
2. If you already know you will need preferences, penalties, or context-specific models, move into advanced rules.

When you finish this section, you should know whether your case will use basic rules, advanced rules, or a controlled combination.

## Enabling common basic rules for a first assignment

If your case needs a quick initial configuration, start with **basic rules**. These cover the most common restrictions and allow you to run calculation with a reasonable foundation before moving into finer controls.

Before you start this section, make sure that:
1. You decided to start with basic rules.
2. You know which minimum restrictions you want to enforce.
3. You understand not all rules should be enabled by default.

To enable basic rules:
1. In GoalBus, go to **Configuration** > **Assignment rules**.
ref: P22_Imagen1.png | compact
2. Open the **Basic rules** section.
3. Review the catalog of available basic rules.
ref: P22_Imagen2.png | full
4. Enable only the ones that match the case you are building.
5. Configure, when applicable:
   1. general limits,
   2. employee-property-specific limits,
   3. or exceptions for specific employees.
6. Save changes.
7. Confirm active rules reflect the policies you want to enforce.

An initial basic-rule set could include:
1. **Work pattern**
2. **Rest between days**
3. **Monthly work time**
4. **Weekly work time**
5. **Days off per week**
6. **First published solution**
7. **Work group**
8. **Pairing**
9. **Assignment compatibility**
10. **Line qualification**
11. **First published solution shift**
12. **Consecutive working days**, when applicable

For the reference case, do not enable a rule just because it exists. Enable it only if:
1. it addresses a real need,
2. you can explain why you need it,
3. and you understand how it will affect assignment.

When you finish this section, you should have an initial control baseline for staff assignment.

## Creating an advanced rules model when you need more precision

If basic rules are not enough, create an **advanced rules model**. This approach lets you control assignment precisely by adjusting limits and preferences according to company policies, labor agreements, and real operating conditions.

Before you start this section, make sure that:
1. You identified what cannot be modeled well with basic rules.
2. You know which behaviors must be mandatory and which should be preferred.
3. You need a finer model that can be reused by scenario or context.

To create an advanced rules model:
1. In **Configuration** > **Assignment rules**, open **Rules models**.
2. Create a new rules model.
3. Give the model a clear **name**.
4. Add a **description** to distinguish it from others.
5. Save the model.
ref: P22_Imagen3.png | compact
6. Add advanced rules one by one.
7. For each rule, decide:
   1. whether it is a hard limit,
   2. or a preference via penalty.
8. Save the model configuration.
9. Activate the created rules model.
10. Confirm the model can be assigned to the appropriate Rostering calculation.

For the reference case, valid options could be:
- **Rostering L1 workday**
- **L1 drivers assignment - advanced rules**

When you finish this section, you should have an advanced model ready to represent more complex constraints and preferences.

## Linking rules to the correct population and real calculation

After enabling basic rules or creating an advanced model, confirm rules apply to the correct population and you are not imposing abstract constraints unrelated to the real calculation.

Before you continue, make sure that:
1. You enabled basic rules or created an advanced model.
2. You know which employees/groups/depots participate in calculation.
3. You know which Scheduling solution will be the input.

To correctly link rules to calculation context:
1. Review the staff population Rostering will apply to.
2. Confirm whether rules affect:
   1. the entire involved roster,
   2. a specific group,
   3. or employees with specific properties.
3. Confirm you are not imposing rules on people who do not participate in that calculation.
4. Confirm the Scheduling scenario logic remains compatible with these rules.
5. If a rule makes assignment infeasible, adjust its limit or scope.
6. Save the final configuration.

For the reference case, ask yourself:
1. Are these rules designed for the drivers who will actually cover L1?
2. Is the affected work group the correct one?
3. Is assignment still feasible after enabling these rules?

When you finish this section, you should have rule configuration connected to real people and a concrete Rostering calculation.

## Confirming the rules baseline is ready to calculate Rostering

The last step is ensuring your configuration is ready to feed staff calculation. The goal is not only to enable rules, but to leave a coherent, understandable, applicable baseline.

Before you finish, make sure that:
1. You chose basic vs. advanced rules according to your case.
2. You enabled or modeled the needed constraints.
3. You linked logic to the correct population.
4. You confirmed assignment remains feasible.

To validate the rules baseline is ready:
1. Review the final set of active rules.
2. Confirm each rule addresses a real need.
3. Ask yourself whether the system could:
   1. block invalid assignments,
   2. respect rests and limits,
   3. reflect fairness and work-group criteria,
   4. and still produce a usable solution.
4. If yes, continue with the next quick start.
5. If no, adjust rules before proceeding.

For the reference case, do not proceed until you can state:
1. Rostering rules for L1 are clear.
2. You know why each rule is enabled.
3. The system can still assign real people with that configuration.
4. The baseline is ready to handle availability and staff exceptions.

When you finish this section, you should have a Rostering rules baseline solid enough to move into absences, inactivity, and availability.

## Additional reading

- [Managing absences, inactivity, and staff availability](P23_Managing_absences_inactivity_and_staff_availability.md)

