---
title: Loading deadhead trips and repositioning
shortTitle: Deadhead trips
intro: "Learn how to configure deadhead-trip matrices and driver repositioning so GoalBus uses real logistics times, minimizes non-productive costs, and builds more realistic timetables and shifts."
contentType: how-tos
versions:
  - "*"
---

## Creating the right matrix for the correct day type

Before calculating Scheduling, you need to define how operations move physically when they are not generating revenue. In GoalBus, this module covers two different things:

1. **Deadhead trips**, which represent a bus with a driver moving between the depot, the parking, the start of a line, or between lines.
2. **Driver repositioning**, which represents the driver moving without a vehicle, for example on foot, by taxi, or by shuttle.

GoalBus does not treat these movements as a single fixed list. The tool makes it clear they must be organized into **matrices by day type**, because traffic changes by operating context. A connection can take 15 minutes on a Sunday and 45 minutes on a Monday morning, so the same link should not always reuse the same time.

Use this quick start when you have already configured parkings and depots and need to prepare the “invisible logistics” that makes realistic planning possible.

Before you begin, make sure that:
1. You already prepared parkings and depots in P5.
2. You know which line or service you will use as reference.
3. You know which day type you are modeling.
4. You understand the difference between a deadhead trip and driver repositioning.

For this quick start, use this reference case:

> **I’m going to prepare the deadhead-trip matrix for a workday on line L1, connecting North Parking to North Terminal, and also the driver-repositioning matrix when needed for reliefs.**

To create the right matrix for your case:
1. In GoalBus, open the **deadhead trips and repositioning** module.
ref: P8_Imagen1.png | full
2. First decide whether you will create a **deadhead trips** matrix, a **driver repositioning** matrix, or both.
3. Click **Create new**.
ref: P8_Imagen2.png | compact
4. Enter a clear **name** for the matrix.
5. Add a **description** that helps you recognize the operating context.
6. Assign the **day types** this matrix will apply to.
7. Save the matrix.
ref: P8_Imagen3.png | compact
8. Confirm the matrix is clearly tied to the correct context and not to generic logic.

For the reference case, valid matrix names could be:
- **Deadheads - January 2026**
- **Driver repositioning - Workdays**

When you finish this section, you should have a matrix created and linked to the appropriate day type.

## Loading connections via bulk import or manual editing

Once the matrix is created, you need to fill it with the real connections between origins and destinations. GoalBus supports two working modes:

1. **Bulk CSV import**, recommended for large networks.
2. **Manual entry**, useful for small cases or for point adjustments.

Before you start this section, make sure that:
1. You already created the correct matrix.
2. You already identified the relevant origins and destinations.
3. You know whether your case can be loaded manually or if bulk import is better.

To load data via bulk import:
1. Prepare a CSV file with GoalBus’ standard format.
2. Make sure you include at least:
   1. Origins
   2. Destinations
   3. Distances
   4. Time bands, when applicable
   5. Durations
3. In GoalBus, select the **upload/import** option.
ref: P8_Imagen4.png | compact
4. Choose the CSV file.
5. Review the system’s **pre-validation**.
6. Check whether the system:
   1. detects errors,
   2. indicates how many records will be created.
ref: P8_Imagen5.png |compact
7. If validation is correct, confirm the upload.
8. Verify the grid is filled with the expected records.

If everything is correct, the matrix will look similar to the following image:
ref: P8_Imagen6.png |full

To load data manually:
1. Open the matrix grid.
2. Add a new record by clicking **New relation**.
ref: P8_Imagen7.png | compact
3. Set the **origin**.
4. Set the **destination**.
5. Enter the corresponding time or distance.
6. If applicable, set the time band.
ref: P8_Imagen8.png | compact
7. Save the record.
8. Repeat until you complete the minimum connections needed for your case.

For the reference case, start with connections such as:
1. North Parking → North Terminal
2. South Terminal → North Parking

When you finish this section, you should have a matrix with real connections, either imported or entered manually.

## Distinguishing deadhead trips from driver repositioning

Now you need to make sure you are not mixing two different logics. GoalBus treats **deadhead trips** and **driver repositioning** similarly in configuration, but with a different business purpose:

1. Deadhead trips use **bus + driver** and model the logistics of moving a vehicle where it is needed.
2. Repositioning uses **driver only** and models the time a person needs to reach a relief point or start point without moving fleet.

Before you continue, make sure that:
1. You already loaded at least the essential connections for your case.
2. You can identify whether each connection corresponds to a vehicle or only to a person.
3. You did not place both logics in the wrong matrix.

To validate that each matrix represents the correct resource:
1. Review a **deadhead trip** connection and confirm it represents:
   1. moving a vehicle from a depot/parking to a line, or
   2. moving a vehicle between lines.
2. Review a **repositioning** connection and confirm it represents:
   1. moving a driver without a vehicle, or
   2. enabling a relief at a terminal.
3. Confirm the deadhead matrix models traffic-dependent times.
4. Confirm the driver-repositioning matrix reflects the real mode of travel (walk, taxi, shuttle).
5. Fix any misplaced connection before proceeding.

For the reference case, ask yourself:
1. Am I modeling a bus leaving the parking, or only a driver going to a terminal?
2. Does the time reflect real traffic, or the driver’s travel mode?
3. Would the engine use this information correctly when building the timetable and shifts?

When you finish this section, you should clearly understand which part of the configuration belongs to vehicle logistics and which belongs to driver logistics.

## Checking the matrix is ready for Scheduling

The final goal of this quick start is not only to fill a table, but to prepare a logistics foundation Scheduling can consume. A precise model improves:

1. **cost transparency**,
2. **realistic shift creation**,
3. **optimization accuracy**.

Before you finish, make sure that:
1. The correct matrix exists.
2. It is linked to the correct day type.
3. The minimum case connections are loaded.
4. You separated deadhead trips from driver repositioning.

To validate the matrix is ready for the next step:
1. Review the reference case you are building.
2. Confirm GoalBus already knows:
   1. where the vehicle departs physically from,
   2. where it enters the line,
   3. how it returns when needed,
   4. and how a driver would move for a relief if applicable.
3. Ask yourself whether the system could already minimize non-productive time and distance in that case.
4. If the answer is yes, continue with the next quick start.
5. If the answer is no, go back and add or correct connections before proceeding.

When you finish this section, you should be able to state that your logistics foundation is realistic enough to support times, services, and Scheduling.

## Additional reading

- [Defining vehicle types and allowed fleet by line](P4_Defining_vehicle_types_and_allowed_fleet_by_line.md)

