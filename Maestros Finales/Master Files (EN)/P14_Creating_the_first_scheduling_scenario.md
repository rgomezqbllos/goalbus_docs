---
title: Creating the first Scheduling scenario with the Classic engine
shortTitle: Classic scenario
intro: 'Learn how to create your first Scheduling scenario with the GoalBus Classic engine, select calculation inputs correctly, and distinguish when to apply vehicle rules versus shift rules.'
contentType: how-tos
versions:
  - '*'
---

## Creating the scenario with the validated offer as the starting point

Now that you have the validated offer, vehicle logic, and shift logic, the next step is to create the **Scheduling scenario** that will use that foundation to calculate an executable solution.

This scenario is the controlled environment where you combine:
1. the **validated offer**,
2. the **deadhead-trip matrix**,
3. the **vehicle rules model**,
4. and the **shift rules model**.

Use this quick start when you have closed the base parameterization and want to prepare the definitive calculation scenario with the Classic engine.

Before you begin, make sure that:
1. You already configured and validated the service offer in P10.
2. You already reviewed operational structure in P11.
3. You already defined vehicle rules in P12.
4. You already defined shift types and shift rules in P13.
5. You already prepared the deadhead-trip matrix in P8.
6. You know which day type and which lines will be part of the calculation.

For this quick start, use this reference case:

> **I’m going to create the first Scheduling scenario for line L1 using the validated workday offer, the corresponding deadhead matrix, and the correct vehicle and shift rules models, to run the final calculation with GoalBus Classic.**

To create the base scenario for your case:
1. In GoalBus, open the **Planning** module.
ref: P14_Imagen1.png | compact
2. Click **New scenario**.
ref: P14_Imagen2.png | compact
3. Enter the basic scenario identity:
   1. **Name**
   2. **Day type**
   3. **Description** (optional)
   4. Scenario **vehicles-only** (or not)
ref: P14_Imagen3.png | compact
4. Select the scenario’s core elements:
   1. The **validated commercial service** you want to cover
   2. The **Shift Rules Model**
   3. The **Vehicle Type Rules Model** (optional)
   4. The **deadhead-trip matrix** that matches the same day type
   5. The **driver repositioning matrix** that will be part of the scenario
ref: P14_Imagen4.png | compact
5. Select the line.
ref: P14_Imagen5.png | compact
6. Save/finish scenario creation.
7. Confirm the scenario appears in the planning main table.

For the reference case, a valid option could be:
- **Scheduling Classic - L1 workday**

When you finish this section, you should have a scenario created with the correct commercial and logistical inputs, similar to the following image:
ref: P14_Imagen6.png | full

## Understanding when to use vehicle rules vs. shift rules

Before configuring the engine, clarify an important distinction: **vehicle rules and shift rules do not solve the same problem**.

Use **vehicle rules** when you want to control fleet behavior. They are the right rules if you need to model:
1. physical vehicle compatibility,
2. capacity or range limits,
3. infrastructure restrictions,
4. operational policies tied to fleet usage.

Use **shift rules** when you want to control how human work is organized. They are the right rules if you need to model:
1. working hours,
2. breaks and rests,
3. start and end times,
4. spread,
5. differences between shift types such as morning, afternoon, or night.

Before you continue, make sure that:
1. You know which constraints belong to the vehicle.
2. You know which constraints belong to the shift.
3. You are not trying to solve a staff problem with fleet rules, or vice versa.

To decide which model to use:
1. Ask whether the constraint affects the **bus** or the **driver**.
2. If it affects the **bus**, use the **vehicle rules model**.
3. If it affects **human work** or the shift type, use the **shift rules model**.
4. If a rule should apply to all shift types, configure it as global or with the broadest available scope.
5. If a rule applies only to a specific shift type, assign it only to that type.

For the reference case:
1. If you want to limit which fleet can cover L1, use **vehicle rules**.
2. If you want to control how a morning or night duty is built, use **shift rules**.
3. If a constraint mixes both, split it and configure it in the correct model.

When you finish this section, you should know which model addresses each need and avoid crossed or contradictory configurations.

## Selecting the GoalBus Classic engine for the final calculation

Now configure the calculation engine. For this quick start, the focus is working with **GoalBus Classic** as the scenario’s main engine. This is the deep optimization engine oriented to obtain the best final solution when parameterization is sufficiently mature.

Before you start this section, make sure that:
1. You already created the scenario.
2. You correctly selected the service, lines, and deadhead-trip matrix.
3. You know which rules models you will use.
4. You are ready for a final (or near-final) calculation, not only a quick tactical test.

To select the Classic engine:
1. Open the scenario you just created.
2. In the top bar, click **Calculation settings**.
ref: P14_Imagen7.png | compact
3. In the side panel, select **GoalBus Classic Engine**.
4. Confirm the scenario is no longer configured with the machine-learning engine.
5. Set **Scheduling flexibility for first solution** (default is 0).
6. Use a prudent value that allows the first solution without distorting the case.
7. Set the **Maximum calculation time** for the engine to search for new solutions.
ref: P14_Imagen8.png | compact
8. Save the configuration.

Initial flexibility only applies to GoalBus Classic and helps the first solution not get blocked if constraints are too rigid at the start. Maximum calculation time acts as a delivery guarantee and forces the system to return the best valid solution it found within the available time window.

For the reference case:
1. Use **GoalBus Classic** as the main engine.
2. Keep the machine-learning engine only for quick pre-validations, not for the final calculation.
3. Use moderate initial flexibility if you suspect restrictions could block the first solution.
4. Set a realistic maximum time so the team receives a viable solution within the expected window.

When you finish this section, you should have the Classic engine configured within a controlled, realistic calculation framework.

## Reviewing the scenario before running it

Before calculating, perform a final review of the full scenario. The goal is to confirm you are not entering calculation with contradictory inputs.

Before you continue, make sure that:
1. You selected the correct validated service.
2. You selected the correct deadhead-trip matrix for the correct day type.
3. You assigned the correct vehicle and shift rules models.
4. You selected GoalBus Classic as the engine.
5. You set flexibility and maximum time.

To review the scenario before running calculation:
1. Review the scenario name and day type.
2. Confirm the **commercial service** matches exactly what you want to schedule.
3. Confirm the **deadhead-trip matrix** matches the same time context.
4. Review the **vehicle rules model** and confirm it protects fleet logic.
5. Review the **shift rules model** and confirm it protects human-work logic.
6. Confirm you are not missing a model required for your case.
7. If everything is coherent, leave the scenario ready for calculation.

For the reference case, do not proceed until you can state:
1. Workday L1 uses the correct validated service.
2. The workday matrix is the correct one.
3. The vehicle model limits fleet realistically.
4. The shift model organizes work coherently.
5. GoalBus Classic is selected.

When you finish this section, you should have a clean, coherent scenario ready for final calculation.

## Additional reading

- [Running and validating the first Scheduling calculation](P15_Running_and_validating_the_first_scheduling_calculation.md)

