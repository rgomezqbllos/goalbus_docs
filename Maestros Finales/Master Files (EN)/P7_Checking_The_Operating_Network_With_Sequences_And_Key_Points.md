---
title: Checking the operating network with sequences and key points
shortTitle: Operational network
intro: Learn how to validate how your network really behaves in operation, reviewing
  sequences, stop permissions and relay points before moving on to times and services.
contentType: how-tos
versions:
- '*'
---
## Checking the operational sequence of the routes

Now that you have already created the base network (stops, lines and routes), the next step is to validate that that network works properly from the operational point of view.

At this point you are no longer creating structure, you are validating how it behaves in practice.

Before you start:
1. You've already created stops, lines and routes on P6.
2. You have at least one route per sense.
3. You know what line you're preparing.

Case:
> Validate that route L1 has a coherent and operational sequence before defining times.

Steps:
1. Open the line you're working on.
2. Access the route view.
ref: P7_Imagen1.png | full
3. Select a sense.
4. Check the stop sequence.
5. Checks that:
   - There are no missing key stops.
   - There are no unnecessary duplicates.
   - The order is correct.
6. Repeat for the other sense.

Expected result:
- A clean and logical sequence that represents the actual route.

## Validating stop permits

Not all stops work the same. Some allow climbing, others lower, and others both.

Before continuing:
1. You've validated the sequence.
2. You know how every stop in reality works.

Steps:
1. Inside the route, check every stop.
2. Configure if you allow:
   - Rise
   - Down
   - Both
ref: P7_Imagen2.png | compact
3. Make sure that:
   - Terminals allow both.
   - Intermediate stops reflect the actual operation.
4. Save the changes.

Expected result:
- Each stop has a behavior consistent with the operation.

## Defining Relay Points

The relay points are critical for roasting and operation.

Before you start:
1. You already have a validated sequence.
2. You know where relays happen in the actual operation.

Steps:
1. Identify stops where driver changes are made.
2. Mark those stops as relay points.
ref: P7_Imagen3.png | compact
3. Checks that:
   - They're well placed.
   - That's enough for the operation.
4. Guard.

Expected result:
- The network already contemplates where driver changes can be made.

## Final validation of the operational network

Before moving forward:

1. Check the entire route again.
2. Confirms:
   - Right sequence.
   - Coherent permissions.
   - Determined relays.
3. Ask yourself:
   - Could you operate this line in real life?
   - Is there any operational detail missing?

If the answer is yes, you can continue.

## Additional readings

- P8 Loading empty travel and travel
