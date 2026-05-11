---
title: Creating the first stage of Scheduling with the Classic engine
shortTitle: Classic stage
intro: Learn how to create your first Scheduling scenario with the GoalBus Classic
  engine, correctly select the calculus entries and distinguish when to apply vehicle
  rules and when to apply shift rules.
contentType: how-tos
versions:
- '*'
---
## Creating the scenario with the validated offer as a starting point

Now that you already have the validated offer, vehicle logic and turn logic, the next step is to create the **Scheduling stage** that will use that base to calculate an executable solution.

This scenario is the controlled environment where you're going to combine:
1. the **validated offer**,
2. the **empty travel matrix**,
3. the **model of vehicle rules**,
4. and the **model of shift rules**.

Use this quick start when you already have the base parameterization closed and want to prepare the definitive scenario for calculation with the Classic engine.

Before you start, make sure that:
1. You have already configured and validated the service offer in P10.
2. You've already checked the operating structure at P11.
3. You've already defined the vehicle rules in P12.
4. You've already defined the types of shifts and the rules of shifts in P13.
5. You've already prepared the empty travel matrix for P7.
6. You know what kind of day and which lines will be part of the calculation.

For this quick start, use this reference case:

> **I will create the first scenario of Schedule for line L1, using the validated workable offer, the corresponding empty travel matrix and the correct models of vehicle and shift rules, to launch the final calculation with GoalBus Classic.**

To create the basic scenario of your case:
1. In GoalBus, open the **Planning** module.
ref: P14_Imagen1.png | compact
2. Click **New scenario**.
ref: P14_Imagen2.png | compact(2x)
3. Introduces the basic scenario identity:
   1. **Name**
   2. **Type of day**
   3. **Description** if you want to give more detail.
   4. **only for vehicles** scenario or not.
ref: P14_Imagen3.png | compact(x10)
4. Select the basic elements of the scenario:
   1. The **validated commercial service** you want to cover.
   2. Select the **Model of Turn Rules**.
   3. Select the **Model of Vehicle Type Rules** (optional).
   4. Select the **empty travel matrix** corresponding to the same day type.
   5. Select the **driver displacement matrix** that will be part of the stage.
ref: P14_Imagen4.png | compact(x10)
5. Select the line.
ref: P14_Imagen5.png | compact(x12)
6. Saves or completes the creation of the stage.
7. Check that the scenario appears in the main planning table.

For the reference case, a valid option could be:
- **Scheduling Classic - L1 workable**

When you finish this section, you should have a scenario created with its correct logistics and commercial inputs created as in the following image:
ref: P14_Imagen6.png | full

## Understanding when to use vehicle rules and when to use shift rules

Before setting up the engine, you need to make clear an important distinction: **Vehicle rules and shift rules don't solve the same problem.**.

Use **vehicle rules** when you want to control fleet behavior. These are the right rules if you need to model:
1. physical compatibility of vehicles,
2. capacity or range limits,
3. infrastructure restrictions,
4. or operational policies linked to the use of the fleet.

Use **rules of shift** when you want to control how human work is organized. It's the right rules if you need to model:
1. working hours,
2. breaks and breaks,
3. hours of beginning and ending,
4. amplitude,
5. or differences between types of shift, such as morning, afternoon or night.

Before continuing, make sure that:
1. You know what restrictions belong to the vehicle.
2. You know what restrictions belong to the shift.
3. You're not trying to solve a personnel problem with fleet rules, or the other way around.

To decide which model to use in each case:
1. Ask yourself if the restriction affects **bus** or **driver**.
2. If it affects **bus**, use **model of vehicle rules**.
3. If it affects the **human work** or the shift type, use the **model of shift rules**.
4. If a rule should apply to all types of shifts, review it as a global rule or with the widest scope available.
5. If a rule only applies to a particular type of shift, assign it only to that type.

For the reference case:
1. If you want to limit which fleet can cover the L1, use **vehicle rules**.
2. If you want to control how a shift is built tomorrow or night, use **rules of shift**.
3. If a restriction mixes both, separate it and configure it in the right model.

When you finish this section, you should be clear about which model responds to each need and avoid cross or contradictory configurations.

## Selecting the GoalBus Classic engine for final calculation

Now you need to set up the calculus engine. For this quick start, the focus is to work with **GoalBus Classic** as the main engine of the stage. This is the deep optimization engine aimed at obtaining the best final solution when the parameterization is ripe enough. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Before starting this section, make sure that:
1. You already have the stage created.
2. You have selected service, lines and empty travel matrix correctly.
3. You're already clear about the rule models you're going to use.
4. You're ready for a final or near-final calculation, not just for a quick tactical test.

To select the Classic engine:
1. Open the scenario you just created by pressing on it.
2. On the top bar, click **Calculation Settings**.
ref: P14_Imagen7.png | compact
3. On the side panel, select **GoalBus Classic Engine**.
4. Confirms that the scenario is no longer configured with the machine learning engine.
5. Determines the **Programming flexibility for first solution** (default is 0).
6. Use a prudent value that allows you to find an initial solution without distorting the case.
7. Select the **Maximum calculation time** that the engine will have for new solutions.
ref: P14_Imagen8.png | compact(x8)
8. Save the settings.

The initial flexibility only applies to the GoalBus Classic engine and serves to ensure that the first solution is not blocked if the restrictions are too rigid from the start. The maximum calculation time acts as a delivery guarantee and forces the system to return the best valid solution that it has found within the available time. filetturn34file0L1-L20 filetturn34file2L1-L20

For the reference case:
1. Use **GoalBus Classic** as the main engine.
2. Reserve the machine learning engine only for previous quick validations, not as a final calculation engine.
3. Use moderate initial flexibility if you suspect that restrictions could block the first solution.
4. Defines a realistic maximum time for the team to receive a viable solution within the expected time. fileciteturn34file0L1-L20fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

When you finish this section, you should have the Classic engine configured with a controlled and realistic calculation framework.

## Checking the stage before you launch it.

Before you calculate, you need to do a final review of the entire scenario. The goal is to confirm that you are not entering the calculation with contradictory entries.

Before continuing, make sure that:
1. You've already chosen the correct validated service.
2. You've already selected the empty travel matrix of the right day type.
3. You've already assigned the right models of vehicle and shift rules.
4. You have already selected GoalBus Classic as an engine.
5. You've already adjusted flexibility and maximum time.

To review the scenario before launching the calculation:
1. Check the name and the stage day guy.
2. Confirm that the **commercial service** corresponds exactly to the one you want to program.
3. Confirms that the **empty travel matrix** corresponds to the same time context.
4. Check the **model of vehicle rules** and confirm that it protects fleet logic.
5. Check the **model of shift rules** and confirm that it protects human work logic.
6. Check that you're not skipping a mandatory model for your case.
7. If everything is consistent, leave the scenario ready for calculation.

For the reference case, do not continue until you can state:
1. The working L1 uses its correct validated service.
2. The working matrix is the right one.
3. The vehicle model realistically limits the fleet.
4. The shift model organizes the work in a coherent way.
5. GoalBus Classic is already selected.

When you finish this section, you should have a clean, coherent and ready for final calculation.

## Additional readings

- [Running and Validating Scheduling's First Calculus](P15_Running_And_Validating_Schedulings_First_Calculus.md)
