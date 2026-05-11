---
title: Loading empty travel and travel
shortTitle: Empty travel
intro: Learn how to set up empty travel and driver travel matrices so that GoalBus
  uses real logistics times, minimizes non-productive costs, and builds more realistic
  schedules and shifts.
contentType: how-tos
versions:
- '*'
---
## Creating the right matrix for the right day type

Before calculating Scheduling, you need to define how the operation moves physically when it is not generating revenue. In GoalBus, this module covers two different things:

1. **Empty travel**, representing the movement of a bus with a driver between the tank, the parking lot, the start of the line or between lines.
2. **Driver displacements**, representing the movement of the driver without a vehicle, e.g. by foot, taxi or shuttle.

GoalBus does not treat these movements as a single and fixed list. The Tool makes it clear that they must be organized in **matrices by type of day**, because traffic changes according to the operating context. A journey can last 15 minutes on a Sunday and 45 minutes on a Monday morning, so the same connection should not always reuse the same time.

Use this quick start when you have already set up parking lots and warehouses, and you need to prepare the invisible logistics that will make realistic planning possible.

Before you start, make sure that:

1. You've already prepared the parking lots and warehouses at P5.
2. You are already clear about the line or service you will use as a reference.
3. You know what kind of day you're modeling.
4. You understand the difference between an empty ride and a driver's ride.

For this quick start, use this reference case:

> **I will prepare the empty travel matrix for a working day of line L1, connecting the North Parking with the North Terminal, and also the driver travel matrix when necessary for relays.**

To create the correct matrix for your case:

1. In GoalBus, open the **Unladen travel and travel** module.
ref: P8_Imagen1.png | full
2. Decide first whether to create an **empty trips** matrix, an **Driver movements** matrix, or both.
3. Click **Create New**.
ref: P8_Imagen2.png | compact(2x5)
4. Enter a clear **name** for the matrix.
5. Add an **description** to allow you to recognize the operating context.
6. Assigns the **types of day** to which that matrix applies.
7. Save the matrix.
ref: P8_Imagen3.png | compact(x8)
8. Check that the matrix is clearly associated with the correct context and not a generic logic.

For the reference case, a valid matrix could be called:

- **Empty - January 2026**
- **Driving displacements - working days**

When you finish this section, you should have a properly created matrix linked to the right day type.

## Loading connections by mass import or manual editing

Once the matrix is created, you need to fill it with the actual connections between origins and destinations. The document indicates that GoalBus allows two forms of work:

1. **Mass import CSV**, recommended for large networks.
2. **Manual input**, useful for small cases or to complete point adjustments.

Before starting this section, make sure that:

1. You've already created the right matrix.
2. You've already identified the relevant origins and destinations.
3. You know if your case can be loaded manually or if a massive import is desirable.

To load data by mass import:

1. Prepare a CSV file with the standard GoalBus format.
2. Make sure you include at least:
   1. Origins
   2. Destinations
   3. Distances
   4. Time slots, when applied.
   5. Durations
3. In GoalBus, select the **load** or **import** option.
ref: P8_Imagen4.png | compact
4. Choose the CSV file.
5. Check the **pre-validation** that makes the system.
6. Check if the system:
   1. detects errors,
   2. indicates how many records will be created.
ref: P8_Imagen5.png |compact
7. If the validation is correct, confirm the load.
8. Check that the grid is filled with the expected records.

If all is correct, the array will be displayed in a similar way to that of the following image:
ref: P8_Imagen6.png |full

To manually load data:

1. Open the grid of the matrix.
2. Add a new record by clicking on **New relationship**.
ref: P8_Imagen7.png | compact
3. Define the **origin**.
4. Define the **destination**.
5. Enter the corresponding time or distance.
6. If applicable, define the time slot.
ref: P8_Imagen8.png | compact(15x)
7. Keep the record.
8. Repeat the process until you complete the minimum connections needed for your case.

For the reference case, start with connections like these:

1. North Parking → North Terminal
2. South Terminal → North Parking

When you finish this section, you should have a matrix with real connections, either loaded by file or manually entered.

## Differentiating empty travel from driver travel

Now you need to check that you are not mixing two different logics. The document highlights that GoalBus treats **empty trips** and **Driver movements** similarly in configuration, but with a different business purpose:

1. The empty journey uses **bus + driver** and models the logistics of moving a vehicle where it is needed.
2. The scroll uses **only driver** and models how long a person needs to reach a relay or starting point without moving fleet.

Before continuing, make sure that:

1. You've already loaded at least the essential connections to your case.
2. You can identify whether each connection corresponds to a vehicle or just one person.
3. You haven't mixed both logics into the same wrong matrix.

To validate that each matrix represents the correct resource:

1. Check a **empty journey** connection and confirm that its logic responds to:
   1. moving a vehicle from a tank or parking lot towards the line; or
   2. move a vehicle between lines.
2. Check a **displacement** connection and confirm that its logic responds to:
   1. moving a driver without a vehicle; or
   2. allow a relay in a terminal or header.
3. Check that the empty travel matrix is modeling traffic-dependent times.
4. Check that the driver travel matrix reflects the actual transfer mode, such as walking, taxi or shuttle.
5. Correct any misplaced connection before continuing.

For the reference case, ask yourself:

1. Am I modeling here a bus leaving the parking lot or just a driver going to a header?
2. Does the time I've set correspond to actual traffic or the driver's mode of travel?
3. Would the engine use this information correctly when constructing the schedule and shifts?

When you finish this section, you should be clear which part of your configuration belongs to the vehicle logistics and which part belongs to the driver's logistics.

## Checking that the matrix is ready for Scheduling

The final goal of this quick start is not only to fill a table, but to prepare a logistics base that Scheduling can consume. The document explains that a precise modeling of these matrices improves three things:

1. the **cost transparency**,
2. the **realistic creation of shifts**,
3. and the **Optimization accuracy**.

Before you finish, make sure that:

1. The correct matrix exists.
2. It's associated with the right kind of day.
3. The minimum connections in the case are already loaded.
4. You have properly separated empty travel and driver travel.

To validate that the matrix is already ready for the next step:

1. Check out the reference case you've been building.
2. Confirms that GoalBus already knows:
   1. from where the vehicle comes out physically,
   2. where it enters the line,
   3. how it comes back when it's due,
   4. and how a driver would move for a relay if applied.
3. Ask yourself if the system could already minimize non-productive times and distances in that case.
4. If the answer is yes, continue with the next quick start.
5. If the answer is no, go back and add or correct connections before continuing.

By the time you finish this section, you should be able to claim that your logistics base is realistic enough to sustain times, services and scheduling.

## Additional readings

- [Defining vehicle types and fleet allowed per line](P4_Defining_Vehicle_Types_And_Fleet_Allowed_Per_Line.md)
