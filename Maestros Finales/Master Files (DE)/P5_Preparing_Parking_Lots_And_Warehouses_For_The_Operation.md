---
title: Preparing parking lots and warehouses for the operation
shortTitle: Car parks and warehouses
intro: Learn how to set up parking spaces and warehouses consistently so that Scheduling
  can use a realistic physical infrastructure, minimize empty mileage, and respect
  the correct data hierarchy.
contentType: how-tos
versions:
- '*'
---
## Configuring the deposit as operational and relay structure

Before creating the parking, you need to check the **deposit**. In GoalBus, the deposit is the operating base of the organization and is the mandatory link for vehicles and drivers. In addition, its configuration not only serves to identify the unit, but also to define where the shifts can start or end, including authorized headers or terminals that allow efficient relays and reduce vacuum mileage.

Before starting this section, make sure that:
1. You know which deposit is responsible for the line or service you're preparing.
2. You understand that the deposit is the main entity and that the parking depends on it.
3. You've already created all the types of vehicles needed for the operation.

To create or validate your case deposit:
1. In GoalBus, open the **deposits** module.
ref: P5_Imagen3.png | full
2. See if the deposit you need already exists.
3. If the deposit already exists, open it and check its settings.
4. If it doesn't exist, create a new one.
ref: P5_Imagen4.png | compact(2x)
5. Defines or validates these fields:
   1. **Code** as a unique identifier.
   2. **Short name** for compact views.
   3. **Share %** as a deposit share in total operations. Among all deposits must add 100%.
   4. **Long name** as the main name of the deposit.
   5. **External ID**, if the client works with ERP or HR integrations.
6. Add the **Authorised start and end stops** as headers or terminals where relays or end of shift are allowed.
7. Save the deposit.
ref: P5_Imagen5.png | compact(8.5x)
8. Confirms that the deposit can already operationally sustain the case you've been building.

For the reference case, check that:
1. The North Deposit is the correct organisational deposit.
2. Relevant L1 headers or terminals are authorized as start or end locations when applying.

When you finish this section, you should have a correctly identified deposit linked to your authorized operating locations.

## Configuring the parking as a physical node of the network

After you have defined the deposit and before going on empty trips, fleet or Scheduling rules, you need to leave the **parking** well configured that will hold your case. In GoalBus, a parking lot is not just an administrative tag. It is a geolocated physical node of the network, and when you create it the system automatically generates an associated stop at those coordinates so that the engine can calculate distances, input times and output times consistently. Furthermore, each parking must be linked to an organisational deposit.

Use this quick start when you have already created the base network and need to connect that network to the actual physical infrastructure before moving on and Scheduling.

Before you start, make sure that:
1. You're clear what line or service you're going to use as a reference case.
2. You know from what physical basis that operation should come out.
3. You've already set up the operating deposits.
4. You've already created all the necessary types of vehicles.

For this quick start, use this reference case:

> **I'm going to prepare the North Depot parking lot and validate that your relationship with the deposit and line L1 is consistent before continuing with empty trips and Scheduling.**

To create or validate your case parking:
1. In GoalBus, open the **parking lots** or **parking lots** module within the network infrastructure.
ref: P5_Imagen1.png | full
2. See if the parking you need already exists.
3. If the parking already exists, open it and check its configuration.
4. If the parking doesn't exist, create a new one.
ref: P5_Imagen2.png | compact(2x)
5. Defines or validates these fields:
   1. **Code** as a short identifier for compact views.
   2. **Short name** for compact views.
   3. **Long name** as a descriptive name of the garage or patio.
   4. **Coordinates** to correctly locate the parking on the map.
   5. **External ID**, if the client works with ERP or HR integrations.
6. Check that the parking is linked to the correct **deposit** previously created.
ref: P5_Imagen6.png | compact(8.5x)
7. Click **Next** to configure the parking capacity and vehicle types allowed. This can be edited in the future as conditions change.
ref: P5_Imagen7.png | compact(8.5x)
8. Visually check the map that your location makes sense for the actual operation.
9. Confirms that the system can already treat that parking as the source or logistical destination of the operation.

When you finish this section, you should have a properly geo-localized and properly subordinated parking space to the proper warehouse.

## Validating the consistency between parking, deposit and line

Now that you have already set up parking and storage, you need to check that this infrastructure fits the line logic and logistical efficiency that GoalBus expects. The line model itself allows you to define **permitted parking lots or warehouses** to force the system to start service from the geographically correct bases and minimize empty mileage. This is not a cosmetic preference: guide the programmer directly when building solutions.

Before continuing, make sure that:
1. The parking is already linked to the correct deposit.
2. The warehouse already has its authorized locations.

To validate the complete coherence of the infrastructure (if you already have a line):
1. Open the **line** configuration that you will use as a reference.
2. Check the **permitted parking spaces** or **permitted deposits** section.
3. Check that the correct deposit is authorized to start services on that line.
4. If the correct deposit is not authorized, add it.
5. Confirm that you are not leaving enabled deposits that have no geographical meaning for that line.
6. Check whether the relationship between line, deposit and parking minimizes driving without income.
7. Confirm that the physical infrastructure you have just prepared could support the service you will create or calculate later.
8. If you detect inconsistencies, correct them before continuing.

For the reference case, ask yourself:
1. Is line L1 authorized to leave from the North Depot?
2. Does that warehouse use the North Parking as its physical base?
3. Does the resulting logic reduce miles in a vacuum rather than increase them?

When you finish this section, you should be able to say that the line, the deposit and the parking form the same operational and logistical logic.

## Additional readings

- [Master network](P6_Preparing_The_Master_Network_With_Stops_Lines_And_Routes.md)
