---
title: Preparing parkings and depots for operations
shortTitle: Parkings and depots
intro: 'Learn how to configure parkings and depots coherently so Scheduling can use realistic physical infrastructure, minimize deadhead mileage, and respect the correct data hierarchy.'
contentType: how-tos
versions:
  - '*'
---

## Configuring the depot as the operational and relief structure

Before creating the parking, you need to review the **depot**. In GoalBus, the depot is the organization’s operating base and the mandatory link for vehicles and drivers. Its configuration not only identifies the unit, but also defines where shifts can start or end, including authorized terminals that enable efficient reliefs and reduce deadhead mileage.

Before you start this section, make sure that:
1. You know which depot is responsible for the line or service you are preparing.
2. You understand the depot is the primary entity and the parking depends on it.

To create or validate the depot for your case:
1. In GoalBus, open the **depots** module.
ref: P5_Imagen3.png | full
2. Check whether the depot you need already exists.
3. If the depot already exists, open it and review its configuration.
4. If it does not exist, create a new one.
ref: P5_Imagen4.png | compact
5. Define or validate these fields:
   1. **Code** as the unique identifier.
   2. **Short name** for compact views.
   3. **Participation percentage %** as the depot’s share of total operations. Across all depots, the total should sum to 100%.
   4. **Long name** as the depot’s primary name.
   5. **External ID**, if the customer works with ERP or HR integrations.
6. Add the **authorized start and end stops**, such as terminals where reliefs or shift endings are allowed.
7. Save the depot.
ref: P5_Imagen5.png | compact
8. Confirm the depot can now operationally support the case you are building.

For the reference case, verify that:
1. North Depot is the correct organizational depot.
2. The relevant terminals for line L1 are authorized as start or end locations when applicable.

When you finish this section, you should have a depot correctly identified and linked to its authorized operational locations.

## Configuring the parking as a physical node in the network

After defining the depot—and before moving on to deadhead trips, fleet, or Scheduling rules—you need to configure the **parking** that will support your case. In GoalBus, a parking is not just an administrative label. It is a geolocated physical node in the network, and when you create it the system automatically generates an associated stop at those coordinates so the engine can calculate distances and entry/exit times coherently. Also, each parking must be linked to an organizational depot.

Use this quick start when you already created the base network and need to connect it to real physical infrastructure before continuing with repositioning and Scheduling.

Before you begin, make sure that:
1. You already prepared stops, lines, and routes in P6.
2. You already reviewed the operational network in P7.
3. You know which line or service you will use as the reference case.
4. You know from which physical base that operation should depart.
5. You already configured the operational depot(s).

For this quick start, use this reference case:

> **I’m going to prepare the North Depot parking and validate that its relationship with the depot and with line L1 is coherent before continuing with deadhead trips and Scheduling.**

To create or validate the parking for your case:
1. In GoalBus, open the **parkings** module within the network infrastructure.
ref: P5_Imagen1.png | full
2. Check whether the parking you need already exists.
3. If the parking already exists, open it and review its configuration.
4. If the parking does not exist, create a new one.
ref: P5_Imagen2.png | compact
5. Define or validate these fields:
   1. **Code** as a short identifier for compact views.
   2. **Short name** for compact views.
   3. **Long name** as the descriptive name of the garage or yard.
   4. **Coordinates** to place the parking correctly on the map.
   5. **External ID**, if the customer works with ERP or HR integrations.
6. Confirm the parking is linked to the correct **depot** created previously.
ref: P5_Imagen6.png | compact
7. Click **Next** to configure parking capacity and allowed vehicle types. This can be edited later as conditions change.
ref: P5_Imagen7.png | compact
8. Visually check on the map that its location makes sense for real operations.
9. Confirm the system can already treat that parking as a logistical origin or destination for operations.

When you finish this section, you should have a properly geolocated parking correctly subordinated to the right depot.

## Validating consistency between parking, depot, and line

Now that you have configured the parking and depot, you need to verify this infrastructure fits the line logic and the logistical efficiency GoalBus expects. The line model itself allows defining **allowed parkings or depots** to force the system to start service from geographically correct bases and minimize deadhead mileage. This is not a cosmetic preference: it directly guides the scheduler when building solutions.

Before you continue, make sure that:
1. The parking is already linked to the correct depot.
2. The depot already has its authorized locations.
3. The line you will use in your case already exists and is validated.

To validate full infrastructure consistency:
1. Open the configuration for the **line** you will use as reference.
2. Review the **allowed parkings** or **allowed depots** section.
3. Confirm the correct depot is authorized to start services for that line.
4. If the correct depot is not authorized, add it.
5. Confirm you are not leaving enabled depots that make no geographic sense for that line.
6. Review whether the relationship between line, depot, and parking minimizes non-revenue driving.
7. Confirm the physical infrastructure you just prepared could support the service you will create or calculate later.
8. If you detect inconsistencies, correct them before proceeding.

For the reference case, ask yourself:
1. Is line L1 authorized to depart from North Depot?
2. Does that depot use North Parking as its physical base?
3. Does the resulting logic reduce deadhead kilometers instead of increasing them?

When you finish this section, you should be able to state that the line, the depot, and the parking form a single operational and logistical logic.

## Additional reading

- [Loading deadhead trips and repositioning](P8_Loading_deadhead_trips_and_repositioning.md)

