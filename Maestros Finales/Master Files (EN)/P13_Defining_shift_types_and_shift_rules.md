---
title: Defining shift types and shift rules
shortTitle: Types and rules
intro: 'Learn how to create shift types, organize them inside rules models, and enable the necessary constraints or penalties so Scheduling builds legally valid and operationally coherent duties.'
contentType: how-tos
versions:
  - '*'
---

## Creating the shift types that will structure work

Before configuring shift rules, you need to define the **shift types** the system will use to group trips into coherent human work. A shift type is not just a visual label. It is the logical category that guides the engine to build duties that are recognizable and usable later in Rostering, daily operations, and integrations.

Use this quick start when you already have a validated offer, defined vehicle logic, and you need to tell the system which work patterns are valid for your case.

Before you begin, make sure that:
1. You already created and validated the service offer in P10.
2. You already validated operational structure in P11.
3. You already defined vehicle rules in P12.
4. You know which service and operating context you will use as reference.

For this quick start, use this reference case:

> **I’m going to define shift types for line L1 so Scheduling can build coherent duties before I create the calculation scenario.**

To create shift types for your case:
1. In GoalBus, go to **Configuration** > **Staff** > **Shift types**.
ref: P13_Imagen1.png | compact
2. Check whether suitable shift types already exist for your case.
3. If a type exists, open it and confirm it is still valid.
4. If it does not exist, create a new one.
5. Define these fields:
   1. **Full name**, clear and descriptive.
   2. **Short name**, for compact views and operational cards.
   3. **External ID**, if the customer needs integration with HR or payroll systems.
ref: P13_Imagen2.png | compact
6. Mark the type as **Active** if it should participate in future calculations.
7. Save the shift type.
8. Repeat for each work category you truly need in your case.

For the reference case, you could create types such as:
1. **Morning shift**
2. **Afternoon shift**
3. **Split shift**, if required by operations

When you finish this section, you should have the shift types that will act as the “DNA” of the duties Scheduling will build.

## Creating or selecting the shift rules model

After creating shift types, you need to define the container where rules will live. Shift rules are not managed as a flat list, but inside **models** that group a coherent set of constraints for a scenario, period, or simulation. This allows you to maintain multiple configurations without mixing historical rules with active ones.

Before you start this section, make sure that:
1. You already created or validated the shift types you will use.
2. You know which service or simulation you will use as reference.
3. You know whether this model will be reusable or case-specific.

To create or select the rules model:
1. In GoalBus, go to **Configuration** > **Staff** > **Shift rules**.
2. Check whether a suitable **rules model** already exists for your case.
3. If it exists, open it and confirm it is still valid.
4. If it does not exist, create a new model by clicking **Add New Model**.
5. Give the model a clear **Name**.
6. If applicable, add a **Description** that identifies its usage.
7. Save the model.
ref: P13_Imagen3.png | compact
8. Confirm you can add rules inside that container.

For the reference case, valid options could be:
- **Shifts - L1**
- **Shift rules**

When you finish this section, you should have a rules model ready to receive specific constraints and penalties.

## Enabling shift rules as constraints or penalties

Now you can start configuring rules. It is important to distinguish two logics:
1. **Constraints**, which are mandatory and block invalid duties.
2. **Penalties**, which do not block, but push the optimizer toward preferred solutions.

This matters because not everything you want in operations should become an absolute prohibition. Some conditions should guide, not wall off.

Before you start this section, make sure that:
1. You created or selected a rules model.
2. You know which work behavior you want to prevent.
3. You know which behavior you want to encourage without making it mandatory.

To manage shift rules for your case:
1. If you want to create a new rule, click **Add New Rule**.
2. Inside the model, review available **rule templates** and give the new rule a **Name** and **Description**.
3. Select the template that matches the control you want to apply.
4. Create a **specific rule** from that template by clicking **Confirm**.
ref: P13_Imagen4.png | compact
6. Decide **which shift types each rule applies to**. Not all rules should apply to all types.
7. Enter the concrete parameters for the rule.
8. Save the rule.
9. Repeat only for the rules your case truly needs.
10. Confirm the rules you need are active. To activate a rule, it must be assigned to at least one shift type.
ref: P13_Imagen5.png | compact

For the reference case, think of examples such as:
1. Morning shifts must start within a specific time window.
2. Split shifts should not exceed a maximum spread.
3. An undesirable sequence can be penalized instead of prohibited.

When you finish this section, you should have an initial set of rules that reflects both mandatory limits and operational preferences.

## Reviewing that rules are assigned to the correct shift types

Once rules are enabled, you need to review **which shift types each rule applies to**. Some rules can be global, others must target specific categories such as morning, afternoon, or split.

Before you continue, make sure that:
1. You enabled at least one rule in the model.
2. You defined the shift types participating in the case.
3. You know whether the rule should be global or specific.

To correctly review the scope:
1. Select each rule you created.
2. Review the **Applicable shift types** section.
3. Select the specific types the rule should apply to.
4. If the rule must affect all types in the scenario, configure it as global by selecting **all shift types**.
5. Confirm there are no two active rules from the same template applied to the same shift type if that would create a logical conflict.
6. Save the configuration.
7. Repeat for each rule in the model.

For the reference case:
1. An early start window can apply only to **Morning shift**.
2. A break rule can apply to several types.
3. A general preference can be global.

When you finish this section, you should have rules with clear scope and no logical conflicts, similar to the following image:
ref: P13_Imagen6.png | full

## Checking the shift logic is still compatible with the service

The last step is to confirm the shift types and rules you defined are still compatible with the validated offer and with the vehicle logic you already closed. There is no value in having “nice” rules if the result leaves the service with no realistic way to be scheduled.

Before you finish, make sure that:
1. You created the needed shift types.
2. You enabled and assigned the relevant rules.
3. You know which service will be the input to the Scheduling scenario.

To validate the case is still calculable:
1. Review the validated service you will use as reference.
2. Confirm the shift types you created can actually organize that work.
3. Review whether any shift rule makes the case too rigid.
4. Confirm there is no strong contradiction with the vehicle rules already enabled.
5. Ask yourself whether the system could build legal, operationally coherent duties with this foundation.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, correct the types or rules before proceeding.

For the reference case, do not proceed until you can state:
1. L1’s validated offer is still compatible with the defined shift types.
2. Rules do not block the case unnecessarily.
3. The model is ready to enter the Scheduling scenario.

When you finish this section, you should be able to state shift logic is sufficiently closed to move on to creating the Scheduling scenario.

## Additional reading

- [Creating the first Scheduling scenario](P14_Creating_the_first_scheduling_scenario.md)

