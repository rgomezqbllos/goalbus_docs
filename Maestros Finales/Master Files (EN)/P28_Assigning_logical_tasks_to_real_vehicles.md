---
title: Assigning logical tasks to real vehicles
shortTitle: Vehicle assignment
intro: 'Learn how to assign the logical vehicle tasks produced in Scheduling to real vehicles that were previously loaded or created.'
contentType: how-tos
versions:
  - '*'
---

## Loading or creating the real vehicles used for assignment

Once you have the Scheduling and Rostering solutions validated and published (Rostering is not strictly required), you can create or load the real vehicles that will be used to assign the logical tasks calculated in the vehicle Scheduling solution.

Use this quick start when you already ran Scheduling and (optionally) Rostering and you need to start vehicle assignment.

Before you begin, make sure that:
1. You published the Scheduling solution in P16.
2. You validated and consolidated the Rostering solution in P27.

For this quick start, use this reference case:

> **I’m going to assign the logical tasks calculated in vehicle Scheduling to the license plates of the vehicles I loaded or created.**

To load or create real vehicle license plates:
1. Open **Configuration** > **Vehicles** > **Registered vehicles**.
ref: P28_Imagen1.png | compact
2. If you want to create multiple plates at once, the best option is importing them.
3. Select the license-plate import button.
ref: P28_Imagen2.png | compact
4. Upload the CSV file with new vehicles following the modal instructions.
ref: P28_Imagen3.png | compact
5. If there are no errors, the vehicles will be registered.
6. If you prefer to create vehicles one by one, click **New vehicle**.
ref: P28_Imagen4.png | compact
7. In the modal, fill in:
   1. **License plate**.
   2. **Depot** the vehicle belongs to.
   3. **Model**.
   4. **Manufacturing year** (optional).
   5. **Start-of-operations date** from which tasks can be assigned.
ref: P28_Imagen5.png | compact
8. Save changes.
9. Confirm the created record appears in the vehicles registry view.

For the reference case, do not proceed until you can state:
1. All required plates are loaded or created.
2. Vehicles are linked to the correct **model**.
3. You do not need additional vehicles beyond those loaded/created.

When you finish this section, you should have all the required license plates to perform assignment.

For the reference case, you can create plates with a format like:
- **001-LFX**
- **002-LFX**
...
- **NNN-LFX**

## Assigning Scheduling logical tasks to real vehicles

Once all required vehicles are loaded/created, you can start vehicle assignment.

Before you start this section, make sure that:
1. You already have all vehicles loaded or created.
2. You know which assignment criteria you want to apply.
3. You have a validated Rostering solution.

To start vehicle assignment:
1. Open the **Vehicle assignment** module.
ref: P28_Imagen6.png | compact
2. Review unassigned tasks in the top bar.
ref: P28_Imagen7.png | compact
3. In the right panel, you will see the tasks to assign manually.
ref: P28_Imagen8.png
4. When you select **assign task**, the system will show available vehicles (no assigned tasks, or assigned without overlaps).
Ref: P28_Imagen9.png
5. Assign tasks to the corresponding vehicles.
6. When you finish, click **Confirm** to **publish** changes.
ref: P28_Imagen10.png
7. If you still have unassigned tasks or do not want to do everything manually, use **Optimize fleet assignment**.
ref: P28_Imagen11.png
8. Repeat for every day you want to work on.

For the reference case, make sure that:
1. All tasks are assigned to a vehicle.
2. Assignments are coherent.
3. All required days are covered.

When you finish this section, you should have a named/assigned vehicle solution.

