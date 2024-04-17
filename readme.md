# Custom Language CoWFCode - README

## Overview

This document provides an overview of the custom programming language developed here. The language has been designed with simplicity and efficiency in mind, featuring a minimalistic instruction set and straightforward syntax.

## Instruction Set

### Instructions

- `load`: Loads a value onto the storage stack, replacing the previous value.
- `loadI`: Loads a constant integer onto the storage stack.
- `gt`: Compares the top two values on the storage stack. If the first value is greater than the second, sets the first value to 1; otherwise, sets it to 0.
- `lt`: Compares the top two values on the storage stack. If the first value is smaller than the second, sets the first value to 1; otherwise, sets it to 0.
- `jumpC`: Jumps to a specified instruction index if the first value on the pile is not 0.
- `jump`: Always jump to a specified instruction index.
- `act`: Executes an action based on certain conditions.
- `nop`: No operation; does nothing.

### Storage

The compiler that references this language only have two available variable storage positions, acting like a pile, where if you load two elements,
in the first instance it will be set in the first storage position, but when a second value is loaded, the first element entered will move
into the last storage position, leaving the first empty that the new variable will be put.

In this language you have a set of keyword that will put in the pile values referencing attributes of the company you are executing the code from, this are:
1. `VAL_ACTIVELOCATIONS`: Represents the active locations.
2. `VAL_ACTIVEFUNDS`: Represents the active funds.
3. `VAL_UUID`: The unique id of the company.
4. `VAL_OWN`: The quantity of Cells the company own.
5. `VAL_RENTEDLOCATIONS`: The quantity of Cells that the company own that are rented.
6. `VAL_NONRENTEDOWNED`: The quantity of Cells that the company own that are not rented at the moment.
7. `VAL_ACTIVEFUNDS`: The quantity of liquid funds the company has.
8. `VAL_N_OBJECT`: Also requiring another ID of object after, returns the quantity of that object that the company has on storage.

### Actions

- `objProduce`: Produces an object if conditions are met.
- `objSell`: Sells an object if conditions are met.
- `objBuy`: Buys a object if conditions are met.
- `cellBuy`: Buys a cell if conditions are met.
- `cellSell`: Sells a cell if conditions are met.
- `cellGiveRent`: Gives a cell for rent if conditions are met.
- `cellGainRent`: Tries to get rent from another company's cell.

### Structure

Usually, the code will be structure in this manner:
`<instruccion> <additional Information 1> <additional Information 2>`

For `gt`, `lt`, `nop`, they dont require any additional value, just the instruction.
For `jump`, `jumpC`, `load`, `loadI` they just require one additional value.
The other instructions can have up to 2 additional values required to work.

For **`act`**:
- `objProduce`: Just need one additional value in the form of a valid object.
- `objBuy`: Just need one additional value in the form of a valid object.
- `objSell`: Just need one additional value in the form of a valid object.
- `cellBuy`: Just need one additional value in the form of the type of cell that you refer.
- `cellSell`: Just need one additional value in the form of the type of cell that you refer.
- `cellGiveRent`: Just need one additional value in the form of the type of cell that you refer.
- `cellGainRent`: Just need one additional value in the form of the type of cell that you refer.

## Usage Example

```CoWFCode
load VAL_ACTIVELOCATIONS
loadI 1
gt
jumpC 5
act objProduce OBJ_PROCC_DESK
load VAL_N_OBJECT OBJ_PROCC_DESK
loadI 1
gt
jumpC 11
act objSell OBJ_PROCC_DESK
load VAL_ACTIVEFUNDS
loadI 50000
gt
jumpC 15
act cellBuy CELL_HFACT
nop 
