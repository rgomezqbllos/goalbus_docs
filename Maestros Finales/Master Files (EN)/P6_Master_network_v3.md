---
title: Preparing the master network with stops, lines, and routes
shortTitle: Master network
intro: "Learn how to create and validate the base network your planning will use—including stops, lines, and routes—so the next steps for times, services, and Scheduling start from a coherent structure."
contentType: how-tos
versions:
  - "*"
---

## Creating or validating the stops your network will use

Before creating lines or routes, you need to make sure the **stops** you will use already exist and are defined correctly. In GoalBus, a stop is not only a geographic point. It is also an operational entity with multiple naming layers for different audiences such as planners, passengers, and internal devices. In addition, the system allows you to deactivate stops instead of deleting them abruptly, so you do not break active routes or trips.

Use this quick start when you already closed the time foundation in P2 and P3 and need to start building the base network on which you will later define routes, travel times, and services.

Before you begin, make sure that:
1. You already configured day types and holidays in P2.
2. You already validated the operational year in P3.
3. You have access to the environment with permissions to view or edit network infrastructure.
4. You know which line or corridor you want to prepare as your first case.

For this quick start, use this reference case:

> **I’m going to prepare line L1, create or validate its base stops, and get its outbound and inbound routes ready to use later in my first Scheduling case.**

To create or validate the stops for your case:
1. In GoalBus, go to the **Stop Configuration** module within service configuration.
ref: P6_Imagen1.png
2. Check whether the base stops for your case already exist.
3. If a stop already exists, open it and confirm its identity is correct.
4. If a stop does not exist, click **New Stop**.
5. Enter or validate these fields:
   1. **Code** as the unique identifier.
   2. **Commercial name** as the passenger-facing name.
   3. **Long name** as the internal descriptive reference.
   4. **Short name** if you need it for compact views.
6. Define the stop location using coordinates or an address.
7. Add an **External ID** if you want an additional identifier.
8. Save the stop.
ref: P6_Imagen2.png | compact
9. Repeat until you have the minimum stops needed for your case.
10. If you find an old stop that should no longer be used in new planning, set it to **Inactive** instead of deleting it.

For the reference case, use a logic like:
1. North Terminal
2. Downtown
3. Hospital
4. University
5. South Terminal

When you finish this section, you should have the base stops ready and in a coherent state to build the line and routes.

## Creating or validating the line as an operational container

After you have the base stops, you need to review the **line**. In GoalBus, a line is more than a simple service number. It is an operational logic container. By configuring it correctly, you define physical and logistical boundaries such as allowed fleet types and the depot/parking geography that later influences optimization.

Before you start this section, make sure that:
1. You already reviewed or created the base stops for your case.
2. You know which service you want to represent.
3. You understand the line is the administrative container, not yet the detailed physical path.

To create or validate the line for your case:
1. In GoalBus, go to **Network Configuration**.
ref: P6_Imagen3.png
2. Check whether the line you need already exists.
3. If the line already exists, open it and review its configuration.
4. If it does not exist, create a new line by clicking **Create line**.
5. Define or validate:
   1. **Line name** for internal naming.
   2. **Short name** for compact views.
   3. **Commercial name**, if applicable.
   4. **Parkings** associated with the line. **Note: parkings must be created first.**
   5. **Vehicle types** to associate available vehicle types for the line. **Note: vehicle types must be created first.**
   6. **External ID** to add an additional identifier.
   7. **Color** to assign a specific color to the line.
6. Confirm the line truly represents the correct service.
7. Save the line.
ref: P6_Imagen4.png
8. Confirm the line can now be used as a container to create specific routes.

For the reference case, you can think of a line as:
- **L1**
- **L1: North Terminal - South Terminal**

When you finish this section, you should have a clear, usable line on which you can later define direction-specific routes.

## Creating or validating outbound and inbound routes

With the line ready, you can now work with **routes**. In GoalBus, a route is the real physical path a vehicle travels. A single line may have multiple valid routes, such as short turns, detours, or depot entries. The system organizes these variations by direction and protects routes “in use” to avoid risky changes to already active services.

Before you start this section, make sure that:
1. You already created or validated the line.
2. You already have the base stops to use in sequence.
3. You know whether you will create a single route per direction or whether your case already needs variants.

To create or validate the routes for your case:
1. In the main lines table, click the line you just created or validated to access the routes view.
ref: P6_Imagen5.png
2. Use the direction tabs/controls to work on **Direction 1** and **Direction 2**.
3. Check whether an appropriate route already exists for the direction you need.
4. If the route does not exist, create a new route variation for that direction.
5. Define the stop sequence in the correct order.
6. Confirm the start terminal and end terminal.
7. Save the route.
8. Repeat for the opposite direction.
9. If you find a route marked as **In use**, do not attempt to change its core geometry without first checking whether there is an unlocked alternative.

For the reference case:
1. Define the outbound route:
   1. North Terminal
   2. Downtown
   3. Hospital
   4. University
   5. South Terminal
2. Define the inbound route:
   1. South Terminal
   2. University
   3. Downtown
   4. North Terminal

When you finish this section, you should have a line with its main routes by direction, ready so in the next quick start you can validate sequences, stop permissions, and operational logic in more detail.

## Additional reading

- [Reviewing the operational network with sequences and key points](P7_Reviewing_the_operational_network.md)

