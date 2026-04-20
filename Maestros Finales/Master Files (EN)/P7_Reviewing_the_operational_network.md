---
title: Reviewing the operational network with sequences and key points
shortTitle: Operational network
intro: 'Learn how to validate how your network behaves in real operations by reviewing sequences, stop permissions, and relief points before moving on to times and services.'
contentType: how-tos
versions:
  - '*'
---

## Reviewing the operational sequence of routes

Now that you have created the base network (stops, lines, and routes), the next step is to validate that the network works correctly from an operational point of view.

At this point you are no longer creating structure—you are validating how it behaves in practice.

Before you begin:
1. You already created stops, lines, and routes in P6.
2. You have at least one route per direction.
3. You know which line you are preparing.

Case:
> Validate that route L1 has a coherent, operational sequence before defining times.

Steps:
1. Open the line you are working on.
2. Go to the routes view.
ref: P7_Imagen1.png | full
3. Select a direction.
4. Review the stop sequence.
5. Verify that:
   - No key stops are missing.
   - There are no unnecessary duplicates.
   - The order is correct.
6. Repeat for the other direction.

Expected result:
- A clean, logical sequence that represents the real path.

## Validating stop permissions

Not all stops work the same way. Some allow boarding, others alighting, and others both.

Before you continue:
1. You already validated the sequence.
2. You know how each stop works in reality.

Steps:
1. Within the route, review each stop.
2. Configure whether it allows:
   - Boarding
   - Alighting
   - Both
ref: P7_Imagen2.png | compact
3. Make sure that:
   - Terminals allow both.
   - Intermediate stops reflect real operations.
4. Save the changes.

Expected result:
- Each stop has behavior coherent with operations.

## Defining relief points

Relief points are critical for Rostering and operations.

Before you begin:
1. You already validated the sequence.
2. You know where reliefs happen in real operations.

Steps:
1. Identify stops where driver changes are performed.
2. Mark those stops as relief points.
ref: P7_Imagen3.png | compact
3. Verify that:
   - They are well located.
   - They are sufficient for operations.
4. Save.

Expected result:
- The network now includes where driver changes can occur.

## Final validation of the operational network

Before moving on:
1. Review the entire route again.
2. Confirm:
   - Correct sequence.
   - Coherent permissions.
   - Reliefs defined.
3. Ask yourself:
   - Could this line operate in real life?
   - Is any operational detail missing?

If the answer is yes, you can continue.

## Additional reading

- [Preparing parkings and depots for operations](P5_Preparing_parkings_and_depots_for_operations.md)

