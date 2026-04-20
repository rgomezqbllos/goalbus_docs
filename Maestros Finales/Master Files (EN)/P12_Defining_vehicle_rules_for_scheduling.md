---
title: Defining vehicle rules for Scheduling
shortTitle: Vehicle rules
intro: 'Learn how to configure vehicle rules that limit which fleet solutions are valid in Scheduling, so calculation respects operational reality, infrastructure, and the validated offer.'
contentType: how-tos
versions:
  - '*'
---

## Preparing the foundation vehicle rules will use

Before enabling vehicle rules, you need to confirm the foundation those rules will consume is already ready. Vehicle rules do not replace poor upstream parameterization. Their purpose is to refine calculation behavior so the engine discards infeasible or undesired combinations.

Use this quick start when you already have a validated service offer, a line with allowed fleet, and a coherent operational structure, and you need to prepare the case before creating the Scheduling scenario.

Before you begin, make sure that:
1. You already configured allowed fleet by line in P4.
2. You already defined the time version and travel times in P9.
3. You already created and validated the service offer in P10.
4. You already reviewed operational structure and service status in P11.
5. You know which line and which service you will use as reference.

For this quick start, use this reference case:

> **I’m going to define vehicle rules for line L1 so Scheduling only uses a fleet consistent with infrastructure, the validated offer, and the real constraints of the service.**

To prepare the case foundation before enabling rules:
1. Open the line you will use as reference.
2. Confirm which vehicle types are allowed.
3. Review which depot or parking operations will depart from.
4. Confirm the input service is already **Validated**.
5. Confirm you are not trying to solve with rules a problem that should have been fixed earlier in the line, fleet, or infrastructure.
6. If you detect a foundation inconsistency, fix it before moving to rule configuration.

When you finish this section, you should have a clear picture of the real case you are trying to protect with vehicle rules.

## Creating or selecting the vehicle-rule model

Once the foundation is reviewed, you need to enter the vehicle rules model/catalog. The goal is not to enable everything. The goal is to choose or build a set of constraints that represents the real logic of the service.

Before you start this section, make sure that:
1. You know which validated service you will use as reference.
2. You confirmed which vehicle types are valid for the line.
3. You know which real problems you want to avoid.

To create or select the rules model:
1. In GoalBus go to **Configuration** > **Vehicles** > **Vehicle type rules**.
ref: P12_Imagen1.png | compact
2. Check whether a suitable rules model already exists for your case.
3. If it exists, open it and review its configuration.
4. If it does not exist, create a new rules model.
5. Give the model a clear **name**.
6. If applicable, add a **description** to distinguish its purpose.
7. Save the model.
ref: P12_Imagen2.png | compact
8. Confirm the model is available so you can add concrete rules.

For the reference case, valid options could be:
- **Vehicles - L1 workday**
- **Fleet rules - L1 workday service**

When you finish this section, you should have a clear container to configure the case’s vehicle constraints.

## Enabling only the vehicle rules you actually need

Now you can start enabling rules. Keep a clear criterion: a rule should represent a real need in operations, safety, infrastructure, or compliance. If a rule does not address a concrete problem, it is better not to enable it yet.

Before you start this section, make sure that:
1. You created or selected a rules model.
2. You know which fleet is valid for the line.
3. You know which combinations must be prohibited or limited.

To enable vehicle rules for your case:
1. Inside the rules model, review available rules by clicking **Add New Rule**.
ref: P12_Imagen3.png
2. Identify which ones match real needs in your service by selecting the corresponding **template**.
3. Define a **Name** and write a **Description** for each new rule.
4. Enable only the rules you truly need for the case.
5. Configure each rule’s parameters when applicable.
6. Repeat until you cover the minimum restrictions needed.
7. Save changes.
8. Review the full model and confirm it is neither too restrictive nor too open.

For the reference case, ask yourself:
1. Which fleet situations should the system prevent?
2. Which combinations are physically possible but undesirable?
3. Which behaviors must be guided by depot, parking, or line logic?

When you finish this section, you should have an initial set of active, coherent vehicle rules similar to the following image:
ref: P12_Imagen4.png | compact

## Aligning rules with the line, fleet, and infrastructure

After enabling rules, you need to verify they are aligned with the line and infrastructure supporting the case. A vehicle rule should not contradict allowed fleet by line or the depot/parking geography.

Before you continue, make sure that:
1. You enabled the initial rule set.
2. You reviewed allowed vehicle types.
3. You know the physical base from which operations depart.

To verify rule consistency:
1. Review the line configuration again.
2. Confirm the rules do not contradict allowed vehicle types.
3. Review the relationship with the authorized depot and parking.
4. Confirm the rules reinforce that logic rather than breaking it.
5. If a rule makes the service infeasible or contradicts infrastructure, fix it or disable it.
6. Save the final version of the model.

For the reference case, make sure that:
1. Line L1 can still use the authorized fleet.
2. North Depot is still a coherent departure base.
3. No rule blocks an operation that should be valid based on the foundation you already configured.

When you finish this section, you should have rules aligned with real service conditions, not an abstract model.

## Confirming the validated offer is still calculable

The last step is to confirm the vehicle rules you enabled still allow you to calculate the validated offer. It is one thing to restrict with intent—and another to close the model so much that the service becomes infeasible before you even create the scenario.

Before you finish, make sure that:
1. You enabled the needed rules.
2. You reviewed their relationship to line, fleet, and infrastructure.
3. You know which service will be the Scheduling input.

To validate the case is still calculable:
1. Review the validated service you will use as reference.
2. Confirm the line still has access to the fleet it needs.
3. Review whether the enabled rules leave at least one reasonable solution for the case.
4. Ask yourself whether the system could create a Scheduling scenario without contradictions.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, fix the rules model before proceeding.

For the reference case, do not proceed until you can state:
1. Line L1 maintains valid, authorized fleet.
2. The validated workday service is still compatible with the enabled rules.
3. The vehicle model is ready to be used inside the Scheduling scenario.

When you finish this section, you should be able to state the vehicle logic is closed and consistent enough to move on to shift rules and scenario creation.

## Additional reading

- [Defining shift types and shift rules](P13_Defining_shift_types_and_shift_rules.md)

