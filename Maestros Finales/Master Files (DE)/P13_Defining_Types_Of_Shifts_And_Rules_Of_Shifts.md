---
title: Defining types of shifts and rules of shifts
shortTitle: Types and rules
intro: Learn how to create shift types, organize them within rule models, and activate
  the restrictions or sanctions needed for Scheduling to build legally valid and operationally
  coherent tasks.
contentType: how-tos
versions:
- '*'
---
## Creating the types of shifts that will structure the work

Before you set up shift rules, you need to define the **types of shifts** that the system will use to group trips into coherent human work. A shift type is not just a visual tag. It is the logical category that guides the engine to build recognizable and usable tasks later on in lists, daily operation and integration with other systems.

Use this quick start when you already have a validated offer, a defined vehicle logic, and you need to tell the system what forms of work are valid for your case.

Before you start, make sure that:
1. You've already created and validated the service offer at P10.
2. You've already validated the operating structure in P11.
3. You've already defined the vehicle rules in P12.
4. You're clear what service and operating context you'll use as a reference.

For this quick start, use this reference case:

> **I'm going to define the shift types of line L1 so that Scheduling can build coherent tasks before creating the calculation scenario.**

To create the shift types of your case:
1. In GoalBus, go to **Settings** > **Staff** > **Types of shifts**.
ref: P13_Imagen1.png | compact
2. Check if there are already appropriate types of shifts for your case.
3. If the type already exists, open it and check if it is still valid.
4. If it doesn't exist, create a new one.
5. Defines these fields:
   1. **Full name**, with a clear and descriptive name.
   2. **Short name**, for compact views and operating cards.
   3. **External ID**, if the client needs integration with HR systems or payroll.
ref: P13_Imagen2.png | compact
6. Marks the type as **Assets** if you must participate in future calculations.
7. Save the shift guy.
8. Repeat the process for every category of work you really need in your case.

For the reference case, you could create types like:
1. **Turn tomorrow**
2. **Late turn**
3. **Broken turn**, if operation requires

When you finish this section, you should have the types of shifts that will serve as “DNA” of the tasks that Scheduling will build.

## Creating or selecting the turn rule model

After creating the shift types, you need to define the container where the rules will live. Turn rules are not managed as a flat list, but within **models** that group a coherent set of restrictions for a stage, a period, or a concrete simulation. That allows you to maintain several configurations without mixing historical rules with active rules.

Before starting this section, make sure that:
1. You've already created or validated the types of shifts you'll use.
2. You know what service or simulation you will use as a reference.
3. You're already clear whether this model will be reusable or case-specific.

To create or select the rule model:
1. In GoalBus, go to **Settings** > **Staff** > **Rules of shift**.
2. Check if an **model rules** suitable for your case already exists.
3. If the model already exists, open it and check if it is still valid.
4. If it does not exist, create a new model by clicking on **Add New Model**.
5. Assigns a clear **Name** to the model.
6. If applicable, add an **Description** that identifies its use.
7. Save the model.
ref: P13_Imagen3.png | compact
8. Confirm that you can already add rules inside that container.

For the reference case, a valid option could be:
- **Turns - L1**
- **Rules of shift**

When you finish this section, you should have a model of rules prepared to receive specific restrictions and sanctions.

## Activate turn rules such as restrictions or sanctions

Now you can start setting the rules. Here it is important to distinguish two logics:
1. **Restrictions**, which are mandatory and block invalid tasks.
2. **Penalties**, which do not block, but push the optimizer towards preferred solutions.

This difference is key because not everything you want in the operation must become an absolute ban. Some conditions must act as a guide and not as a wall.

Before starting this section, make sure that:
1. You already have a model of rules created or selected.
2. You know what work behavior you want to stop.
3. You know what behavior you want to favor without making it mandatory.

To manage the turn rules of your case:
1. If you want to create a new rule, tap **Add New Rule**.
2. Within the rule model, check the available **Rules templates** and give an **Name** and an **Description** to the new rule.
3. Select the template that corresponds to the control you want to apply.
4. Create an **specific rule** from that template by clicking on **Confirm**.
ref: P13_Imagen4.png | compact
6. Decide **to which types of shifts each rule applies**. Not all rules should apply to all types. Some may be global and others should address specific categories, such as tomorrow, afternoon or match.
7. Enter the specific parameters of the rule.
8. Keep the rule.
9. Repeat the process only for the rules that your case really needs.
10. Check whether the rules you need to apply are active or not. To prun a rule, it must have been assigned to at least one type of turn.
ref: P13_Imagen5.png | compact(x19)

For the reference case, think of examples such as:
1. Tomorrow's shift should start inside a specific window.
2. A split turn should not exceed a certain level of amplitude.
3. An undesirable sequence can be penalized rather than prohibited.

When you finish this section, you should have an initial set of rules that reflect both mandatory limits and operational preferences.

## Checking that the rules are assigned to the correct shift type

Once the rules have been activated, you need to check **to which types of shifts are applied each**. Not all rules should apply to all types. Some may be global and others should be directed to specific categories, such as tomorrow, late or match.

Before continuing, make sure that:
1. You've already activated at least one rule within the model.
2. You've already defined the types of shifts involved in the case.
3. You know if the rule should be global or specific.

To properly review the scope of application:
1. Select each rule you've created.
2. Check the **Types of shifts applicable** section.
3. Select the specific types to which the rule should apply.
4. If the rule must affect all types of the scenario, set it as global by selecting **all types of shift**.
5. Check that there are no two active rules of the same template applying to the same type of shift if that would generate a logical conflict.
6. Save the settings.
7. Repeat the revision for each model rule.

For the reference case:
1. An early start window can only be applied to **Turn tomorrow**.
2. A rest rule can be applied to several types.
3. A general preference could be global.

When you finish this section, you should have rules with a clear scope and no logical conflicts with each other similar to the following image:
ref: P13_Imagen6.png | compact(x19)

## Checking that the shift logic remains compatible with the service

The last step is to check that the types of shifts and the rules you have just defined are still compatible with the validated offer and with the logic of vehicles you have already closed. It is not helpful to have “good” rules if the result leaves the service without a realistic way to be programmed.

Before you finish, make sure that:
1. You've already created the kinds of shifts you need.
2. You've already activated and assigned the corresponding rules.
3. You're clear what service the entrance to the Scheduling stage will be.

To validate that the case is still workable:
1. Check the validated service you will use as a reference.
2. Check that the types of shifts you created can arrange that work.
3. Check if any shift rules leave the case too rigid.
4. Checks that there is no strong contradiction with the vehicle rules already activated.
5. Ask yourself if the system could already build tasks legally and operationally consistent with this base.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, correct the types or rules before following.

For the reference case, do not continue until you can state:
1. The validated L1 offer remains compatible with the defined shift types.
2. Rules don't unnecessarily block the case.
3. The model is already ready to enter the stage of Scheduling.

By the time you finish this section, you should be able to say that the logic of shifts is already closed enough to move on to the creation of the Scheduling scenario.

## Additional readings

- [Creating the first stage of Scheduling](P14_Creating_The_First_Stage_Of_Scheduling_With_The_Classic_Engine.md)
