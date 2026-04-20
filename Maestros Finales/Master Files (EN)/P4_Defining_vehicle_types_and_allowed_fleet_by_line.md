---
title: Defining vehicle types and allowed fleet by line
shortTitle: Fleet by line
intro: 'Learn how to configure vehicle types and line-level allowed-fleet constraints so GoalBus blocks infeasible assignments, respects physical and environmental limits, and prepares a coherent foundation before defining times and services.'
contentType: how-tos
versions:
  - '*'
---

## Defining the allowed vehicle types for a line

Before moving on to travel times, services, or Scheduling rules, you need to make it clear which **vehicle types** can operate each line. In GoalBus, this constraint is not decorative: it works as a safety, compliance, and physical feasibility filter. The goal is to prevent the system from proposing a vehicle that does not fit on a street, violates an environmental restriction, or should not run on that service.

Use this quick start when you already have the network, parkings, and depots prepared and need to close the fleet foundation your case will use before defining times and service supply.

Before you begin, make sure that:
1. You already prepared the master network in P6.
2. You already reviewed the operational network in P7.
3. You already configured parkings and depots in P5.
4. You know which line you will use as the reference case.
5. You understand, at least at a basic level, which physical or environmental constraints affect that line.

For this quick start, use this reference case:

> **I’m going to define which vehicle types can operate line L1 to ensure my first planning work only uses a fleet consistent with the physical and regulatory reality of the service.**

To define the allowed vehicle types for your case:
1. In GoalBus, open the configuration for the **line** you will use as reference.
2. Find the **Allowed vehicle types** section.
3. Check whether the line already has types assigned.
4. If the line already has types defined, confirm they are still correct for your case.
5. If they are not defined yet, first check whether the **vehicle type** you need already exists in the global vehicle configuration.
6. If the type **does exist**, select it as allowed for that line.
7. If the type **does not exist**, exit the line configuration and go to the global **vehicles** configuration to create or complete the vehicle-type catalog first from the **Vehicle Types** panel.
ref: P4_Imagen1.png | full
8. Create the vehicle type you need using a clear business-friendly category, for example:
   1. Minibus
   2. Standard electric
   3. Articulated diesel
ref: P4_Imagen2.png | compact
9. Save the new vehicle type.
ref: P4_Imagen3.png | compact
10. Return to the line configuration.
11. Select the specific vehicle types that are authorized to operate on that line.
ref: P4_Imagen4.png | compact
12. Leave unchecked the types that should not operate that service.
13. Save the configuration.
14. Review the line again and confirm the filter now matches the operational reality.

For the reference case, ask yourself:
1. Can line L1 run a standard bus, a minibus, or both?
2. Is there a vehicle type that must be excluded due to size or environment?
3. If the type you need did not exist, did you create it before trying to assign it to the line?
4. Should the system block a manual assignment if you try to use an unauthorized vehicle?

When you finish this section, you should have a line-level fleet constraint that can serve as a foundation for downstream calculation.

## Linking the line to the allowed depots or parkings

After defining which fleet fits—or does not fit—on the line, you need to review from which physical bases that service can depart. GoalBus lets you define **allowed parkings or depots** per line to force the system to start service from geographically correct locations and reduce deadhead mileage.

Before you start this section, make sure that:
1. You already configured the line’s allowed vehicle types.
2. You already prepared the parkings and depots for the case in P5.
3. You know from which operating base the service should realistically start.

To link the line to its allowed depots or parkings:
1. In the same line configuration, locate the **Allowed parkings** or **Allowed depots** section.
2. Check whether the line already has authorized depots.
3. Select only the depots/garages that are geographically authorized to start services on that line.
4. Exclude bases that do not make operational sense for that corridor.
5. Save the configuration.
6. Confirm the line now has a coherent departure logic from the most reasonable base.

For the reference case, verify that:
1. Line L1 can depart from North Depot.
2. The associated primary parking is the correct one.
3. You are not allowing a distant depot that would force many deadhead kilometers to start the first trip.

When you finish this section, you should have the line, the allowed fleet, and the service’s departure geography aligned.

## Validating the line already has a coherent fleet foundation

Now that you defined the allowed vehicle types and the authorized depots/parkings, you need to do a final validation.

Before you continue, make sure that:
1. The line already has allowed vehicle types.
2. If the needed vehicle type did not exist, it has already been created in the global configuration.
3. The line already has authorized depots or parkings.
4. The configuration reflects the reality of the case you are building.

To validate that the fleet foundation is ready:
1. Review the full line configuration again.
2. Confirm the selected vehicle types represent the fleet that should actually operate the service.
3. Confirm the authorized depots/parkings minimize deadhead mileage.
4. Ask yourself whether the system, with this configuration, would already avoid:
   1. physically impossible assignments,
   2. environmental compliance violations,
   3. departures from geographically inefficient bases.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct the line or create the missing vehicle type before proceeding.

When you finish this section, you should be able to state that the line has a sufficiently mature fleet foundation to support travel times, services, and Scheduling rules.

## Additional reading

- [Defining time versions and travel times](P9_Defining_time_versions_and_travel_times.md)

