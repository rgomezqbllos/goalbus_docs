---
title: Defining Rostering rules for staff assignment
shortTitle: Rostering Rules
intro: Learn how to set up basic and advanced Rostering rules so that the staff assignment
  respects labor limits, equity criteria, and real operating restrictions before calculating
  the staffing table.
contentType: how-tos
versions:
- '*'
---
## Understanding what they control Rostering's rules

Before you calculate staff assignments, you need to define the **Rostering rules** that will guide how employees are assigned to shifts. These rules do not build work, because that step has already been resolved by Scheduling. Here, what you do is control how that work is shared among real people, respecting operational policies, equity criteria and labor limits.

Use this quick start when you already have a stable enough Scheduling solution, a loaded driver template, and a revised operating secondment.

Before you start, make sure that:
1. You've already closed the transition from Scheduling at P19.
2. You already loaded and checked drivers on P20.
3. You've already validated the operational secondment to P21.
4. You're already clear what Scheduling solution will act as a basis.
5. You know which collective or group of employees will be affected by the calculation.

For this quick start, use this reference case:

> **I will configure the Rostering rules for the L1 line and its group of drivers, so that the calculation assigns real staff respecting breaks, work limits and operating criteria.**

To understand the role of these rules:
1. It treats Rostering's rules as restrictions and preferences on the assignment of people.
2. Use these rules when you want to control:
   1. breaks,
   2. working time,
   3. weekly patterns,
   4. working group,
   5. pairings,
   6. and other criteria of equity or domestic politics.
3. Do not use these rules to correct problems of:
   1. offer,
   2. times,
   3. floats,
   4. or shift base construction.
4. If you find that the problem remains structural, go back to Scheduling before continuing.

When you finish this section, you should be clear that Rostering rules govern people and not the base structure of work.

## Distinguishing between basic rules and advanced rules

Before you create a rule model, you need to distinguish two configuration levels:
1. **Basic rules**
2. **Advanced Rules**

The basic rules are designed to quickly configure common restrictions. They are useful when you want an agile parameterization or an initial test. The advanced rules are designed to model more precisely restrictions and preferences through limits and penalties.

Before starting this section, make sure that:
1. You know if your case needs speed or precision.
2. You understand that basic rules have less modeling flexibility than advanced ones.
3. You know if you're going to need different models depending on the use.

To choose the right type of rules:
1. Use **basic rules** if you want to quickly cover common restrictions.
2. Use **advanced rules** if you need to model complex policies, agreements, or specific operating conditions in detail.
3. Note that active basic rules apply both in daily operation and in assignment calculation scenarios.
4. If you need different models for different contexts, for example one for daily operation and one for future calculation, work with advanced rules.
5. Decide what approach you will use before you start parameterizing.

For the reference case, use this logic:
1. If you're starting and want a first layer of control, start with basic rules.
2. If you already know that you will need to adjust preferences, penalties or models by context, continue with advanced rules.

When you finish this section, you should be clear whether your case will be solved with basic, advanced rules or a controlled combination of both.

## Activate the most common basic rules for a first assignment

If your case needs a quick initial setup, you can start with the **basic rules**. These cover the most common restrictions and allow you to start the calculation on a reasonable basis before entering finer levels of control.

Before starting this section, make sure that:
1. You've already decided to start with basic rules.
2. You know what minimum restrictions you want to impose.
3. You are clear that not all rules must be activated by default.

To activate basic rules:
1. In GoalBus, go to **Settings** > **Rules of allocation**.
ref: P22_Imagen1.png | compact
2. Open the **Basic rules** section.
3. Check the catalogue of basic rules available.
ref: P22_Imagen2.png | full
4. Activate only those that correspond to the case you're building.
5. Sets, when applying:
   1. general limits,
   2. specific limits for employee properties,
   3. or exceptions for certain employees.
6. Save the changes.
7. Check that active rules really reflect the policies you want to impose.

An initial basis of basic rules may include:
1. **Work pattern**
2. **Rest between days**
3. **Monthly working time**
4. **Weekly working time**
5. **Day off per week**
6. **First Solution Published**
7. **Working Group**
8. **Pairing**
9. **Allocation compatibility**
10. **Line Enabling**
11. **Turn of First Solution Published**
12. **Consecutive working days**, when applied

For the reference case, do not activate a rule just because it exists. Activate it only if:
1. responds to a real need,
2. You can explain why you need it,
3. And you know how it will affect the assignment.

When you finish this section, you should have a first control base for staff assignment.

## Creating a model of advanced rules when you need more precision

If the basic rules are not enough, the next step is to create an **model of advanced rules**. This approach allows you to accurately control how assignments are generated, adjusting limits and preferences according to company policies, labor agreements and real operating conditions.

Before starting this section, make sure that:
1. You've already identified which part of the case can't be solved well with basic rules.
2. You know which behaviors should be mandatory and which only preferred.
3. You already need a finer model that can be reused by scenario or context.

To create a model of advanced rules:
1. In **Settings** > **Rules of allocation**, open the **Model Rules** section.
2. Creates a new model of rules.
3. Assigns a clear **name** to the model.
4. Add an **description** that allows you to distinguish it from other models.
5. Save the model.
ref: P22_Imagen3.png | compact
6. Start adding advanced rules one by one.
7. For each rule, decide:
   1. if it acts as a mandatory limit,
   2. or if it acts as a preference by penalty.
8. Saves the model settings.
9. Activates the created rule model.
10. Check that the model can already be assigned to the proper Rostering calculation.

For the reference case, a valid option could be:
- **Rostering L1 workable**
- **L1 Driver Assignment - Advanced Rules**

When you finish this section, you should have an advanced model ready to represent more complex restrictions and preferences.

## Relating the rules to the correct collective and to the actual calculation

After activating basic rules or creating an advanced model, you need to check that the rules apply to the correct collective and that you are not imposing abstract restrictions unrelated to actual calculation.

Before continuing, make sure that:
1. You've already activated basic rules or created an advanced model.
2. You know which employees, groups or deposits will participate in the calculation.
3. You're clear what Scheduling solution will serve as input.

To correctly relate the rules to the calculation context:
1. Check the personnel group that Rostering will apply to.
2. Check if the rules affect:
   1. all the staff involved,
   2. to a specific group,
   3. or employees with specific properties.
3. Confirm that you are not imposing rules on people who will not even participate in that calculation.
4. Check whether the logic of the Scheduling scenario is still compatible with these rules.
5. If a rule makes the division of work unworkable, it adjusts its limit or scope.
6. Saves the final version of the configuration.

For the reference case, ask yourself:
1. Are these rules intended for drivers who will actually cover L1?
2. Is the working group concerned the right one?
3. Is the assignment still viable after activating these rules?

When you finish this section, you should have a set of rules connected to real people and with a specific Rostering calculation.

## Confirming that the rule base is already ready to calculate Rostering

The last step is to make sure that your settings are ready to feed the staff calculation. It’s not just about activating rules, but having left a coherent, understandable and applicable basis.

Before you finish, make sure that:
1. You've already chosen between basic and advanced rules as the case may be.
2. You have already activated or modeled the necessary restrictions.
3. You've already linked logic to the right collective.
4. You've already checked that the assignment is still viable.

To validate that the rule base is already ready:
1. Check the final set of active rules.
2. Confirms that each responds to a real need.
3. Ask yourself if the system could already:
   1. block invalid assignments,
   2. respect rests and limits,
   3. reflect equity criteria and working group,
   4. and continue to generate a usable solution.
4. If the answer is yes, continue with the next quick start.
5. If the answer is no, adjust the rules before following.

For the reference case, do not continue until you can state:
1. The Rostering rules for L1 are now clear.
2. You know why you activated every rule.
3. The system can still assign real people with that configuration.
4. The base is already ready to deal with staff availability and exceptions.

When you finish this section, you should have a strong enough Rostering rule base to move on to the treatment of absences, inactivity, and availability.

## Additional readings

- [Managing absences, inactivity and staff availability](P23_Managing_Absences_Inactivity_And_Staff_Availability.md)
