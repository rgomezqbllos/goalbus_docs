---
title: Defining vehicle types and fleet allowed per line
shortTitle: Fleet per line
intro: Learn how to configure vehicle types and fleet restrictions allowed per line
  so that GoalBus blocks unfeasible assignments, respects physical and environmental
  limits, and prepares a coherent base before defining times and services.
contentType: how-tos
versions:
- '*'
---
## Defining the permitted vehicle types for a line

As a first step, you need to make clear which **vehicle types** can operate each line. In GoalBus, this restriction is not decorative: it acts as a safety, compliance and physical viability filter. The goal is to prevent the system from proposing a vehicle that does not fit on a street, that does not comply with an environmental restriction, or that should not circulate in that service.

Use this quick start when you need to close the fleet base that your case will use before defining times and service offer.

Before you start, make sure that:
1. You're clear what line you'll use as a reference case.
2. You know, at least at the basic level, what physical or environmental restrictions affect that line.

For this quick start, use this reference case:

> **I'm going to define which types of vehicle can operate the L1 line to make sure that my first planning only uses a fleet consistent with the physical and regulatory reality of the service.**

To define the permitted vehicle types of your case:
1. In GoalBus, if any line already exists, open the **line** configuration that you are going to use as a reference.
2. Find the **Types of vehicles allowed** section.
3. Check if the line already has assigned types.
4. If the line already has defined types, it confirms that they are still correct for the case.
5. If they are not yet defined, check first if the **Type of vehicle** you need already exists in the general vehicle configuration.
6. If type **Yes, it does exist.**, select it as allowed for that line.
7. If type **does not exist**, exit the line settings and go to the general **vehicles** settings to create or complete first the type catalog available from the **Vehicle types** panel.
ref: P4_Imagen1.png | full
8. Create the type of vehicle you need using a clear and understandable category for the business, for example:
   1. Minibus
   2. Electrical standard
   3. Articulated diesel
ref: P4_Imagen2.png | compact(2x5)
9. Save the new type of vehicle.
ref: P4_Imagen3.png | compact(x9)
10. Go back to the line settings.
11. Mark the specific vehicle types that are allowed to operate on that line.
ref: P4_Imagen4.png | compact(8x)
12. Leave unmarked the guys who don't have to operate that service.
13. Save the settings.
14. Recheck the line (if any already exists) and confirm that the filter already correctly represents operational reality.

For the reference case, ask yourself:
1. Does line L1 support a standard bus, a minibus or both?
2. Is there a type of vehicle to be excluded by size or environment?
3. If there wasn't the guy you needed, did you create it before you tried to assign it to the line?
4. Should the system block a manual mapping if you try to use an unauthorized vehicle?

When you finish this section, you should have defined a fleet-by-line restriction that already serves as a basis for further calculation.

## Relating the line to the permitted warehouses or parking spaces

After defining which fleet fits or does not fit in the line, you need to check from which physical bases that service can exit. GoalBus allows you to define **permitted parking lots or warehouses** per line to force the system to start service from geographically correct locations and reduce empty mileage.

Before starting this section, make sure that:
1. You've already configured the permitted vehicle types of the line.
2. You know from what operational base the service should really start.

To relate the line to your permitted warehouses or parking:
1. Within the same line configuration, locate the **Parking permitted** or **Permissible deposits** section.
2. Check if the line already has authorized deposits.
3. Select only those warehouses or garages that are geographically authorized to start services on that line.
4. Leave out the bases that don't make operational sense for that broker.
5. Save the settings.
6. Check that the line now has a coherent logic of exit from the most reasonable base.

For the reference case, it finds that:
1. Line L1 can exit from the North Depot.
2. The main associated parking is the right one.
3. You're not allowing a distant deposit that forces you to travel many miles in a vacuum to start the first trip.

When you finish this section, you should have the line (if it already exists), the fleet allowed and the service exit geography aligned.

## Validating that the line already has a coherent fleet base

Now that you have already defined the permitted vehicle types and the authorized warehouses or parking spaces, you need to make a final validation.

Before continuing, make sure that:
1. The line already has vehicle types allowed.
2. If the vehicle type required did not exist, it was previously created in the general configuration.
3. The line already has authorized warehouses or parking.
4. The configuration reflects the reality of the case you're building.

To validate that the fleet base is already ready:
1. Check the complete line configuration again.
2. Confirms that the selected vehicle types represent the fleet that should actually operate that service.
3. Confirms that authorized warehouses or parkings minimize empty mileage.
4. Ask yourself if the system, with this configuration, would already avoid:
   1. physically impossible assignments,
   2. environmental non-compliances,
   3. departures from geographically inefficient bases.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct the line or create the missing vehicle type before continuing.

When you finish this section, you should be able to state that you have all the types of vehicle and fleet necessary for planning your line.

## Additional readings

- [Preparing parking and warehouses](P5_Preparing_Parking_Lots_And_Warehouses_For_The_Operation.md)
