---
title: Defining Vehicle Rules for Scheduling
shortTitle: Vehicle rules
intro: Learn how to set up vehicle rules that will limit which fleet solutions are
  valid in Scheduling, so that the calculation respects operational reality, infrastructure
  and validated offer.
contentType: how-tos
versions:
- '*'
---
## Preparing the base that will use the vehicle rules

Before activating vehicle rules, you need to check that the basis that those rules are going to consume is already ready. Vehicle rules do not replace a previous bad parameterization. Their function is to refine the calculation behavior so that the engine discards unviable or unwanted combinations.

Use this quick start when you already have a validated service offer, a line with allowed fleet and a coherent operating structure, and you need to prepare the case before creating the Scheduling scenario.

Before you start, make sure that:
1. You've already set up the fleet allowed per line on P8.
2. You've already defined the time version and travel times in P9.
3. You've already created and validated the service offer at P10.
4. You've already checked the operating structure and status of the service at P11.
5. You're clear what line and service you'll use as a reference.

For this quick start, use this reference case:

> **I'm going to define the vehicle rules for line L1, so that Scheduling only uses a fleet consistent with infrastructure, validated offer and actual service restrictions.**

To prepare the case base before activating rules:
1. Open the line you will use as a reference.
2. Check which types of vehicle are allowed.
3. Check from which deposit or parking the operation will leave.
4. Confirm that the service you will use as input is already **Validation**.
5. Check that you are not trying to solve with rules a problem that should have been corrected earlier online, fleet or infrastructure.
6. If you detect an inconsistency on that base, correct it before moving on to the rules settings.

When you finish this section, you should be clear about what real case you're trying to protect by vehicle rules.

## Creating or selecting the model of vehicle rules

Once you have checked the base, you need to enter the model or catalogue of vehicle rules. At this point it is not about activating everything. It is about choosing or building a set of restrictions that represents the real logic of the service.

Before starting this section, make sure that:
1. You know what validated service you'll use as a reference.
2. You've already confirmed which types of vehicle are valid for the line.
3. You know what real problems you want to avoid.

To create or select the rule model:
1. In GoalBus see **Settings** > **Vehicles** > **Vehicle type rules**.
ref: P12_Imagen1.png | compact
2. Check if there is already a proper model of rules for your case.
3. If the model already exists, open it and check its configuration.
4. If it does not exist, create a new model of rules.
5. Assigns a clear **name** to the model.
6. If applicable, add an **description** that allows you to distinguish its purpose.
7. Save the model.
ref: P12_Imagen2.png | compact
8. Confirms that the model is already available to add concrete rules.

For the reference case, a valid option could be:
- **Vehicles - L1 workable**
- **Fleet Rules - L1 Workable Service**

When you finish this section, you should have a clear container to set up the vehicle restrictions of the case.

## Activate only the vehicle rules you really need

Now you can start activating rules. Here it is important to keep a clear criterion: a rule must represent a real need for operation, security, infrastructure or compliance. If a rule does not respond to a particular problem, it is not appropriate to activate it yet.

Before starting this section, make sure that:
1. You have already created or selected a model of rules.
2. You know what fleet is valid for the line.
3. You know what combinations should be banned or limited.

To activate the vehicle rules of the case:
1. Within the rule model, check the available rules catalog by clicking on **Add New Rule**.
ref: P12_Imagen3.png
2. Identify which ones respond to the actual needs of your service by selecting the appropriate **template**.
3. Define an **Name** and type an **Description** for each new rule.
4. Activate only the rules you really need for the case.
5. Configure the specific parameters of each rule when applying.
6. Repeat the process to cover the minimum restrictions required.
7. Save the changes.
8. Review the complete model and confirm that it is not very restrictive or too open.

For the reference case, ask yourself:
1. What fleet situations should the system prevent?
2. What combinations would be physically possible but not desirable?
3. What behaviors should be guided by the logic of the deposit, parking or line?

When you finish this section, you should have an initial set of active and consistent vehicle rules similar to the one in the following image:
ref: P12_Imagen4.png | compact(20x)

## Relating rules to line, fleet and infrastructure

After activating the rules, you need to check that they are really aligned with the line and infrastructure that sustains the case. A vehicle rule should not contradict the fleet allowed by line or the geography of warehouses and parking.

Before continuing, make sure that:
1. You've already activated the initial set of rules.
2. You've already checked the permitted vehicle types.
3. You know the physical base from which the operation comes out.

To check the consistency of the rules:
1. Check the line settings again.
2. Confirms that the rules do not contradict permitted vehicle types.
3. Check the relationship with the warehouse and the authorized parking.
4. It proves that the rules reinforce that logic, rather than break it.
5. If a rule makes the service unworkable or contradicts the infrastructure, correct it or disable it.
6. Save the final version of the model.

For the reference case, make sure that:
1. Line L1 can still use the authorized fleet.
2. The North Depot remains a coherent exit for the service.
3. No rule blocks an operation that should be valid according to the already configured base.

When you finish this section, you should have rules aligned with the reality of the service, not with an abstract or generic model.

## Confirming that the validated offer is still calculable

The last step is to check that the vehicle rules you have just activated continue to allow calculation of the validated offer. It is one thing to restrict with criteria, and another is to close the model so much that the service ceases to be viable before even creating the scenario.

Before you finish, make sure that:
1. You've already activated the necessary rules.
2. You've already checked his relationship with line, fleet, and infrastructure.
3. You're clear what service Scheduling's entrance will be.

To validate that the case is still workable:
1. Recheck the validated service you will use as a reference.
2. Check that the line still has access to the fleet it needs.
3. Check whether the activated rules leave at least one reasonable solution for the case.
4. Ask yourself if the system could already create a Scheduling scenario without falling into contradiction.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct the rule model before following.

For the reference case, do not continue until you can state:
1. Line L1 maintains a valid and authorized fleet.
2. The validated workable service remains compatible with the activated rules.
3. The vehicle model is now ready for use within the Scheduling scenario.

When you finish this section, you should be able to say that the logic of vehicles is already closed and is consistent enough to move on to the definition of shift rules and the creation of the scenario.

## Additional readings

- [Defining types of shifts and rules of shifts](P13_Defining_Types_Of_Shifts_And_Rules_Of_Shifts.md)
