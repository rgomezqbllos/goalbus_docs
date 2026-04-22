---
title: Preparing the master network with stops, lines and routes
shortTitle: Master network
intro: Learn how to create and validate the network base that will use your planning,
  including stops, lines, and routes, so that the next steps in times, services, and
  scheduling depart from a coherent structure.
contentType: how-tos
versions:
- '*'
---
## Creating or validating the stops your network will use

Before creating lines or routes, you need to make sure that the **stops** that you will use already exist and are correctly defined. In GoalBus, a stop is not just a geographic point. It is also an entity with operational identity and multiple name layers that serve different audiences, such as planners, passengers and internal devices. In addition, the system allows you to disable stops rather than remove them abruptly, so as not to break active routes or trips.

Use this quick start when you have already closed the time base in P2 and P3, and you need to start building the base network on which you will then define routes, travel times and services.

Before you start, make sure that:

1. You've already set up the types of holidays and days in P2.
2. You've already validated the operating year on P3.
3. You have access to the environment with permissions to consult or edit network infrastructure.
4. You're clear what line or corridor you want to prepare as a first case.

For this quick start, use this reference case:

> **I will prepare line L1, create or validate your base stops and list your back and forth routes for later use in my first case of Scheduling.**

To create or validate the stops of your case:

1. In GoalBus, go to the **Stop Settings** module within the service settings.
ref: P6_Imagen1.png
2. Find out if the base stops on your case already exist.
3. If a stop already exists, open it and confirm that your identity is correct.
4. If a stop does not exist, click **New Stop**.
5. Enter or validate these fields:
   1. **Code** as a unique identifier.
   2. **Trade name** as a visible passenger name.
   3. **Long name** as an internal descriptive reference.
   4. **Short name** if you need it for compact views.
6. Define the location of the stop by coordinates or direction.
7. Add an **External ID** if you want an extra identifier.
8. Save the stop.
ref: P6_Imagen2.png | compact(20x)
9. Repeat the process until you have the minimum stops necessary for your case.
10. If you detect an old stop that should not continue to be used in new planning, switch it to **Inactive** instead of deleting it.

For the reference case, use a logic like this:

1. North Terminal
2. Centre
3. Hospital
4. University
5. South Terminal

When you finish this section, you should have the base stops ready and in a consistent state to build the line and routes.

## Creating or validating the line as an operating container

After you have the base stops, you need to check the **line**. In GoalBus, a line is more than just a service number. It is an operating logic container. By properly configuring it, you define physical and logistical limits of the service, such as the type of fleet allowed or the operational geography of deposits and parkings that will then influence optimization.

Before starting this section, make sure that:

1. You've already checked or created the base stops on your case.
2. You know what service you want to represent.
3. You are clear that the line is the administrative container and not yet the detailed physical path.

To create or validate your case line:

1. In GoalBus, go to the **Network Settings** module.
ref: P6_Imagen3.png
2. See if the line you need already exists.
3. If the line already exists, open it and check its settings.
4. If it does not exist, create a new line by clicking on **Create Line**.
5. Defines or validates:
   1. **Name of the Line** for internal name.
   2. **Short name** for compact views.
   3. **Trade name**, if applicable.
   4. **Parking** associated with the line. **EYE: the previous creation of Parkings is necessary.**
   5. **Vehicle types** to associate the types of vehicles available for the line. **EYE: Pre-creation of vehicle types is necessary.**
   6. **External ID** to add an extra identifier.
   7. **Colour** to assign a certain color to the line.
6. Check that the line really represents the right service.
7. Save the line.
ref: P6_Imagen4.png | compact(8.5x)8. Confirma que la línea ya puede usarse como contenedor para crear rutas específicas.

For the reference case, you can think of a line like:

- **L1**
- **L1: North Terminal - South Terminal**

When you finish this section, you should have a clear and usable line over which you can then define paths by meaning.

## Creating or validating the back and forth routes

With the line already ready, you can now work with the **routes**. In GoalBus, a route is the real physical path that travels a vehicle. The same line can have several valid routes, for example short turns, detours or warehouse entrances. The system organizes these variations by direction or sense, and protects routes “in use” to avoid dangerous changes in already active services.

Before starting this section, make sure that:

1. You already have the line created or validated.
2. You already have the base stops you'll use in the sequence.
3. You know if you're going to create a single path by meaning or if your case already needs variants.

To create or validate the routes of your case:

1. In the main line table, click on the line you just created or validated to access the path view.
ref: P6_Imagen5.png
2. Use the tabs or steering controls to work with **Sentido 1** and **Sentido 2**.
3. Check if there is already a suitable path for the sense you need.
4. If the route does not exist, create a new route variation for that sense.
5. Defines the sequence of stops in the correct order.
6. Confirms the start header and end header.
7. Save the route.
8. Repeat the logic for the opposite sense.
9. If you find a path marked as **In use**, do not attempt to alter its basic geometry without first checking whether there is an unlocked alternative.


For the reference case:
1. Defines the one-way route:
   1. North Terminal
   2. Centre
   3. Hospital
   4. University
   5. South Terminal
2. Defines the path back:
   1. South Terminal
   2. University
   3. Centre
   4. North Terminal

When you finish this section, you should have a line with its main routes by direction, ready for you to review sequences, relevant points and operational logic in the next quick start.

## Additional readings

- [Reviewing operational network: sequences, stop permissions and relay points]
